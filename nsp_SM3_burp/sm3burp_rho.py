#rho碰撞
import os
import time
import random
from subprocess import *
import SM3

global n

def sm3(x):
    cmd = ['echo',str(x),'|','openssl','dgst','-sm3']
    p = Popen(' '.join(cmd),shell=True,stdout=PIPE)
    p.wait()
    output, unused_err = p.communicate()
    output=output.decode()[-65:-1]
    return output

def f_(a):
    global n
    return int(sm3(a)[:n//4],base=16)

def f(a):
    global n
    return int(SM3.sm3hex(a)[:n//4],base=16)

def rho_method(x):
    x1 = x
    x2 = f(x)
    chain = [x1]
    t3 = time.time()
    while(f(x1) != f(x2)):
        x1 = f(x1)
        chain.append(x1)
        x2 = f(f(x2))
    if(x1 == x2):
        chain.append(x1)
        return chain,None
    return  x1,x2

def get_collsion(length):
    global n
    n = length
    t1 = time.time()
    for i in range(10):
        t = random.randint(2,2**(n//2))
        a,b = rho_method(t)
        if(b != None):
            print(a,b)
            break
        else:
            x=a[-1]
            while(f(x) not in a):
                x=f(x)
                a.append(x)
            a.append(f(x))
            enter = a.index(a[-1])
            print(a[enter-1],a[-2])
            print(SM3.sm3hex(a[enter-1]),SM3.sm3hex(a[-2]))
            break
    t2 = time.time()
    print(t2-t1)

#24bit 10171825 15716607 67.73195576667786
#32bit 2892063108 4115544131 1318.8399724960327
#40bit 155312306235 164714478065 17311.484718561172
get_collsion(40)