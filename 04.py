import mysql.connector
import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.geometry("400x250") 
my_connect = mysql.connector.connect(
  host="localhost",
  user="root", 
  passwd="root",
  database="detection"
)
my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM object limit 0,10")
i=0 
for object in my_conn: 
    for j in range(len(object)):
        e = Label(my_w,width=10, text=object[j]) 
        e.grid(row=i, column=j) 
        #e.insert(END, object[j])
    i=i+2
my_w.mainloop()