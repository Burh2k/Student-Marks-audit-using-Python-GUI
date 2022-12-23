from tkinter import *
import easygui

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
    read=easygui.fileopenbox()
    global files
    files.append(read)

# def select_window():
    

Label(text="TEACHER PORTAL",bg="black",fg="white",font=("arial",30,"bold"),width="300",height="2").pack()

f=Frame(root,width="200",height="350",bg="#aaa")
f.place(x=10,y=110)

f1=LabelFrame(f,text="Functions",bg="#aaa")
f1.pack()

Button(f1,text="New..",command=open_window).pack()
Label(f1,text=" ",bg="#aaa").pack()
Button(f1,text="Select",command=select_window).pack()

F2=Frame(root,width="525",height="355",bg="#aaa")
F2.place(x=100,y=110)
root.mainloop()