from collections import defaultdict
from RingSign_Pure import genK
import json
def SVkey():
    key = genK()
    sk = key[1]
    vk = key[0]
    return sk,vk
def makejson(keynum):
    port=50051
    keylist=defaultdict(list)
    for i in range(keynum):
        t=SVkey()
        keylist[port].append(t[0])
        keylist[port].append(t[1])
        port+=2
    json_str = json.dumps(keylist, indent=4)
    with open('./keys/svkey.json', 'w') as json_file:
        json_file.write(json_str)
    return

if __name__ == "__main__":
    makejson(5)