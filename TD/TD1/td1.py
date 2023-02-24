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
    return tableau[0]

tableau2 = [45, 47, 78, 96, 12]
tableau2.sort()
print(minimum_tableau_trie(tableau2))

"""
Question 2 : Ajout d'un élément"""

def ajouter_tableau(tab):
    tab.append(420)
    return tab

tableau3 = [1, 54, 87, 69, 59, 32, 2, 4]
print(ajouter_tableau(tableau3))

def ajouter_tableau_trie(tab, v):
    tab.append(v)
    tab.sort()
    return tab

tableau4 = [1, 58, 65, 2, 47, 89]
print(ajouter_tableau_trie(tableau4, 420))

"""
Question 3 : suppression d'un élément
Définir la fonction `supprimer_tableau` prenant en paramètre un tableau et un indice `id` et supprimant dans le tableau la valeur d'indice `id`.
On utilisera pour cela la fonction `.pop()` qui supprime la dernière case d'un tableau, mais pas la fonction `.pop(i)`"""

def supprimer_tableau(tab, id):
    a = []
    for j in range(len(tab)):
        a.append(tab[j])  # [tab[j]]
        if j == id:
            a.pop()
    return a

tableau5 = [1, 87, 56, 95, 102, 42]
print(supprimer_tableau(tableau5, 4))

def supprimer_tableau_trie(tab, id):
    tab.pop(id)
    return tableau2

tableau6 = [54, 78, 69, 12, 3]
tableau6.sort()
print(supprimer_tableau_trie(tableau6, 2))

""" Exercice 5 - réarrangement de tableau
Question 1 : Écrire une fonction `deplacer(T, k)` prenant en paramètre un tableau `T` et une valeur `k` et permutant les valeurs du tableau `T` 
de manière à ce que toutes les valeurs strictement inférieures à `k` soient au début de tableau. """

def deplacer(T, k):
    T.sort()
    ajouter_tableau_trie(T, k)
    return T

tableau7 = [8, 6, 2, 9, 78, 320]
print(deplacer(tableau7, 42))

"""Question 2 : Définir une fonction de tests unitaires de la fonction `deplacer`.
utilisation assert """

def test_deplacer():
    assert deplacer([],5) == 5, "tableau vide"
    assert deplacer()

test_deplacer()
