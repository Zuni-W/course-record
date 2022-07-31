import struct

meow_default_seed = bytes.fromhex(
    "3243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c8"
    "9452821e638d01377be5466cf34e90c6cc0ac29b7c97c50dd3f84d5b5b547091"
    "79216d5d98979fb1bd1310ba698dfb5ac2ffd72dbd01adfb7b8e1afed6a267e9"
    "6ba7c9045f12c7f9924a19947b3916cf70801f2e2858efc16636920d871574e6"
)

aes_sbox_inverse = list(bytes.fromhex(
    "52096ad53036a538bf40a39e81f3d7fb7ce339829b2fff87348e4344c4dee9cb"
    "547b9432a6c2233dee4c950b42fac34e082ea16628d924b2765ba2496d8bd125"
    "72f8f66486689816d4a45ccc5d65b6926c704850fdedb9da5e154657a78d9d84"
    "90d8ab008cbcd30af7e45805b8b34506d02c1e8fca3f0f02c1afbd0301138a6b"
    "3a9111414f67dcea97f2cfcef0b4e67396ac7422e7ad3585e2f937e81c75df6e"
    "47f11a711d29c5896fb7620eaa18be1bfc563e4bc6d279209adbc0fe78cd5af4"
    "1fdda8338807c731b11210592780ec5f60517fa919b54a0d2de57a9f93c99cef"
    "a0e03b4dae2af5b0c8ebbb3c83539961172b047eba77d626e169146355210c7d"
))

aes_sbox=[0x63,0x7C,0x77,0x7B,0xF2,0x6B,0x6F,0xC5,0x30,0x01,0x67,0x2B,0xFE,0xD7,0xAB,0x76,
	0xCA,0x82,0xC9,0x7D,0xFA,0x59,0x47,0xF0,0xAD,0xD4,0xA2,0xAF,0x9C,0xA4,0x72,0xC0,    
	0xB7,0xFD,0x93,0x26,0x36,0x3F,0xF7,0xCC,0x34,0xA5,0xE5,0xF1,0x71,0xD8,0x31,0x15,    
	0x04,0xC7,0x23,0xC3,0x18,0x96,0x05,0x9A,0x07,0x12,0x80,0xE2,0xEB,0x27,0xB2,0x75,    
	0x09,0x83,0x2C,0x1A,0x1B,0x6E,0x5A,0xA0,0x52,0x3B,0xD6,0xB3,0x29,0xE3,0x2F,0x84,    
	0x53,0xD1,0x00,0xED,0x20,0xFC,0xB1,0x5B,0x6A,0xCB,0xBE,0x39,0x4A,0x4C,0x58,0xCF,    
	0xD0,0xEF,0xAA,0xFB,0x43,0x4D,0x33,0x85,0x45,0xF9,0x02,0x7F,0x50,0x3C,0x9F,0xA8,    
	0x51,0xA3,0x40,0x8F,0x92,0x9D,0x38,0xF5,0xBC,0xB6,0xDA,0x21,0x10,0xFF,0xF3,0xD2,    
	0xCD,0x0C,0x13,0xEC,0x5F,0x97,0x44,0x17,0xC4,0xA7,0x7E,0x3D,0x64,0x5D,0x19,0x73,    
	0x60,0x81,0x4F,0xDC,0x22,0x2A,0x90,0x88,0x46,0xEE,0xB8,0x14,0xDE,0x5E,0x0B,0xDB,    
	0xE0,0x32,0x3A,0x0A,0x49,0x06,0x24,0x5C,0xC2,0xD3,0xAC,0x62,0x91,0x95,0xE4,0x79,    
	0xE7,0xC8,0x37,0x6D,0x8D,0xD5,0x4E,0xA9,0x6C,0x56,0xF4,0xEA,0x65,0x7A,0xAE,0x08,    
	0xBA,0x78,0x25,0x2E,0x1C,0xA6,0xB4,0xC6,0xE8,0xDD,0x74,0x1F,0x4B,0xBD,0x8B,0x8A,    
	0x70,0x3E,0xB5,0x66,0x48,0x03,0xF6,0x0E,0x61,0x35,0x57,0xB9,0x86,0xC1,0x1D,0x9E,    
	0xE1,0xF8,0x98,0x11,0x69,0xD9,0x8E,0x94,0x9B,0x1E,0x87,0xE9,0xCE,0x55,0x28,0xDF,   
	0x8C,0xA1,0x89,0x0D,0xBF,0xE6,0x42,0x68,0x41,0x99,0x2D,0x0F,0xB0,0x54,0xBB,0x16
        ]


def gf_multiply(a: int, b: int) -> int:
    r = 0
    for i, bit in enumerate(bin(b)[-1:1:-1]):
        r ^= int(bit) * (a << i)
    while r.bit_length() > 8:
        r ^= 0x11b << (r.bit_length() - 9)
    return r

gf_table = {(a, b): gf_multiply(a, b) for a in range(16) for b in range(256)}

