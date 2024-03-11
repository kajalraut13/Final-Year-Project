from logging import root
from tkinter import *
from tkinter import messagebox
import os



def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Login page")
    root2.geometry("450x300")
    root2.config(bg="white")

    global username_verification
    global password_verification
    Label(root2, text='Please Enter your Username and Password', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="black",
                   bg="white",width=300).pack()
    username_verification = StringVar()
    password_verification = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=username_verification).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=password_verification, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Login", bg="black", fg='white', relief="groove", font=('arial', 12, 'bold')).pack()
    Label(root2, text="")

def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Login System")
    root.geometry("500x500")
    Label(root,text='Welcome to Log In System',  bd=20, font=('arial', 20, 'bold'), relief="groove", fg="black",
                   bg="white",width=300).pack()
    Button(root,text='Log In', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="black",
                   bg="white",command=login).pack()




main_display()


