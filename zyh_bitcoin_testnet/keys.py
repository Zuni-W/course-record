from constant import *
from jacobi import fast_multiply
from transform import hex2int, hash160, short2byte, sha256_twice, b58encode, b58decode

# testnet
wif_prefix = 0xef
addr_prefix = 0x6F
script_prefix = 0xc4


def wif2privkey(wif):
    assert 52 == len(wif)
    privkey_encoded = b58decode(wif).hex()
    wif_version = privkey_encoded[:2]
    checksum = privkey_encoded[-8:]

    vs = bytes.fromhex(privkey_encoded[:-8])
    check = sha256_twice(vs)[0:4]

    if wif_version == wif_prefix.to_bytes(1, byteorder='big').hex() and checksum == check.hex():
        privkey = privkey_encoded[2:-10]
        return privkey

    else:
        return None


def get_pubkey(string):
    decoded_privkey = hex2int(string)
    pubkey = fast_multiply(G, decoded_privkey)
    (pubkey_x, pubkey_y) = pubkey
    if (pubkey_y % 2) == 0:
        compressed_prefix = '02'
    else:
        compressed_prefix = '03'

    compressed_pubkey = compressed_prefix + pubkey_x.to_bytes(32, byteorder='big').hex()
    return compressed_pubkey


def pubkey2address(string):
    data = bytes.fromhex(string)
    data_hash = hash160(data)
    vs = short2byte(addr_prefix) + data_hash
    check = sha256_twice(vs)[0:4]
    return b58encode(vs + check)