def inverse_mix_column(col: bytearray):
    a, b, c, d = col
    return (
        gf_table[14, a] ^ gf_table[11, b] ^ gf_table[13, c] ^ gf_table[ 9, d],
        gf_table[ 9, a] ^ gf_table[14, b] ^ gf_table[11, c] ^ gf_table[13, d],
        gf_table[13, a] ^ gf_table[ 9, b] ^ gf_table[14, c] ^ gf_table[11, d],
        gf_table[11, a] ^ gf_table[13, b] ^ gf_table[ 9, c] ^ gf_table[14, d],
    )

def mix_column(col:bytearray):
    a,b,c,d=col
    return (
        gf_table[2, a] ^ gf_table[3, b] ^ gf_table[1, c] ^ gf_table[ 1, d],
        gf_table[ 1, a] ^ gf_table[2, b] ^ gf_table[3, c] ^ gf_table[1, d],
        gf_table[1, a] ^ gf_table[ 1, b] ^ gf_table[2, c] ^ gf_table[3, d],
        gf_table[3, a] ^ gf_table[1, b] ^ gf_table[ 1, c] ^ gf_table[2, d],

            )

def aesenc(a: bytearray, b: bytearray):
    for i in range(16):
        a[i] ^= b[i]

    for column_index in range(4):
        a[column_index*4 : column_index*4 + 4] = \
            mix_column(a[column_index*4 : column_index*4 + 4])

    for i in range(16):
        a[i] = aes_sbox[a[i]]
    for row_index in range(4):
        row = a[row_index::4]
        for _ in range(row_index):
            row = row[1:] + row[:1]
        a[row_index::4] = row


def aesdec(a: bytearray, b: bytearray):
    for row_index in range(4):
        row = a[row_index::4]
        for _ in range(row_index):
            row = row[-1:] + row[:-1]
        a[row_index::4] = row
    for i in range(16):
        a[i] = aes_sbox_inverse[a[i]]
    for column_index in range(4):
        a[column_index*4 : column_index*4 + 4] = \
            inverse_mix_column(a[column_index*4 : column_index*4 + 4])
    for i in range(16):
        a[i] ^= b[i]

from random import *
from copy import *
a=[randint(0,255) for i in range(16)]

b=[randint(0,255) for i in range(16)]

c=copy(a)
aesdec(a,b)
aesenc(a,b)

print(c==a)
def paddq(a: bytearray, b: bytearray):
    mask64 = 2**64 - 1
    a0, a1 = struct.unpack("<QQ", bytes(a))
    b0, b1 = struct.unpack("<QQ", bytes(b))
    a[:] = struct.pack("<QQ", (a0 + b0) & mask64, (a1 + b1) & mask64)

def psubq(a: bytearray, b: bytearray):
    mask64 = 2**64 - 1
    a0, a1 = struct.unpack("<QQ", bytes(a))
    b0, b1 = struct.unpack("<QQ", bytes(b))
    a[:] = struct.pack("<QQ", (a0 - b0+mask64+1) & mask64, (a1 - b1+mask64+1) & mask64)

paddq(a,b)
psubq(a,b)
print(c==a)
def pxor(a: bytearray, b: bytearray):
    for i in range(16):
        a[i] ^= b[i]

