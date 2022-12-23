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

def submit():
    global a1
    global a2
    global a3
    global a4
    global a5

    try:
        a1 = int(entry.get())
    except:
        a1 = 0
    try:
         a2 = int(entry2.get())
    except:
         a2 = 0
    try:
         a3 = int(entry3.get())
    except:
         a3 = 0
    try:
         a4 = int(entry4.get())
    except:
         a4 = 0
    try:
         a5 = int(entry5.get())
    except:
         a5 = 0    
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)
    
def reset():
    entry.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)


Label(text="TEACHER PORTAL",bg="black",fg="white",font=("arial",30,"bold"),width="300",height="2").pack()

f=Frame(root,width="200",height="350",bg="#aaa")
f.place(x=10,y=110)

f1=LabelFrame(f,text="Functions",bg="#aaa")
f1.pack()

Button(f1,text="Browse File",command=open_window).pack()
Label(f1,text=" ",bg="#aaa").pack()


F2=Frame(root,width="500",height="355",bg="#aaa")
F2.place(x=136,y=110)

Label(F2,text="Weigtage",bg="#aaa",fg="black",font=("arial",18,"bold")).place(x=30,y=1)

Lab_Reports = Label(F2,text = "Lab Reports").place(x = 30,y = 55) 
entry = Entry(F2, width=25, textvariable=StringVar())
entry.place(x=200,y=54)

Lab_Performance = Label(F2,text = "Lab Performance").place(x = 30,y = 95)
entry2 = Entry(F2, width=25, textvariable=StringVar())
entry2.place(x=200,y=95)

Midterm = Label(F2,text = "Midterm").place(x = 30,y = 135) 
entry3 = Entry(F2, width=25, textvariable=StringVar())
entry3.place(x=200,y=135)

Final_term = Label(F2,text = "Final term").place(x = 30,y = 175) 
entry4 = Entry(F2, width=25, textvariable=StringVar())
entry4.place(x=200,y=175)

Cea = Label(F2,text = "Complex Engineering Activity").place(x = 30,y = 210) 
entry5 = Entry(F2, width=25, textvariable=StringVar())
entry5.place(x=200,y=210)

Button(F2,text="SUBMIT", command = submit).place(x=300,y=260)
display=Button(f1, text='Display')
display.pack(padx=1, pady=2)
generate=Button(f1, text='Generate in New File')
generate.pack(padx=5, pady=5)
search=Button(f1, text='Search')
search.pack( side=LEFT, padx=8, pady=8)
root.mainloop()