from tkinter import *
from turtle import right

raiz = Tk()
raiz.title = 'Mi ventana'

# raiz.resizable(True, False)

raiz.geometry('650x400')
raiz.config(bg='black')

# New Frame
my_frame = Frame()
my_frame.pack(fill='x')
my_frame.config(bg='white')
my_frame.config(width='300', height='200')

raiz.mainloop()