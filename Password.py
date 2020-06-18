from tkinter import *
from random import *
import string
import pyperclip

""" Functions """


def password():

    if check.get() == 1:
        length1 = length.get()

        characters = string.ascii_letters + string.punctuation + string.digits
        password = "".join(choice(characters) for x in range(length1))

        passwordety.delete(0, END)
        passwordety.insert(0, password)
        return

    else:
        length1 = length.get()

        characters = string.ascii_letters + string.digits
        password = "".join(choice(characters) for x in range(length1))

        passwordety.delete(0, END)
        passwordety.insert(0, password)

def copy():

    pyperclip.copy(passwordety.get())

""" Main Window """

root = Tk()

check = IntVar(value=1)

root.title('Password Generator')
root.geometry('350x300+400+200')
root.resizable(height=FALSE,width=FALSE)
root.iconbitmap(r"logo.ico")

new = LabelFrame(root,)
new.pack(padx = 10, pady = 10)

title = Label(new, text='Password Generator', font=('Ubuntu', 18, ))
title.grid(row=1, columnspan=5, padx=5, pady=5)

char = Label(new, text = 'Password Length', font = ('bold'))
char.grid(row=2, columnspan=5)

length = Scale(new,  from_=6, to=32, orient=HORIZONTAL, length = 260)
length.set(16)
length.grid(row=3, columnspan=5, padx=5)

checkbox = Checkbutton(new, text="Punctuation Characters  (Recommended)", variable = check)
checkbox.grid(row=4, columnspan=5, padx=5, pady=5)

passwordety = Entry(new, width = 40,)
passwordety.grid(row=5, columnspan=5, padx=5, pady=5)

gnrtbtn = Button(new, text='Generate', command = password)
gnrtbtn.grid(row = 6, column = 1,pady=5, padx =5)

copybtn = Button(new, text='Copy Passowrd', command = copy )
copybtn.grid(row = 6, column = 2,pady=5, padx =5)

exitbtn = Button(new, text='Exit', command=exit, width = 5)
exitbtn.grid(row=7, column=1, padx=5, pady=5)

root.mainloop()
