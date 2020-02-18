# import matplotlib.pyplot as plt
from fiboClass import fibonacciGCDTest
from Task2 import Exponentiation
from random import *


def main():
    fTest = fibonacciGCDTest()
    Etest = Exponentiation()
    test = int(input("1 for user test, 0 for computer generated scatterplot:\n"))

    if test == 1:
        print('** Fibonacci and GCD ** ')
        k = int(input('k value: '))
        fTest.fiboUserTest(k)

    else:
        print('** Fibonacci and GCD ** ')
        fTest.fiboNotUserTest()

    if test == 1:
        print('** Exponentiation ** ')
        a = int(input("Enter value for a:\n"))

        n = int(input("Enter value for n:\n"))

        print("Decrease by One Result: " + str(Etest.DecreaseByOne(a, n)) + ", Number of Multiplication: " + str(Etest.getByOneCount()))

        print("Decrease by Constant Factor Result: " + str(Etest.DecreaseByConstantFactor(a, n)) + ", Number of "
                                                                                            "Multiplication: " + str(
            Etest.getConstantFactorCount()))

        print("Divide and Conquer Result: " + str(Etest.DivideAndConquer(a, n)) + ", Number of Multiplication: " + str(Etest.getDivideCount()))
    else:
        print('** Exponentiation ** ')
        Etest.notUserTest()


main()
