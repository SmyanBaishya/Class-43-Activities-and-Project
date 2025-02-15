import tkinter as tk
from tkinter import *

# Setting up the Main Window
root = Tk()
root.geometry("400x300")
root.title("main")

# Function to open New (Top Level) window
def topwin():
  # Setting up Top Window
  top = Toplevel()
  top.geometry("180x100")
  top.title("toplevel")
  # Adding a label widget to Top window
  l2 = Label(top, text = "This is a toplevel window")
  l2.pack()

  top.mainloop()

# Adding a label and button widget to Root (Main) window
l = Label(root, text = "This is the root window")
btn = Button(root, text = "Click here to open another window", command = topwin)

# Arranging widgets
l.pack()
btn.pack()

# ACTIVITY DOES NOT WORK ON VSC. GO TO REPLIT > TKINTER TO RUN.