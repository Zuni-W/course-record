from subprocess import *
from Crypto.Util.number import *

a='55bb48c7ad2434b92d964b1bcc5cb48ffd6b1221d2aecb3e46c2489d0a7627863160aee3df5e3cc049862f22bcf5071f161c00468b58bdff8328d952fd6c6c04'
for i in range(1,17):
        if call(["./dec_oracle",hex(int(a[64:64+32],16)^int((hex(i)[2:].zfill(2)),16))[2:]+a[64+32:] ])==200: 
            flag3=chr(i^1)*(i^1)
            print(i^1,flag3)

for k in range(len(flag3)+1,17): 
    for i in range(256):  
        if call(["./dec_oracle",hex(bytes_to_long(flag3.encode())^int(a[64:64+32],16)^int((hex(i)[2:].zfill(2)+(hex(k)[2:].zfill(2))*(k-1)),16))[2:]+a[64+32:] ])==200: 
            flag3=chr(i^k)+flag3                                      

t=32 
flag2="" 
for k in range(1,17): 
    for i in range(128):  
        if call(["./dec_oracle",hex(bytes_to_long(flag2.encode())^int(a[t:t+32],16)^int((hex(i)[2:].zfill(2)+(hex(k)[2:].zfill(2))*(k-1)),16))[2:].zfill(32)+a[t+32:t+64] ])==200: 
            flag2=chr(i^k)+flag2 

t=0
flag=""
for k in range(1,17):
    for i in range(128):
        if call(["./dec_oracle",hex(bytes_to_long(flag.encode())^int(a[t:t+32],16)^int((hex(i)[2:].zfill(2)+(hex(k)[2:].zfill(2))*(k-1)),16))[2:].zfill(32)+a[t+32:t+64] ])==200:
            flag=chr(i^k)+flag

print(flag+flag2+flag3)
