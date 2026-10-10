import lib_tas
import random as r

tas = [1, 2, 3, 4, 5, 6, 7] #Cette liste represente un tas
tas_trou = [1, 2, 3, None, 5, 6, 7] #Cette liste ne represente pas un tas (la liste possède un trou)
tas_ordre = [1, 2, 7, 3, 4, 5, 6] #Cette liste ne represente pas un tas (7 ne peut pas etre avant 3')

gros_tas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] #Cette liste represente un tas
gros_tas_trou = [1, 2, 3, None, 5, 6, 7, None, 9, 10, 11, 12] #Cette liste ne represente pas un tas (la liste possède plusieurs trous)
gros_tas_ordre = [1, 2, 3, 4, 5, 12, 6, 7, 8, 9, 10, 11] #Cette liste ne represente pas un tas (12 ne peut pas etre avant 11)

print("****Test pour lib_tas****")
print("**Test de check_heap**")

print(lib_tas.check_heap(tas)) #True
print(lib_tas.check_heap(tas_trou)) #False
print(lib_tas.check_heap(tas_ordre)) #False

print(lib_tas.check_heap(gros_tas)) #True
print(lib_tas.check_heap(gros_tas_trou)) #False
print(lib_tas.check_heap(gros_tas_ordre)) #False

# test pour une pille vide
print(lib_tas.check_heap([])) #True

print("**Test de heapify**")

# test heapify sur liste nulle
print(lib_tas.check_heap(lib_tas.heapify([]))) #True
print(lib_tas.check_heap(lib_tas.heapify(gros_tas_ordre))) #True
print(lib_tas.check_heap(lib_tas.heapify(gros_tas_trou))) #True
# test heapify sur listes aléatoires
for i in range(50):
    randlist = list(range(r.randint(1, 50)))
    r.shuffle(randlist)
    randlist = lib_tas.heapify(randlist)
    if not(lib_tas.check_heap(randlist)):
        print('fail')

print("**Test de heappop**")

print(lib_tas.heappop(gros_tas))
print(lib_tas.check_heap(lib_tas.heappop(gros_tas)))

print("**Test de heappush**")

print(lib_tas.heappush(gros_tas, 4))
print(lib_tas.check_heap(lib_tas.heappush(gros_tas, 4)))
