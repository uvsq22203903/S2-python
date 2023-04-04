import tkinter as tk

taille_fenetre = 100 #Taille de la fenêtre de recherche
min_match = 3 #Taille du plus petit match permis


def match_size(mot,i,j): #renvoie la valeur du plus grand sous-mot commun,
                       #dans le mot aux positions i et j avec j < i
    k = 0
    while i+k < len(mot):
        if (mot[i+k]==mot[j+k]):
            k+=1
        else:
            break
    return k

def max_match(mot, i): #renvoie le couple (position,taille) du plus grand match 
                      #trouvé dans mot à partir de la position i
    j = max(0, i - taille_fenetre)  #première position où chercher un match
    max_match = (0, 0)
    while j < i: #on cherche un match dans la fenetre de recherche
        tailleActuelle = match_size(mot, i, j)
        if (max_match[1] < tailleActuelle):
            max_match = (j, tailleActuelle)
        j += 1
    return max_match


def compresse():
    texte_a_compresser = entree.get()
    texte_compresse = [] #cette liste doit etre étendue pour contenir le texte compressé
    #construction du code LZ77
    i = 0
    while i < len(texte_a_compresser): #pour chaque lettre du texte
        temp = max_match(texte_a_compresser, i)
        if temp[1] < min_match:
            texte_compresse.append(texte_a_compresser[i])
            i += 1
        else:
            texte_compresse.append((i - temp[0], temp[1]))
            i +=  temp[1]
        
    affichage_compression.config(text = str(texte_compresse)) #affichage du texte compressé 
    affichage_compression.config(text = str(texte_compresse)) # affichage du texte compressé
    resultat.config(text = "Taille compressée de " + str(taille(texte_compresse)) + ". Taille non compressée " \
                + str(len(texte_a_compresser)) + ". Ratio de compression" + str(len(texte_a_compresser)/taille(texte_compresse)))
    """affichage_decompression.config(text = decompresse(texte_compresse))
    affichage_binaire.config(text = code_binaire(texte_compresse))"""
    
    

def taille(liste_LZ):# calcule la taille de la liste. Un caractère compte 1 et 
                                   # une paire d'entier compte 2
    taille = 0
    for elem in liste_LZ:
        if isinstance(elem, str):  # verifie si elem est de type str
            taille += 1
        else:
            taille += 2
    return taille

def changeFenetre():
    global taille_fenetre
    taille_fenetre = int(entree_fenetre.get())
    
def match2():
    global min_match
    min_match = 2
    
def match3():
    global min_match
    min_match = 3

# ------------------
# Définition Tkinter
# ------------------

racine = tk.Tk()
racine.title("Compression de texte")

entree = tk.Entry(racine, width = 50,font = ("helvetica", "20"))
entree.grid(row = 1, column = 0)


entree_fenetre = tk.Entry(racine, width = 50,font = ("helvetica", "20"))
entree_fenetre.grid(row = 0, column = 0)

bouton_fenetre = tk.Button(racine, text = "Régler la fenetre de recherche", command = changeFenetre, font = ("helvetica", "30"))
bouton_fenetre.grid(row = 0, column = 1)

affichage_compression = tk.Message(racine, font = ("helvetica", "20"), width = 1000)
affichage_compression.grid(row = 2, column = 0, columnspan = 2)


affichage_decompression = tk.Message(racine, font = ("helvetica", "20"), width = 1000)
affichage_decompression.grid(row = 5, column = 0, columnspan = 2)


affichage_binaire = tk.Message(racine, font = ("helvetica", "20"), width = 1000)
affichage_binaire.grid(row = 6, column = 0, columnspan = 2)


bouton_compresser = tk.Button(racine, text = "Compresser", command = compresse, font = ("helvetica", "30"))
bouton_compresser.grid(row = 1, column = 1)


bouton_match2 = tk.Button(racine, text = "Match minimal de taille 2", command = match2, font = ("helvetica", "30"))
bouton_match2.grid(row = 4, column = 0)


bouton_match3 = tk.Button(racine, text = "Match minimal de taille 3", command = match3, font = ("helvetica", "30"))
bouton_match3.grid(row = 4, column = 1)

resultat = tk.Label(racine, font = ("helvetica", "20"))
resultat.grid(row = 3, column = 0, columnspan = 2)



# -------------------
# Programme principal
# -------------------

print(match_size("blablaba", 2, 3))
print(max_match("blabloblobloblablabla", 9))


racine.mainloop()