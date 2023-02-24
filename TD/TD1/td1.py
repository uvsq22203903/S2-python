""" Exercice 1 
insertion_tableau prend en param L(liste), v(valeur), i(indice)
Insère la valeur v à l'indice i dans L --> utilisation L.append"""

def insertion_tableau(L, v, i):
    L.append(v)
    a = len(L)-1
    while a > i:
        L[a] = L[a-1]
        a-=1
    L[i] = v


def insertion_tableau2(L, v, i):
    temp = [v]
    for j in range(i,len(L)):
        temp.append(L.pop(j))
    L += temp
    return L


Liste = [0, 1, 2, 3]
print(insertion_tableau(Liste, 42, 1))
# print(insertion_tableau2(Liste, 42, 1))


""" Exercice 2 
suppression_tableau prent en param tab(tableau) et i(indice)
supprime dans le tableau l'élément se trouvant à l'indice donné --> utilisation L.pop() 

suppr 1 elemnt : fct L.pop() (sans argument) pour suppr dernière case."""

def suppression_tableau(tab, i):
    taille = len(tab)
    tab.pop()
    return tab


tableau = [0, 1, 2]
# print(suppression_tableau(tableau, 2))

"""Exercice 3
Définir la fonction `copie_tableau` retournant une copie du tableau `L` passé en paramètre (fonction comparable à `L.copy()`). 

Cette fonction ne doit pas utiliser la fonction `L.copy`, seule la fonction `L.append` est permise pour augmenter la taille du tableau."""

def copie_tableau(L):
    L2 = []
    for i in L:
        L2.append(i)
    return L2

Liste = [0, 25, 48, 65]
print(copie_tableau(Liste))

"""Exercice 4
Question 1: Définir la fonction `minimum_tableau` prenant en paramètre un tableau de nombres et retournant le minimum.
"""

def minimum_tableau(tab):
    min = tab[0]
    for i in range(len(tab)):
        if min > tab[i]:
            min = tab[i]
    return min

tableau = [1, 2, 3, 4, 5, 6]
print(minimum_tableau(tableau))

def minimum_tableau_trie(tableau):
    minimum = tableau[0]
    return minimum

tableau2 = [45, 47, 78, 96, 12]
tableau2.sort()
print(minimum_tableau_trie(tableau2))