import random
from SM3 import SM3,sm3hex
from SM2 import SM2
import json
from Crypto.Cipher import AES
import binascii

class PGP:
    def __init__(self):
        self.sm2 = SM2()
        self.sm2.init_keys()
        self.bs = 16
        self.PADDING = lambda s: s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)
        self.sk = self.sm2.sk
        self.pk = self.sm2.pk


    def digest(self,msg):
        hash = sm3hex(bin(int(msg.hex(),base=16))[2:])
        return hash

    def send(self,origin,pk):
        hash = self.digest(origin.encode())
        mac = self.sm2.sign(hash.encode())
        send_msg = origin+'#'+json.dumps(mac, ensure_ascii=True)
        text = send_msg
        key = b'1234567890abcdef'
        aes = AES.new(key, AES.MODE_ECB)
        cipher = aes.encrypt(self.PADDING(text).encode())
        en_key = self.sm2.encrypt(key.hex()[2:],pk)
        return  (en_key,cipher)

    def recv(self,kc,pk):
        en_key,cipher = kc
        key = b'1234567890abcdef'
        aes = AES.new(key, AES.MODE_ECB)
        plain = aes.decrypt(cipher)
        origin_, mac_ = plain.decode().split('#')
        mac_ = json.loads(mac_[:-ord(mac_[-1])])
        hash = self.digest(origin_.encode())
        if self.sm2.verify(hash.encode(),mac_[0],mac_[1],pk) == False:
            return  False
        return origin_

if __name__ == "__main__":
    A = PGP()
    B = PGP()
    bPk = '%064x%064x' % (int(B.pk.x), int(B.pk.y))
    aPk = '%064x%064x' % (int(A.pk.x), int(A.pk.y))
    email = "ToDifficult"
    t = A.send(email, bPk)
    print(B.recv(t, aPk))