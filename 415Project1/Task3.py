import matplotlib.pyplot as plt
from random import *
class Sorting:

    def __init__(self):
        self.InsertionSortCount = 0
        self.SelectionSortCount = 0
        self.yAxis = []
        self.xAxis = []



    def SelectionSort(self, list):

        for i in range(len(list)):
            minidx = i
            for j in range(i+1,len(list)):
                self.SelectionSortCount += 1
                if list[j] < list[minidx]:
                    minidx = j
            list[i], list[minidx] = list[minidx], list[i]
        return list






    def InsertionSort(self, list):
        for i in range(len(list)):
            curr = list[i]
            position = i
            while position > 0 and list[position-1] > curr:
                self.InsertionSortCount += 1
                list[position] = list[position-1]
                position = position - 1
            list[position] = curr
        return list


    def getSelectionCount(self):
        temp = self.SelectionSortCount
        self.SelectionSortCount = 0
        return temp

    def getInsertionCount(self):
        temp = self.InsertionSortCount
        self.InsertionSortCount = 0
        return temp

    def notUserTest(self):
        #Sorted list gen, best case
        self._generateGraphs('best')
        self._generateGraphs('average')
        self._generateGraphs('worst')

        #random list gen, average case

    def _generateGraphs(self, case):
        if case == 'best':
            listoList = self._generateSorted()
        if case == 'average':
            listoList = self._generateRandom()
        if case == 'worst':
            listoList = self._generateReverse()

        self._generateXYAxisInsert(listoList)
        sortedInsertion = plt.scatter(self.xAxis, self.yAxis, c='green')
        self.xAxis = []
        self.yAxis = []
        self._generateXYAxisSelection(listoList)
        sortedSelection = plt.scatter(self.xAxis, self.yAxis, c = 'blue')
        self.xAxis = []
        self.yAxis = []
        plt.xlabel('Size of List')
        plt.ylabel('Number of Swaps')
        plt.title(str(case) + ' Case for Insertion and Selection sort')
        plt.legend((sortedInsertion, sortedSelection), ('Insertion Sort', 'Selection Sort'))
        plt.show()

    def _generateReverse (self):
        listoList = []
        for i in range(102, 2, -1):
            list = []
            for j in range(i, 2, -1):
                list.append(j)
            listoList.append(list)
        return listoList


    def _generateRandom (self):
        listoList = []
        for i in range(2, 102):
            list = []
            for j in range(1, i):
                list.append(randint(1, 1000))
            listoList.append(list)
        return listoList

    def _generateSorted(self):
        listoList = []
        for i in range(2, 102):
            list = []
            for j in range(1, i):
                list.append(j)
            listoList.append(list)
        return listoList

    def _generateXYAxisInsert(self, listoList):
        for i in range(len(listoList)):
            self.InsertionSort((listoList[i]))
            self.yAxis.append(self.getInsertionCount())
            self.xAxis.append(len(listoList[i]))

    def _generateXYAxisSelection(self, listoList):
        for i in range(len(listoList)):
            self.SelectionSort(listoList[i])
            self.yAxis.append(self.getSelectionCount())
            self.xAxis.append(len(listoList[i]))