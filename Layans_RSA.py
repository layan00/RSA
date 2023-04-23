# This file consist of Layan's implementation of RSA cryptosystem of text files
# last edited 4/23/2023
# RSA system reqs:
#               - pick and save two random 512-bit primes p and q (p != q)
#               - print n = p*q  to topSecret.txt
#               - get Phi = (p-1)*(q-1)
#               - get e must be co-prime to phi and < phi
#               - get d s.t. 1 < d < ϕ, s.t. ed ≡ 1 mod ϕ
# funcs: Encryption c = (msg ^ e) % n
#        Decryption m = (c ^ d) % n


#includes
import random
import EEthm


# test if a number is prime
# standard primality test from wikipedia; I modified it a little bit.
def Rabin_Miller(num, k=25):
     
    r,s = 0, num-1
    
    # to speed up the R-M exponentiation step 
    while s % 2 == 0:
        r += 1
        s //= 2 
    for _ in range(k):
        a = random.randrange(2,num-1)
        x = pow(a,s,num)
        if x == 1 or x == num-1:
            continue
        for _ in range(r-1):
            x = pow(x,2,num)
            if x == num - 1:
                break # probably prime
        else:
            return False
    return True

#   pick random distinct primes p and q
def pickqp():
    # generate random integers under the range of 512 for each p and q where p*q = 1024-bits
    while True:
        # pick random number and guarantee that it is of size 512
        p = random.getrandbits(511) + (1 << 511) 
        # Miller-Rabin test
        if(Rabin_Miller(p)):
           break
        
    while True:
        # pick random number and guarantee that it is of size 512 and != p
        q = random.getrandbits(511) + (1 << 511) 
        # Miller-Rabin test
        if(Rabin_Miller(q) and p != q):
            break

    return p, q ;

def gcd(a,b):
        return EEthm.EEthm(a,b)

def get_e(phi):

    while True:
        e = random.randint(2,phi-1)
        if gcd(e,phi):
            return e

def Encrypt(n,e, message):

    #c = (msg ^ e) % n
    with open(message,'r') as fofo: 
            while 1:
                x = fofo.read(1)    # reads message file byte by byte
                if not x:
                    wr.close()
                    break
                print(x)
                with open("cipher.txt", 'a') as wr:    
                    wr.write(str(pow(ord(x),e,n))) # write to file as string
                    if x == ' ' or '\n':
                        wr.write('\n')


def Decrypt(file, n, d):
    with open(file, 'r') as fifi:
        for line in fifi.readlines():
            x = int(line)    # reads message file byte by byte
            with open("hw1_dec.txt", 'a') as wr:    
                wr.write(chr(pow(x,d,n))) # write to file as string
                wr.close()            

def main():
    
    ans = input("Would you like to (e)ncrypt or (d)ecrypt file? ")

#-----------------Encrypt-----------------#

    if ans == 'e':
        yn = input("do you want to encrypt using your own n and e keys?(y/n) ")
        if yn == 'y':
            file = input("please input file name for keys n and e: ")
            with open(file, 'r') as f:
                    n = int(f.readline())
                    e = int(f.readline())
                    f.close()
            message = input("please input message file: ") 
            Encrypt(n,e, message)
        
        elif yn == 'n':
            # compute RSA keys 
            p,q = pickqp()
            # n is of size approximately 1024
            n = p * q 
            phi = (p-1)*(q-1)

            # Choose an integer e, 1 < e < ϕ, such that gcd(e,ϕ)=1
            e = get_e(phi)

            # in case we wanted to encrypt using the same keys
            with open("ne.txt", "w") as wr:
                wr.write(str(n))
                wr.write('\n')
                wr.write(str(e))
                wr.close()
           
            #get d from the pulverizer where 1 < d < ϕ, s.t. ed ≡ 1 mod ϕ
            d = EEthm.get_d(phi,e)

            # print n and d to topSecret.txt
            with open("topSecret.txt", "w") as wr:
                wr.write(str(n))
                wr.write('\n')
                wr.write(str(d))
                wr.close()
            message = input("please input message file: ")
            Encrypt(n,e,message)

#-----------------Decrypt-----------------#
    elif ans == 'd':
        cipherf = input("Input cipher file: ") 
        keysf = input("Input public and secret keys' file [n,d]: ") # topSecret.txt
        with open(keysf, 'r')as f:
            n = int(f.readline())
            d = int(f.readline())
            f.close()
        Decrypt(cipherf, n, d)


main()

# end of program #