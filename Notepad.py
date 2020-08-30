from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
x = Tk()
x.geometry("644x788")
x.title("Notepad-Untitled")

def openfi():
    global file
    file= askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
         file = None
    else:
         x.title(os.path.basename(file)+ "-Notepad")
         textbox.delete(1.0, END)
         f = open(file, "r")
         textbox.insert(1.0, f.read())
         f.close()


def newfile():
    global file
    x.title("Untitled-Notepad")
    file=None
    textbox.delete(1.0,END)#1.O IS 1 LINE AND FIRST CHAR AND TO THE END


def savefi():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt'
                                 ,defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file == "":
           file = None
        else:
            #save as a new file
            f = open(file,"w")
            f.write(textbox.get(1.0,END))
            f.close()
            x.title(os.path.basename(file)+ "-Notepad")
    else:
        #save the new file
        f = open(file, "w")
        f.write(textbox.get(1.0, END))
        f.close()

def cut():
    textbox.event_generate(("<<Cut>>"))

def copy():
    textbox.event_generate (("<<Copy>>"))

def msg():
    showinfo("Notepad","Created by Lakshay")
#ADDING MENU BAR
menubar = Menu(x)

#Adding FILE TAB
m1= Menu(menubar,tearoff=0)
m1.add_command(label="Open",command=openfi)
m1.add_command(label="Save",command=savefi)
m1.add_command(label="New file",command=newfile)
m1.add_separator()
m1.add_command(label="Exit",command=x.destroy)
menubar.add_cascade(label="File",menu=m1)


#ADDING EDIT TAB
m2 = Menu(menubar,tearoff=0)
m2.add_command(label="Cut",command= cut)
m2.add_command(label="Copy",command=copy)
menubar.add_cascade(label="Edit",menu=m2)

#ADDING HELP TAB

m3 = Menu(menubar,tearoff=0)
m3.add_command(label="about",command=msg)
menubar.add_cascade(label="Help",menu=m3)

x.config(menu=menubar)

#ADDING TEXT BOX
scroll_bar = Scrollbar(x)
scroll_bar.pack(fill=Y,side='right')
textbox= Text(x,yscrollcommand= scroll_bar.set,font="lucida 14")
file = None
textbox.pack(fill='both',expand=TRUE)
scroll_bar.config(command=textbox.yview)


x.mainloop()
