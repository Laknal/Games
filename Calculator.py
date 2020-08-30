from tkinter import *
x = Tk()

x.geometry("600x970")

x.wm_iconbitmap("cal1.ico")  #IF YOU DON'T HAVE ICO FILE REMOVE THIS LINE
x.configure(background='yellow')
x.title("CALCULATOR by Lakshay")
#Defining click command
def click(event):
	global scvalue
	text = event.widget.cget("text") #this command takes the widget text values
	if text == "=":
	   if scvalue.get().isdigit():
		   value = int(scvalue.get())
	   else:
		    try:
		        value = eval(screen.get())
		    except Exception as e:
			    print(e)
			    value = "ERROR"
	   scvalue.set(value)
	   screen.update()
	elif text == "C":
		scvalue.set("")
		screen.update()
	else:
		scvalue.set(scvalue.get() + text)
		screen.update()
#This is the textvariable
scvalue = StringVar()
scvalue.set("")


#This is the screen(entry)
screen = Entry(x,textvar=scvalue,font="lucida 40 bold")
screen.pack(ipadx=8,fill=X,pady=10,padx=10)

f4= Frame(x,bg="yellow")

b = Button(f4,text="/",padx=23,pady=5,font="lucida 30 bold")
b.pack(side="left",padx=6)
b.bind("<Button-1>",click)

b = Button(f4,text="*",padx=23,pady=5,font="lucida 30 bold")
b.pack(side="left",padx=6)
b.bind("<Button-1>",click)

b = Button(f4,text="-",padx=23,pady=5,font="lucida 30 bold")
b.pack(side="left",padx=6)
b.bind("<Button-1>",click)

f4.pack()

f1= Frame(x,bg="yellow")
b = Button(f1,text="9",padx=10,pady=5,font="lucida 35 bold")
b.pack(side="left",padx=10)
b.bind("<Button-1>",click)

b = Button(f1,text="8",padx=10,pady=5,font="lucida 35 bold")
b.pack(side="left",padx=10)
b.bind("<Button-1>",click)

b = Button(f1,text="7",padx=10,pady=5,font="lucida 35 bold")
b.pack(side="left",padx=10)
b.bind("<Button-1>",click)


f1.pack()
f2= Frame(x,bg="yellow")

b = Button(f2,text="6",padx=10,pady=5,font="lucida 35 bold")
b.pack(side="left",padx=10)
b.bind("<Button-1>",click)


b = Button(f2,text="5",padx=10,pady=5,font="lucida 35 bold")
b.pack(side="left",padx=10)
b.bind("<Button-1>",click)

b = Button(f2,text="4",padx=10,pady=5,font="lucida 35 bold")
b.pack(side="left",padx=10)
b.bind("<Button-1>",click)
f2.pack()



f3= Frame(x,bg="yellow")

b = Button(f3,text="3",padx=10,pady=5,font="lucida 35 bold")
b.pack(side="left",padx=10)
b.bind("<Button-1>",click)

b = Button(f3,text="2",padx=10,pady=5,font="lucida 35 bold")
b.pack(side="left",padx=10)
b.bind("<Button-1>",click)

b = Button(f3,text="1",padx=10,pady=5,font="lucida 35 bold")
b.pack(side="left",padx=10)
b.bind("<Button-1>",click)




f3.pack()



f5= Frame(x,bg="yellow")

b = Button(f5,text="0",padx=18,pady=5,font="lucida 30 bold")
b.pack(side="left",padx=10)
b.bind("<Button-1>",click)

b = Button(f5,text=".",padx=19,pady=5,font="lucida 30 bold")
b.pack(side="left",padx=10)
b.bind("<Button-1>",click)

b = Button(f5,text="+",padx=18,pady=5,font="lucida 30 bold")
b.pack(side="left",padx=10)
b.bind("<Button-1>",click)


f5.pack()

f6 = Frame(x,bg="yellow")

b = Button(f6,text="=",padx=10,pady=5,font="lucida 35 bold")
b.pack(side="left",padx=8)
b.bind("<Button-1>",click)

b = Button(f6,text="C",padx=10,pady=5,font="lucida 35 bold")
b.pack(side="left",padx=8)
b.bind("<Button-1>",click)

b = Button(f6,text="%",padx=7,pady=5,font="lucida 35 bold")
b.pack(side="left",padx=8)
b.bind("<Button-1>",click)

f6.pack()
x.mainloop()