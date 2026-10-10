import math

def check_heap(L : list) -> bool :
    # Verification Complétude
    for i in range(len(L)):
        if L[i] is None:
            return False
    # Verification Monotonie
    for i in range(1, len(L)):
        if(L[math.floor((i-1)/2)] > L[i]):
            return False
    return True

def __heapifyUp(L: list, i):
    parent = math.floor((i-1)/2)
    if((parent >= 0)and(L[parent] > L[i])):
        temp = L[i]
        L[i] = L[parent]
        L[parent] = temp
        __heapifyUp(L, parent)
    
def heapify(L: list) -> list :
    for i in range(1, len(L)):
        __heapifyUp(L, i)
    return L
