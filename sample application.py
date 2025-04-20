import pyodbc
from tkinter import *

def CShop(databasename):
    cshop = Tk()
    cshop.geometry('1000x800')
    cshop.title('SHOP INFO')

    MAIN_LABEL = Label(cshop, text=f'{databasename} SHOP INFORMATION', font=('Ink Free', 30, 'bold'), pady=50, bg='khaki1')
    MAIN_LABEL.pack(fill='x')

    Check_SALES = Button(cshop, text='SALES RECORD', font=('Arial', 20, 'bold'), pady=50, bg='sandy brown')
    Check_SALES.config(command=lambda: CSales(databasename))
    Check_SALES.place(x = 325, y = 200, height = 70, width = 300)

    Check_Employee = Button(cshop, text='CHECK EMPLOYEES', font=('Arial', 20, 'bold'), pady=50, bg='sandy brown')
    Check_Employee.config(command=lambda: CEmployee(databasename))
    Check_Employee.place(x=325, y=300, height=70, width=300)

    Check_Products = Button(cshop, text='CHECK PRODUCTS', font=('Arial', 20, 'bold'), pady=50, bg='wheat1')
    Check_Products.config(command=lambda: CEmployee(databasename))
    Check_Products.place(x=325, y=400, height=70, width=300)



def CSales(databasename):
    print(databasename)

def CEmployee(databasename):
    print(databasename)


def CProducts(databasename):
    print(databasename)

def Buy_Products(databasename):
    print(databasename)

def Add_Products(databasename):

    def check_products():
        try:
            connect = pyodbc.connect(
                'DRIVER={SQL SERVER};'
                'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
                f'DATABASE={databasename};'
                'Trusted_Connection=yes;'
            )
            connect.autocommit = True
            cursor = connect.cursor()
            query_stmt = "SELECT * FROM ITEM WHERE merch_ID = ? or merch_name = ?"
            cursor.execute(query_stmt,)



            for data in cursor:
                UPDATE_TEXT.insert('end',f'Item ID: {data[0]}, Name: {data[1]}, Cost: {data[2]}, Quantity: {data[3]}\n')
        except pyodbc.Error as ex:
            INFO_ADD.config(text=f'UPDATE FAILED', fg='red')
            print(ex)



    def add_product():
        try:
            ID = int(EP_ID.get())
            Name = EP_NAME.get()
            Cost = int(E_Cost.get())
            Quantity = int(E_Quantity.get())
            connect = pyodbc.connect(
                'DRIVER={SQL SERVER};'
                'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
                f'DATABASE={databasename};'
                'Trusted_Connection=yes;'
            )
            connect.autocommit = True
            cursor = connect.cursor()
            query_stmt = f'''INSERT INTO ITEM (Item_ID,Item_name,Item_value,Item_quatity) VALUES (?,?,?,?)'''
            cursor.execute(query_stmt,(ID,Name,Cost,Quantity))
            INFO_ADD.config(text = 'Appending Product Successfull', fg = 'green')
        except pyodbc.Error as ex:
            INFO_ADD.config(text = f'Appending Products FAILED {ex}', fg = 'red')
            print(ex)


    add_window = Tk()
    add_window.geometry('1000x800')
    add_window.title('Add Product to table')

    MAIN_LABEL = Label(add_window, text=f'Add Product to INVENTORY', font=('Ink Free', 30, 'bold'), pady=50,bg='ivory2')
    MAIN_LABEL.pack(fill='x')


    LP_ID = Label(add_window, text = 'Product ID', font= ('Arial',15,'bold'))
    LP_ID.place(x = 25, y = 200, height = 70, width = 200)

    EP_ID = Entry(add_window, font = ('Arial',15,'bold'), relief= RAISED, bd= 5)
    EP_ID.place(x=200, y=210, height=50, width=300)



    LP_NAME = Label(add_window, text = 'Product Name', font = ('Arial',15,'bold'))
    LP_NAME.place(x = 25, y = 300, height = 70, width = 200)
    EP_NAME = Entry(add_window, font=('Arial', 15, 'bold'), relief=RAISED, bd=5)
    EP_NAME.place(x=200, y=310, height=50, width=300)



    L_Cost = Label(add_window, text = 'Cost', font= ('Arial',15,'bold'))
    L_Cost.place(x = 25, y = 400, height = 70, width = 200)
    E_Cost = Entry(add_window, font=('Arial', 15, 'bold'), relief=RAISED, bd=5)
    E_Cost.place(x=200, y=410, height=50, width=300)


    L_Quantity = Label(add_window, text='Quantity', font=('Arial', 15, 'bold'))
    L_Quantity.place(x=25, y=500, height=70, width=200)
    E_Quantity = Entry(add_window, font=('Arial', 15, 'bold'), relief=RAISED, bd=5)
    E_Quantity.place(x=200, y=510, height=50, width=300)


    ADD_BUTTON = Button(add_window, text = 'SUBMIT', font = ('Arial',15,'bold'), relief= RIDGE, bg= 'salmon')
    ADD_BUTTON.config(command=add_product, activebackground='green')
    ADD_BUTTON.place(x = 175, y = 600, height = 50, width = 200)

    status = Label(add_window, text='Status', font=('Arial', 15, 'bold'))
    status.place(x=100, y=650, height=50, width=300)

    INFO_ADD = Label(add_window, text = '', font = ('Arial',15,'bold'))
    INFO_ADD.place(x = 100, y = 700, height = 50, width = 300)

    B_UPDATE = Button(add_window,text = 'Check Update INVENTORY', font=('Arial', 17, 'bold'), relief=RAISED, bd=5)
    B_UPDATE.config(command=check_products)
    B_UPDATE.place(x = 550, y = 160, height = 50, width = 400)

    UPDATE_TEXT = Text(font =('Arial',11,'bold'),bg = 'blanched almond')
    UPDATE_TEXT.place(x = 550, y= 200, height = 500, width = 400)

