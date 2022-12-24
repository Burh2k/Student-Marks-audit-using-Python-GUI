from tkinter import *
from tkinter import filedialog
import pandas as pd
import os

files=[]
names=[]

root=Tk()
root.geometry('640x480')
root.title("Teacher Portal")
root.resizable(False,False)



def clear_frame():
   for widgets in F2.winfo_children():
      widgets.destroy()

def evaluate(y):
    clear_frame()
    Label(F2,text="Weightage",bg="#aaa",fg="black",font=("arial",18,"bold")).place(x=30,y=1)

    Lab_Reports = Label(F2,text = "Lab Reports").place(x = 30,y = 55) 
    entry = Entry(F2, width=25)
    entry.place(x=200,y=54)

    Lab_Performance = Label(F2,text = "Lab Performance").place(x = 30,y = 95)
    entry2 = Entry(F2, width=25)
    entry2.place(x=200,y=95)

    Midterm = Label(F2,text = "Midterm").place(x = 30,y = 135) 
    entry3 = Entry(F2, width=25)
    entry3.place(x=200,y=135)

    Final_term = Label(F2,text = "Final term").place(x = 30,y = 175) 
    entry4 = Entry(F2, width=25)
    entry4.place(x=200,y=175)

    Cea = Label(F2,text = "Complex Engineering Activity").place(x = 30,y = 210) 
    entry5 = Entry(F2, width=25)
    entry5.place(x=200,y=210)
    

    Button(F2,text="SUBMIT", command=lambda:submit(y,int(entry.get()),int(entry2.get()),int(entry3.get()),int(entry4.get()),int(entry5.get()))).place(x=300,y=260)


def submit(clas,a1,a2,a3,a4,a5):
    clear_frame()   

    clas["Performance total"]=(clas.iloc[:,2:16].sum(axis=1)/210)*a2
    clas["Lab Reports total"]=(clas.iloc[:,16:30].sum(axis=1)/210)*a1
    clas["Mid total"]=(clas.iloc[:,30]/55)*a3
    clas["Final total"]=(clas.iloc[:,31]/50)*a4
    clas["CEA total"]=(clas.iloc[:,32]/20)*a5
    clas["Grand total"]=(clas.iloc[:,33:38].sum(axis=1)) 

    clas.loc[clas['Grand total']>=80,'Grade']='A'
    clas.loc[clas['Grand total']>=70, 'Grade']='B'
    clas.loc[clas['Grand total']>=60, 'Grade']='C'
    clas.loc[clas['Grand total']>=50, 'Grade']='D'
    clas.loc[clas['Grand total']<=50, 'Grade']='F'
    
    Label(F2,text="FILE EVALUATED",bg="#aaa",fg="black").place(x=30,y=1)



def open_window():
    clear_frame()
    root.read=filedialog.askopenfilename(initialdir="F:/",title="Select a File",filetypes=(("CSV File","*.csv"),("All Files", "*.*")))
    global files
    global names
    y=pd.read_csv(root.read)
    files.append(y)
    names.append(os.path.split(root.read)[1])
    Label(F2,text="FILE ADDED SUCCESSFULLY!!!",bg="#aaa").place(x=30,y=1) 
    Button(F2,text="EVALUATE", command=lambda:evaluate(y)).place(x=30,y=31)
    
def fw(ss,s):
     clear_frame()
     ss.to_csv(s, index=False, sep=';')
     Label(F2,text="FILE WRITE SUCCESSFUL!!!",bg="#aaa").place(x=30,y=1) 
def wtc():
    clear_frame()
    global files
    global names
    if files:
         Label(F2,text = "Select File",bg="#aaa").place(x = 30,y = 30)
         clicked = StringVar()
         clicked.set(names[0])
         
         OptionMenu(F2,clicked,*files).place(x=30,y=60)
         Label(F2,text = "Enter Name of File",bg="#aaa").place(x = 30,y = 100) 
         s=Entry(F2,width=25,textvariable=StringVar())
         s.place(x=30,y=130)
         Button(F2,text="Write",command=lambda:fw(files[names.index(clicked.get())],s.get())).place(x=30,y=160)
    else:
         Label(F2,text = "No Files Added",bg="#aaa",fg="red").place(x = 30,y = 60)
    
def sear(a,b):
     clear_frame()
     y=a.loc[a['Roll numbers'] == b]
     Label(F2,text = y,bg="#aaa",fg="black").place(x = 30,y = 1)   


def search():
    clear_frame()
    global files
    global names
    if files:
         Label(F2,text = "Select File",bg="#aaa").place(x = 30,y = 30)
         clicked = StringVar()
         clicked.set(names[0])
         
         OptionMenu(F2,clicked,*files).place(x=30,y=60)
         Label(F2,text = "Enter Roll Number",bg="#aaa").place(x = 30,y = 100) 
         s=Entry(F2,width=25,textvariable=StringVar())
         s.place(x=30,y=130)
         Button(F2,text="Search",command=lambda:sear(files[names.index(clicked.get())],s.get())).place(x=30,y=160)
    else:
         Label(F2,text = "No Files Added",bg="#aaa",fg="red").place(x = 30,y = 60)



Label(text="TEACHER PORTAL",bg="black",fg="white",font=("arial",30,"bold"),width="300",height="2").pack()

f=Frame(root,width="200",height="350",bg="#aaa")
f.place(x=10,y=110)

f1=LabelFrame(f,text="Functions",bg="#aaa")
f1.pack()

Button(f1,text="Browse File",command=open_window).pack(padx=5,pady=10)
Button(f1, text='Display').pack(padx=5,pady=10)
Button(f1, text='Write to CSV',command=wtc).pack(padx=5,pady=10)
Button(f1, text='Search',command=search).pack(padx=5,pady=10)
Button(f1, text='Exit',command=root.quit).pack(padx=5,pady=10)


F2=Frame(root,width="500",height="355",bg="#aaa")
F2.place(x=136,y=110)

root.mainloop()