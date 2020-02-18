import matplotlib.pyplot as plt

class Sorting:

    def __init__(self):
        self.InsertionSortCount = 0
        self.SelectionSortCount = 0



    def SelectionSort(self, list):

        for i in range(len(list)):
            minidx = i
            for j in range(i+1,len(list)):
                self.SelectionSortCount += 1
                if list[j] < list[minidx]:
                    minidx = j
            list[i], list[minidx] = list[minidx], list[i]







    def InsertionSort(self, list):
        for i in range(len(list)):
            curr = list[i]
            position = i
            while position > 0 and list[position-1] > curr:
                self.InsertionSortCount += 1
                list[position] = list[position-1]
                position = position - 1
            list[position] = curr



    def getSelectionCount(self):
        temp = self.SelectionSortCount
        self.SelectionSortCount = 0
        return temp;

    def getInsertionCount(self):
        temp = self.InsertionSortCount
        self.InsertionSortCount = 0
        return temp;