# -*- coding: utf-8 -*-
# Copyright © 2022 F0rest <si1encef0rest@outlook.com>
# Thank you for frey's code of Curve
# Distributed under terms of the MIT license.

import random
from hashlib import sha256
from Curve import Point, CurveFp, inv_mod
from math import gcd
import json


def read_PK():
    """读取公钥文件
    Input:  None
    Output: PK[HexStr1,HexStr2,...]
    """
    PK = []
    with open('./keys/svkey.json', 'r', encoding='utf8') as fp:
        svkey = json.load(fp)
        for i in svkey.keys():
            PK.append(svkey[i][1])
    PK.sort()
    return PK


def read_ecc_table():
    """"读取椭圆曲线配置文件
    Input: None
    Output: (direction)ecc_table{基点g,椭圆曲线的阶q,大素数p,a,b}
    """
    ecc_table = {}
    with open("./keys/ecc_table.txt", "r") as f:
        ecc_table['q'] = f.readline().strip()
        # n是基点的阶
        ecc_table['p'] = f.readline().strip()
        ecc_table['g'] = f.readline().strip()
        # g就是基点
        ecc_table['a'] = f.readline().strip()
        ecc_table['b'] = f.readline().strip()
    return ecc_table


def genK():
    """生成公私钥对
    Input:  None 读取椭圆曲线配置文件
    Output: 输出128位宽Pk(HEXStr),64位宽Sk(HEXStr)
    """
    ecc_table = read_ecc_table()
    a = int(ecc_table['a'], base=16)
    b = int(ecc_table['b'], base=16)
    p = int(ecc_table['p'], base=16)
    q = int(ecc_table['q'], base=16)
    g = ecc_table['g']
    gx = int(ecc_table['g'][:len(g) // 2], base=16)
    gy = int(ecc_table['g'][len(g) // 2:], base=16)
    E = CurveFp(p, a, b)
    G = Point(E, gx, gy)
    sk = random.randint(2, q)
    while (gcd(sk, q) != 1):
        sk = random.randint(2, q)
    temp = sk * G
    return '%064x%064x' % (temp.x, temp.y), '%064x' % sk


class RingSign:
    def __init__(self, sk, pk):
        ecc_table = read_ecc_table()
        self.a = int(ecc_table['a'], base=16)
        self.b = int(ecc_table['b'], base=16)
        self.p = int(ecc_table['p'], base=16)
        self.q = int(ecc_table['q'], base=16)
        g = ecc_table['g']
        gx = int(ecc_table['g'][:len(g) // 2], base=16)
        gy = int(ecc_table['g'][len(g) // 2:], base=16)
        self.E = CurveFp(self.p, self.a, self.b)
        self.G = Point(self.E, gx, gy)
        self.PK = read_PK()
        # self.PK=['58db65e432c126a9b8b13e3d64aa656547eab29271d9d332291a8731540913bc807fad0ae4dc2405875b248455b786e1d9b46e4bf82b9c95601e4f03d34db1b8',
        #            '25d8084843c007ffb1361105232f0dec8cdebc3796f3c62511309eca13dabf873dbbe087961aefefbfa893eee9f21348a62611c3ccb3f55168a52abb2c0d49f8','0be9b1a1cefdd34fc4e46e7590e5a7faaacafc8c5dfffe77d31a2296a32ac4d9485b06e8eee1e490b538171b0bbfbbceeed1389801a1bbeb830017917196af45']
        self.sk, self.pk = sk, pk
        self.SIZE = len(self.PK)
        self.S = self.genS()

    def genS(self):
        """
        Input:  None 读取椭圆曲线配置文件
        Output: S[int,int,...]
        """
        q = self.q
        S = []
        for i in range(self.SIZE):
            s = random.randint(2, q)
            while (gcd(s, q - 1) != 1):
                s = random.randint(2, q)
            # TODO:s的范围可能有点问题
            S.append(s)
        return S

    def H(self, PK, msg, Z):
        """
        L=PK["hexstr1","hexstr2",...],msg为bytes,Z为HexStr
        输出为Z_q^*上数值
        """
        q = self.q
        data = msg.hex()
        str = "".join(PK) + data + Z
        hash = sha256(str.encode()).hexdigest()
        return int(hash, base=16) % q

    def point2hex(self, g):
        """将点通过横纵坐标拼接转换为字符串
        Input:  Point
        Output: HexStr
        """
        return '%064x%064x' % (int(g.x), int(g.y))

    def culc_s(self, q, k, sk, Ci):
        """计算S[i]
        Input:  (int)曲线的阶q,(int)随机选取的k,(int)私钥sk,(int)C[i]
        Output: (int)S[i]
        """
        invert = inv_mod(1 + sk, q)
        temp = k - Ci * sk
        return invert * temp % q

    def culc_z(self, pk, Ci, Si):
        """计算Z[i]
        Input:  节点i的公钥pk,(int)C[i],(int)S[i]
        Output: (int)S[i]
        """
        G = self.G
        sg = int(Si) * G
        sc = (Si + Ci)
        point = Point(self.E, int(pk[:64], base=16), int(pk[64:], base=16))
        return self.point2hex(sg + int(sc) * point)

    def RSign(self, msg):
        """对消息msg进行签名
                Input:  (bytes)msg
                Output: (list)sign[int,int,int,...]
        """
        SIZE = self.SIZE
        PK = self.PK
        pk = self.pk
        q = self.q
        G = self.G
        sk = self.sk
        S = self.S
        C = ['0'] * SIZE
        index = PK.index('%0128x' % (pk))
        k = random.randint(2, q)
        while (gcd(k, q) != 1):
            k = random.randint(2, q)
        # print(self.point2hex(k*G))
        # print(k)
        C[(index + 1)%SIZE] = self.H(PK, msg, self.point2hex(k * G))
        numbers = [j for j in range(index + 1, SIZE)] + [j for j in range(index)]
        for i in numbers:
            Zi = self.culc_z(PK[i], C[i], S[i])
            C[(i + 1) % SIZE] = self.H(PK, msg, Zi)
        S[index] = self.culc_s(q, k, sk, C[index])
        sign = [C[0]] + S
        return sign

    def RVerify(self, msg, sign):
        """对消息msg的签名sign进行校验
        Input:  (bytes)msg (list)sign[int,int,int,...]
        Output: (boolean)Ture/False
        """
        SIZE = self.SIZE
        PK = self.PK
        q = self.q

        C_ = [sign[0]] + [0] * (SIZE)
        S_ = sign[1:]
        for i in range(SIZE):
            if (gcd(C_[i], q) != 1 or gcd(S_[i], q) != 1):
                return False
            Zi = self.culc_z(PK[i], C_[i], S_[i])
            C_[i + 1] = self.H(PK, msg, Zi)
        if (C_[0] != C_[SIZE]):
            return False
        else:
            return True


if __name__ == "__main__":
    sk = 0xbc5c1ca07f682407d97302a07b5206078df5fc1f907efd00257dfdcad8979ba4
    pk = 0xfc7519ff51bb9cd87fe354c95e541c63e99ca9e522ed3e5ebc3de34dbf8419a97ef0a266f8e5ec84a0cd04051275271a018a5a75f44bfba04ffe6e6bff351756
    Cipher = RingSign(sk, pk)
    msg = b'hello'
    #print(msg.decode())
    sign = Cipher.RSign(msg)
    #sign = [0x71FF7FFF2CFF42FF5549FFFF12623206FFFFFF2DFFFFFFFFFF24674F0E522672,0x340B86AB8757AAE47FF68F0D768C52798F7CCB015A1A8533E861C2DF4143C448,0xF741F55B0567DBA18961ED7F81D37EB3CA6746A3979DEC5C5DA8EE112B33DA4A,0xE823D7DFD46C4452667447E10B48831F4FD984EEF38F366A9556459B97CE7D33,0x41FC5D5FA4703EA2E0FA80F488ED6F25421E3473EB41DCDED4F4D5B80EE58EED,0x2A8DB09268E590457F8BC7B7B77BD2EE7BEB665D67FE52304C8A160DB8ED7621]
    signhex = list(map(hex,sign))
    print(signhex)
    print(Cipher.RVerify(msg, sign))
    #sign = [sign[0]+10000000] + sign[1:]
    #print(sign)
    #print(Cipher.RVerify(msg, sign))
    # print(genK())