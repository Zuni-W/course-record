"""
椭圆加密算法中的椭圆和基点是公开的
例如国密SM2的公开参数
推荐使用素数域256位椭圆曲线。
椭圆曲线方程：y ^ 2 = x ^ 3 + ax + b。
曲线参数：
p  = FFFFFFFE FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF 00000000 FFFFFFFF FFFFFFFF
a  = FFFFFFFE FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF 00000000 FFFFFFFF FFFFFFFC
b  = 28E9FA9E 9D9F5E34 4D5A9E4B CF6509A7 F39789F5 15AB8F92 DDBCBD41 4D940E93
n  = FFFFFFFE FFFFFFFF FFFFFFFF FFFFFFFF 7203DF6B 21C6052B 53BBF409 39D54123
Gx = 32C4AE2C 1F198119 5F990446 6A39C994 8FE30BBF F2660BE1 715A4589 334C74C7
Gy = BC3736A2 F4F6779C 59BDCEE3 6B692153 D0A9877C C62A4740 02DF32E5 2139F0A0
"""
from Curve import *
from random import randint
from math import gcd,ceil,log2,floor
from SM3 import sm3bin,sm3hex

UNCOMPRESS = 0
COMPRESS = 1


def point2hex(g:Point):
        """将点通过横纵坐标拼接转换为字符串
        Input:  Point
        Output: HexStr
        """
        return '%064x%064x' % (int(g.x), int(g.y))

