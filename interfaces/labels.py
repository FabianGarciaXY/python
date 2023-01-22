from tkinter import *

from black import main
from pyrsistent import m

root = Tk()

# Main Interface
main_frame = Frame(root, width=500, height=400)
main_frame.pack()

# Labels
Label(main_frame, text='This is a label', fg='gray', font=(20)).place(x=100, y=200) # Position


root.mainloop()