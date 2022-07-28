# Elliptic curve parameters (secp256k1)
P = 2**256 - 2**32 - 977
N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
A = 0
B = 7
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
G = (Gx, Gy)

wif_prefix  = 0xef
addr_prefix = 0x6F
script_prefix = 0xc4

b58chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

short2byte = lambda x: bytes([x])

def sha256_twice(src):
    return sha256(sha256(src).digest()).digest()

def hash160(src):
    return hashlib.new('ripemd160', sha256(src).digest()).digest()
    
def hex2int(src, order='big'):
    return int.from_bytes(bytes.fromhex(src), byteorder=order)


def b58decode(src, length = None):
    base = 58
    
    long_value = 0
    for (i, c) in enumerate(src[::-1]):
        long_value += b58chars.find(c) * (base ** i)

    result = bytes()
    while long_value >= 256:
        div, mod = divmod(long_value, 256)
        result = short2byte(mod) + result
        long_value = div
    result = short2byte(long_value) + result
    nPad = 0
    for c in src:
        if c == b58chars[0]:
            nPad += 1
        else:
            break

    result = short2byte(0)*nPad + result
    if length is not None and len(result) != length:
        raise "len(b58decode_result) != length"
    return result

def b58encode(src):
    base = 58
    
    long_value = 0
    for (i, c) in enumerate(src[::-1]):
        long_value += (256**i) * c

    result = ''
    while long_value >= base:
        div, mod = divmod(long_value, base)
        result = b58chars[mod] + result
        long_value = div
    result = b58chars[long_value] + result

    # Bitcoin does a little leading-zero-compression:
    # leading 0-bytes in the input become leading-1s
    nPad = 0
    for c in src:
        if c == 0 : nPad += 1
        else: break

    return (b58chars[0]*nPad) + result


def wif_to_privkey(string):
    wif_compressed = 52 == len(string)
    pvkeyencoded = b58decode(string).hex()
    wifversion = pvkeyencoded[:2]
    checksum = pvkeyencoded[-8:]

    vs = bytes.fromhex(pvkeyencoded[:-8])
    check = sha256_twice(vs)[0:4]

    if wifversion == wif_prefix.to_bytes(1, byteorder='big').hex() and checksum == check.hex():
        if wif_compressed == True:
            compressed = True
            privkey = pvkeyencoded[2:-10]        
        else:
            compressed = False
            privkey = pvkeyencoded[2:-8]

        return {'compressed': compressed, 'privkey': privkey}

    else:
        return None


def get_public_key(string):
    decoded_private_key = hex2int(string)
    public_key = fast_multiply(G, decoded_private_key)
    hex_encoded_public_key = str('04') + public_key[0].to_bytes(32, byteorder='big').hex() + public_key[1].to_bytes(32, byteorder='big').hex()

    (public_key_x, public_key_y) = public_key
    if (public_key_y % 2) == 0:
        compressed_prefix = '02'
    else:
        compressed_prefix = '03'

    hex_compressed_public_key = compressed_prefix + public_key_x.to_bytes(32, byteorder='big').hex()

    return {'pubkeyhex': hex_encoded_public_key, 'pubkeyhex_compressed': hex_compressed_public_key}


 def pubkey_to_address(string):
    #data = binascii.unhexlify(string)
    data = bytes.fromhex(string)
    data_hash = hash160(data)
    vs = short2byte(addr_prefix) + data_hash   
    check = sha256_twice(vs)[0:4]
    return b58encode(vs + check)
 