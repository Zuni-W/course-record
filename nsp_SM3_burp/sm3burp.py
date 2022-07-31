import time
from subprocess import *

count=0
outlist = []
t1 = time.time()
for i in range(2**19):
    cmd = ['echo',str(i),'|','openssl','dgst','-sm3']
    p = Popen(' '.join(cmd),shell=True,stdout=PIPE)
    p.wait()
    output, unused_err = p.communicate()
    output = output.decode()[-9:-1]
    if output in outlist:
        count+=1
        print(i,outlist.index(output))
        t2 = time.time()
        break
        #print(outlist.index(output))
    else:
        outlist.append(output)

print(t2-t1)

#print(count)
#2**16 24041 16bit
#2**16 1928 20bit
#2**16 104 24bit
#2**16 4 28bit
#2**19 521  32bit
