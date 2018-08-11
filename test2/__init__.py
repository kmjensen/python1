'''
Created on 27. jul. 2018

@author: Kell
'''
from test import MyClass
from printClass import MyPrint
from math import sqrt

from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
 
window = Tk()
 
window.title("Welcome to LikeGeeks app  ");
 
window.geometry('700x400')

lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)

txt = Entry(window,width=10)
 
txt.grid(column=1, row=0)

def clicked():
 
    lbl.configure(text=txt.get() )

btn = Button(window, text="Click Me", command=clicked)
 
btn.grid(column=2, row=0)

combo = Combobox(window)
 
combo['values']= (1, 2, 3, 4, 5, "Text")
 
combo.current(1) #set the selected item
 
combo.grid(column=3, row=0)

rad1 = Radiobutton(window,text='First', value=1)
 
rad2 = Radiobutton(window,text='Second', value=2)
 
rad3 = Radiobutton(window,text='Third', value=3)
 
rad1.grid(column=0, row=1)
 
rad2.grid(column=1, row=1)
 
rad3.grid(column=2, row=1)



txt = scrolledtext.ScrolledText(window,width=40,height=10)
 
txt.grid(column=0,row=2)

window.mainloop()

def hello(myInput):
    return "Hello World: " + myInput

t = MyClass("ww");
tt = MyPrint("kk");
myInput = input("Please type your name: ") 
print(hello(myInput))
sqrt
