import matplotlib.pyplot as plt
class fibonacciGCDTest:
    
    def __init__(self):
        self.numOfMod = 0 #num of mod in GCD
    def __fibo(self, n):
    #tell you fibo number at nth index
        if n == 1:
            return 1
        elif n == 0:
            return 0
        return self.__fibo(n-1) + self.__fibo(n-2)
    
    def __fiboNumOfAdd(self, n):
    #computes number of addition in the fibonacci sequence at a given input n
        if n == 1:
            return 1
        elif n == 0:
            return 0
        return self.__fiboNumOfAdd(n-1) + self.__fiboNumOfAdd(n-2) + 1

    def __gcd(self, m, n):
        if (n == 0):
            return m
        self.numOfMod+=1
        return self.__gcd(n, m % n)
                
    def fiboNotUserTest(self):
    #used when using a computer generated test
        self.fxAxis = [] #fibo x axis
        self.fyAxis = [] #fibo y axis
        self.gxAxis = [] #gcd x axis
        self.gyAxis = [] #gcd y axis
        #chooses number 1-20 (x)
        for i in range (1, 21):
            fx = i
            fy = self.__fiboNumOfAdd(i)
            self.fxAxis.append(fx)#creates x axis for fibonacci, x is index of fibo number
            self.fyAxis.append(fy)#creates y axis for fibonacci, y is number of additions
        #creates graph from here 
        plt.scatter(self.fxAxis, self.fyAxis)    
        plt.xlabel('Index of Fibonacci Number')
        plt.ylabel('Number of Addition')
        plt.title('Fibonacci Analysis')
        plt.show()
        #to here

        #GCD test starts here
        for i in range (1, 21):
            n = self.__fibo(i) #store this for use of gx
            self.__gcd(self.__fibo(i+1), n) #compute for numberofMod
            gx = n
            gy = self.numOfMod
            self.gxAxis.append(gx)#creates x axis for fibonacci, x is index of fibo number
            self.gyAxis.append(gy)#creates y axis for fibonacci, y is number of additions
            self.numOfMod = 0
            
        plt.scatter(self.gxAxis, self.gyAxis)    
        plt.xlabel('n')
        plt.ylabel('Number of Modulo')
        plt.title('Euclids GCD Analysis')
        plt.show()
    def fiboUserTest(self, k):
        print("The fibonacci number at index " + str(k)+ " is: ")
        print(self.__fibo(k))
        print("The gcd of fibonacci number " + str(self.__fibo(k + 1)) + " and " + str(self.__fibo(k)))
        print(self.__gcd(self.__fibo(k + 1), self.__fibo(k)))








        
        
