import lib_tas

tas = [1, 2, 3, 4, 5, 6, 7] #Cette liste represente un tas
tas_trou = [1, 2, 3, None, 5, 6, 7] #Cette liste ne represente pas un tas (la liste possède un trou)
tas_ordre = [1, 2, 7, 3, 4, 5, 6] #Cette liste ne represente pas un tas (7 ne peut pas etre avant 3')

gros_tas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] #Cette liste represente un tas
gros_tas_trou = [1, 2, 3, None, 5, 6, 7, None, 9, 10, 11, 12] #Cette liste ne represente pas un tas (la liste possède plusieurs trous)
gros_tas_ordre = [1, 2, 3, 4, 5, 6, 12, 7, 8, 9, 10, 11] #Cette liste ne represente pas un tas (12 ne peut pas etre avant 7)

print(lib_tas.check_heap(tas)) #True
print(lib_tas.check_heap(tas_trou)) #False
print(lib_tas.check_heap(tas_ordre)) #False

print(lib_tas.check_heap(gros_tas)) #True
print(lib_tas.check_heap(gros_tas_trou)) #False
print(lib_tas.check_heap(gros_tas_ordre)) #False

