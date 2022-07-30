from pprint import pprint
from keys import wif2privkey, get_pubkey, pubkey2address
from sign import sign
from tx import make_tx, serialize_tx
from blockcypher import pushtx
from secrets import *


if __name__ == "__main__":
    value = 1000
    source_pair = {'privkey': wif2privkey(source_wif), 'wif': source_wif}
    source_pair['pubkey'] = get_pubkey(source_pair['privkey'])
    source_pair['address'] = pubkey2address(source_pair['pubkey'])

    inputs = [{'prev_hash': prev_hash[i], 'index': prev_index[i], 'address': source_pair['address']} for i in range(len(prev_hash))]
    outputs = [{'address': target_address, 'value': value}]

    unsigned_tx, unsigned_tx_raw = make_tx(inputs, outputs)
    signed_tx = sign(unsigned_tx, source_pair)
    signed_tx_raw = serialize_tx(signed_tx)

    pprint(signed_tx)
    print(serialize_tx(signed_tx))

    pprint(pushtx(tx_hex=signed_tx_raw, api_key=token, coin_symbol='btc-testnet'))
