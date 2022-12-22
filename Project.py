from tkinter import *
root=Tk()
root.geometry('1200x800')
root.title("gaming zone")
root.resizable(False,False)
def Reset():
    entery_GTA_5.delete(0, END)
    entery_AMOUNG_US.delete(0, END)
    entery_PUBG.delete(0, END)
    entery_IGI_3.delete(0, END)
    entery_TAKEN_3.delete(0, END)
    entery_FREE_FIRE.delete(0, END)
    entery_CRICKET_2007.delete(0, END)
    entery_ROAD_RASH.delete(0, END)

def Total():
    try:
        a1 = int(GTA_5.get())
    except:
        a1 = 0
    try:
        a2 = int(AMOUNG_US.get())
    except:
        a2 = 0
    try:
        a3 = int(PUBG.get())
    except:
        a3 = 0
    try:
        a4 = int(IGI_3.get())
    except:
        a4 = 0
    try:
        a5 = int(TAKEN_3.get())
    except:
        a5 = 0
    try:
        a6 = int(FREE_FIRE.get())
    except:
        a6 = 0
    try:
        a7 = int(CRICKET_2007.get())
    except:
        a7 = 0
    try:
        a8 = int(ROAD_RASH.get())
    except:
        a8 = 0

    c1 = 150 * a1
    c2 = 40 * a2
    c3 = 120 * a3
    c4 = 100 * a4
    c5 = 80 * a5
    c6 = 60 * a6
    c7 = 90 * a7
    c8 = 50 * a8

    lbl_Total=Label(f2,font=("aria", 15, "bold"), text="TOTAL BILL", width=10, fg="black", bg="lightyellow")
    lbl_Total.place(x=20,y=490)

    entry_total = Entry(f2, font=("aria", 15, "bold"), textvariable=TOTALL_BILL, bd=6, width=10, bg="lightyellow")
    entry_total.place(x=160, y=490)

    total_cost = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8
    string_bill = "Rs.", str('%.2f' % total_cost)
    TOTALL_BILL.set(string_bill)


def InformationEntry():
    txtPaymentSlip.delete("1.0", END)
    txtPaymentSlip.insert(END,"GTA 5 :\t\t" + GTA_5.get() + "\n\n")
    txtPaymentSlip.insert(END, "AMOUNG US :\t\t" + AMOUNG_US.get() + "\n\n")
    txtPaymentSlip.insert(END, "PUBG :\t\t" + PUBG.get() + "\n\n")
    txtPaymentSlip.insert(END, "IGI 3 :\t\t" + IGI_3.get() + "\n\n")
    txtPaymentSlip.insert(END, "TAKEN 3 :\t\t" + TAKEN_3.get() + "\n\n")
    txtPaymentSlip.insert(END, "FREE FIRE :\t\t" + FREE_FIRE.get() + "\n\n")
    txtPaymentSlip.insert(END, "CRICKET 2007 :\t\t" + CRICKET_2007.get() + "\n\n")
    txtPaymentSlip.insert(END, "ROAD RASH :\t\t" + ROAD_RASH.get() + "\n\n")

class games:
    def __init__(self,GTA_5,AMOUNG_US,PUBG,IGI_3,TAKEN_3,FREE_FIRE,CRICKET_2007,ROAD_RASH):
        self.GTA_5=GTA_5
        self.AMOUNG_US=AMOUNG_US
        self.PUBG=PUBG
        self.IGI_3=IGI_3
        self.TAKEN_3=TAKEN_3
        self.FREE_FIRE=FREE_FIRE
        self.CRICKET_2007=CRICKET_2007
        self.ROAD_RASH=ROAD_RASH

Label(text="GAMING ZONE",bg="black",fg="white",font=("arial",30,"bold"),width="300",height="2").pack()

#GAMES AVAILABLE
#FIRST FRAME
f=Frame(root,bg="pink",width="350",height="700")
f.place(x=10,y=118)
Label(f,text="GAMES AVAILABLE",font=("arial",25,"bold"),fg="white",bg="black").place(x=10,y=80)
Label(f,font=("calibri",18,"bold"),text="GTA 5......Rs 150/hour",fg="black",bg="pink").place(x=10,y=140)
Label(f, font=("calibri", 18, "bold"), text="AMOUNG US......Rs 40/hour", fg="black",bg="pink").place(x=10, y=180)
Label(f, font=("calibri", 18, "bold"), text="PUB G......Rs 120/hour", fg="black",bg="pink").place(x=10, y=220)
Label(f, font=("calibri", 18, "bold"), text="IGI 3......Rs 100/hour", fg="black",bg="pink").place(x=10, y=260)
Label(f, font=("calibri", 18, "bold"), text="TAKEN 3......Rs 80/hour", fg="black",bg="pink").place(x=10, y=300)
Label(f, font=("calibri", 18, "bold"), text="FREE_FIRE ......Rs 60/hour", fg="black",bg="pink").place(x=10, y=340)
Label(f, font=("calibri", 18, "bold"), text="CRICKET 2007......Rs 90/hour", fg="black",bg="pink").place(x=10, y=380)
Label(f, font=("calibri", 18, "bold"), text="ROAD_RASH......Rs 50/hour", fg="black",bg="pink").place(x=10, y=420)

