root=Tk()
root.geometry('640x480')
root.title("Teacher Portal")
root.resizable(True,True)

# def inputt()


Label(text="TEACHER PORTAL",bg="black",fg="white",font=("arial",30,"bold"),width="300",height="2").pack()

f=Frame(root,width="200",height="350",bg="#aaa")
f.pack()

f1=LabelFrame(f,text="Functions",bg="#aaa")
f1.pack()

Button(f1,text="New..").pack()
Button(f1,text="Select").pack()

f2 = Frame(root, bg="lightyellow", width=350, height=7000)
f2.place(x=400, y=118)

root.mainloop()