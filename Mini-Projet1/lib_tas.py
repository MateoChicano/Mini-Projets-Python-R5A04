import math

def check_heap(L : list) -> bool :
    # Verification Complétude
    for i in range(len(L)):
        if L[i] is None:
            if not all(x is None for x in L[i:]):
                return False
    # Verification Monotonie
    for i in range(1, len(L)):
        if(L[i] is not None):
            if(L[math.floor((i-1)/2)] > L[i]):
                return False
    return True

def __heapifyUp(L: list, i):
    if(L[i] is None):
        return
    parent = math.floor((i-1)/2)
    if((L[parent] is None)or((parent >= 0)and(L[parent] > L[i]))):
        temp = L[i]
        L[i] = L[parent]
        L[parent] = temp
        __heapifyUp(L, parent)
    
def heapify(L: list) -> list :
    for i in range(1, len(L)):
        if(L[i] is None):
            L = L[:i] + L[i + 1:]
            L.append(None)
        else:
            __heapifyUp(L, i)
    return L

def heappop(L: list) -> list :
    L = L[1:]
    heapify(L)
    return(L)    
    
def heappush(L: list, a) -> list :
    L.append(a)
    __heapifyUp(L, len(L)-1)
    return(L)