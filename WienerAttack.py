import RSA
import ContinuedFractions as CF
from Functions import *

keySet = RSA.RSA(512, True)
print('RSA key set generated')

N,e = keySet.getPublicKey()

fraction = CF.ContinuedFraction(e, N)
convergents = fraction.getConvergents()

crack_d = 0
for k,d in convergents:
    if k!=0 and (e*d)%k == 1:
        phiN = (e*d-1)//k
        s = N - phiN + 1
        disc = s*s - 4*N
        p = (s + Sqrt(disc) + 1) // 2
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
