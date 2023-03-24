# ----------------------------------
# Exercice 1 - Test de compréhension
# ----------------------------------

cours = {'nom cours': 'Java','theme': 'Algorithmique','etudiants': [{'nom': 'Martin', 'prenom': 'Jean', 'Dept': '95'}, {'nom': 'Mohamed', 'prenom': 'Ali', 'Dept': '93'}, {'nom': 'Durand', 'prenom': 'Bertrand', 'Dept': '95'}]}

print(list(cours.values()))  # affiche le contenu de cours 
print("-----------")
print(list(cours))  # affiche les clés de cours
print("-----------")
print(cours['theme'])  # affiche la clé correspondant à la valeur theme
print("-----------")
tabE=cours['etudiants']
etud= tabE[0]
print(etud['nom'])  # affiche dans cours, dans étudiants, la valeur correspondant à la clé 0 de nom
print("-----------")

"""comment peut-on avoir les informations sur les étudiants inscrits à ce cours?"""

print(list(cours['etudiants']))
print("-----------")

"""Qu'affiche le programme suivant ?"""

etds=cours['etudiants']
tmp1=etds[1]
print(tmp1)
pr=tmp1['Dept']
print(pr)  # affiche les informations de l'étudiant qui est à l'indice 1 du dictionnaire des étudiants
print("-----------")

# -----------------------------------
# Exercice 2 - Planètes et satellites
# -----------------------------------

"""Définir le dictionnaire lunes représenté ci-dessous. Ce dictionnaire stocke le nombre de satellites de chaque planète. 
Dans un premier temps, définir de façon littérale le dictionnaire pour les 4 premiers couples clef:valeur puis ajouter 
successivement les 4 derniers couples."""

lunes = {"Mercure":0, "Vénus":0, "Terre":1, "Mars":2}
lunes["Jupiter"]=63
lunes["Saturne"]=61
lunes["Uranus"]=27
lunes["Neptune"]=11

print(lunes)
print("-----------")

"""Exploration d'un dictionnaire"""

lunes["Neptune"]=13
print(lunes)  # modifier le dico
print("-------------")
print("Le nombre de satellites de la Terre est",lunes['Terre'])  # affihcer nbr satellites Terre
print("-------------")
print(list(lunes))  # afficher liste des planètes
print("-------------")
print(lunes.values())  # afficher le nbr de satellites de chaque planète
print("-------------")
print(sum(lunes.values()))  # affiche le nbr total de satellites

# -------------------------------
# Exercice 3 - Gestion d'un stock
# -------------------------------

"""Saisie d'une référence"""


