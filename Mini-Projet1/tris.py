import time as t 
import matplotlib.pyplot as plt
import numpy as np
import heapq
import lib_tas

N = [10,20,50,100,200,500]

def triselection(L):
    for i in range(0, len(L)-1):
        jm = i
        for j in range(i+1, len(L)):
            if L[j] < L[jm]:
                jm = j
        c = L[jm]
        L[jm] = L[i]
        L[i] = c
    return L
    
def tribulles(L):
    for i in range(len(L)-1, 0, -1):
        for j in range(0, i, 1):
            if L[j] > L[j+1]:
                c = L[j+1]
                L[j+1] = L[j]
                L[j] = c
    return L

def triinsertion(L):
    for i in range(0, len(L)-1, 1):
        j = i
        while(L[j] < L[j-1] and j > 0):
            c = L[j-1]
            L[j-1] = L[j]
            L[j] = c
            j = j-1
    return L

def tripython(L):
    L.sort()
    return L

def triheap(L):
    h = []
    for i in range(len(L)):
        heapq.heappush(h, L[i])
    for i in range(len(L)):
        L[i] = heapq.heappop(h)
    return L

def trilib_tas(L):
    h = lib_tas.heapify(L)
    for i in range(len(L)):
        L[i] = lib_tas.heappop(h)
    return L

res1 = np.zeros(len(N))
res2 = np.zeros(len(N))
res3 = np.zeros(len(N))
res4 = np.zeros(len(N))
res5 = np.zeros(len(N))
res6 = np.zeros(len(N))

for k,n in enumerate(N):
    t1 = t.time()
    for i in range(100):
        X1 = triselection(np.random.randint(-1000,1000,n))
    t2 = t.time()
    res1[k] = (t2-t1)/100
    
    t1 = t.time()
    for i in range(100):
        X2 = tribulles(np.random.randint(-1000,1000,n))
    t2 = t.time()
    res2[k] = (t2-t1)/100
    
    t1 = t.time()
    for i in range(100):
        X3 = triinsertion(np.random.randint(-1000,1000,n))
    t2 = t.time()
    res3[k] = (t2-t1)/100
    
    t1 = t.time()
    for i in range(100):
        X4 = tripython(np.random.randint(-1000,1000,n))
    t2 = t.time()
    res4[k] = (t2-t1)/100
    
    t1 = t.time()
    for i in range(100):
        X5 = triheap(np.random.randint(-1000,1000,n))
    t2 = t.time()
    res5[k] = (t2-t1)/100
    
    t1 = t.time()
    for i in range(100):
        X6 = trilib_tas(np.random.randint(-1000,1000,n))
    t2 = t.time()
    res6[k] = (t2-t1)/100

plt.figure(1)
plt.title("Comparaison des temps d'exécution")
plt.xlabel("taille de la liste")
plt.ylabel("Temps d'exécution")
plt.plot(N, res1, label="tri selection")
plt.plot(N, res2, label="tri bulles")
plt.plot(N, res3, label="tri insertion")
plt.plot(N, res4, label="tri python")
plt.plot(N, res5, label="tri heap")
plt.plot(N, res6, label="tri lib_tas")

plt.legend()
plt.grid()
plt.show()

