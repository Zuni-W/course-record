import hashlib
from typing import Literal

b58chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

short2byte = lambda x: bytes([x])


def sha256_twice(src):
    return hashlib.sha256(hashlib.sha256(src).digest()).digest()


def hash160(src):
    return hashlib.new('ripemd160', hashlib.sha256(src).digest()).digest()


def hex2int(src, order: Literal['big', 'little'] = 'big'):
    return int.from_bytes(bytes.fromhex(src), byteorder=order)


def b58decode(src, length=None):
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

    result = short2byte(0) * nPad + result
    if length is not None and len(result) != length:
        raise Exception("len(b58decode_result) != length")
    return result


def b58encode(src):
    base = 58

    long_value = 0
    for (i, c) in enumerate(src[::-1]):
        long_value += (256 ** i) * c

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
        if c == 0:
            nPad += 1
        else:
            break

    return (b58chars[0] * nPad) + result


def b58check(src, version=0):
    src_bytes = bytes.fromhex(src)
    return b58encode(short2byte(version) + src_bytes + sha256_twice(short2byte(version) + src_bytes)[:4])
