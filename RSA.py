from Functions import *

class RSA:
    #p, q
    #phiN
    #private key = d
    #public key = e,N
    def __init__(self, exponent, weak = False):
        self.p = GenPrime(10**exponent,10**(exponent+1))
        self.q=self.p
        if not weak:
            self.q = GenPrime(10**(exponent+2),10**(exponent+3))
        else:
            self.q = GenPrime(self.p//2,self.p-1)
        self.N=self.p*self.q
        self.phiN=(self.p-1)*(self.q-1)
        if not weak:
            self.e = 65537
            self.d = Inverse(self.e,self.phiN)
        else:
            self.e = 0
            while self.e==0:
                self.d = randint(2,Sqrt(self.N,4)//3)
                self.e = Inverse(self.d, self.phiN)


    def getPublicKey(self):
        return self.N,self.e

    def encrypt(self, message):
        return ExponentiationRapide(message, self.e, self.N)

    def decrypt(self, message):
        return ExponentiationRapide(message, self.d, self.N)

    def __str__(self):
        return "N=%i \ne=%i \nd=%i" %(self.N,self.e,self.d)


#print RSA(256)