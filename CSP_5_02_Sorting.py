import random

def bubbleSort(items:list):
    swaps = 0
    comparisons = 0
    n = len(items)
    
    for i in range(n):
        for j in range(n - 1):
            comparisons = comparisons + 1
            if items[j] > items[j + 1]:
                temp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = temp
                swaps = swaps + 1
    
    return items, swaps, comparisons

def insertionSort(items: list):
    swaps = 0
    comparisons = 0
    
    for i in range(1, len(items)):
        current = items[i]
        position = i
        
        while position > 0 and items[position - 1] > current:
            comparisons = comparisons + 1
            items[position] = items[position - 1]
            position = position - 1
            swaps = swaps + 1
        
        if position > 0:
            comparisons = comparisons + 1
        
        items[position] = current
    
    return items, swaps, comparisons

def selectionSort(items : list):
    swaps = 0
    comparisons = 0
    
    for i in range(len(items)):
        smallest_index = i
        
        for j in range(i + 1, len(items)):
            comparisons = comparisons + 1
            if items[j] < items[smallest_index]:
                smallest_index = j
        
        temp = items[i]
        items[i] = items[smallest_index]
        items[smallest_index] = temp
        swaps = swaps + 1
    
    return items, swaps, comparisons

y = [9,8,7,6,5,4,3,2,1]
print(bubbleSort(y.copy()))
print(insertionSort(y.copy()))
print(selectionSort(y.copy()))
print()
x = [x for x in range(50)]
random.shuffle(x)
print(bubbleSort(x.copy()))
print(insertionSort(x.copy()))
print(selectionSort(x.copy()))
