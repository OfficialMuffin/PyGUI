"""
GUI
Created by OfficialMuffin
17/05/18

"""

import tkinter
from tkinter import *

def login(): #Function to login
    loginSuccess.configure(text="Loggged In!")

def register(): #Function to register
    regComplete.configure(text="Registered! You may now login")

#Init tkinter GUI
window = tkinter.Tk()

#Title of GUI
window.title("GUI Python")

#Resolution of GUI
window.geometry("500x400")

#Background Colour
window.configure(background="#a1bdcd")

#GUI Image (Not Working)
#image = tkinter.PhotoImage(file="qt.png")
#imgwindow = tkinter.Label(window, image=image)
#imgwindow.pack()

#GUI Icon (Not Working)
#window.wm_iconbitmap('full-folder.png')

#Create Login Labels
usr = tkinter.Label(window, text="Username: ", bg="#a1bdcd")
usrnmfield = tkinter.Entry(window)
psswd = tkinter.Label(window, text="Password: ", bg="#a1bdcd")
psswdfield = tkinter.Entry(window)
loginSuccess = tkinter.Label(window, bg="#a1bdcd")
login = tkinter.Button(window, text = "Login", fg="#a1bdcd", bg="#383a39", command=login)

#Print out Login labels on GUI
usr.pack()
usrnmfield.pack()
psswd.pack()
psswdfield.pack()
loginSuccess.pack()
login.pack()

#Create Register Labels
eml = tkinter.Label(window, text="Email: ")
emailfield = tkinter.Entry(window)
confemail = tkinter.Label(window, text="Confirm Email: ", bg="#a1bdcd")
confe = tkinter.Entry(window)
username = tkinter.Label(window, text="Choose Username: ", bg="#a1bdcd")
usernamefield = tkinter.Entry(window)
password = tkinter.Label(window, text="Password: ", bg="#a1bdcd")
passwordfield = tkinter.Entry(window)
confp = tkinter.Label(window, text="Confirm Password: ", bg="#a1bdcd")
confirmpasswordfield = tkinter.Entry(window)
regComplete = tkinter.Label(window, bg="#a1bdcd")
register = tkinter.Button(window, text="Register", fg="#a1bdcd", bg="#383a39", command=register)

#Print out Register labels on GUI
eml.pack()
emailfield.pack()
confemail.pack()
confe.pack()
username.pack()
usernamefield.pack()
password.pack()
passwordfield.pack()
confp.pack()
confirmpasswordfield.pack()
regComplete.pack()
register.pack()

#Must keep the line below at bottom of code
window.mainloop()

