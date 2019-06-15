from random import randint
from math import sqrt

def GenPrime(Min, Max):
    while True:
        n = randint(Min//2, Max//2)*2+1
        if CheckPrime_MillerRabin(n,10**-20):
            return n

def CheckPrime_Basic(n):
    if (n==1):
        return False
    for i in range(2,int(sqrt(n))+1):
        k=n*1.0/i
        if k==int(k):
            return False
    return True
def CheckPrime_MillerRabin(n,p):
    r=1
    if (n<100):
        return(CheckPrime_Basic(n))
    elif n%2==0:
        return(False)
    s=0
    d=n-1
    while d%2==0:
        s+=1
        d=d//2
    while r>p:
        a=randint(2,n-1)
        t=False
        A=ExponentiationRapide(a,d,n)
        t=(A==1)
        i=0
        while i<s and t==False:
            t=(A==n-1 or t)
            A=A**2%n
            i+=1
        if t==False:
            return(t)
        r=r/4
    return(True)

def ExponentiationRapide(g,n,p): #Calcule g**n [mod p]
    k=n
    r=g%p
    u=1
    while k>1:
        if k%2==1:
            u=r*u%p
        r=r**2%p
        k=k//2
    r=u*r%p
    return(r)

def Inverse(a,p):
    t,newt,r,newr=0,1,p,a
    while newr!=0:
        q=r//newr
        t,newt=newt, t-q*newt
        r,newr=newr,r-q*newr
    if r!=1 :
        return 0
    elif t<0 :
        return t+p
    return t

def Sqrt(N, b=2):
    m=0
    M=N
    while (M-m>1):
        c = (m+M)//2
        if pow(c,b)<N:
            m = c
        else:
            M = c
    return m
