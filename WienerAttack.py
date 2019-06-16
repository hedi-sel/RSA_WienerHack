import RSA
import ContinuedFractions as CF
from Functions import *

keySet = RSA.RSA(1024, True) #Generates a 1024-bits weak key, verifying the conditions to apply Wiener's theorem
print('RSA key set generated')

N,e = keySet.getPublicKey()

fraction = CF.ContinuedFraction(e, N) #Generates the continued fraction expantion of e/n
convergents = fraction.getConvergents()

crack_d = 0
for k,d in convergents:
    if k!=0 and (e*d)%k == 1:
        #We still need to check wether d is the right key
        phiN = (e*d-1)//k #If d is the right key, this should be equal to Phi(N)
        s = N - phiN + 1  #... and this should be equal to p+q
        # We solve the equation x²-sx+N = 0, the solutions should be p and q
        disc = s*s - 4*N
        p = (s + Sqrt(disc) + 1) // 2 #Sqrt computes the rounded down square root
        q = (s - Sqrt(disc)) // 2
        if (p*q == N):
            crack_d = d
            break

if (crack_d == keySet.d):
    print("We cracked the secret key!")
elif (crack_d == 0):
    print("We didn't find any candidate")
else:
    print("We found a wrong secret key :(")