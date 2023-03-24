import tkinter as tk
import numpy as np
import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog

def save(matPix, filename):
    Image.fromarray(matPix).save(filename)

def load(filename):
    return np.array(pil.Image.open(filename))

create=True
nomImgCourante=""
nomImgDebut = ""


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

def reaffiche():
    global imgDebut
    global nomImgCourante
    if not create :
        imgDebut=ImageTk.PhotoImage(file=nomImgDebut)
        canvas.itemconfigure(dessin, image=imgDebut)
        canvas['width'] = imgDebut.width()
        canvas['height'] = imgDebut.height()
        nomImgCourante = nomImgDebut

def arreter():
    fenetre.quit()

def filtre_vert():
    mat=load(nomImgCourante)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if len(mat[i,j])==4:
                mat[i,j]=(0,mat[i,j,1],0,mat[i,j,3])
            else :
                mat[i,j]=(0,mat[i,j,1],0)
    modify(mat)

def gris():
    #On utilisera la conversion CIE709 qui permet de calculer la teinte de gris qui va être affichée dans le pixel
    #La teinte affichée est : gris=0,2125*rouge + 0,0721*bleu + 0,7154*vert
    mat=load(nomImgCourante)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            grise=0.215*mat[i,j,0]+0.0721*mat[i,j,2]+0.7154*mat[i,j,1]
            if len(mat[i,j])==4:
                mat[i,j]=(grise,grise,grise,mat[i,j,3])
            else :
                mat[i,j]=(grise,grise,grise)     
    modify(mat)

def noirBlanc():
    mat=load(nomImgCourante)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            couleur=sum(mat[i,j,:2])//3
            if couleur>127:
                couleur=255
            else:
                couleur=0
            if len(mat[i,j])==4:
                mat[i,j]=(couleur,couleur,couleur,mat[i,j,3])
            else :
                mat[i,j]=(couleur,couleur,couleur)
            # un pixel est blanc quand sa luminosité est > à 127, noir sinon
    modify(mat)


def zoom():
    mat=load(nomImgCourante)
    if len(mat[0,0])==4:
        matzoom=np.empty((mat.shape[0]*2,mat.shape[1]*2,4),dtype=np.uint8)
    else:
        matzoom=np.empty((mat.shape[0]*2,mat.shape[1]*2,3),dtype=np.uint8)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            matzoom[2*i,2*j]=mat[i,j]
            matzoom[2*i+1,2*j]=mat[i,j]
            matzoom[2*i,2*j+1]=mat[i,j]
            matzoom[2*i+1,2*j+1]=mat[i,j]
    modify(matzoom)


def shrink():
    mat=load(nomImgCourante)
    matshrink = np.empty((mat.shape[0]//2, mat.shape[1]//2,3), dtype = np.uint8)
    for i in range(matshrink.shape[0]):
        for j in range(matshrink.shape[1]):
            matshrink[i,j]=(mat[2*i,2*j]//4+mat[2*i+1, 2*j]//4+mat[2*i+1, 2*j+1]//4)
    modify(matshrink)


def poster():
    shrink()
    zoom()

def rotate():
    mat=load(nomImgCourante)
    matrotate = np.empty((mat.shape[1], mat.shape[0], 3), dtype = np.uint8)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            matrotate[j, mat.shape[0]-i-1] = mat[i, j]
    modify(matrotate)

def luminosite():
    mat=load(nomImgCourante)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if (mat[i, j][0]+3*scale_lum.get()<245):
                mat[i,j][0]=(mat[i,j][0]+3*scale_lum.get())
            else:
                mat[i,j][0]=255
            if (mat[i,j][1]+8*scale_lum.get()<256):
                mat[i,j][1]=(mat[i,j][1]+8*scale_lum.get())
            else:
                mat[i,j][1]=255
            if (mat[i,j][2]+scale_lum.get()<245):
                mat[i,j][2]=(mat[i,j][2]+scale_lum.get())
            else:
                mat[i,j][2]=255
    modify(mat)


create=True
#Fonctions auxiliaires 
    
fenetre = tk.Tk()
fenetre.title("mon petit photoshop")


#Création des Widgets
Zoom=tk.Button(fenetre,text="zoom",command=zoom)
noirblanc=tk.Button(fenetre,text="Noir et blanc",command=noirBlanc)
filtregris=tk.Button(fenetre,text="filtre gris",command=gris)
filtrevert=tk.Button(fenetre,text="filtre vert",command=filtre_vert)
retour=tk.Button(fenetre,text="Retour",command=reaffiche)
Charger=tk.Button(fenetre,text="Charger", command=lambda:charger(fenetre))
quitter=tk.Button(fenetre,text="Quitter", command=arreter)
# label=tk.Label(fenetre,text="Emma CLUZET 22203903")
Shrink = tk.Button(fenetre, text="Shrink", command= shrink)
Flou = tk.Button(fenetre, text="Flou", command= poster)
rotation = tk.Button(fenetre, text="Rotation", command= rotate)
Luminosite = tk.Button(fenetre, text="luminosité", command=luminosite)
scalelum=tk.Scale(fenetre, from_=0, to_=32)
# Positionnement des Widgets

Zoom.grid(column=3,row=0)
noirblanc.grid(column=0,row=2)
filtregris.grid(column=3,row=2)
filtrevert.grid(column=3,row=3)
retour.grid(column=0,row=0)
Charger.grid(column=0,row=4)
quitter.grid(column=3,row=4)
# label.grid(column=2,row=4)
Shrink.grid(column=0, row=3)
Flou.grid(column=3, row=1)
rotation.grid(column=0, row=1)
Luminosite.grid(column=0, row=5)
scalelum.grid(column=4, row=2)
#Lancement de la boucle 

fenetre.mainloop()