def inv_meow_hash(input_bytes:bytes,output_bytes:bytes) -> bytes:
    lanes = [
        bytearray([0]*16)
        for i in range(8)
    ]
    lanes[0]=bytearray(output_bytes)
    get_lane = lambda i: lanes[i % 8]
    def inv_meow_mix_reg(i, reads):
        pxor  (get_lane(i + 1), reads[3])
        psubq (get_lane(i + 2), reads[2])
        aesenc(get_lane(i + 4), get_lane(i + 1))
        pxor  (get_lane(i + 4), reads[1])
        psubq (get_lane(i + 6), reads[0])
        aesenc(get_lane(i + 0), get_lane(i + 4))

    def inv_meow_mix(i, block):
        inv_meow_mix_reg(i, [
            block[offset : offset + 16] for offset in (15, 0, 1, 16)
        ])

    def inv_meow_mix_funky(i, block):
        inv_meow_mix_reg(i, (
            b"\0" + block[:15], block[:16], block[17:] + block[:1], block[16:],
        ))

    def inv_meow_shuffle(i):
        pxor  (get_lane(i + 1), get_lane(i + 2))
        psubq (get_lane(i + 5), get_lane(i + 6))
        aesenc(get_lane(i + 4), get_lane(i + 1))
        pxor  (get_lane(i + 4), get_lane(i + 6))
        psubq (get_lane(i + 1), get_lane(i + 5))
        aesenc(get_lane(i + 0), get_lane(i + 4))

    def meow_mix_reg(i, reads):
        aesdec(get_lane(i + 0), get_lane(i + 4))
        paddq (get_lane(i + 6), reads[0])
        pxor  (get_lane(i + 4), reads[1])
        aesdec(get_lane(i + 4), get_lane(i + 1))
        paddq (get_lane(i + 2), reads[2])
        pxor  (get_lane(i + 1), reads[3])

    def meow_mix(i, block):
        meow_mix_reg(i, [
            block[offset : offset + 16] for offset in (15, 0, 1, 16)
        ])

    def meow_mix_funky(i, block):
        meow_mix_reg(i, (
            b"\0" + block[:15], block[:16], block[17:] + block[:1], block[16:],
        ))

    def meow_shuffle(i):
        aesdec(get_lane(i + 0), get_lane(i + 4))
        paddq (get_lane(i + 1), get_lane(i + 5))
        pxor  (get_lane(i + 4), get_lane(i + 6))
        aesdec(get_lane(i + 4), get_lane(i + 1))
        paddq (get_lane(i + 5), get_lane(i + 6))
        pxor  (get_lane(i + 1), get_lane(i + 2))


    original_length = len(input_bytes)
    target_length = ((len(input_bytes) // 32) + 1) * 32
    input_bytes += b"\0" * (target_length - original_length)
    # Cut off the last block, which we will absorb differently.
    input_bytes, tail_block = input_bytes[:-32], input_bytes[-32:]



    for i in range(11,-1,-1):
        inv_meow_shuffle(i)


    message_length_block = struct.pack("<QQQQ", 0, 0, original_length, 0)
    inv_meow_mix_funky(1, message_length_block)
    inv_meow_mix_funky(0, tail_block)



    # Absorb all complete 256-byte blocks.
    off = 256
    while off <= len(input_bytes):
        for _ in range(8):
            inv_meow_mix(off // 32, input_bytes[off : off+32])
            off -= 32

    print(lanes)
    return b"".join([bytes(i) for i in lanes])




def meow_hash(key_bytes: bytes, input_bytes: bytes) -> bytes:
    assert len(key_bytes) == 128
    lanes = [
        bytearray(key_bytes[i*16 : i*16 + 16])
        for i in range(8)
    ]
    get_lane = lambda i: lanes[i % 8]

    def meow_mix_reg(i, reads):
        aesdec(get_lane(i + 0), get_lane(i + 4))
        paddq (get_lane(i + 6), reads[0])
        pxor  (get_lane(i + 4), reads[1])
        aesdec(get_lane(i + 4), get_lane(i + 1))
        paddq (get_lane(i + 2), reads[2])
        pxor  (get_lane(i + 1), reads[3])

    def meow_mix(i, block):
        meow_mix_reg(i, [
            block[offset : offset + 16] for offset in (15, 0, 1, 16)
        ])

    def meow_mix_funky(i, block):
        meow_mix_reg(i, (
            b"\0" + block[:15], block[:16], block[17:] + block[:1], block[16:],
        ))

    def meow_shuffle(i):
        aesdec(get_lane(i + 0), get_lane(i + 4))
        paddq (get_lane(i + 1), get_lane(i + 5))
        pxor  (get_lane(i + 4), get_lane(i + 6))
        aesdec(get_lane(i + 4), get_lane(i + 1))
        paddq (get_lane(i + 5), get_lane(i + 6))
        pxor  (get_lane(i + 1), get_lane(i + 2))

    # Pad the input to a multiple of 32 bytes; but add a full block of zeros if we're already a multiple.
    original_length = len(input_bytes)
    target_length = ((len(input_bytes) // 32) + 1) * 32
    input_bytes += b"\0" * (target_length - original_length)
    # Cut off the last block, which we will absorb differently.
    input_bytes, tail_block = input_bytes[:-32], input_bytes[-32:]

    # Absorb all complete 256-byte blocks.
    off = 0
    while off + 256 <= len(input_bytes):
        for _ in range(8):
            meow_mix(off // 32, input_bytes[off : off+32])
            off += 32

    # Absorb the tail block and message length in a funky way that's different than all other absorptions.
    meow_mix_funky(0, tail_block)
    message_length_block = struct.pack("<QQQQ", 0, 0, original_length, 0)
    meow_mix_funky(1, message_length_block)

    # Now return to absorbing any remaining 32-byte blocks.
    while off + 32 <= len(input_bytes):
        meow_mix(2 + off // 32, input_bytes[off : off + 32])
        off += 32

    # Finalize.
    for i in range(12):
        meow_shuffle(i)

    # Aggregate the state down into a single lane.
    paddq(lanes[0], lanes[2])
    paddq(lanes[4], lanes[6])
    paddq(lanes[1], lanes[3])
    paddq(lanes[5], lanes[7])
    pxor(lanes[0], lanes[1])
    pxor(lanes[4], lanes[5])
    paddq(lanes[0], lanes[4])

    return lanes[0]




outputs=b"sdu_cst_20220610"
inputs=b"Wang Chaoran 202022460107"
print(len(inputs))
key=inv_meow_hash(inputs,outputs)
print(key)
outputs=meow_hash(key,inputs)
print(outputs)
