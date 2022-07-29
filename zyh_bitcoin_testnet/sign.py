import hashlib
import hmac

from jacobi import ecdsa_raw_sign
from transform import hex2int, sha256_twice
from tx import serialize_tx, address2script





def der_encode_sig(v, r, s):
    b1, b2 = r.to_bytes(32, byteorder='big').hex(), s.to_bytes(32, byteorder='big').hex()
    if len(b1) and b1[0] in '89abcdef':
        b1 = '00' + b1
    if len(b2) and b2[0] in '89abcdef':
        b2 = '00' + b2
    left = '02'+(len(b1)//2).to_bytes(1, byteorder='big').hex()+b1
    right = '02'+(len(b2)//2).to_bytes(1, byteorder='big').hex()+b2
    return '30'+(len(left+right)//2).to_bytes(1, byteorder='big').hex()+left+right


def ecdsa_tx_sign(tx, priv):
    hashcode = 1  # SIGHASH_ALL
    hashtx = sha256_twice(bytes.fromhex(tx) + hashcode.to_bytes(4, byteorder='little'))
    rawsig = ecdsa_raw_sign(hashtx, priv)
    return der_encode_sig(*rawsig)+hashcode.to_bytes(1, byteorder='big').hex()


def serialize_script_unit(unit):
    if isinstance(unit, int):
        if unit < 16:
            return (unit + 80).to_bytes(1, byteorder='big')
        else:
            return unit.to_bytes(1, byteorder='big')
    elif unit is None:
        return b'\x00'
    else:
        if len(unit) <= 75:
            return (len(unit)).to_bytes(1, byteorder='big')+unit
        elif len(unit) < 256:
            return (76).to_bytes(1, byteorder='big')+(len(unit)).to_bytes(1, byteorder='big')+unit
        elif len(unit) < 65536:
            return (77).to_bytes(1, byteorder='big')+len(unit).to_bytes(2, byteorder='little')+unit
        else:
            return (78).to_bytes(1, byteorder='big')+len(unit).to_bytes(4, byteorder='little')+unit


def serialize_script(script):
    result = bytes()
    for b in map(serialize_script_unit, script):
        result += b
    return result.hex()


def signature_form(tx, script):
    sign_tx = tx.copy()
    for inp in sign_tx["inputs"]:
        inp["script"] = ""
    sign_tx["inputs"][0]["script"] = script
    return serialize_tx(sign_tx)


def sign(tx, pair):
    address = pair['address']
    signing_tx = signature_form(tx, address2script(address))
    sign = ecdsa_tx_sign(signing_tx, pair['privkey'])
    tx["inputs"][0]["script"] = serialize_script([bytes.fromhex(sign), bytes.fromhex(pair['pubkey'])])
    return tx


