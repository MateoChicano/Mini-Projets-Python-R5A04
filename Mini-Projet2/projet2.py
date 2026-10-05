# Mini-projet 2
import numpy as np
import heapq as hpq
import matplotlib.pyplot as plt
import time as t

# Tailles de liste différentes pour tester l'évolution du temps d'execution
N = [10,100,500,1000,2000,5000]

# Valeur Max pour les elements de la liste (Nmin = 0)
Nmax = 10000

# Version 1 de l'algorithme avec des listes classiques
def element_commun1(L1: [], L2: []):
    L1.sort()
    L2.sort()
    while(len(L1)!=0 and len(L2)!=0):
        if(L1[0]==L2[0]):
            return L1[0]
        if(L1[0]<=L2[0]):
            L1.pop(0)
        else:
            L2.pop(0)
    return None

# Version 2 de l'algorithme avec des tas
def element_commun2(L1: [], L2: []):
    hpq.heapify(L1)
    hpq.heapify(L2)
    while(len(L1)!=0 and len(L2)!=0):
        if(L1[0]==L2[0]):
            return L1[0]
        if(L1[0]<=L2[0]):
            hpq.heappop(L1)
        else:
            hpq.heappop(L2)
    return None

res1 = np.zeros(len(N))
res2 = np.zeros(len(N))

# Pour chaques valeurs de n on calcule le temps d'execution des deux fonctions 
# et on les enregistre dans res1 et 2 respectivement
for k,n in enumerate(N):
    liste1 = np.random.randint(Nmax, size=n).tolist()
    liste2 = np.random.randint(Nmax, size=n).tolist()
    
    t1 = t.time()
    element_commun1(liste1, liste2)
    t2 = t.time()
    res1[k] = (t2-t1)
    
    t1 = t.time()
    element_commun2(liste1, liste2)
    t2 = t.time()
    res2[k] = (t2-t1)

# Puis on affiche le graphique de comparaison
plt.figure(1)
plt.title("Comparaison des temps d'exécution")
plt.xlabel("taille de la liste")
plt.ylabel("Temps d'exécution")
plt.plot(N, res1, label="element commun 1 (listes)")
plt.plot(N, res2, label="element commun 2 (tas)")

plt.legend()
plt.grid()
plt.show()
    
