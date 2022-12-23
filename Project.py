from tkinter import *
from tkinter import filedialog
#import easygui
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

lab=Label(F2,text="Weigtage",bg="#aaa",fg="black",font=("arial",18,"bold")).place(x=30,y=1)

Lab_Reports = Label(F2,text = "Lab Reports").place(x = 30,y = 55) 
entry = Entry(F2, width=25, textvariable=int())
entry.place(x=200,y=54)

Lab_Performance = Label(F2,text = "Lab Performance").place(x = 30,y = 95)
entry2 = Entry(F2, width=25, textvariable=int())
entry2.place(x=200,y=95)

Midterm = Label(F2,text = "Midterm").place(x = 30,y = 135) 
entry2 = Entry(F2, width=25, textvariable=int())
entry2.place(x=200,y=135)

Final_term = Label(F2,text = "Final term").place(x = 30,y = 175) 
entry2 = Entry(F2, width=25, textvariable=int())
entry2.place(x=200,y=175)

CEA = Label(F2,text = "Complex Engineering Activity").place(x = 30,y = 210) 
entry2 = Entry(F2, width=25, textvariable=int())
entry2.place(x=200,y=210)

Button(F2,text="SUBMIT").place(x=300,y=260)

root.mainloop()