#SECOND FRAME
f2 = Frame(root, bg="lightyellow", width=350, height=7000)
f2.place(x=830, y=118)

Bill=Label(f2,text="YOUR TOTAL BILL",font=("arial",25,"bold"),fg="white",bg="black")
Bill.place(x=15, y=30)
txtPaymentSlip = Text(f2, height=22, width=34, bd=16, font=('arial', 13, 'bold'), fg="black", bg="white")
txtPaymentSlip.place(x=0, y=90)


# ENTRY OF GAMES
f1=Frame(root,bd=5,height=600,width=450,relief=RAISED)
f1.pack()
Label(f1,text="HOW MANY GAMES YOU PLAYED ?",font=("arial",17,"bold"),fg="white",bg="black").place(x=20,y=35)
GTA_5=StringVar()
AMOUNG_US=StringVar()
PUBG=StringVar()
IGI_3=StringVar()
TAKEN_3=StringVar()
FREE_FIRE=StringVar()
CRICKET_2007=StringVar()
ROAD_RASH=StringVar()
TOTALL_BILL=StringVar()


#Label 1
lbl_GTA_5=Label(f1,font=("aria",20,"bold"),text="GTA 5",width=12,fg="black")
lbl_GTA_5.place(x=1,y=110)
#entry 1
entery_GTA_5=Entry(f1,font=("aria",20,"bold"),textvariable=GTA_5,bd=6,width=8,bg="lightpink")
entery_GTA_5.place(x=260, y=110)

#Label 2
lbl_AMOUNG_US=Label(f1,font=("aria",20,"bold"),text="AMOUNG US",width=12,fg="black")
lbl_AMOUNG_US.place(x=1,y=160)
#entry 2
entery_AMOUNG_US=Entry(f1,font=("aria",20,"bold"),textvariable=AMOUNG_US,bd=6,width=8,bg="lightpink")
entery_AMOUNG_US.place(x=260, y=160)

#Label 3
lbl_PUBG=Label(f1,font=("aria",20,"bold"),text="PUBG",width=12,fg="black")
lbl_PUBG.place(x=1,y=210)
#entry 3
entery_PUBG=Entry(f1,font=("aria",20,"bold"),textvariable=PUBG,bd=6,width=8,bg="lightpink")
entery_PUBG.place(x=260, y=210)

#Label 4
lbl_IGI_3=Label(f1,font=("aria",20,"bold"),text="IGI 3",width=12,fg="black")
lbl_IGI_3.place(x=1,y=260)
#entry 4
entery_IGI_3=Entry(f1,font=("aria",20,"bold"),textvariable=IGI_3,bd=6,width=8,bg="lightpink")
entery_IGI_3.place(x=260, y=260)

#Label 5
lbl_TAKEN_3=Label(f1,font=("aria",20,"bold"),text="TAKEN 3",width=12,fg="black")
lbl_TAKEN_3.place(x=1,y=310)
#entry 5
entery_TAKEN_3=Entry(f1,font=("aria",20,"bold"),textvariable=TAKEN_3,bd=6,width=8,bg="lightpink")
entery_TAKEN_3.place(x=260, y=310)

#Label 6
lbl_FREE_FIRE=Label(f1,font=("aria",20,"bold"),text="FREE FIRE",width=12,fg="black")
lbl_FREE_FIRE.place(x=1,y=360)
#entry 6
entery_FREE_FIRE=Entry(f1,font=("aria",20,"bold"),textvariable=FREE_FIRE,bd=6,width=8,bg="lightpink")
entery_FREE_FIRE.place(x=260, y=360)

#Label 7
lbl_CRICKET_2007=Label(f1,font=("aria",20,"bold"),text="CRICKET 2007",width=12,fg="black")
lbl_CRICKET_2007.place(x=1,y=410)
#entry 7
entery_CRICKET_2007=Entry(f1,font=("aria",20,"bold"),textvariable=CRICKET_2007,bd=6,width=8,bg="lightpink")
entery_CRICKET_2007.place(x=260, y=410)

#Label 8
lbl_ROAD_RASH=Label(f1,font=("aria",20,"bold"),text="ROAD_RASH",width=12,fg="black")
lbl_ROAD_RASH.place(x=1,y=460)
#entry 8
entery_ROAD_RASH=Entry(f1,font=("aria",20,"bold"),textvariable=ROAD_RASH,bd=6,width=8,bg="lightpink")
entery_ROAD_RASH.place(x=260, y=460)

#BUTTON

btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,"bold"),width=8,text="RESET",command=Reset)
btn_reset.place(x=10,y=540)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,"bold"),width=8,text="TOTAL",command=Total)
btn_total.place(x=150,y=540)

btn_display=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,"bold"),width=8,text="ENTRY",command=InformationEntry)
btn_display.place(x=300,y=540)

ahmer=games("gta","amoung","pubg","igi","taken","free","cricket","road")
root.mainloop()