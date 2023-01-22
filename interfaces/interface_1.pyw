from tkinter import *

# Creación de la ventana
raiz = Tk()
raiz.title("Mi ventana")

# Metodo para redimencionar
# Recibe 2 parametros booleanos correspodientes a width y height
# Para indicar si prodra redimencionar
raiz.resizable(1, 1)

#raiz.iconbitmap("")
raiz.geometry("600x300")
raiz.config(bg="black")


raiz.mainloop()
