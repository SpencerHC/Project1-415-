from fiboClass import fibonacciGCDTest
from Task2 import Exponentiation

Etest = Exponentiation()
Etest.notUserTest()
a = int(input("Enter value for a:\n"))

n = int(input("Enter value for n:\n"))

print("Decrease by One: " + str(Etest.DecreaseByOne(a, n)) + ", " + str(Etest.getByOneCount()))

print("Decrease by Constant Factor: " + str(Etest.DecreaseByConstantFactor(a, n)) + ", " + str(Etest.getConstantFactorCount()))

print("Divide and Conquer: " + str(Etest.DivideAndConquer(a, n)) +  ", " + str(Etest.getDivideCount()))