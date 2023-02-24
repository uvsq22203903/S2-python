import tkinter as tk

def couleur():
    pass

def cercle():
    pass

def carre():
    pass

def croix():
    pass

root = tk.Tk()
root.title("Mon dessin")
canvas = tk.Canvas(root, width= 500, height=500, bg = 'black')
canvas.grid(row = 0, column = 1)


btn1 = tk.Button(text = "choisir une couleur", command = couleur)
btn2 = tk.Button(text= "cercle", command = cercle)
btn3 = tk.Button(text= "carré", command= carre)
btn4 = tk.Button(text = "Croix", command= croix)
root.mainloop()