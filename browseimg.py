from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image,ImageTk

def showimage():
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="SElect file",filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("ALL file","*.*")))
    img=Image.open(fln)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image=img
    
root=Tk()
frm=Frame(root)
frm.pack(side=BOTTOM,padx=15,pady=15)
lbl=Label(root)
lbl.pack()
btn=Button(frm,text="Browse Image",command=showimage)
btn.pack(side=tk.LEFT)
btn2=Button(frm,text="Predict",command=lambda: exit())
btn2.pack(side=tk.LEFT,padx=10)
root.title("Image Browser")
root.geometry("300x350")
root.mainloop()