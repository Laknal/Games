'''from plyer import notification
import time
if __name__=="__main__":
     notification.notify(
        title = 'Please AAnchal..Bagh jao',
        message = 'SUCCESS',
        app_icon = 'C:\\Users\\Neet\\PycharmProjects\\GUI\\alarm.ico',
        timeout = 10,
     )'''
from plyer import notification
import time
from tkinter import *

def add():
    value = int(entr_var2.get())
    notification.notify (
        title=(f"{entr_var.get()}"),
        message=f'{entr_var1.get()}',
        app_icon='C:\\Users\\Neet\\PycharmProjects\\GUI\\alarm.ico',
        timeout= value
    )

x = Tk()
x.geometry("600x600")
x.title("Notification Setter")
x.configure(background='yellow')
x.wm_iconbitmap("alarm.ico")
Label(x,text="Title:",font="lucida 30 bold",bg='red',fg='white').grid(row=0,column=0)
entr_var= StringVar()
en1=Entry(x,font='lucida 20',width=20,textvariable=entr_var).grid(row=0,column=2,pady=12,padx=12)
Label(x,text="Msg:",font="lucida 30 bold",bg='red',fg='white').grid(row=2,column=0)
entr_var1= StringVar()
en2=Entry(x,font='lucida 20',width=20,textvariable=entr_var1).grid(row=2,column=2,pady=12,padx=12)
Label(x,text="Timeout:",font="lucida 30 bold",bg='red',fg='white').grid(row=4,column=0)
entr_var2= StringVar()
en3=Entry(x,font='lucida 20',width=20,textvariable= entr_var2).grid(row=4,column=2,pady=12,padx=12)
Button(x,text="Notify",command=add,width=20,height=2,font='lucida 15 bold',bg='red',fg='white').grid(row=6,column=2)
x.mainloop()



