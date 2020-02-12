#import matplotlib.pyplot as plt
from fiboClass import fibonacciGCDTest
from random import *
def main():
    fTest = fibonacciGCDTest()
    test = int(input("1 for user test, 0 for computer generated scatterplot:\n"))
    if test == 1:
        k = int(input('k value: '))
        fTest.fiboUserTest(k)
        
    else:     
        fTest.fiboNotUserTest()  
            
    
    
main()
