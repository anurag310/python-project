import tkinter
from tkinter import *
import wikipedia as wk

window = Tk()
window.title("My mini WikiPedia")
window.config(bg="black")
f1_heading = Frame(window)
f2_frame = Frame(window)
f3_result = Frame(window)

Label(f1_heading,text="My mini WikiPedia",font=("Times",30,"bold"),bg="lightgreen").pack(side=TOP)

Label(f2_frame,text="Search Here",font=("Arial",20,"bold"),bg="yellow").pack(side=LEFT)

Label(f3_result,text="Searched results:",font=("Arial",25,"bold"),bg="lightpink").pack(side=LEFT)

entry_box = Entry(f3_result,width=40,font=("Arial",20,"bold"))
entry_box.pack(side=LEFT, fill=BOTH, expand=5)
entry_box.focus_set()


query= ''
text = Text(window,font("Arial",18,"bold"),bg="lightblue",padx=55,pady=10)

button1 = Button(f2_frame,text="Search",font=("Arial",15,"bold"),bg="red",fg="white")
button1.pack(side=RIGHT)

f1_heading.pack()
f2_frame.pack(side=TOP)
f3_result.pack(side=TOP, pady=20, padx=50)
text.pack()




window.mainloop()