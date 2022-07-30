IV = [0x7380166F, 0x4914B2B9, 0x172442D7, 0xDA8A0600,
      0xA96F30BC, 0x163138AA, 0xE38DEE4D, 0xB0FB0E4E]

def ROL(x,offset):
    return (((x<<offset) | (x>>(32-offset))) & 0xFFFFFFFF)

def FF(X,Y,Z,i):
    if i>=0 and i<=15:
        return X ^ Y ^ Z
    else:
        return ((X & Y) | (X & Z) | (Y & Z))

def GG(X,Y,Z,i):
    if i>=0 and i<=15:
        return X ^ Y ^ Z
    else:
        return ((X & Y) | (~X & Z))
    
def P0(s):
    return s^ROL(s,9)^ROL(s,17)

def P1(s):
    return s^ROL(s,15)^ROL(s,23)

def T(i):
    if i>=0 and i<=15:
        return 0x79cc4519
    else:
        return 0x7a879d8a

def msg_padding(m):
    length = len(m)
    m = m+'1'+('0'*(448-(length+1)%512))+bin(length)[2:].zfill(64)
    return m

def msg_extension(b):
    #print(len(b))
    W=[int(b[i:i+32],base=2) for i in range(0,len(b),32)]
    W1=[]
    for j in range(16,68):
        temp = P1(W[j-16] ^ W[j-9] ^ ROL(W[j-3],15)) ^ ROL(W[j-13],7)^W[j-6]
        W.append(temp)
    for j in range(0,64):
        W1.append(W[j]^W[j+4])
    return W,W1

def check(v):
    print(''.join([hex(i)[2:] for i in v]))

def msg_compress(v,putin):
    A,B,C,D,E,F,G,H = v
    a,b,c,d,e,f,g,h = v
    W,W1 = msg_extension(putin)
    for j in range(64):
        SS1 = ROL((ROL(A,12)+E+ROL(T(j),j%32))%(2**32),7)
        SS2 = SS1 ^ ROL(A,12)
        TT1 = (FF(A,B,C,j)+D+SS2+W1[j])%(2**32)
        TT2 = (GG(E,F,G,j)+H+SS1+W[j])%(2**32)
        D = C
        C = ROL(B,9)
        B = A
        A = TT1
        H = G
        G = ROL(F,19)
        F = E
        E = P0(TT2)
        out = [a^A,b^B,c^C,d^D,e^E,f^F,g^G,h^H]
        #逐轮check
        #print(j,end=' ')
        #check(out)
    out = [a^A,b^B,c^C,d^D,e^E,f^F,g^G,h^H]
    return out


def SM3(m):
    v = IV
    m = msg_padding(m)
    #print(m)
    block = [m[i:i+512] for i in range(0,len(m),512)]
    #print('block_num',len(block))
    v = msg_compress(v,block[0])
    
    for i in block[1:]:
        #print(i)
        v = msg_compress(v,i)
    return v
    
def sm3hex(msg):
    msg = bin(msg)[2:].zfill(8)
    return ''.join([hex(i)[2:].zfill(8) for i in SM3(msg)])

#print(sm3hex(49))