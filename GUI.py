from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox 

GUI = Tk() # this is the main screen of the program
GUI.title('program saves information') #this is the name of the program
GUI.geometry('500x400') #this is the scale of thd program

L1 = Label(GUI,text='program saves information',font=('Angsna New',),fg='green')
L1.place(x=30,y=20)
####################
def Button2() :
    text = 'Now you have money in your account 300 cash.'
    messagebox.showinfo('money in your account',text)

FB1 = Frame(GUI) #same as bord
FB1.place(x=100,y=50)
B2 = ttk.Button(FB1,text='How much cash do you have ?',command=Button2)
B2.pack(ipadx=20,ipady=20)
####################
def Button3() :
    text = 'Python 101, Math.'
    messagebox.showinfo('learn subject on 10-20 Feb.',text)

FB2 = Frame(GUI) #same as bord
FB2.place(x=200,y=200)
B2 = ttk.Button(FB1,text='What subject do you study this week ?',command=Button3)
B2.pack(ipadx=20,ipady=20)

GUI.mainloop()
