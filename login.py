from tkinter import *
from tkinter import font
import tkinter.messagebox
from turtle import Screen

from matplotlib.pyplot import text

def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Login System")
    root.geometry("500x500")
    
    Label(root, text='Please Enter your Username and Password', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="black",
                   bg="white",width=300).pack()
    Label(root, text="").pack()
    Label(root, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root,text="" ).pack()
    Label(root, text="").pack()
    Label(root, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root, text="", show="*").pack()
    Label(root, text="").pack()
    Button(root, text="Login", bg="black", fg='white', relief="groove", font=('arial', 12, 'bold'),command=login).pack()
    Label(root, text="")

    Button(root, text="Exit", bg="black", fg='white', relief="groove", font=('arial', 12, 'bold'),command=root.destroy).pack()
    Label(root, text="")
    
    
    


    


def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Login page")
    root2.geometry("450x300")
    root2.config(bg="white")

    
    

    

main_display()
