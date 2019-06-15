import RSA
import ContinuedFractions as CF
from Functions import *

keySet = RSA.RSA(528, True)
print('RSA key set generated')

N,e = keySet.getPublicKey()

fraction = CF.ContinuedFraction(e, N)
convergents = fraction.getConvergents()

crack_d = 0
for k,d in convergents:
    if k!=0 and (e*d)%k == 1:
        phiN = (e*d-1)//k
        s = N - phiN



print (keySet.decrypt(keySet.encrypt( 777 )))

print((d*e) % keySet.phiN == 1)
