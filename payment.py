from tkinter import *
from tkinter import ttk



Billing = Tk()
Billing.title("Payment menu")
Billing.geometry("1400x700")
Billing.resizable(False,False)
cover1 = Label(Billing, bg = "#c3e8c1", relief = RIDGE, bd = 5)
cover1.place(x = 0, width = 1400, height = 120)
LogoLabel = Label(Billing, text="SHOP", font=('Times New Roman', 30, 'bold'), bg='gray1',fg='ghost white', pady=5, padx=5)
LogoLabel.place(x=7, y=6)
INFO1 = Label(Billing, bg = "#c3e8c1", text = "Pending payment for product", font = ('Arial',30,'bold'))
INFO1.place(x = 200, y= 20)
INFO2 = Label(Billing, bg ="#c3e8c1", text = "Items that are pending payment are lister here", font = ('Arial',15, "bold") )
INFO2.place(x = 200, y = 70)

cover2 = Label(Billing, bg = "#0f0f0f", relief = RAISED, bd = 5)
cover2.place(x = 0, y=  120, width = 950, height = 580)

cover3 = Label(Billing, bg = "#1d3852", relief = RIDGE, bd = 3)
cover3.place(x = 950,y = 630, width = 450, height = 80)
LABEL3 = Label(Billing, text = "Please pay on time to avoid problems", font= ('Arial',17,"bold"), fg = 'ghost white', bg ="#1d3852" )
LABEL3.place(x = 965, y = 650)

cover4 = Label(Billing, bg = "#235b82", relief  = RIDGE, bd = 3)
cover4.place(x = 950, y =530,width = 450, height = 100 )


cover5 = Label(Billing, bg = "#A6CAEC", relief = RIDGE, bd = 5 )
cover5.place(x = 950, y = 180, width = 450, height = 350)

cover7 = Label(Billing, text = "", bg = "#E3F2FD",bd = 3, relief = RAISED)
cover7.place(x = 965, y = 195, width = 420, height = 320)

cover6 = Label(Billing, bg = "#235b82", relief = RIDGE, bd = 3)
cover6.place(x = 950, y = 120, height = 60, width = 450)


LABEL4 = Label(Billing, text = "TOTAL AMOUNT TO PAID: ",fg = "ghost white", font = ("Arial",15,"bold"), bg ="#235b82")
LABEL4.place(x = 960, y= 540 )

EntryCost = Entry(Billing, font =("Helvetica",15,"bold"), relief = RIDGE , bd = 5)
EntryCost.configure(state = DISABLED)
EntryCost.place(x = 1030, y= 580, height = 40, width = 300)


MAINLABEL = Label(Billing, text = "Select Payment Method", font = ("Helvetica",22,"bold"), bg = "#235b82", fg = "ghost white")
MAINLABEL.place(x = 1010, y = 130)

LABEL1 = Label(Billing, text = "Selected Item:", bg = "#E3F2FD", font = ("Helvetica",15,"bold"))
LABEL1.place(x = 980, y =220)

LABEL2 = Label(Billing, text = "Total quantity:", bg = "#E3F2FD", font = ("Helvetica",15,"bold"))
LABEL2.place(x = 980, y =270)

LABEL2 = Label(Billing, text = "Total Cost:", bg = "#E3F2FD", font = ("Helvetica",15,"bold"))
LABEL2.place(x = 980, y =320)



E_NAME = Entry(Billing,font = ("Helvetica",17,"bold"), relief = RIDGE , bd = 5 , state= DISABLED)
E_NAME.place(x = 1150, y = 215, width = 210, height = 40)

E_QUAN = Entry(Billing,font = ("Helvetica",17,"bold"), relief = RIDGE , bd = 5 , state= DISABLED)
E_QUAN.place(x = 1150, y = 265, width = 210, height = 40)

E_NAME = Entry(Billing,font = ("Helvetica",17,"bold"), relief = RIDGE , bd = 5 , state= DISABLED)
E_NAME.place(x = 1150, y = 315, width = 210, height = 40)

n = StringVar()

E_PAYMENT  = ttk.Combobox(Billing, textvariable = n)
E_PAYMENT.config(font = ("Helvetica",15,"bold"))
E_PAYMENT.place(x = 1075, y = 390, width = 200, height = 40)


E_PAYMENT['values'] = ("G-CASH","PAY MAYA","7-ELEVEN",'BDO')

PAYNOW = Button(Billing, text ="PAY NOW!",font = ("Helvetica",15,"bold"), relief = RAISED, bd = 5,bg ="#3F51B5", fg = "ghost white")
PAYNOW.place(x = 1120, y = 450)

Back = Button(Billing, text="BACK", font=('Times New Roman', 20, 'bold'), bg='gray46', fg='ghost white',pady=5, padx=5, relief=RAISED, bd=5)
Back.place(x=1200, y=15, width=150, height=60)
Billing.mainloop()
