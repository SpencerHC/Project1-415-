import matplotlib.pyplot as plt

class Exponentiation:

    def __init__(self):
        self.ByOneCount = 0
        self.ConstantFactorCount = 0
        self.DivideCount = 0

    def DecreaseByOne(self, a, n):
        if n==0:
            return 1;
        self.ByOneCount += 1
        return a * self.DecreaseByOne(a, n - 1)


    def DecreaseByConstantFactor(self, a, n):
        if n == 0:
            return 1
        elif (n % 2) == 1:
            self.ConstantFactorCount = self.ConstantFactorCount + 2;
            return a * self.__Squared(self.DecreaseByConstantFactor(a, ((n - 1) / 2)))
        else:
            self.ConstantFactorCount = self.ConstantFactorCount + 1;
            return self.__Squared(self.DecreaseByConstantFactor(a, (n / 2)))

    def DivideAndConquer(self, a, n):
        if n == 0:
            return 1
        elif (n % 2) == 1:
            self.DivideCount = self.DivideCount + 2;
            return a * self.DivideAndConquer( a, (n - 1) / 2) * self.DivideAndConquer( a, (n - 1) / 2)
        else:
            self.DivideCount = self.DivideCount + 1;
            return self.DivideAndConquer(a, n / 2) * self.DivideAndConquer(a, n / 2)

    def __Squared(self,n):
        return n * n;

    def getByOneCount(self):
        saved = self.ByOneCount
        self.ByOneCount = 0
        return saved
    def getConstantFactorCount(self):
        saved = self.ConstantFactorCount
        self.ConstantFactorCount = 0
        return saved
    def getDivideCount(self):
        saved = self.DivideCount
        self.DivideCount = 0
        return saved