from tkinter import *



Billing = Tk()
Billing.title("Payment menu")
Billing.geometry("1400x700")

cover1 = Label(Billing, bg = "#c3e8c1", relief = RIDGE, bd = 5)
cover1.place(x = 0, width = 1400, height = 120)
LogoLabel = Label(Billing, text="SHOP", font=('Times New Roman', 30, 'bold'), bg='gray1',fg='ghost white', pady=5, padx=5)
LogoLabel.place(x=7, y=6)
INFO1 = Label(Billing, bg = "#c3e8c1", text = "Pending payment for product", font = ('Arial',30,'bold'))
INFO1.place(x = 200, y= 20)

Back = Button(Billing, text="BACK", font=('Times New Roman', 20, 'bold'), bg='gray46', fg='ghost white',pady=5, padx=5, relief=RAISED, bd=5)
Back.place(x=1200, y=15, width=150, height=60)
Billing.mainloop()
