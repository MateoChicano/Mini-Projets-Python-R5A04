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

def heapify(L: list) -> list :
        
    
    
    return L