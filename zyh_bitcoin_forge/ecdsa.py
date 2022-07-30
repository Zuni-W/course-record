import hashlib
import hmac

from constant import *
from transform import hex2int


def generate_k(tx_hash, priv):
    v = b'\x01' * 32
    k = b'\x00' * 32
    priv_bytes = bytes.fromhex(priv)
    tx_hash = hex2int(tx_hash.hex()).to_bytes(32, byteorder='big')
    k = hmac.new(k, v + b'\x00' + priv_bytes + tx_hash, hashlib.sha256).digest()
    v = hmac.new(k, v, hashlib.sha256).digest()
    k = hmac.new(k, v + b'\x01' + priv_bytes + tx_hash, hashlib.sha256).digest()
    v = hmac.new(k, v, hashlib.sha256).digest()
    return hex2int(hmac.new(k, v, hashlib.sha256).digest().hex())


def inv(a, n):
    if a == 0:
        return 0
    lm, hm = 1, 0
    low, high = a % n, n
    while low > 1:
        r = high//low
        nm, new = hm-lm*r, high-low*r
        lm, low, hm, high = nm, new, lm, low
    return lm % n


def to_jacobian(p):
    o = (p[0], p[1], 1)
    return o


def jacobian_double(p):
    if not p[1]:
        return (0, 0, 0)
    ysq = (p[1] ** 2) % P
    S = (4 * p[0] * ysq) % P
    M = (3 * p[0] ** 2 + A * p[2] ** 4) % P
    nx = (M**2 - 2 * S) % P
    ny = (M * (S - nx) - 8 * ysq ** 2) % P
    nz = (2 * p[1] * p[2]) % P
    return (nx, ny, nz)


def jacobian_add(p, q):
    if not p[1]:
        return q
    if not q[1]:
        return p
    U1 = (p[0] * q[2] ** 2) % P
    U2 = (q[0] * p[2] ** 2) % P
    S1 = (p[1] * q[2] ** 3) % P
    S2 = (q[1] * p[2] ** 3) % P
    if U1 == U2:
        if S1 != S2:
            return (0, 0, 1)
        return jacobian_double(p)
    H = U2 - U1
    R = S2 - S1
    H2 = (H * H) % P
    H3 = (H * H2) % P
    U1H2 = (U1 * H2) % P
    nx = (R ** 2 - H3 - 2 * U1H2) % P
    ny = (R * (U1H2 - nx) - S1 * H3) % P
    nz = (H * p[2] * q[2]) % P
    return (nx, ny, nz)


def from_jacobian(p):
    z = inv(p[2], P)
    return ((p[0] * z**2) % P, (p[1] * z**3) % P)


def jacobian_multiply(a, n):
    if a[1] == 0 or n == 0:
        return (0, 0, 1)
    if n == 1:
        return a
    if n < 0 or n >= N:
        return jacobian_multiply(a, n % N)
    if (n % 2) == 0:
        return jacobian_double(jacobian_multiply(a, n//2))
    if (n % 2) == 1:
        return jacobian_add(jacobian_double(jacobian_multiply(a, n//2)), a)


def fast_multiply(a, n):
    return from_jacobian(jacobian_multiply(to_jacobian(a), n))


def fast_add(a, b):
    return from_jacobian(jacobian_add(to_jacobian(a), to_jacobian(b)))


def get_pubkey(privkey):
    decoded_privkey = hex2int(privkey)
    pubkey = fast_multiply(G, decoded_privkey)
    return pubkey


def add(P_1, P_2):
    y_diff = (P_2[1] - P_1[1]) % P
    x_diff = (P_2[0] - P_1[0]) % P

    if x_diff == 0 and y_diff != 0:
        return None
    elif x_diff == 0 and y_diff == 0:
        if P_1[1] == 0:
            return None
        else:
            ld = ((3 * P_1[0] * P_1[0] + 2 * A * P_1[0] + B) * inv(2 * P_1[1], P)) % P
    else:
        ld = (y_diff * inv(x_diff, P)) % P
    nu = (P_1[1] - ld * P_1[0]) % P
    x = (ld * ld - A - P_1[0] - P_2[0]) % P
    y = (-ld * x - nu) % P
    return x, y


def ecdsa_raw_sign(msghash, priv):
    z = hex2int(msghash.hex())
    k = generate_k(msghash, priv)
    # print(msghash)
    r, y = fast_multiply(G, k)
    # print(r, y)
    r = r % N
    s = (inv(k, N) * (z + r * hex2int(priv))) % N
    return {'r': r % N, 's': s}


def ecdsa_raw_verify(msghash, sign, pub):
    z = hex2int(msghash.hex()) % N
    w = inv(sign['s'], N)
    m1 = (z * w) % N
    m2 = (sign['r'] * w) % N
    c = fast_add(fast_multiply(G, m1), fast_multiply(pub, m2))

    if (c[0] % N) == (sign['r'] % N):
        return True
    return False
