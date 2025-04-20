from tkinter import *
import pyodbc

def delete():
    Entry1.delete(0,END)

def CheckTable():
    print('EMPTY TALBE')


def CreateTable(databasename):

    def TBCREATE(databasename):
        try:

            Name = databasename
            connection = pyodbc.connect(
                'DRIVER={SQL SERVER};'
                'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
                f'Database={Name};'
                'Trusted_Connection=yes;'
            )

            connection.autocommit = True
            query_stmt = f'''CREATE TABLE {TENTRY.get()}
                          ({ECOL1.get()} {Tradio_var1.get()},
                          {ECOL2.get()} {Tradio_var2.get()})'''

            connection.execute(query_stmt)
            INFO1.config(text=f'SUCCESSFULLY CREATED table {TENTRY.get()}')

        except pyodbc.Error as ex:
            INFO1.config(text=f'CREATE FAILED')



    CTB = Tk()
    CTB.geometry('1000x800')
    CTB.title(f'CREATE TABLE in {databasename}')

    CTBLABEL = Label(CTB,text = f'Create A new Table', font = ('Arial',20,'bold'),bg = 'bisque', padx= 800, pady= 50)
    CTBLABEL.pack(fill = 'x', pady = 30)

    frames = Frame(CTB)
    frames.pack(pady = 20)

    TALBENAME = Label(frames, text = 'TABLE Name', font = ('Arial', 15,'bold'))
    TALBENAME.grid(row = 1, column = 0)

    TENTRY = Entry(frames, font = ('Arial',15))
    TENTRY.grid(row = 1,column = 1)


    COL1 = Label(frames, text = 'Column 1: ',font= ('Arial',15,'bold'))
    COL1.grid(row=2, column = 0)

    ECOL1 = Entry(frames, font=('Arial', 15))
    ECOL1.grid(row=2, column=1)

    Tradio_var1 = StringVar(value='')
    TRadio1 = Radiobutton(frames,text = 'varchar(50)',variable=Tradio_var1,value= 'varchar(50)')
    TRadio1.grid(row = 2, column = 2, padx = 20)


    TRadio2 = Radiobutton(frames, text = 'integer', variable=Tradio_var1, value= 'integer')
    TRadio2.grid(row = 2, column = 3, padx = 80)



    COL2 = Label(frames, text = 'Column 2: ',font= ('Arial',15,'bold'))
    COL2.grid(row=3, column = 0)

    ECOL2 = Entry(frames, font=('Arial', 15))
    ECOL2.grid(row=3, column=1)

    Tradio_var2 = StringVar(value='')
    TRadio21 = Radiobutton(frames,text = 'varchar(50)',variable=Tradio_var2,value= 'varchar(50)')
    TRadio21.grid(row = 3, column = 2, padx = 20)


    TRadio22 = Radiobutton(frames, text = 'integer', variable=Tradio_var2, value= 'integer')
    TRadio22.grid(row = 3, column = 3, padx = 80)

    CREATEBOT = Button(frames, text = 'CREATE TABLE', relief=RAISED, bd = 5, command= lambda : TBCREATE(databasename), bg = 'salmon', font = ('Arial',15,'bold'))
    CREATEBOT.grid(row = 4, column = 2, padx = 80)

    INFO1 = Label(frames, text='STATUS', font=('Aria', 20, 'bold'))
    INFO1.grid(row=5, column=1)




def db_connect():
    try:
        if Entry1.get() == "":
            INFO.config(text= "PLS ENTER A NAME BRO!")
        else:
            Name = Entry1.get()
            connection = pyodbc.connect(
                'DRIVER={SQL SERVER};'
                'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
                f'Database={Name};'
                'Trusted_Connection=yes;'
            )

            INFO.config(text = f'Connected to {Name}')
            Connected(Name)
    except pyodbc.Error as ex:
      INFO.config(text=f'Connection Failed')

def Connected(databasename):
    new_window = Tk()
    new_window.title(f'Database {databasename}')
    new_window.geometry('1000x800')

    MAINLABEL = Label(new_window,text = f'Welcom to Database {databasename}', font = ('Arial',20,'bold'),bg = 'bisque', padx= 800, pady= 50)
    MAINLABEL.pack(padx = 50, pady = 30)

    Check_Button = Button(new_window, text = 'CHECK TABLES',command=CheckTable, relief= RAISED, font = ('Arial',20,'bold'), bd = 5)
    Check_Button.config(bg = 'bisque')
    Check_Button.place(x = 375, y = 200, height = 80, width = 300)

    Create_Button = Button(new_window, text = 'CREATE NEW TABLE', command= lambda: CreateTable(databasename), relief= RAISED, font=('Aria',20,'bold'), bd = 5)
    Create_Button.config(bg = 'salmon')
    Create_Button.place(x=375, y=300, height=80, width=300)



    window.destroy()

def db_creat():
    try:
        Name = Entry1.get()
        connection = pyodbc.connect(
            'DRIVER={SQL SERVER};'
            'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
            'Database=master;'
            'Trusted_Connection=yes;'
        )

        connection.autocommit = True
        connection.execute(f'CREATE DATABASE {Name}')
        INFO.config(text =f'SUCCESSFULLY CREATED DATABSE {Name}')

    except pyodbc.Error as ex:
        INFO.config(text=f'CREATE FAILED')


window = Tk()
window.geometry('800x500')
icon = PhotoImage(file = 'hospital.png')
window.iconphoto(True, icon)

Label1 = Label(window, text = 'WELCOME TO DATABASE CONNECTION MANAGEMENT', font = ('Arial',20),padx = 40, bg = 'salmon')
Label1.config()
Label1.grid(row = 0 , column = 1)

Label2 = Label(window ,  text = 'Enter A name: ', font = ('Aria',20, 'bold'))
Label2.place(x = 50, y = 45)

Entry1 = Entry(window, font= ('Arial',20), relief=RAISED, bd = 5)
Entry1.grid(row = 1, column = 1)


Button1 = Button(window, text ='CONNECT DATABASE', command=db_connect, padx= 20, font = ('Arial',15))

Button1.config(bg = 'salmon')
Button1.grid(row = 2, column = 1)


Button2 = Button(window, text = 'CREATE DATABASE', command = db_creat, padx= 20, font = ('Arial',15))
Button2.config(bg = 'bisque')
Button2.grid(row = 3, column = 1)


BUTTON3 = Button(window, text = 'Delete', command= delete, padx=20, font =('Arial',15))
BUTTON3.config(bg = 'coral')
BUTTON3.grid(row= 4, column = 1)
INFO = Label(window , text = 'STATUS', font = ('Aria',20,'bold'))
INFO.grid(row = 5, column = 1)

window.mainloop()