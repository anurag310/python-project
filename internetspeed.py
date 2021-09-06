from tkinter import *
from tkinter import messagebox
import pyspeedtest

def one():
    speed = pyspeedtest.SpeedTest("www.google.com")
    a1 = (str(speed.download())+["Bytes per second"])
    message.showinfo("Your download speed",a1)
root = Tk()
root.title("INTERNET SPEED CHECKER")
root.config(bg="light green")
root.geometry("500×200")

label1 = Label(root,text="Internet speed checker",font=("Arial",30,"bold"),bg="blue").pack()
button1 = Button(root, text="Click !!",font("Arial",20,"bold"),bg="yellow",height=1,width=10,command= one).pack()


root.mainloop()