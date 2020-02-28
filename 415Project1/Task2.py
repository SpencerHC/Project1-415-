import matplotlib.pyplot as plt

class Exponentiation:

    def __init__(self):
        self.ByOneCount = 0
        self.ConstantFactorCount = 0
        self.DivideCount = 0
        self.yAxis = []
        self.xAxis = []

    def DecreaseByOne(self, a, n):
        if n==0:
            return 1
        self.ByOneCount += 1
        return a * self.DecreaseByOne(a, n - 1)


    def DecreaseByConstantFactor(self, a, n):
        if n == 0:
            return 1
        elif (n % 2) == 1:
            self.ConstantFactorCount = self.ConstantFactorCount + 2
            return a * self.__Squared(self.DecreaseByConstantFactor(a, ((n - 1) / 2)))
        else:
            self.ConstantFactorCount = self.ConstantFactorCount + 1
            return self.__Squared(self.DecreaseByConstantFactor(a, (n / 2)))

    def DivideAndConquer(self, a, n):
        if n == 0:
            return 1
        elif (n % 2) == 1:
            self.DivideCount = self.DivideCount + 2
            return a * self.DivideAndConquer( a, (n - 1) / 2) * self.DivideAndConquer( a, (n - 1) / 2)
        else:
            self.DivideCount = self.DivideCount + 1
            return self.DivideAndConquer(a, n / 2) * self.DivideAndConquer(a, n / 2)

    def __Squared(self,n):
        return n * n

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

    def notUserTest(self):
        for i in range(1, 500):
            self.DecreaseByOne(5, i)
            self.xAxis.append(i)
            self.yAxis.append(self.getByOneCount())

        dcbOne = plt.scatter(self.xAxis, self.yAxis, c='green')
        self.xAxis = []
        self.yAxis = []

        for i in range(1, 500):
            self.DecreaseByConstantFactor(5, i)
            self.xAxis.append(i)
            self.yAxis.append(self.getConstantFactorCount())

        dcbcf = plt.scatter(self.xAxis, self.yAxis, c='blue')
        self.xAxis = []
        self.yAxis = []

        for i in range(1, 500):
            self.DivideAndConquer(5, i)
            self.xAxis.append(i)
            self.yAxis.append(self.getDivideCount())
        dac = plt.scatter(self.xAxis, self.yAxis, c='red')
        self.xAxis = []
        self.yAxis = []


        plt.legend((dcbOne, dcbcf, dac), ('Decrease by One', 'Decrease By Constant Factors', 'Divide and Conquer'))

        self._generateGraphs('Exponent of 5', 'Number of Multiplication',
                         'Exponenation Analysis')

    def _generateGraphs(self, xlabel, ylabel, title):
        plt.scatter(self.xAxis, self.yAxis)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()
        self.xAxis =[]
        self.yAxis = []