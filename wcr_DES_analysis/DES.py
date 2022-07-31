import random
import time


key_chart=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,
10,2,59,51,43,35,27,19,11,3,60,52,44,36,
63,55,47,39,31,23,15,7,62,54,46,38,30,22,
14,6,61,53,45,37,29,21,13,5,28,20,12,4]

key_48_chart=[14,17,11,24,1,5,3,28,15,6,21,10,
23,19,12,4,26,8,16,7,27,20,13,2,
41,52,31,37,47,55,30,40,51,45,33,48,
44,49,39,56,34,53,46,42,50,36,29,32]


S_boxs=[
[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13],
[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9],
[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,
13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,
13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12],
[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,
13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,
10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14],
[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,
14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,
4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,
11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3],
[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,
10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,
9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,
4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13],
[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,
13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,
1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,
6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12],
[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,
1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,
7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,
2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]

P_box=[16,7,20,21,29,12,28,17,
1,15,23,26,5,18,31,10,
2,8,24,14,32,27,3,9,
19,13,30,6,22,11,4,25]


def key_ip(key):
    ipkey=[]
    for item in key_chart:
        ipkey.append(int(key[item-1]))
    return ipkey
def generate_key(ipkey):
    keymid1=ipkey[1:28]+ipkey[0:1]+ipkey[29:]+ipkey[28:29]
    keymid2=keymid1[1:28]+keymid1[0:1]+keymid1[29:]+keymid1[28:29]
    keymid3=keymid2[2:28]+keymid2[0:2]+keymid2[30:]+keymid2[28:30]
    key1=[]
    for item in key_48_chart:
        key1.append(keymid1[item-1])
    key2=[]
    for item in key_48_chart:
        key2.append(keymid2[item-1])
    key3=[]
    for item in key_48_chart:
        key3.append(keymid3[item-1])
    return key1,key2,key3

def key_inv48_56(x):
    t=["?"]*56
    for i in range(48):
        t[key_48_chart[i]-1]=x[i]
    return "".join(t)

def key_inv56_64(x):
    t=["0"]*64
    for i in range(56):
        t[key_chart[i]-1]=x[i]
    return "".join(t)


def key3_to_key(x):
    x1=key_inv48_56(x)
    k1=x1[24:28]+x1[:24]+x1[28+24:28+28]+x1[28:28+24]
    k=key_inv56_64(k1)
    return k

def compare(x,y):
    if len(x)!=len(y):
        print("wrong")
    for i in range(len(x)):
        if x[i]!=y[i] and x[i]!="?" and y[i]!="?":
            return False
    return True    
        
def E_extend(ipci):
    eci1=ipci[31:32]+ipci[0:5]
    eci2=ipci[3:9]
    eci3=ipci[7:13]
    eci4=ipci[11:17]
    eci5=ipci[15:21]
    eci6=ipci[19:25]
    eci7=ipci[23:29]
    eci8=ipci[27:]+ipci[0:1]
    return eci1,eci2,eci3,eci4,eci5,eci6,eci7,eci8



def row_col(eci):
    row=eci[0]*2+eci[5]
    col=eci[1]*8+eci[2]*4+eci[3]*2+eci[4]
    return row*16+col


def list_xor(list1,list2):
    ans=[]
    for i in range(len(list1)):
        ans.append(list1[i]^list2[i])
    return ans

E=lambda x:((x>>1)&0xf)|(x&0x20)|((x&1)<<4)

def S_box(eci1,eci2,eci3,eci4,eci5,eci6,eci7,eci8,key):
    eci11=list_xor(eci1,key[0:6])
    eci21=list_xor(eci2,key[6:12])
    eci31=list_xor(eci3,key[12:18])
    eci41=list_xor(eci4,key[18:24])
    eci51=list_xor(eci5,key[24:30])
    eci61=list_xor(eci6,key[30:36])
    eci71=list_xor(eci7,key[36:42])
    eci81=list_xor(eci8,key[42:])
    col1=row_col(eci11)
    col2=row_col(eci21)
    col3=row_col(eci31)
    col4=row_col(eci41)
    col5=row_col(eci51)
    col6=row_col(eci61)
    col7=row_col(eci71)
    col8=row_col(eci81)
    s1=bin(S_boxs[0][col1])[2:].zfill(4)
    s2=bin(S_boxs[1][col2])[2:].zfill(4)
    s3=bin(S_boxs[2][col3])[2:].zfill(4)
    s4=bin(S_boxs[3][col4])[2:].zfill(4)
    s5=bin(S_boxs[4][col5])[2:].zfill(4)
    s6=bin(S_boxs[5][col6])[2:].zfill(4)
    s7=bin(S_boxs[6][col7])[2:].zfill(4)
    s8=bin(S_boxs[7][col8])[2:].zfill(4)
    return s1+s2+s3+s4+s5+s6+s7+s8

def P_exchange(s):
    p=[]
    for item in P_box:
        p.append(int(s[item-1]))
    return p



def enc(left,right,key):
    eci1,eci2,eci3,eci4,eci5,eci6,eci7,eci8=E_extend(right)
    S=S_box(eci1,eci2,eci3,eci4,eci5,eci6,eci7,eci8,key)
    P=P_exchange(S)
    plainmid=list_xor(left,P)
    return plainmid

def print_pl(plaintext):
    ans=[]
    for i in range(0,64,4):
        ans.append(hex(plaintext[i]*8+plaintext[i+1]*4+plaintext[i+2]*2+plaintext[i+3])[2:])
    print("The plaintext is:",''.join(ans))
    return ans



def DES3(ciphertext,key):
    ipkey=key_ip(key)
    key1,key2,key3=generate_key(ipkey)
    L0,R0=[int(i) for i in ciphertext[:32] ],[int(i) for i in ciphertext[32:]]
    L1=R0
    R1=enc(L0,R0,key1)
    L2=R1
    R2=enc(L1,R1,key2)
    L3=R2
    R3=enc(L2,R2,key3)
    return "".join([str(i) for i in L3+R3])


Sdiff=[[[set() for k in range(2**4)] for j in range(2**6)] for i in range(8)]
Sdiff1=[[[0 for k in range(2**4)] for j in range(2**6)] for i in range(8)]

for i in range(8):
    for j in range(2**6):
        for k in range(2**6):
            Sdiff[i][j][S_boxs[i][E(k)]^S_boxs[i][E(k^j)]]|={k}
            Sdiff1[i][j][S_boxs[i][E(k)]^S_boxs[i][E(k^j)]]+=1

def xor(str1,str2):
    if len(str1)!=len(str2):
        print("wrong")
    t=""
    for i in range(len(str1)):
        if str1[i]==str2[i]:
            t+="0"
        else:
            t+="1"
    return t        
def Pinv(str1):
    t=[0]*32
    for i in range(32):
        t[P_box[i]-1]=str1[i]
    return "".join(t)

def differ_analysis(m0,m1,c0,c1):
    ss=xor(c0[:32],c1[:32])
    s=xor(m0[:32],m1[:32])
    al=xor(s,xor(c0[32:],c1[32:]))
    Sin=list(E_extend(ss))
    Sc=list(E_extend(c0[:32]))
    a=Pinv(al)

    keyset1=[set() for i in range(8)]
    for i in range(8):
        t=(Sdiff[i][(int(Sin[i],2))][(int(a[i*4:i*4+4],2))])
        for j in t:
            keyset1[i]|={(j)^int(Sc[i],2)}
    return keyset1

\
"""
明文：0X80CB4F7C993B1782 密文：0X746A0EFD1EE535D4
明文：0XEBEB4AF9993B1782 密文：0X626106E0607EC3BD

明文：0X54A281EFDCD118C9 密文：0XB29D363555820170
明文：0X2812AC18DCD118C9 密文：0X6D0DC7CE3844BE01

"""


m0=bin(0X80CB4F7C993B1782)[2:].zfill(64)
m1=bin(0XEBEB4AF9993B1782)[2:].zfill(64)
c0=bin(0X746A0EFD1EE535D4)[2:].zfill(64)
c1=bin(0X626106E0607EC3BD)[2:].zfill(64)
keyset1=differ_analysis(m0,m1,c0,c1)
m0=bin(0x54a281efdcd118c9)[2:].zfill(64)
m1=bin(0x2812ac18dcd118c9)[2:].zfill(64)
c0=bin(0xb29d363555820170)[2:].zfill(64)
c1=bin(0x6d0dc7ce3844be01)[2:].zfill(64)

keyset2=differ_analysis(m0,m1,c0,c1)

for i in range(8):
    print(keyset1[i])
print()
for i in range(8):
    print(keyset2[i])

print()
keyset=[]
for i in range(8):
    print(keyset2[i]&keyset1[i])
    keyset.append(keyset2[i]&keyset1[i])


key3=[""]
for i in keyset:
    key3_new=[]
    for j in i:
        for k in key3:
            key3_new.append(k+bin(j)[2:].zfill(6))
    key3=key3_new

def test(p):
    def t(x):
        j=0
        k=""
        for i in p:
            if i=="?":
                k+=x[j]
                j+=1
            else:
                k+=i
        if compare(DES3(m0,k),c0):
            print(k)
        return compare(DES3(m0,k),c0)
    return t            
   


from pwn import *
from pwnlib.util.iters import mbruteforce
ans=[]
for i in key3:
    t=key3_to_key(i)
    print(t)
    ans.append([t,mbruteforce(test(t),"01",t.count("?"),method="fixed")])

for i in ans:
    if None not in i:
        print(test(i[0])(i[1]))
        m1,m0=m0,m1
        c1,c0=c0,c1
        print(test(i[0])(i[1]))

