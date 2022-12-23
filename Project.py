from tkinter import *
root=Tk()
root.geometry('1200x800')
root.title("Teacher Portal")
root.resizable(True,True)

Label(text="TEACHER PORTAL",bg="black",fg="white",font=("arial",30,"bold"),width="300",height="2").pack()

f=Frame(root,bg="pink",width="350",height="700")
f.place(x=10,y=118)


# def printValue():
#     pname = player_name.get()
#     Label(root, text=f'{pname}, Registered!', pady=20, bg='#ffbf00').pack()

# player_name = Entry(root)
# player_name.pack(pady=30)

# Button(
#     root,
#     text="Register Player", 
#     padx=10, 
#     pady=5,
#     command=printValue
#     ).pack()

root.mainloop()