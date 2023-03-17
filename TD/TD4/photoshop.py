import tkinter as tk
import numpy as np
import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog

# -------------------------
# Déclaration des fonctions
# -------------------------

def save(matPix, filename):
    Image.fromarray(matPix).save(filename)

def load(filename):
    return np.array(pil.Image.open(filename))


"""permet d'afficher une image dans un canevas dans la colonne 1 d'une grid"""
def charger(widg):
    global create
    global photo
    global img
    global canvas
    global dessin
    global nomImgCourante
    global nomImgDebut
    filename= filedialog.askopenfile(mode='rb', title='Choose a file')
    img = pil.Image.open(filename)
    nomImgCourante=filename.name
    nomImgDebut = filename.name
    photo = ImageTk.PhotoImage(img)
    if create:    
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        dessin = canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.grid(row=0,column=1,rowspan=4,columnspan=2)
        create=False
        
    else:
        canvas.grid_forget()
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        dessin=canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.grid(row=0,column=1,rowspan=4,columnspan=2)

def modify(matrice):
    global imgModif
    global nomImgCourante
    save(matrice,"modif.png")
    imgModif=ImageTk.PhotoImage(file="modif.png")
    canvas.itemconfigure(dessin, image=imgModif)
    canvas['width'] = imgModif.width()
    canvas['height'] = imgModif.height()
    nomImgCourante="modif.png"

"""permet de modifier une matrice de pixels au sein même d'un canevas créé par la methode `charger()`, 
et la fonction callback `reaffiche` qui permet de réafficher l'image de départ après lui avoir appliqué des effets."""

def reaffiche():
    global imgDebut
    global nomImgCourante
    if not create :
        imgDebut=ImageTk.PhotoImage(file=nomImgDebut)
        canvas.itemconfigure(dessin, image=imgDebut)
        canvas['width'] = imgDebut.width()
        canvas['height'] = imgDebut.height()
        nomImgCourante = nomImgDebut

def quitter():
    root.quit()

def filtre_vert():
    mat=load(nomImgCourante)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if len(mat[i, j]) == 4: # i j cordonnéee d'un pixel --> 3 valeur RGB + alpha donc 4
                mat[i,j]=(0,mat[i,j,1],0, mat[i,j,3])
            else:
                mat[i,j]=(0, mat[i,j,1],0)
    modify(mat)

def gris():
    #On utilisera la conversion CIE709 qui permet de calculer la teinte de gris qui va être affichée dans le pixel
    #La teinte affichée est : gris=0,2125*rouge + 0,0721*bleu + 0,7154*vert
    mat=load(nomImgCourante)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            grise = 0.2125*mat[i,j,0]+0.0721*mat[i,j,2]+0.7154*mat[i,j,1]
            if len(mat[i,j]) == 4:
                mat[i,j]=(grise, grise, grise, mat[i,j,3])
            else:
                mat[i,j]=(grise, grise, grise)
            # calcul de la teinte de gris du pixel (CIE709)
    modify(mat)

def noirBlanc():
    mat=load(nomImgCourante)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            couleur = sum(mat[i,j,:2])//3
            if couleur > 127:  # un pixel est blanc quand sa luminosité est > à 127, noir sinon
                couleur = 255
            else:
                couleur = 0
            if couleur>127:
                mat[i,j] = (255, 255, 255)
            else:
                mat[i,j] = (0, 0, 0)
    modify(mat)

def zoom():
    mat=load(nomImgCourante)
    #créer une matrice de largeur et hauteur deux fois plus grande 
    matzoom=np.empty((mat.shape[0]*2, mat.shape[1]*2,3),dtype=np.uint8)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            mat[i,j]
    modify(mat)

# ----------------------
# Création de la fenêtre
# ----------------------

root = tk.Tk()
root.title("Mon Petit Photoshop")
#canvas = tk.Canvas(root, width= 500, height= 500, bg='#DC7F57')
#canvas.grid(row= 0, rowspan= 3, column= 1)

# --------------
# Widget & Label
# --------------

Charger = tk.Button(root, text= "Charger", command= lambda : charger(root))
quitter = tk.Button(root, text= 'Quitter', command= quitter)
reaffichage = tk.Button(root, text= 'Revenir à l\'image de départ', command = reaffiche)
#identite = tk.Label(root, text="Emma Cluzet 22203903")
vert = tk.Button(root, text="filtre vert", command= filtre_vert)
grisaille = tk.Button(root, text= "Nuance de gris", command= gris)
noirblanc= tk.Button(root, text="Noir et Blanc", command= noirBlanc)
# - -- - - - - - - - - - - - --  -- - - - - - - - - -
Charger.grid(row= 5, column= 0)
quitter.grid(row=5, column= 2)
reaffichage.grid(row= 0, column= 0)
#identite.grid(row=5, column= 1)
vert.grid(row= 1, column= 0)
grisaille.grid(row=2, column=0)
noirblanc.grid(row=4, column= 0)

# -------------------
# Programme Principal
# -------------------

create=True
nomImgCourante=""
nomImgDebut = ""


root.mainloop()