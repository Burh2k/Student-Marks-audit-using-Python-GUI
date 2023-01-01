import csv
from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox,ttk
from PIL import ImageTk, Image
import pandas as pd
import os
#import customtkinter

files=[]
names=[]

root=Tk()
root.geometry('640x480+660+250')
root.title("Teacher Portal")
root.resizable(False,False)
root.attributes('-alpha',0.95)



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
    Button(F2,text="RESET",command=lambda:evaluate(y)).place(x=250,y=260)

def evald():
    clear_frame()
    global files
    global names
    if files:
         Label(F2,text = "Select File",bg="#aaa").place(x = 30,y = 30)
         clicked = StringVar()
         clicked.set(names[0])
         
         OptionMenu(F2,clicked,*names).place(x=30,y=60)
         Button(F2,text="Select",command=lambda:evaluate(files[names.index(clicked.get())])).place(x=30,y=160)
    else:
         Label(F2,text = "No Files Added",bg="#aaa",fg="red").place(x = 30,y = 60)

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
     ss.to_csv(s+".csv", index=False, sep=',')
     Label(F2,text="FILE WRITE SUCCESSFUL!!!",bg="#aaa").place(x=30,y=1) 
def wtc():
    clear_frame()
    global files
    global names
    if files:
         Label(F2,text = "Select File",bg="#aaa").place(x = 30,y = 30)
         clicked = StringVar()
         clicked.set(names[0])
         
         OptionMenu(F2,clicked,*names).place(x=30,y=60)
         Label(F2,text = "Enter Name of File",bg="#aaa").place(x = 30,y = 100) 
         s=Entry(F2,width=25,textvariable=StringVar())
         s.place(x=30,y=130)
         Button(F2,text="Write",command=lambda:fw(files[names.index(clicked.get())],s.get())).place(x=30,y=160)
    else:
         Label(F2,text = "No Files Added",bg="#aaa",fg="red").place(x = 30,y = 60)
    
def sear(a,b):
     clear_frame()
     y=a.loc[a['Roll numbers'] == int(b)]
     frame1 = tk.LabelFrame(F2, text="Excel Data")
     frame1.place(height=250, width=500)

     # Frame for open file dialog
     file_frame = tk.LabelFrame(F2, text="Functions")
     file_frame.place(height=105, width=500, y=20,rely=0.65, relx=0)
     global tv1
     tv1 = ttk.Treeview(frame1)
     tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

     treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
     treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
     tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
     treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
     treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget
     tv1.delete(*tv1.get_children())
     tv1["column"] = list(y.columns)
     tv1["show"] = "headings"
     for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

     y_rows = y.to_numpy().tolist() # turns the dataframe into a list of lists
     for row in y_rows:
        tv1.insert("", "end", values=row)
        
     Button(file_frame,text="Reset",command=clear_frame).place(rely=0.20, relx=0)
       


def watch():
     frame1 = tk.LabelFrame(F2, text="Excel Data")
     frame1.place(height=250, width=500)

     # Frame for open file dialog
     file_frame = tk.LabelFrame(F2, text="Open File")
     file_frame.place(height=105, width=500, y=20,rely=0.65, relx=0)

     # Buttons
     button1 = tk.Button(file_frame, text="Browse A File", command=lambda: File_dialog())
     button1.place(rely=0.65, relx=0.50)

     button2 = tk.Button(file_frame, text="Load File", command=lambda: Load_excel_data())
     button2.place(rely=0.65, relx=0.30)

     # The file/file path text
     global label_file
     label_file = ttk.Label(file_frame, text="No File Selected")
     label_file.place(rely=0, relx=0)
     ## Treeview Widget
     global tv1
     tv1 = ttk.Treeview(frame1)
     tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

     treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
     treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
     tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
     treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
     treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget
    
     Button(file_frame,text="Reset",command=clear_frame).place(rely=0.65, relx=0.42)

def File_dialog():
    """This Function will open the file explorer and assign the chosen file path to label_file"""
    filename = filedialog.askopenfilename(initialdir="/",title="Select A File",filetype=(("CSV File","*.csv"),("All Files", "*.*")))
    label_file["text"] = filename
    return None

def Load_excel_data():
     """If the file selected is valid this will load the file into the Treeview"""
     file_path = label_file["text"]
     try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

     except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
     except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
     tv1.delete(*tv1.get_children())
     tv1["column"] = list(df.columns)
     tv1["show"] = "headings"
     for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

     df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
     for row in df_rows:
        tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
     #tv1.delete(*tv1.get_children())

def search():
    clear_frame()
    global files
    global names
    if files:
         Label(F2,text = "Select File",bg="#aaa").place(x = 30,y = 30)
         clicked = StringVar()
         clicked.set(names[0])
         
         OptionMenu(F2,clicked,*names).place(x=30,y=60)
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

root.iconbitmap('portal.ico')

Button(f1,text="Browse File",command=open_window).pack(padx=5,pady=10)
Button(f1, text='Evaluate', command=evald).pack(padx=5,pady=10)
Button(f1, text='Display', command=watch).pack(padx=5,pady=10)
Button(f1, text='Write to CSV',command=wtc).pack(padx=5,pady=10)
Button(f1, text='Search',command=search).pack(padx=5,pady=10)
Button(f1, text='Exit',command=root.quit).pack(padx=5,pady=10)



F2=Frame(root,width="515",height="355",bg="#aaa")
F2.place(x=114,y=110)

root.mainloop()