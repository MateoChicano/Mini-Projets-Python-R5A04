

def check_heap(liste : list) -> bool :
    taille = len(liste)
    for i in range(taille):
        pred_left = left
        pred_right = right

        left = 2 * i + 1 #element le plus a gauche de la branche gauche
        right = 2 * i + 2 #element le plus a gauche de la branche droite
    return True