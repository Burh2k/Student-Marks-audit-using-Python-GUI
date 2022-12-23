from tkinter import *
from tkinter import filedialog
import easygui
import os

files=[]

root=Tk()
root.geometry('640x480')
root.title("Teacher Portal")
root.resizable(False,False)

# def inputt()
def clear_frame():
   for widgets in F2.winfo_children():
      widgets.destroy()

def open_window():
    clear_frame()
    root.read=filedialog.askopenfilename(initialdir="F:/",title="Select a File",filetypes=(("CSV File","*.csv"),("All Files", "*.*")))
    global files
    files.append(os.path.split(root.read)[1])
    Label(F2,text=files).pack()

# def select_window():
    
clicked=StringVar()
clicked.set("None")

Label(text="TEACHER PORTAL",bg="black",fg="white",font=("arial",30,"bold"),width="300",height="2").pack()

f=Frame(root,width="200",height="350",bg="#aaa")
f.place(x=10,y=110)

f1=LabelFrame(f,text="Functions",bg="#aaa")
f1.pack()

Button(f1,text="New..",command=open_window).pack()
Label(f1,text=" ",bg="#aaa").pack()
drop=OptionMenu(f1, clicked, files).pack()

F2=Frame(root,width="525",height="355",bg="#aaa")
F2.place(x=100,y=110)
root.mainloop()