def MAIN_MENU(databasename):
    sub_win = Tk()
    sub_win.geometry('1000x800')
    sub_win.title('Welcom to YAMITEA SHOP')

    MAIN_LABEL = Label(sub_win,text = f'Welcome to {databasename} SHOP', font = ('Ink Free',30, 'bold'), pady=50, bg = 'khaki1')
    MAIN_LABEL.pack(fill = 'x')

    MENU = Label(sub_win, text = 'MAIN MENU', font = ('Arial',15,'bold'), pady= 50, bg = 'salmon')
    MENU.place(x = 375, y = 200, height = 70, width = 200)


    Check_Shop = Button(sub_win, text = 'CHECK SHOP', font = ('Arial',20,'bold'),pady = 50, bg = 'sienna1')
    Check_Shop.config(command = lambda : CShop(databasename))
    Check_Shop.place(x = 325, y = 300, height = 70, width = 300)

    BUY_PRODUCTS = Button(sub_win, text = 'BUY PRODUCTS', font = ('Arial',20,'bold'),pady = 50, bg = 'tan1')
    BUY_PRODUCTS.config(command=lambda: Buy_Products(databasename))
    BUY_PRODUCTS.place(x=325, y=400, height=70, width=300)



    ADD_PRODUCTS = Button(sub_win, text='ADD PRODUCTS', font=('Arial', 20, 'bold'), pady=50, bg='tan2')
    ADD_PRODUCTS.config(command=lambda: Add_Products(databasename))
    ADD_PRODUCTS.place(x=325, y=500, height=70, width=300)


    window.destroy()






def CONNECT_DB():
    try:
        Name = ENTRY.get()
        connect = pyodbc.connect(
            'DRIVER={SQL SERVER};'
            'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
            f'DATABASE={Name};'
            'Trusted_Connection=yes;'
        )

        INFO.config(text = f'Connected to {Name}')
        MAIN_MENU(Name)
    except pyodbc.Error as ex:
        INFO.config(text = 'FAILED TO CONNECT')





window = Tk()
window.geometry('1000x800')
window.title("YAMITEA SHOP")
icon = PhotoImage(file = 'cat.png')
window.iconphoto(True,icon)

MAIN = Label(window,text = 'Connect to the shop database', font = ('Arial',20, 'bold'), bg = 'salmon', pady= 50)
MAIN.pack(fill = 'x')

frames= Frame(window)
frames.pack(pady = 20)

ENT_LABEL = Label(frames, text = 'Enter the DATABASE NAME: ',font = ('Arial',20,'bold'))
ENT_LABEL.grid(row = 1, column= 0)


ENTRY = Entry(frames,font = ('Arial',20,'bold'))
ENTRY.grid(row = 1, column = 1)


Connect_Button = Button(frames, text = 'Connect to Database', font = ('Arial',20,'bold'), relief= RAISED, bd = 5, bg = 'salmon', command=CONNECT_DB)
Connect_Button.grid(row = 2, column  = 0)

INFO = Label(frames, text = 'Connection Status', font = ('Arial',20,'bold'))
INFO.grid(row = 2 , column = 1)



window.mainloop()