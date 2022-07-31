def exgcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = exgcd(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y, q


def inv(a,p):
    t=exgcd(a,p)
    if t[2]==0:
        return "wrong"
    else :
        return (t[0]%p+p)%p

def is_sqrt(x,p):
    if pow(x,(p-1)//2,p)==1:
        return True
    else :
        return False

def sqrt(x,p):
    return pow(x,(p-3)//4+1,p)

class point():
    def __init__(self,gx,gy="no"):
        if gy=="no" and type(gx)==str:
            self.x=int(gx[:len(gx)//2],16)
            self.y=int(gx[len(gx)//2:],16)
        elif gy=="no" and type(gx)==bytes:
            self.x=bytes_to_long(gx[:len(gx)//2])
            self.y=bytes_to_long(gx[len(gx)//2:])
        else:
          if type(gx)==str:
              self.x=int(gx,16)
          elif type(gx)==bytes:
              self.x=bytes_to_long(gx)
          else:
              self.x=gx
          if type(gy)==str:
              self.y=int(gy,16)
          elif type(gy)==bytes:
              self.y=bytes_to_long(gy)
          else:
              self.y=gy

    def __eq__(self,other):
        return self.x==other.x and self.y==other.y

    def __str__(self):
        return str((self.x,self.y))

    def bytes(self):
        return long_to_bytes(self.x)[:].rjust(32,b"\0")+long_to_bytes(self.y)[:].rjust(32,b"\0")

    def bytesxy(self):
        return long_to_bytes(self.x)[2:].rjust(32,b"\0"),long_to_bytes(self.y)[2:].rjust(32,b"\0")

class ECC():
    def __init__(self,p,n,a,b,G):
        self.p=p
        self.n=n
        self.a=a
        self.b=b
        self.G=G
        assert(self.p%4==3)
        assert(((self.G.x**3+self.G.x*self.a+self.b)%self.p)==((self.G.y**2)%self.p))
        assert((4*self.a**3+27*self.b**2)%self.p!=0)

    def check(self,G):
        assert(((G.x**3+G.x*self.a+self.b)%self.p)==((G.y**2)%self.p))


    def add_point(self,G1,G2):
        if G1.x==G2.x and G1.y!=G2.y:
            return point(0,0)
        if G1==point(0,0):
            return G2
        if G2==point(0,0):
            return G1
        if G1==G2:
            t=(((3*G1.x**2+self.a)%self.p)*inv(G1.y*2,self.p))%self.p
        else:
            t=(((G1.y-G2.y)%self.p)*inv((G1.x-G2.x)%self.p,self.p))%self.p
        Px=(t**2 - G1.x - G2.x)%self.p
        Py=((t*(G1.x-Px)%self.p) - G1.y)%self.p
        return point(Px,Py)

    def mul(self,k0,G1):
        tmp=G1
        ans=point(0,0)
        while k0!=0:
            if k0&1!=0:
                ans=self.add_point(ans,tmp)
            tmp=self.add_point(tmp,tmp)
            k0>>=1
        return ans

    def getpoint(self):
        ans=point(0,0)
        while 1:
            x=randint(1,self.p)
            if is_sqrt(x**3+x*self.a+self.b,self.p):
                y=sqrt(x**3+x*self.a+self.b,self.p)
                ans=point(x,choice([y,self.p-y]))
                break
        return ans


from hashlib import sha256
from Crypto.Util.number import *
SHA256=lambda x:long_to_bytes(int(sha256(x).hexdigest(),16))[2:].rjust(32,b"\0")

def KDF(Z,klen):
    ans=b""
    ct=1
    for i in range(0,klen,32):
        ans+=SHA256(Z+(long_to_bytes(ct).rjust(4,b"\0")))
        ct+=1
    return ans[:klen]


def Z(E,ID,Q):
    if type(ID)==str:
        ID=ID.encode()
    return SHA256(long_to_bytes(len(ID)*8).rjust(2,b"\0")+ID+long_to_bytes(E.a).rjust(32,b"\0")+long_to_bytes(E.b).rjust(32,b"\0")+E.G.bytes()+Q.bytes())

def sign(E,q,Z,M):
    M1=Z+M
    e=bytes_to_long(SHA256(M1))
    k=randint(1,E.p)
    x1=E.mul(k,E.G).x
    r=(e+x1)%E.n
    assert(r!=0)
    assert(r+k!=E.n)
    s=((k-r*q)*inv(1+q,E.n))%E.n
    assert(s!=0)
    return long_to_bytes(r).rjust(32,b"\0")+long_to_bytes(s).rjust(32,b"\0")

def verify(E,Q,Z,M,S):
    r,s=S[:len(S)//2],S[len(S)//2:]
    e=bytes_to_long(SHA256(Z+M))
    r=bytes_to_long(r)
    s=bytes_to_long(s)
    t=(s+r)%E.n
    assert(t!=0)
    x1=E.add_point(E.mul(s,E.G),E.mul(t,Q)).x
    return ((e+x1)%E.n)==(r%E.n)
    




    
ecc_table = {
    'n': 'FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123',
    'p': 'FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF',
    'g': '32c4ae2c1f1981195f9904466a39c9948fe30bbff2660be1715a4589334c74c7'
         'bc3736a2f4f6779c59bdcee36b692153d0a9877cc62a474002df32e52139f0a0',
    'a': 'FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFC',
    'b': '28E9FA9E9D9F5E344D5A9E4BCF6509A7F39789F515AB8F92DDBCBD414D940E93',
}

from random import *
G=point(ecc_table["g"])
E=ECC(p=int(ecc_table["p"],16),n=int(ecc_table["n"],16),a=int(ecc_table["a"],16),b=int(ecc_table["b"],16),G=G)



M=b"helloworld"
q=randint(1,E.p)
Q=E.mul(q,G)

ID=b"Zuni-W"
myZ=Z(E,ID,Q)

S=sign(E,q,myZ,M)

print(S)

ans=verify(E,Q,myZ,M,S)

print(ans)
