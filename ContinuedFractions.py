
class ContinuedFraction:
    def __init__(self, num, den):
        self.list = []
        while (den > 0):
            self.list.append(num//den)
            num, den = den, num % den

    def getConvergents(self):
        if len(self.list) == 0:
            return [(0,1)]
        convergents = []
        for i in range(0,len(self.list)):
            num, den = self.list[i], 1
            for j in range(i-1,-1,-1):
                num, den = self.list[j]*num+den, num
            convergents.append((num,den))
        return convergents
