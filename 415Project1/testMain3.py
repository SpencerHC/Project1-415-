from Task3 import Sorting

sort = Sorting()

list = [5,4,3,2,1,0,-1]

sort.InsertionSort(list)

print(list)
print(str(sort.getInsertionCount()))