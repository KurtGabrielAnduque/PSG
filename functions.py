from tkinter import *

class Payroll:

    def __init__(self, GUI):
        self.GUI = GUI
        Main_Label = Label(self.GUI,bd=3,text="PAYROLL SYSTEM",font=('Arial bold',20))
        Main_Label.pack(padx = 20,pady = 20)


        # mga label under frame1 ===================================================
        Frame1 = Frame(self.GUI,bd=5,relief=RIDGE, bg = "white")
        Frame1.place(x=10,y=70, width = 750, height = 630)




        F1_Label = Label(self.GUI, bd=3, text= "Employee Details", font = ('Arial bold',20), bg='grey')
        F1_Label.place(x = 12 ,y = 70, width = 748, height = 50)

        F1_Label2 = Label(self.GUI, text='Employee I.D.: ', font= ('Arial bold', 15), bg= 'white')
        F1_Label2.place(x = 20 , y= 130, width = 200, height = 50)
        F1_Entry1 = Entry(self.GUI,font=('Arial',15), bg = 'old lace',bd =3)
        F1_Entry1.place(x = 200, y = 135, width = 200, height = 40)
        F1_Button1 = Button(self.GUI,text="Search", font = ('Arial',15),bg = 'lavender' ,bd =3)
        F1_Button1.place(x = 410,y = 135, width = 150, height = 40)


        F1_Label3 = Label(self.GUI, text='Name: ', font= ('Arial bold', 15), bg='white')
        F1_Label3.place(x = 20, y = 200, width = 150, height = 50 )
        F1_Entry2 = Entry(self.GUI, font=('Arial', 15), bg = 'old lace',bd =3)
        F1_Entry2.place(x = 150, y = 205 , width = 200 , height = 40)


        F1_Label4 = Label(self.GUI, text="Age: ", font = ('Arial bold', 15), bg= 'white')
        F1_Label4.place(x = 25, y = 265, width = 150, height = 50)
        F1_Entry3 = Entry(self.GUI,font=('Arial',15), bg = 'old lace',bd =3)
        F1_Entry3.place(x =150, y = 270, width = 200, height = 40)

        F1_Label5 = Label(self.GUI, text = "Gender: ", font = ('Arial bold', 15), bg ='white')
        F1_Label5.place(x = 25, y = 330, width = 150, height = 50)
        F1_Entry4 = Entry(self.GUI, font = ('Arial', 15), bg= 'old lace',bd =3)
        F1_Entry4.place(x = 150, y =335, width = 200, height = 40)


        F1_Label6 = Label(self.GUI, text="Email: ", font= ('Arial bold', 15), bg= 'white')
        F1_Label6.place(x = 25, y = 390, width = 150, height = 50)
        F1_Entry5 = Entry(self.GUI, font = ('Arial', 15), bg = 'old lace',bd =3)
        F1_Entry5.place(x = 150, y = 395, width = 200, height = 40)


        F1_Label8 = Label(self.GUI, text="Date of Birth: ", font = ('Arial bold', 15), bg = 'white')
        F1_Label8.place(x = 400, y = 200, width = 150, height = 50)
        F1_Entry6 = Entry(self.GUI, font=('Arial',15), bg = 'old lace',bd =3)
        F1_Entry6.place(x = 540, y= 205, width = 200, height= 40)


        F1_Label9 = Label(self.GUI, text="Contact No : ", font = ('Arial bold', 15) ,bg= 'white')
        F1_Label9.place(x = 400, y= 265, width = 150, height = 50)
        F1_Entry7 = Entry(self.GUI, font = ('Arial', 15), bg = 'old lace',bd =3)
        F1_Entry7.place(x = 540, y = 270 , width = 200, height = 40)

        F1_Label10 = Label(self.GUI, text="Status: ", font = ('Arial bold', 15), bg = 'white')
        F1_Label10.place(x = 400, y = 330, width = 150, height = 50)
        F1_Entry8 = Entry(self.GUI,font = ('Arial', 15), bg = 'old lace',bd =3)
        F1_Entry8.place(x = 540, y = 335, width = 200, height = 40)

        F1_Label11 = Label(self.GUI, text="Address: ", font =('Arial bold', 15), bg = 'white')
        F1_Label11.place(x = 20,  y = 450, width = 150, height = 50)
        F1_Entry9 = Text(self.GUI, font = ('Arial',15), bg = 'old lace',bd =3)
        F1_Entry9.place(x = 150, y = 460, width = 590, height = 200)
        #==========================================================================================





        #MGA ELEMENT UNDER FRAME 2 DITO PAPASOK ===================================================
        Frame2 = Frame(self.GUI, bd=5, relief=RIDGE, bg='white')
        Frame2.place(x=770, y=70, width=610, height=420)

        F2_Label = Label(self.GUI, bd= 3, text= "Employee Salary Details", font= ('Arial bold', 20), bg = 'grey')
        F2_Label.place(x = 772, y = 70, width = 608, height = 50)

        #department
        F2_Label1 = Label(self.GUI, text="Department: ", font = ('Arial bold', 15), bg = 'white')
        F2_Label1.place(x = 780 , y = 130, width = 150 , height = 50)
        F2_Entry1 = Entry(self.GUI, font = ('Arial', 15), bg= 'old lace',bd =3)
        F2_Entry1.place(x = 920,  y = 135, width = 150, height = 40)

        #No of days
        F2_Label2 = Label(self.GUI, text="No. of days: ", font = ('Arial bold', 15), bg= 'white')
        F2_Label2.place(x = 780, y= 200, width = 150 , height = 50)
        F2_Entry2 = Entry(self.GUI, font=('Arial', 15), bg = 'old lace',bd =3)
        F2_Entry2.place(x = 920, y = 205, width = 150 , height = 40)

        #rate per day
        F2_Label3 = Label(self.GUI,text="Rate per day: ", font = ('Arial bold', 15), bg='white')
        F2_Label3.place(x = 1080, y = 130, width = 150, height = 50)
        F2_Entry3 = Entry(self.GUI, font=('Arial', 15), bg='old lace',bd =3)
        F2_Entry3.place(x = 1220, y = 135, width = 150, height = 40)


        #salary
        F2_Label4 = Label(self.GUI, text="Salary: ", font=('Arial bold', 15), bg = 'white')
        F2_Label4.place(x = 1080, y = 200, width = 150, height = 50)
        F2_Entry4 = Entry(self.GUI, font=('Arial', 15), bg= 'old lace',bd =3)
        F2_Entry4.place(x = 1220, y= 205 , width = 150, height = 40)

        F2_Label5 = Label(self.GUI, text = "SSS: ", font= ('Arial bold', 15), bg = 'white')
        F2_Label5.place(x = 780, y= 260, width = 150, height = 50)
        F2_Label5 = Entry(self.GUI, font=('Arial', 15), bg='old lace', bd = 3)
        F2_Label5.place(x = 920, y = 265, width = 150, height = 40)


        F2_Label6 = Label(self.GUI, text = "PAG-IBIG: ", font = ('Arial bold', 15), bg = 'white')
        F2_Label6.place(x = 1080, y = 260, width = 150, height = 50)
        F2_Entry6 = Entry(self.GUI,font=('Arial', 15), bg='old lace', bd = 3)
        F2_Entry6.place(x = 1220, y = 265, width = 150, height = 40)


        F2_Label7 = Label(self.GUI, text = "PHILHEALTH: ", font = ('Arial bold', 15), bg = 'white')
        F2_Label7.place(x = 780, y = 310, width = 150, height = 50)
        F2_Entry7 = Entry(self.GUI, font=('Arial', 150), bg = 'old lace', bd= 3)
        F2_Entry7.place(x = 920, y = 315, width = 150, height = 40)

        F2_Label8 = Label(self.GUI, text= "TAX: ", font=('Arial bold', 15), bg='white')
        F2_Label8.place(x = 1080, y = 310, width = 150, height = 50)
        F2_Entry8 = Entry(self.GUI, font= ('Arial', 15),bg = 'old lace', bd = 3)
        F2_Entry8.place(x = 1220, y = 315, width = 150, height = 40)





        #BUTTONS
        # calculate
        F2_Button1 = Button(self.GUI, text=" CALCULATE ", font = ('Arial bold', 15), bg = 'coral',bd =3)
        F2_Button1.place(x = 800, y = 370, width = 180, height = 50)

        # save
        F2_Button2 = Button(self.GUI, text=" SAVE ", font = ('Arial bold', 15), bg = 'khaki1',bd=3)
        F2_Button2.place(x = 990, y = 370, width = 180, height = 50)

        #clear
        F2_Button3 = Button(self.GUI,text=" CLEAR ", font= ('Arial bold',15), bg = 'light pink', bd= 3)
        F2_Button3.place(x = 1180, y= 370 , width = 180, height = 50)

        #update
        F2_Button4 = Button(self.GUI, text=" UPDATE ", font =('Arial bold',15), bg= 'plum1', bd =3 )
        F2_Button4.place(x = 799, y = 430, width = 270)

        #delete

        F2_Button5 = Button (self.GUI, text=" DELETE ", font=('Arial bold', 15), bg='RosyBrown1', bd = 3)
        F2_Button5.place(x = 1090, y = 430, width = 270)

        # ==========================================================================================



        #Frame4 elements under =====================================================================
        Frame4 = Frame(self.GUI, bd=5, relief=RIDGE, bg='white')
        Frame4.place(x=770, y=500, width=610, height=200)



        F4_Label = Label(self.GUI, bd=3, text="PAY SLIP", font =('Arial bold', 20), bg='grey')
        F4_Label.place(x=773, y= 500, width = 606, height = 50)

        F4_textbox = Text(self.GUI, font = ('Arial', 8), bg='old lace', bd = 3)
        F4_textbox.place(x=773, y= 550, width =606, height = 150)


        #===========================================================================================