class SM2:
    def pow(self,g:int,a:int):
        """输出Fp域上元素g**a"""
        e = a % (self.p - 1)
        if e == 0:
            return 1
        e = bin(e)[2:]
        x = g
        for i in range(len(e)-2,-1,-1):
            x = x * x % self.p
            if e[-i-1] =='1':
                x = g*x % self.p
        return x % self.p

    def Lucas(self,x,y,k):
        """intput:X,Y,k;ouput:Uk,Vk"""
        if(k == 0):
            return 0,2
        U = 1
        V = x
        delta = (self.pow(x,2)-4*y)
        for i in range(len(bin(k))-4,-1,-1):
            U,V = U * V  % self.p, ((self.pow(V,2) + (delta * self.pow(U,2))) // 2) % self.p
            if bin(k)[-i-1] == '1':
                U,V = (((x*U+V))//2) % self.p, (((x*V+delta*U))//2) % self.p
        return U % self.p,V % self.p
    
    def sqrt(self,g):
        if g == 0:
            return 0
        if self.p % 4 == 3:
            u = self.p//4
            y = self.pow(g,u+1)
            z = self.pow(y,2)
            if z == g:
                return y
            else:
                raise None
        if self.p % 8 == 5:
            u = self.p//8
            z = (self.pow(g,2*u+1))%self.p
            if z == 1:
                return (self.pow(g,u+1))%self.p
            elif z == p-1 or z == -1:
                return (2*g*self.pow(4*g,u))%self.p
            else:
                return None
        if self.p % 8 == 1:
            u = self.p // 8
            Y= g
            while(1):
                X = randint(1,self.p - 1)
                U,V = self.Lucas(X,Y,4*u+1) 
                if self.pow(V,2) == (4*Y)%self.p:
                    return (V/2) % self.p
                if (U % self.p != 1) and (U % self.p != self.p-1):
                    return None



    def element2Bytes(self,x:int):
        """int in Fp to Hexstr,len is 32"""
        t = ceil(log2(self.p))
        l = ceil(t/8)*2
        return hex(x)[2:].zfill(l)

    def Bytes2element(self,s):
        """Hexstr to int in Fp"""
        return int(s,base=16) % self.p
    
    def yBar(self,P):
        return int(bin(P.y)[-1])
    
    def uncompress(self,xp,ybar):
        alpha = (pow(xp,3) + self.a * xp + self.b) % self.p
        beta = self.sqrt(alpha)
        if beta == None:
            print("the num don't have a sqrt solution.")
            raise Exception
        else:
            if(bin(beta)[-1] == str(ybar)):
                return beta
            else:
                return self.p - beta


    def Point2Bytes(self,P):
        X1=self.element2Bytes(P.x)
        if self.mode == COMPRESS:
            ybar=self.yBar(P)
            if ybar == 0:
                PC='02'
            elif ybar == 1:
                PC='03'
            else:
                raise Exception
            return PC+X1
        elif self.mode == UNCOMPRESS:
            Y1=self.element2Bytes(P.y)
            PC='04'
            return PC+X1+Y1
    
    def Bytes2Point(self,s):
        l = ceil(log2(self.p)/8)*2
        if self.mode == UNCOMPRESS:
            if(s[:2] =='04'):
                xp=self.Bytes2element(s[2:2+l])
                yp=self.Bytes2element(s[2+l:])
                return Point(self.E,xp,yp)
            else:
                raise Exception
        elif self.mode == COMPRESS:
            if(s[:2] =='02' or s[:2]=='03'):
                xp=self.Bytes2element(s[2:2+l])
                if s[:2] == '02':
                    ybar = 0
                else:
                    ybar = 1
                yp = self.uncompress(xp,ybar)
                return Point(self.E,xp,yp)
            else:
                raise Exception

    def __init__(self,mode = UNCOMPRESS):
        self.mode = mode
        self.a = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFC
        self.b = 0x28E9FA9E9D9F5E344D5A9E4BCF6509A7F39789F515AB8F92DDBCBD414D940E93
        self.p = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF
        self.q = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123
        gx = 0x32C4AE2C1F1981195F9904466A39C9948FE30BBFF2660BE1715A4589334C74C7
        gy = 0xBC3736A2F4F6779C59BDCEE36B692153D0A9877CC62A474002DF32E52139F0A0
        self.E = CurveFp(self.p, self.a, self.b)
        self.G = Point(self.E, gx, gy)
    
    def gen_keys(self):
        """
        pk:Hexstr(64)||Hexstr(64)
        sk:Hexstr(64)
        """
        sk = random.randint(2, self.q)
        while (gcd(sk, self.q) != 1):
            sk = random.randint(2, self.q)
        temp = sk * self.G
        return '%064x%064x' % (temp.x, temp.y), '%064x' % sk

    def init_keys(self):
        pk,sk = self.gen_keys()
        self.sk= int(sk,base=16)
        self.pk = Point(self.E,int(pk[:64],base=16),int(pk[64:],base=16))
        return
    
    def Hash(self,Hexstr):
        l = len(Hexstr) * 4
        return sm3hex(bin(int(Hexstr,base=16))[2:].zfill(l))
    
    def KDF(self,Z,klen):
        ct = 0x00000001
        Ha=[]
        for i in range(1,ceil(klen/256)+1):
            Ha.append(sm3bin(bin(int(Z,base=16))[2:]+bin(ct)[2:].zfill(32)))
            ct += 1
            ct =  ct&0xffffffff
        if klen%256 == 0:
            Ha.append(Ha[-1])
        else:
            Ha.append(Ha[-1][0:(klen%256)])
        return ''.join(Ha)[:klen]

    def encrypt(self,msg,pk):
        #msg为Hexstr
        msg  = bin(int(msg,base=16))[2:].zfill(len(msg)*4)
        k = randint(1,self.q)
        C1 = self.Point2Bytes(k*self.G)
        p2 = k*self.Bytes2Point('04'+pk)
        S = self.element2Bytes(p2.x) + self.element2Bytes(p2.y)
        t = self.KDF(S,len(msg))
        C2 = hex(int(msg,base=2) ^ int(t,base=2))[2:].zfill(len(msg)//4)
        C3 = self.Hash(self.element2Bytes(p2.x) + hex(int(msg,base=2))[2:] +self.element2Bytes(p2.y))
        return C1+C2+C3

    def decrypt(self,msg):
        #msg为Hexstr
        t = ceil(log2(self.q))
        l = ceil(t/8)*2
        if msg[:2] == '04':
            C1=msg[:2*l+2]
            C2=msg[2*l+2:-64]
        else:
            C1=msg[:l+2]
            C2=msg[l+2:-64]
        C3 = msg[-64:]
        try:
            p1 = self.Bytes2Point(C1)
        except:
            print("C1 is not a point on the E")
            return
        p2 = p1 * self.sk
        S = self.element2Bytes(p2.x) + self.element2Bytes(p2.y)
        t = self.KDF(S,len(C2)*4)
        plain = hex(int(t,base=2) ^ int(C2,base=16))[2:].zfill(len(C2))
        _C3 = self.Hash(self.element2Bytes(p2.x) + plain + self.element2Bytes(p2.y))
        if _C3 == C3:
            return plain
        else:
            print("C3 have a error")
            return None

if __name__ == "__main__":
    cipher = SM2()
    cipher.init_keys()
    pk=point2hex(cipher.pk)
    plaintext = 'a5'
    secret = cipher.encrypt(plaintext,pk)
    plain = cipher.decrypt(secret)
    print(secret)
    print(plain)