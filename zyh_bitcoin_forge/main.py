from pprint import pprint

from constant import *
from transform import sha256_twice, hex2int
from ecdsa import ecdsa_raw_sign, ecdsa_raw_verify, get_pubkey
import ecdsa
from mini_ecdsa import *
from secret import priv


def make_forge_message_sign(pub):
    sysrand = SystemRandom()
    u = sysrand.randrange(1, N)
    v = sysrand.randrange(1, N)
    R = ecdsa.fast_add(ecdsa.fast_multiply(G, u), ecdsa.fast_multiply(pub, v))
    r = R[0]
    e = (r * u * ecdsa.inv(v, N)) % N
    s = (r * ecdsa.inv(v, N)) % N
    sign = {'r': r, 's': s}
    return e.to_bytes(32, byteorder='big'), sign


if __name__ == '__main__':
    # msg = 'SATOSHI NAKAMOTO'
    # curve = CurveOverFp.secp256k1()
    # Gm = Point(Gx, Gy)
    # pubkey = get_pubkey(priv)
    # pairs = (hex2int(priv), Point(pubkey[0], pubkey[1]))
    # sign = sign(msg, curve, Gm, N, pairs)
    # print(verify('SATOSHI NAKAMOTO', curve, Gm, N, sign))

    msg_bytes = b'SATOSHI NAKAMOTO'
    msghash = sha256_twice(msg_bytes)
    pub = get_pubkey(priv)
    sign = ecdsa_raw_sign(msghash, priv)
    print(msg_bytes)
    pprint(sign)
    print(ecdsa_raw_verify(msghash, sign, pub))

    forge_bytes, sign = make_forge_message_sign(pub)
    print(forge_bytes)
    pprint(sign)
    print(ecdsa_raw_verify(forge_bytes, sign, pub))
    #

