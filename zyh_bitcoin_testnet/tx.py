from transform import b58decode


def num_to_varint(a):
    x = int(a)
    if x < 253: return x.to_bytes(1, byteorder='big')
    elif x < 65536: return int(253).to_bytes(1, byteorder='big') + x.to_bytes(2, byteorder='little')
    elif x < 4294967296: return int(254).to_bytes(1, byteorder='big') + x.to_bytes(4, byteorder='little')
    else: return int(255).to_bytes(1, byteorder='big') + x.to_bytes(8, byteorder='little')


def address2script(address):
    return '76a914' + b58decode(address).hex()[2:-8] + '88ac'


def serialize_tx(tx):
    tx_raw = ""
    tx_raw += tx["version"].to_bytes(4, byteorder='little').hex()
    tx_raw += num_to_varint(len(tx["inputs"])).hex()
    for inp in tx["inputs"]:
        tx_raw += bytes.fromhex(inp["prev_hash"])[::-1].hex()
        tx_raw += inp["index"].to_bytes(4, byteorder='little').hex()
        tx_raw += num_to_varint(len(inp["script"])//2).hex()
        if inp["script"]:
            tx_raw += inp["script"]
        tx_raw += inp["sequence"].to_bytes(4, byteorder='little').hex()
    tx_raw += num_to_varint(len(tx["outputs"])).hex()
    for outp in tx["outputs"]:
        tx_raw += outp["value"].to_bytes(8, byteorder='little').hex()
        tx_raw += num_to_varint(len(outp["script"])//2).hex() + outp["script"]
    tx_raw += tx["locktime"].to_bytes(4, byteorder='little').hex()
    return tx_raw


def make_tx(inputs: list, outputs: list, locktime=0):
    for i in inputs:
        assert (i.get('prev_hash', 0) and i.get('index', -1) != -1 and i.get('address', 0))
    for i in outputs:
        assert (i.get('address', 0) and i.get('value', 0))

    tx = {"version": 1, "inputs": [], "outputs": [], "locktime": locktime}
    for i, inp in enumerate(inputs):
        tx["inputs"].append({
            "prev_hash": inp['prev_hash'],
            "index": inp['index'],
            "script": "",
            "sequence": 0xffffffff
        })
    for i, outp in enumerate(outputs):
        tx["outputs"].append({
            "address": outp['address'],
            "script": address2script(outp['address']),
            "value": outp['value']
        })

    return tx, serialize_tx(tx)
