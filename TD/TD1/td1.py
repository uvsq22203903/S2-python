""" Exercice 1 
insertion_tableau prend en param L(liste), v(valeur), i(indice)
Insère la valeur v à l'indice i dans L --> utilisation L.append"""

def insertion_tableau(L, v, i):
    L.append(0)
    a = len(L)-1
    while a > i:
        L[a] = L[a-1]
        a-=1
    L[i] =v

Liste = [0, 1, 2, 3]
print(insertion_tableau(Liste, 42, 1))

""" Exercice 2 
suppression_tableau prent en param tab(tableau) et i(indice)
supprime dans le tableau l'élément se trouvant à l'indice donné --> utilisation L.pop() 

suppr 1 elemnt : fct L.pop() (sans argument) pour suppr dernière case."""

def suppression_tableau(tab, i):
    
    tab.pop()


tableau = [0, 1, 2]
print(suppression_tableau(tableau, 2))