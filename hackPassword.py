import hashlib

from passlib.hash import sha512_crypt

passwordToHack = "$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0"

def hack(number):
    return sha512_crypt.using(salt="penguins", rounds=5000).hash(number)
    
def testHack():
    for x in range(0, 10):
        for y in range(0,10):
            for z in range(0,10):
                if hack(str(x)+str(y)+str(z)) == "$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0":
                    return str(x)+str(y)+str(z)


print(testHack())

