"""
GUI
Created by OfficalMuffin
17/05/18

"""

import tkinter

#Init tkinter GUI
window = tkinter.Tk()

#Title of GUI
window.title("GUI Python")

#Resolution of GUI
window.geometry("500x400")

#GUI Icon (Not Working)
#window.wm_iconbitmap('full-folder.png')

#Create Login Labels
usr = tkinter.Label(window, text="Username: ")
usrnmfield = tkinter.Entry(window)
psswd = tkinter.Label(window, text="Password: ")
psswdfield = tkinter.Entry(window)
login = tkinter.Button(window, text = "Login")

#Create Register Labels
eml = tkinter.Label(window, text="Email: ")
emailfield = tkinter.Entry(window)
confemail = tkinter.Label(window, text="Confirm Email: ")
confe = tkinter.Entry(window)
username = tkinter.Label(window, text="Choose Username: ")
usernamefield = tkinter.Entry(window)
password = tkinter.Label(window, text="Password: ")
passwordfield = tkinter.Entry(window)
confp = tkinter.Label(window, text="Confirm Password: ")
confirmpasswordfield = tkinter.Entry(window)
register = tkinter.Button(window, text = "Register")


#Print out Login labels on GUI
usr.pack()
usrnmfield.pack()
psswd.pack()
psswdfield.pack()
login.pack()

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
register.pack()

#Must keep the line below at bottom of code
window.mainloop()

