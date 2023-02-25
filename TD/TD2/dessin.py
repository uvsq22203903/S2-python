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
canvas.grid(row = 1, column = 1)


btn1 = tk.Button(text = "Choisir une couleur", command = couleur)
btn2 = tk.Button(text= "Cercle", command = cercle)
btn3 = tk.Button(text= "Carré", command= carre)
btn4 = tk.Button(text = "Croix", command= croix)
btn1.grid(row=0, column = 1)
btn2.grid(row=1//3, column= 0)
btn3.grid(row=1//3, column= 0)
btn4.grid(row=1//3, column= 0)
root.mainloop()