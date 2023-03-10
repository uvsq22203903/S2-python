import tkinter as tk
import random

def couleur():
    global color
    color = input("Quel couleur : white, black, red, green, blue, cyan, yellow ? ")


"""une fonction qui affiche un disque de diamètre 100 
en bleu à un endroit choisi au hasard dans le canevas. Le cercle doit être inclu intégralement dans le canevas."""

def cercle():
    x1 = random.randint(0, 300)
    y1 = random.randint(0, 300)
    x2 = x1+200
    y2 = y1+200
    cercle = canvas.create_oval(x1,y1,x2,y2, fill= color)
    


def carre():
    x1 = random.randint(0, 400)
    y1 = random.randint(0, 400)
    x2 = x1 + 100
    y2 = y1 + 100
    carre = canvas.create_rectangle(x1, y1, x2, y2, fill= color)
    


def croix():
    x1 = random.randint(0, 400)
    y1 = random.randint(0, 400)
    x2 = x1 +100
    y2 = y1 + 100
    croix1 = canvas.create_line(x1, y1, x2, y2, fill= color, width=3)
    croix2 = canvas.create_line(x1, y2, x2, y1, fill= color, width=3)
    

def undo():
    canvas.delete()

# - - - - - - - - - - - -
# Création de la fenêtre
# - - - - - - - - - - - -

root = tk.Tk()
root.title("Mon dessin")
canvas = tk.Canvas(root, width= 500, height= 500, bg= 'black', bd= 8, relief= 'ridge')
canvas.grid(row= 1, rowspan= 4, column= 1)
color='blue'
# - - - - - - - - - - -
# Création des boutons
# - - - - - - - - - - -

btn1 = tk.Button(text= "Choisir une couleur", bg='#D0F3BD',bd=5, relief='ridge', activebackground='dark orange', activeforeground='light yellow', font='Arial', command= couleur)
btn2 = tk.Button(text= "Cercle", bg='light blue', bd= 5, relief='ridge', activebackground='dark orange', activeforeground='light yellow', font='Arial', command= cercle)
btn3 = tk.Button(text= "Carré", bg='#FF574A', bd= 5, relief='ridge', activebackground='dark orange', activeforeground='light yellow', font='Arial', command= carre)
btn4 = tk.Button(text= "Croix", bg='#FFEA80', bd= 5, relief='ridge', activebackground='dark orange', activeforeground='light yellow', font='Arial', command= croix)
#btn5 = tk.Button(text= "Effacer", bd= 5, relief= 'ridge', activebackground='dark orange', activeforeground='light yellow', font='Arial', command= undo)

btn1.grid(row=0, column= 1)
btn2.grid(row=1, column= 0)
btn3.grid(row=2, column= 0)
btn4.grid(row=3, column= 0)
#btn5.grid(row=4, column= 0)
root.mainloop()