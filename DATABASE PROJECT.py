from ctypes.wintypes import HBRUSH

from future.backports.email.headerregistry import Address
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyodbc


#=============================================================================main seller window========================================================
def seller_window(ID,Address,Phone,Name,email,seller_win):
    def Logout():
         seller_main.destroy()

    def ship_orders():
        orders = Tk()
        orders.geometry('1400x700')
        orders.title(f'Ship orders to your customers')
        orders.resizable(False,False)

        seller_main.withdraw()


    def manage_market():

        def submit_market(P_ID,P_NAME,P_TEXT,P_PRICE,P_STOCK):
            try:
                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                cursor = connect.cursor()
                query_stmt = "INSERT INTO MARKET (product_ID,product_NAME,seller_id,description,price, current_stock) VALUES (?,?,?,?,?,?)"
                cursor.execute(query_stmt, (int(P_ID), P_NAME, int(ID), P_TEXT, int(P_PRICE), int(P_STOCK)))

                query_stmt2 = "DELETE FROM Inventory WHERE product_ID = ? and product_NAME = ?"
                cursor.execute(query_stmt2, (int(P_ID), P_NAME))
                messagebox.showinfo(title="WARNING", message=f'INSERTED TO MARKET SUCCESSFULY PLS click the check button to referesh treeview')

                connect.commit()

                for record in TREEVIEW.get_children():
                    TREEVIEW.delete(record)

            except pyodbc.Error as ex:
                messagebox.showwarning(title="WARNING", message =f'{ex}')


        def check_data():
            P_ID = Product_ID.get()
            P_NAME = Product_Name.get()
            P_STOCK = Stock_EN.get()
            P_PRICE = PRICE_EN.get()
            P_TEXT = DTEXT.get("1.0",END).strip()

            if P_ID == "" or P_NAME == "" or P_STOCK == "" or P_PRICE == "" or P_TEXT == "":
                messagebox.showwarning(title="WARNIGN", message="PLS FILL THE NECESSARY FIELDS BEFORE SUBMIT TO THE MARKET")

            else:
                submit_market(P_ID,P_NAME,P_TEXT,P_PRICE,P_STOCK)



        def select_data():
            Product_ID.config(state=NORMAL)
            Product_Name.config(state=NORMAL)
            Stock_EN.config(state=NORMAL)

            selected = TREEVIEW.focus()
            values = TREEVIEW.item(selected,'values')

            Product_ID.delete(0,END)
            Product_Name.delete(0,END)
            Stock_EN.delete(0,END)
            PRICE_EN.delete(0,END)
            DTEXT.delete('1.0',END)

            Product_ID.insert(0, values[0])
            Product_Name.insert(0, values[1])
            Stock_EN.insert(0, values[2])

            Product_ID.config(state=DISABLED)
            Product_Name.config(state=DISABLED)
            Stock_EN.config(state=DISABLED)



        def update_stock ():
            try:

                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                cursor = connect.cursor()
                query_stmt = "SELECT * FROM Inventory"

                cursor.execute(query_stmt)
                products = cursor.fetchall()

                counter = 0
                for product in products:
                    counter += 1
                    TREEVIEW.insert('', 'end', text=f'{counter}', values=(f'{product[1]}', f'{product[2]}', f'{product[3]}'))


            except pyodbc.Error as ex:
                messagebox.showwarning(title = "WARNING", message=f"Failed to load Products {ex}")


        def BACK():
            market.destroy()
            seller_main.deiconify()

        market = Tk()
        market.geometry('1400x700')
        market.title(f'Mange your market')
        market.resizable(False,False)
        market.config(bg='peach puff')

        Welcome = Label(market, text="Manage Market", font=('Helvetica', 30, 'bold'), padx=20,bg='peach puff')
        Welcome.place(x=0, y=20)
        description = Label(market,
                            text="Manage your items that are currently on the market",
                            font=('Helvetica', 15, 'bold'), padx=20, bg='peach puff')
        description.place(x=0, y=80)

        Back = Button(market, text="BACK", font=('Times New Roman', 20, 'bold'), bg='gray46', fg='ghost white',
                      pady=5, padx=5, relief=RAISED, bd=5)
        Back.config(command=BACK)
        Back.place(x=1200, y=15, width=150, height=60)

        cover_update = Label(market, bg='gray65')
        cover_update.place(x=0, y=130, width=600, height=590)


        #LABELS

        Product = Label(market, text="Product ID:", font=('Times New Roman', 20, 'bold'), fg='gray1',
                        bg='gray65')
        Product.place(x=20, y=140)

        Product_ID = Entry(market, font=('Times New Roman:', 20, 'bold'), relief=RAISED, bd=5)
        Product_ID.config(state=DISABLED)
        Product_ID.place(x=210, y=140, width=350, height=40)

        PName = Label(market, text="Product Name:", font=('Times New Roman', 20, 'bold'), fg='gray1',bg='gray65')
        PName.place(x=20, y=210)

        Product_Name = Entry(market, font=('Times New Roman', 20, 'bold'), relief=RAISED, bd=5)
        Product_Name.config(state=DISABLED)
        Product_Name.place(x=210, y=210, width=350, height=40)

        Stock = Label(market, text="Current Stock:", font=('Times New Roman', 20, 'bold'), fg='gray1',bg='gray65')
        Stock.place(x=20, y=280)

        Stock_EN = Entry(market, font=('Times New Roman', 20, 'bold'), relief=RAISED, bd=5)
        Stock_EN.config(state=DISABLED)
        Stock_EN.place(x=210, y=280, width=350, height=40)

        PRICE = Label(market, text="PRICE:", font=('Times New Roman', 20, 'bold'), fg='gray1',bg='gray65')
        PRICE.place(x=20, y=350)

        PRICE_EN = Entry(market, font=('Times New Roman', 20, 'bold'), relief=RAISED, bd=5)
        PRICE_EN.place(x=210, y=350, width=350, height=40)

        DESCP = Label(market, text="Description:", font=('Times New Roman', 20, 'bold'), fg='gray1', bg='gray65')
        DESCP.place(x=20, y=400)

        DTEXT = Text(market,font = ('Arial',11), relief= RAISED, bd = 5)
        DTEXT.place(x = 20, y = 440, width = 550, height = 200)

        BUT1 = Button(market, text = "Search", font = ('Helvetica',15,"bold"), relief= RAISED, bd = 5)
        BUT1.config(bg = 'SkyBlue1', activebackground= 'cyan')
        BUT1.config(command=select_data)
        BUT1.place(x = 40, y = 650, width = 200, height = 40)

        BUT2 = Button(market, text="Submit", font=('Helvetica', 15, "bold"), relief=RAISED, bd=5)
        BUT2.config(bg = 'green', activebackground='lawn green')
        BUT2.config(command = check_data)
        BUT2.place(x=350, y=650, width=200, height=40)



        cover2 = Label(market, bg="gray1")
        cover2.place(x=600, y = 130, width=800, height=590)

        TREEVIEW = ttk.Treeview(market)
        TREEVIEW.place(x = 625, y = 150, width = 750, height = 480)

        TREEVIEW['columns'] = ('Product_ID', 'Product_Name', 'Stock')
        TREEVIEW.column("#0", width=40, minwidth=50)
        TREEVIEW.column("Product_ID", anchor=W, width=120, minwidth=120)
        TREEVIEW.column("Product_Name", anchor=W, width=120, minwidth=120)
        TREEVIEW.column("Stock", anchor=W, width=120, minwidth=120)

        TREEVIEW.heading("#0", text="box")
        TREEVIEW.heading("Product_ID", text='Product_ID')
        TREEVIEW.heading("Product_Name", text='Product_Name')
        TREEVIEW.heading("Stock", text="Stocks")

        BUT3 = Button(market, text="CHECK", font=('Helvetica', 15, "bold"), relief=RAISED, bd=5)
        BUT3.config(bg='green', activebackground='lawn green')
        BUT3.config(command = update_stock)
        BUT3.place(x=900, y=650, width=200, height=40)


        seller_main.withdraw()

    def manage_profits():
        profits = Tk()
        profits.geometry('1200x600')
        profits.title(f'Seller {Name} Profits')
        profits.resizable(False,False)

        seller_main.withdraw()



    def check_inv():
        def view():
            try:
                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                cursor = connect.cursor()
                query_stmt = "SELECT * FROM Inventory"
                cursor.execute(query_stmt)
                products = cursor.fetchall()

                TEXT_PRODUCT.delete('1.0', 'end')

                for product in products:
                    TEXT_PRODUCT.insert('end',f'Seller ID: {product[0]}, Product ID: {product[1]}, Product Name: {product[2]}, Stock: {product[3]}\n')


            except pyodbc.Error as ex:
                status.config(text="FAILE TO COLLECT Products", fg='red')
                print(ex)



        def update(merch_ID, merch_name, current_stock):
            try:
                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                cursor = connect.cursor()
                query_stmt = "UPDATE Inventory SET current_stock = ? WHERE product_ID = ? and product_NAME = ?"

                cursor.execute(query_stmt, (int(current_stock), int(merch_ID), merch_name))
                connect.commit()

                if cursor.rowcount > 0:
                    status.config(text="Product Updated Successfully", fg = 'green')
                    Product_ID.delete(0, END)
                    Product_Name.delete(0, END)
                    Stock_EN.delete(0, END)
                else:
                    status.config(text="FAILED TO UPDATE PRODUCTS", fg='red')

            except pyodbc.Error as ex:
                status.config(text="FAILED TO UPDATE PRODUCTS", fg='red')
                print(ex)

        def check_update():
            merch_ID = Product_ID.get()
            merch_name = Product_Name.get()
            current_stock = Stock_EN.get()

            if merch_ID == "" or merch_name == "" or current_stock == "":
                status.config(text="PLS FILL ALL FIELDS!!!")

            else:
                update(merch_ID, merch_name, current_stock)

        def search(merch_ID, merch_name):

            if merch_ID == '':
                merch_ID = 0

            try:
                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                connect.autocommit = True
                cursor = connect.cursor()

                quert_stmt = "SELECT * FROM Inventory WHERE product_ID = ? or product_NAME = ?"
                cursor.execute(quert_stmt, (merch_ID, merch_name))
                product = cursor.fetchone()

                if product:
                    status.config(text="Load Success", fg='green')
                    PID = product[1]
                    Pname = product[2]
                    quantity = product[3]

                    Product_ID.delete(0,END)
                    Product_Name.delete(0,END)
                    Stock_EN.delete(0,END)

                    Product_ID.insert(0, f'{PID}')
                    Product_Name.insert(0, f'{Pname}')
                    Stock_EN.insert(0,f'{quantity}')

                else:
                    status.config(text="Failed to load product", fg='red')


            except pyodbc.Error as ex:
                status.config(text="Failed to load product", fg = 'red')
                print(ex)


        def check_search():
            merch_ID = Product_ID.get()
            merch_name = Product_Name.get()


            if merch_ID == "" and merch_name == "":
                status.config(text="PLS FILL ALL FIELDS!!!")

            else:
                search(merch_ID, merch_name)


        def ADD(merch_ID,merch_name,current_stock):
            try:
                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                connect.autocommit = True
                cursor = connect.cursor()
                # INSERT INTO ITEM (Item_ID,Item_name,Item_value,Item_quatity) VALUES (?,?,?,?)
                quert_stmt = "INSERT INTO Inventory (seller_ID,product_ID,product_NAME,current_stock) VALUES (?,?,?,?)"
                cursor.execute(quert_stmt,(ID,int(merch_ID),merch_name,int(current_stock)))
                connect.commit()

                if cursor.rowcount > 0:
                    status.config(text="Product Added Successfully", fg='green')
                    Product_ID.delete(0, END)
                    Product_Name.delete(0, END)
                    Stock_EN.delete(0, END)
                else:
                    status.config(text="Failed to Add product")

            except pyodbc.Error as ex:
                status.config(text = "Failed to Add product")
                print(ex)


        def ADD_check():
            merch_ID = Product_ID.get()
            merch_name = Product_Name.get()
            current_stock = Stock_EN.get()

            if merch_ID == "" or merch_name == "" or current_stock == "":
                status.config(text = "PLS FILL ALL FIELDS!!!")

            else:
                ADD(merch_ID,merch_name,current_stock)


        def BACK():
            inventory.destroy()
            seller_main.deiconify()

        inventory = Tk()
        inventory.geometry('1400x700')
        inventory.title(f'Seller {Name} inventory')
        inventory.resizable(False,False)
        inventory.config(bg = 'peach puff')


        Welcome = Label(inventory,text = "Welcome to the Inventory",font=('Helvetica', 30, 'bold'), padx= 20,bg= 'peach puff')
        Welcome.place(x = 0 , y = 20)
        description = Label(inventory,text="This is where your items are listed. You can add stocks or remove your products",font=('Helvetica', 15, 'bold'), padx=20,bg= 'peach puff')
        description.place(x = 0, y = 80)

        Back = Button(inventory, text="BACK", font=('Times New Roman', 20, 'bold'), bg='gray46', fg='ghost white', pady=5,padx=5, relief=RAISED, bd=5)
        Back.config(command=BACK)
        Back.place(x=1200, y=15, width=150, height=60)

        cover_update = Label(inventory,bg = '#2b2d40')
        cover_update.place(x = 0, y = 130,width = 550, height = 590)

        status = Label(inventory, text = "",font=('Times New Roman', 25, 'bold'), fg='ghost white', bg = '#2b2d40')
        status.place(x = 100,y = 140)

        desc1 = Label(inventory, text="Add or Update Products", font=('Times New Roman', 30, 'bold'), fg='ghost white', bg='#2b2d40')
        desc1.place(x=70, y=190)

        Product =  Label(inventory, text = "Product ID",font=('Times New Roman', 25, 'bold'), fg='ghost white', bg = '#2b2d40')
        Product.place(x = 180, y = 270)

        Product_ID = Entry(inventory,font=('Times New Roman', 25, 'bold'),relief=RAISED, bd = 5)
        Product_ID.place(x = 70,  y = 320, width = 400, height = 40)

        PName = Label(inventory, text="Product Name", font=('Times New Roman', 25, 'bold'), fg='ghost white', bg='#2b2d40')
        PName.place(x=160, y=370)

        Product_Name = Entry(inventory, font=('Times New Roman', 25, 'bold'), relief=RAISED, bd=5)
        Product_Name.place(x=70, y=420, width=400, height=40)

        Stock = Label(inventory, text="Current Stock", font=('Times New Roman', 25, 'bold'), fg='ghost white', bg='#2b2d40')
        Stock.place(x=160, y=470)

        Stock_EN = Entry(inventory, font=('Times New Roman', 25, 'bold'), relief=RAISED, bd=5)
        Stock_EN.place(x=70, y=520, width=400, height=40)


        #3 BUTTONS

        BUT1 = Button(inventory,text="ADD",font=('Times New Roman', 20, 'bold'),bg= "green", relief=RAISED, bd = 5)
        BUT1.config(command=ADD_check)
        BUT1.place(x = 20, y = 600, width = 150)

        BUT2 = Button(inventory, text="Search", font=('Times New Roman', 20, 'bold'), bg="#424ec2", relief=RAISED, bd=5)
        BUT2.config(command= check_search)
        BUT2.place(x=200, y=600, width=150)

        BUT3 = Button(inventory, text="Update", font=('Times New Roman', 20, 'bold'), bg="#424ec2", relief=RAISED, bd=5)
        BUT3.config(command= check_update)
        BUT3.place(x=380, y=600, width=150)


        cover2 = Label(inventory, bg = "#353354")
        cover2.place(x = 550, y= 130,width = 850, height = 590)

        cover3 = Label(inventory, bg = '#0a0a0a')
        cover3.place(x = 550, y= 130,width = 850, height = 100)

        desc4 = Label(inventory, text="CURRENT INVENTORY", font=('Times New Roman', 25, 'bold'), fg='ghost white',bg='#0a0a0a')
        desc4.place(x=780, y=160)

        TEXT_PRODUCT = Text(inventory,relief= RAISED , bd = 5,padx= 10, pady=10, font= ('Arial', 15))
        TEXT_PRODUCT.place(x = 575, y = 250, width = 800 , height = 380)

        UPDATE_BUT = Button(inventory, text="VIEW INVENTORY", font=('Times New Roman', 20, 'bold'), bg="#424ec2", relief=RAISED, bd=5)
        UPDATE_BUT.config(command = view)
        UPDATE_BUT.place(x=850, y=640, width=300, height = 50)

        seller_main.withdraw()




    def manage_account():

        def BACK():
            manage.destroy()
            seller_main.deiconify()


        manage = Tk()
        manage.geometry('800x500')

        ACC = Label(manage, text="My Profile", pady= 5,bg= 'gray46',font=('Helvetica', 30, 'bold'))
        ACC.pack(fill = "x")

        ACC = Label(manage, text="Manage and protect your account", pady=5, bg='gray46',font=('Helvetica', 11, 'bold'))
        ACC.pack(fill="x")

        LogoLabel = Label(manage, text="LULU SHOP", font=('Times New Roman', 20, 'bold'), bg='gray1',fg='ghost white', pady=5, padx=5)
        LogoLabel.place(x=7, y=6)

        Back = Button(manage, text="BACK", font=('Times New Roman', 20, 'bold'), bg='gray46',fg='ghost white', pady=5, padx=5, relief=RAISED, bd =5)
        Back.config(command = BACK)
        Back.place(x=630, y=6, width = 150, height = 60)

        USER_ID = Label(manage,text= f"Seller ID: {ID}",font=('Helvetica', 20, 'bold'))
        USER_ID.place(x = 100, y = 100)

        USER_NAME = Label(manage, text= f'Sellers Name: {Name}',font=('Helvetica', 20, 'bold'))
        USER_NAME.place(x = 100 , y = 180)

        USER_ADD = Label(manage, text = f'Seller Addres: {Address}',font=('Helvetica', 20, 'bold'))
        USER_ADD.place(x=100, y=260)

        USER_Phone = Label(manage, text=f'Seller Phone number: {Phone}',font=('Helvetica', 20, 'bold'))
        USER_Phone.place(x=100, y=340)

        USER_EM = Label(manage, text=f'Seller Email Address: {email}',font=('Helvetica', 20, 'bold'))
        USER_EM.place(x=100, y=420)




        seller_main.withdraw()

    seller_main = Tk()
    seller_main.resizable(False,False)
    seller_main.geometry('1400x700')
    seller_main.title(f'Welcome Seller {Name}')
    seller_main.config(bg = 'gray46')


    # =============================== GUI DESIGN ===================================================
    taskbar = Label(seller_main,bg = 'Slate gray')
    taskbar.place(x = 0, width = 1400, height = 80)

    welcome = Label(seller_main,bg='PeachPuff2')
    welcome.place(x = 0, y = 80, width = 600, height = 620)

    welcome1 = Label(seller_main, text = "Welcome Back", font=('Times New Roman',40, 'bold'), bg= "PeachPuff2")
    welcome1.place(x = 120, y = 200)

    logout_btn = Button(seller_main, text="Log-out", bg="#f44336", fg="white", font=("Helvetica", 17, "bold"))
    logout_btn.config(command=Logout)
    logout_btn.place(x=1250, y=15)

    welcome2 = Label(seller_main, text="Seller", font=('Times New Roman', 30), bg="PeachPuff2")
    welcome2.place(x=230, y=280)

    welcome3 = Label(seller_main, text=f"{Name}", font=('Times New Roman', 30), bg="PeachPuff2")
    welcome3.place(x=100, y=360)


    LogoLabel = Label(seller_main,text="LULU SHOP", font=('Times New Roman', 30,'bold'), bg = 'gray1',fg= 'ghost white', pady=5, padx= 5)
    LogoLabel.place(x = 7 , y = 6 )

    MAINLABEL = Label(seller_main, text="MAIN MENU", font=('Times New Roman', 40, 'bold'), bg='gray46',pady=5, padx=5)
    MAINLABEL.place(x=850, y=90)

    #======================================================================
    #=========================== 3 BUTTONS ================================
    #======================================================================

    BUT1 = Button(seller_main,text= 'MY ACCOUNT', font = ('Times New Roman',30,'bold'),bg = 'Slate gray', fg = 'ghost white', relief=RAISED, bd = 5)
    BUT1.config(activebackground="SlateBlue3")
    BUT1.config(command=manage_account)
    BUT1.place(x = 800 , y = 190, height = 70, width = 420)

    BUT2 = Button(seller_main, text='CHECK INVENTORY', font=('Times New Roman', 30, 'bold'), bg='Slate gray',fg='ghost white', relief=RAISED, bd=5)
    BUT2.config(activebackground="SlateBlue3")
    BUT2.config(command=check_inv)
    BUT2.place(x=800, y=290, height=70, width=420)

    BUT3 = Button(seller_main, text='MANAGE PROFITS', font=('Times New Roman', 30, 'bold'), bg='Slate gray',fg='ghost white', relief=RAISED, bd=5)
    BUT3.config(activebackground="SlateBlue3")
    BUT3.config(command = manage_profits)
    BUT3.place(x=800, y=390, height=70, width=420)

    BUT4 = Button(seller_main, text='MANAGE MARKET', font=('Times New Roman', 30, 'bold'), bg='Slate gray',fg='ghost white', relief=RAISED, bd=5)
    BUT4.config(activebackground="SlateBlue3")
    BUT4.config(command = manage_market)
    BUT4.place(x=800, y=490, height=70, width=420)

    BUT5 = Button(seller_main, text='SHIP ORDERS', font=('Times New Roman', 30, 'bold'), bg='Slate gray',fg='ghost white', relief=RAISED, bd=5)
    BUT5.config(activebackground="SlateBlue3")
    BUT5.config(command = ship_orders)
    BUT5.place(x=800, y=590, height=70, width=420)

    seller_win.destroy()
#=============================================================================SELLER LOGIN========================================================
def login_sel():
    def create_sel():

        def creation(Name,Email,Phone,Password,Address):
            try:
                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                connect.autocommit = True
                cursor = connect.cursor()

                cursor.execute("SELECT MAX(seller_ID) FROM Sellers")

                last_id = cursor.fetchone()[0]

                if last_id:
                    new_id = last_id + 1
                else:
                    new_id = 1001

                query_stmt = "INSERT INTO Sellers (seller_ID,seller_Address,phone_number,password,seller_name,seller_email) VALUES(?,?,?,?,?,?)"
                cursor.execute(query_stmt, new_id, Address, Phone, Password, Name, Email)
                NOTIF.config(text="Creation of Account is successful", fg = 'green')

            except pyodbc.Error as ex:
                print(f'Failed to create account {ex}')

        def check_create():
            Name = En_Name.get()
            Email = En_Email.get()
            Phone = En_Phone.get()
            Password = En_Password.get()
            Address = En_Address.get()

            if  Name == '' or Email == '' or Phone == '' or Password == '' or Address == '':
                NOTIF.config(text = 'all fields must be filled !!!!', fg = 'red')
                return
            else:
                creation(Name,Email,Phone,Password,Address)

        create_window = Tk()
        create_window.geometry('900x600')
        create_window.resizable(False,False)
        create_window.title('Create an Account')

        main_Label1 = Label(create_window, text='Welcome new seller!', font=('Helvetica', 30, 'bold'), pady= 10,bg='misty rose')
        main_Label1.pack(fill="x")
        main_Label2 = Label(create_window, text='Fill up the needed details', font=('Helvetica', 15, 'bold'), bg='misty rose')
        main_Label2.pack(fill="x")
        main_Label3 = Label(create_window, text='below and join us today!! \N{grinning face}', font=('Helvetica', 15, 'bold'), bg='misty rose')
        main_Label3.pack(fill="x")

        NOTIF = Label(create_window, text='',font=('Helvetica', 15, 'bold'))
        NOTIF.pack(fill="x")

        FName = Label(create_window, text = 'Full Name (Lastname, Firstname):',font=('Helvetica', 17, 'bold'))
        FName.place(x = 40,y = 170)

        En_Name = Entry(create_window, font=('Helvetica', 15, 'bold'), relief= RIDGE, bd=5)
        En_Name.place(x = 40, y = 210, height = 40, width = 360)

        Phone = Label(create_window, text='Phone number:', font=('Helvetica', 17, 'bold'))
        Phone.place(x=500, y=170)

        En_Phone = Entry(create_window, font=('Helvetica', 15, 'bold'), relief=RIDGE, bd=5)
        En_Phone.place(x=500, y=210, height=40, width=360)

        Email = Label(create_window, text='Email address:', font=('Helvetica', 17, 'bold'))
        Email.place(x=40, y=270)

        En_Email = Entry(create_window, font=('Helvetica', 15, 'bold'), relief=RIDGE, bd=5)
        En_Email.place(x=40, y=310, height=40, width=360)

        Password = Label(create_window, text='Create Password:', font=('Helvetica', 17, 'bold'))
        Password.place(x=500, y=270)

        En_Password = Entry(create_window, font=('Helvetica', 15, 'bold'), relief=RIDGE, bd=5)
        En_Password.place(x=500, y=310, height=40, width=360)

        Address = Label(create_window, text='Full address', font=('Helvetica', 17, 'bold'))
        Address.place(x=375, y=380)

        En_Address = Entry(create_window, font=('Helvetica', 15, 'bold'), relief=RIDGE, bd=5)
        En_Address.place(x=40, y=420, height=40, width=800)



        main_Label4 = Label(create_window, text='Your details will be reviewed before your account is created,',font=('Helvetica', 12, 'bold'), bg='khaki2')
        main_Label4.place(x= 0, y = 550,width = 900)

        main_Label5 = Label(create_window,text='you will receive emails whether your account is approve or not',font=('Helvetica', 12, 'bold'), bg='khaki2')
        main_Label5.place(x=0, y=570, width = 900)

        Sign_But = Button(create_window, text = 'Sign up',  font=('Helvetica', 22,'bold'), relief= RAISED, bd = 4, activebackground= 'green')
        Sign_But.place(x = 380 , y = 470)
        Sign_But.config(command= check_create)

    def login(Email,Pass):
        try:
            connect = pyodbc.connect(
                'DRIVER={SQL SERVER};'
                'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
                'DATABASE=SHOPEE_FINAL;'
                'Trusted_Connection=yes;'
            )

            connect.autocommit = True
            cursor = connect.cursor()

            cursor.execute(f"SELECT * FROM Sellers Where seller_email =? and password =?",(Email,Pass))

            seller = cursor.fetchone()


            if seller:
                ID = seller[0]
                Address = seller[1]
                Phone = seller[2]
                Name = seller[4]
                email = seller[5]
                seller_window(ID,Address,Phone,Name,email,seller_win)

            else:
                INDICATOR.config(text="Login Failed Incorrect INPUTS", fg='red')


        except pyodbc.Error as ex:
            INDICATOR.config(text="Failed to Login Account", fg='red')
            print(f'{ex}')

    def check_login():
        Email = USER_ENTRY.get()
        Pass = PASS_ENTRY.get()

        if Pass == '' or Email == '':
            INDICATOR.config(text = 'all fields must be filled !!!!', fg = 'red')

        else:
            login(Email,Pass)

    seller_win = Tk()
    seller_win.geometry('800x500')
    seller_win.title('Login as Seller')
    seller_win.resizable(False,False)

    main_Label = Label(seller_win, text='LOGIN AS SELLER', font=('Helvetica', 20, 'bold'), pady=20, bg='misty rose')
    main_Label.pack(fill="x")

    USER = Label(seller_win, text= 'Login using email', font = ('Helvetica', 20 ,'bold'))
    USER.place(x = 50 , y = 100)

    USER_ENTRY = Entry(seller_win, font = ('Helvetica', 20 ,'bold'), relief= RAISED, bd = 4)
    USER_ENTRY.place(x = 50, y = 150, height = 60, width = 400)

    PASS = Label(seller_win, text='Enter Password', font=('Helvetica', 20, 'bold'))
    PASS.place(x=50, y=225)

    PASS_ENTRY = Entry(seller_win, font=('Helvetica', 20, 'bold'), relief=RAISED, bd=4, show = '*')
    PASS_ENTRY.place(x=50, y=275, height=60, width=400)

    LOG_BUT = Button(seller_win, text= 'LOGIN', font=('Helvetica', 20, 'bold'), relief= RAISED, bd = 5)
    LOG_BUT.config(activebackground= 'green')
    LOG_BUT.config(command= check_login)
    LOG_BUT.place(x = 525, y= 200, height = 70 , width = 200)

    INDICATOR = Label(seller_win, text = 'Status', font=('Helvetica',20, 'bold'))
    INDICATOR.place(x = 230, y = 350)


    CRAETE_Label = Label(seller_win, text = 'Not a member yet?',font=('Helvetica',20, 'bold'))
    CRAETE_Label.place(x = 150, y = 425)

    CREATE_But = Button(seller_win, text = 'Create ACCOUNT',font=('Helvetica',20, 'bold'),relief= RAISED, bd = 5, bg = 'sky blue')
    CREATE_But.config(command = create_sel)
    CREATE_But.place(x = 425, y = 415)


    main_window.destroy()

#=============================================================================MAIN BUYER WINDOW========================================================
def buyer_window(ID, Address, Phone, Name, email, buyer_win):
    def CHECK_OUT():
        def BACK():
            COUT.destroy()
            buyer_main.deiconify()

        COUT = Tk()
        COUT.geometry("1400x700")
        COUT.title("CHECK OUT PRODUCTS TO RECEIVE")
        COUT.resizable(False, False)

        Back = Button(COUT, text="BACK", font=('Times New Roman', 20, 'bold'), bg='gray46', fg='ghost white', pady=5, padx=5, relief=RAISED, bd=5)
        Back.config(command=BACK)
        Back.place(x=1200, y=15, width=150, height=60)

        buyer_main.withdraw()


    def CHECK_CART():

        def DISPLAY_CART():
            try:

                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                cursor = connect.cursor()
                query_stmt = "SELECT * FROM Cart"

                cursor.execute(query_stmt)
                products = cursor.fetchall()

                counter = 0

                for item in TREEVIEW.get_children():
                    TREEVIEW.delete(item)

                for product in products:
                    get_name_seller = "SELECT product_NAME FROM MARKET WHERE product_ID = ?"
                    product_result = cursor.execute(get_name_seller, (product[0])).fetchone()
                    product_name = product_result[0] if product_result else "UNKNOWN"

                    counter += 1
                    TREEVIEW.insert('', 'end', text=f'{counter}', values=(
                    f'{product[0]}', f'{product_name}', f'{product[1]}', f'{product[2]}', f'{product[3]}',
                    f'{product[4]}'))


            except pyodbc.Error as ex:
                messagebox.showwarning(title="WARNING", message=f"Failed to load Products {ex}")

        def BACK():
            CCART.destroy()
            buyer_main.deiconify()

        CCART = Tk()
        CCART.geometry("1400x700")
        CCART.title("MANAGE YOU CART SELECT PRODUCTS YOU WANT TO CHECK OUT")
        CCART.resizable(False, False)
        CCART.config(bg = "peach puff")

        Back = Button(CCART, text="BACK", font=('Times New Roman', 20, 'bold'), bg='gray46', fg='ghost white', pady=5,padx=5, relief=RAISED, bd=5)
        Back.config(command=BACK)
        Back.place(x=1200, y=15, width=150, height=60)

        cover1 = Label(CCART, bg='gray1', pady=10, relief=RIDGE, bd=5)
        cover1.place(x=0, y=130, width=950, height=570)
        cover2 = Label(CCART    , bg="gray46", relief=RIDGE, bd=5)
        cover2.place(x=950, y=130, width=450, height=570)

        LogoLabel = Label(CCART, text="LULU SHOP", font=('Times New Roman', 30, 'bold'), bg='gray1', fg='ghost white',
                          pady=5, padx=5)
        LogoLabel.place(x=7, y=6)

        WELCOME3 = Label(CCART, text="SHOPPING CART", font=('Helvetica', 30, 'bold'), bg='peach puff',
                         fg='gray1', pady=5, padx=5)
        WELCOME3.place(x=530, y=10)

        WELCOME4 = Label(CCART, text="This is where you will be managing\nthe items in your cart", font=('Helvetica', 17, 'bold'),bg='peach puff', fg='gray1', pady=5, padx=5)
        WELCOME4.place(x=500, y=60)

        cover3 = Label(CCART, bg="#131e61")
        cover3.place(x=970, y=150, width=410, height=100)

        cover4 = Label(CCART, bg="#131e61")
        cover4.place(x=970, y=150, width=410, height=100)
        cover5 = Label(CCART, bg="#303a73")
        cover5.place(x=970, y=250, width=410, height=430)

        SELECT_LABEL = Label(CCART, text="Select Items in cart \nthat you want to checkout",font=('Helvetica', 20, 'bold'), fg='ghost white', bg="#131e61")
        SELECT_LABEL.place(x=1010, y=165)

        TREEVIEW = ttk.Treeview(CCART)
        TREEVIEW.place(x=25, y=165, width=900, height=450)

        TREEVIEW['columns'] = ('Product_ID', 'Product_Name', 'buyer_ID', 'cart_ID', 'quantity', 'total_cost')
        TREEVIEW.column("#0", width=40, minwidth=90)
        TREEVIEW.column("Product_ID", anchor=W, width=120, minwidth=130)
        TREEVIEW.column("Product_Name", anchor=W, width=120, minwidth=130)
        TREEVIEW.column("buyer_ID", anchor=W, width=120, minwidth=130)
        TREEVIEW.column("cart_ID", anchor=W, width=120, minwidth=130)
        TREEVIEW.column("quantity", anchor=W, width=220, minwidth=130)
        TREEVIEW.column("total_cost", anchor=W, width=120, minwidth=130)

        TREEVIEW.heading("#0", text="box")
        TREEVIEW.heading("Product_ID", text='Product_ID')
        TREEVIEW.heading("Product_Name", text='Product_Name')
        TREEVIEW.heading("buyer_ID", text="buyer_ID")
        TREEVIEW.heading("cart_ID", text='cart_ID')
        TREEVIEW.heading("quantity", text='quantity')
        TREEVIEW.heading("total_cost", text="total_cost")

        BUT3 = Button(CCART, text="CHECK MARKET", font=('Helvetica', 15, 'bold'), bg='#2c61d4', relief=RAISED, bd=5)
        BUT3.config(command=DISPLAY_CART)
        BUT3.place(x=375, y=630)

        # patuloy ng mga buttons kulang parin
        # pati design bai

        buyer_main.withdraw()

# ===========================================================================================================================
# ===============================================UNDER CONSTRUCTION==========================================================
# ===========================================================================================================================
    def SHOPPING():

        def ADD_CART():
            product_Name = E_NAME.get()
            Seller_Name = E_SNAME.get()
            QUANTITY = E_QUANTITY.get()
            COST = E_COST.get()

            if QUANTITY == "":
                messagebox.showwarning(title="WARNING",message="PLS FILL THE QUANTITY YOU WANT TO BUY BEFORE CALCULATE")

            try:

                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                cursor = connect.cursor()

                query_stmt = "SELECT seller_ID FROM Sellers WHERE seller_name = ?"
                seller_result = cursor.execute(query_stmt,(Seller_Name,)).fetchone()
                seller_id = seller_result[0]

                query_stmt1 = "SELECT product_ID FROM MARKET WHERE product_NAME = ? and seller_ID = ?"
                product_result = cursor.execute(query_stmt1,(product_Name,seller_id)).fetchone()
                product_ID = product_result[0]

                #cursor.execute("SELECT MAX(buyer_ID) FROM Buyers")
                cart_ID = cursor.execute("SELECT MAX(cart_ID) FROM Cart").fetchone()[0]

                if cart_ID:
                    new_cart_ID = cart_ID + 1
                else:
                    new_cart_ID = 30000
                # "INSERT INTO Buyers (buyer_ID,buyer_Address,phone_number,password,buyer_name,buyer_email) VALUES(?,?,?,?,?,?)"
                query_stmt3 = "INSERT INTO Cart (product_ID,buyer_ID,cart_ID,quantity,total_cost) VALUES (?,?,?,?,?)"
                cursor.execute(query_stmt3,(product_ID,ID,new_cart_ID,QUANTITY,COST))
                connect.commit()

                messagebox.showinfo(title="NOTIFICATION", message="SUCCESSFULY ADDED TO CART PLS CHECK YOUR CART TO VERIFY")

            except pyodbc.Error as ex:
                messagebox.showwarning(title="WARNING", message=f"FAILED TO MOVE PRODUCTS TO CART {ex}")




        def DISPLAY_MARKET():
            try:

                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                cursor = connect.cursor()
                query_stmt = "SELECT * FROM MARKET"

                cursor.execute(query_stmt)
                products = cursor.fetchall()


                counter = 0

                for item in TREEVIEW.get_children():
                    TREEVIEW.delete(item)

                for product in products:
                    get_name_seller = "SELECT seller_name FROM Sellers WHERE seller_ID = ?"
                    seller_result = cursor.execute(get_name_seller,(product[2])).fetchone()
                    seller_name = seller_result[0] if seller_result else "UNKNOWN"

                    counter += 1
                    TREEVIEW.insert('', 'end', text=f'{counter}',values=(f'{product[0]}', f'{product[1]}', f'{seller_name}',f'{product[4]}',f'{product[3]}',f'{product[5]}'))


            except pyodbc.Error as ex:
                messagebox.showwarning(title="WARNING", message=f"Failed to load Products {ex}")

        def SELECT():
            E_NAME.config(state=NORMAL)
            E_SNAME.config(state=NORMAL)
            E_COST.config(state=NORMAL)


            selected = TREEVIEW.focus()
            values = TREEVIEW.item(selected, 'values')

            E_NAME.delete(0, END)
            E_SNAME.delete(0, END)
            E_COST.delete(0,END)
            E_QUANTITY.delete(0, END)


            E_NAME.insert(0, values[1])
            E_SNAME.insert(0, values[2])
            E_COST.insert(0,values[3])




            E_NAME.config(state=DISABLED)
            E_SNAME.config(state=DISABLED)
            E_COST.config(state=DISABLED)


        def BACK():
            MARKET.destroy()
            buyer_main.deiconify()

        def CALCULATE():
            QUANTITY = E_QUANTITY.get()
            COST = E_COST.get()
            if QUANTITY == "":
                messagebox.showwarning(title="WARNING",message="PLS FILL THE QUANTITY YOU WANT TO BUY BEFORE CALCULATE")
            else:
                TOTAL_COST = int(QUANTITY) * int(COST)
                E_COST.config(state=NORMAL)

                E_COST.delete(0,END)

                E_COST.insert(0,TOTAL_COST)

                E_COST.config(state=DISABLED)

        MARKET = Tk()
        MARKET.geometry("1400x700")
        MARKET.title("WELCOME    TO MAIN MARKET")
        MARKET.resizable(False,False)
        MARKET.config(bg = "peach puff")

        Back = Button(MARKET, text="BACK", font=('Times New Roman', 20, 'bold'), bg='gray46', fg='ghost white', pady=5,padx=5, relief=RAISED, bd=5)
        Back.config(command=BACK)
        Back.place(x=1200, y=25, width=150, height=60)

        cover1 = Label(MARKET,bg ='gray1', pady=10, relief=RIDGE, bd = 5)
        cover1.place(x=0, y=130, width=950, height=570)
        cover2 = Label(MARKET, bg = "gray46",relief=RIDGE, bd = 5)
        cover2.place(x = 950, y = 130,width = 450, height = 570)

        LogoLabel = Label(MARKET, text="LULU SHOP", font=('Times New Roman', 30, 'bold'), bg='gray1',fg='ghost white', pady=5, padx=5)
        LogoLabel.place(x=7, y=6)

        WELCOME3 = Label(MARKET, text="Welcome to the market", font=('Helvetica', 30, 'bold'), bg='peach puff', fg='gray1', pady=5, padx=5)
        WELCOME3.place(x=300, y=20)

        WELCOME4 = Label(MARKET, text="Browse for items you want yo buy", font=('Helvetica', 17, 'bold'), bg='peach puff',fg='gray1', pady=5, padx=5)
        WELCOME4.place(x=300, y=70)

        cover3 = Label(MARKET,bg = "#131e61")
        cover3.place(x = 970, y = 150, width = 410, height = 100)

        cover4 = Label(MARKET, bg="#131e61")
        cover4.place(x=970, y=150, width=410, height=100)
        cover5 = Label(MARKET, bg="#303a73")
        cover5.place(x=970, y=250, width=410, height=430)


        SELECT_LABEL = Label(MARKET, text = "Select Items in market \nto add in your cart", font=('Helvetica', 20, 'bold'),fg='ghost white',bg="#131e61")
        SELECT_LABEL.place(x = 1020, y = 165)

        TREEVIEW = ttk.Treeview(MARKET)
        TREEVIEW.place(x=25, y=165, width=900, height=450)

        TREEVIEW['columns'] = ('Product_ID', 'Product_Name','Seller_Name','Price','Description','Current_Stock')
        TREEVIEW.column("#0", width=40, minwidth=50)
        TREEVIEW.column("Product_ID", anchor=W, width=120, minwidth=120)
        TREEVIEW.column("Product_Name", anchor=W, width=120, minwidth=120)
        TREEVIEW.column("Seller_Name", anchor=W, width=120, minwidth=120)
        TREEVIEW.column("Price", anchor=W, width=120, minwidth=120)
        TREEVIEW.column("Description", anchor=W, width=220, minwidth=220)
        TREEVIEW.column("Current_Stock", anchor=W, width=120, minwidth=120)


        TREEVIEW.heading("#0", text="box")
        TREEVIEW.heading("Product_ID", text='Product_ID')
        TREEVIEW.heading("Product_Name", text='Product_Name')
        TREEVIEW.heading("Seller_Name", text="Seller_Name")
        TREEVIEW.heading("Price", text='Price')
        TREEVIEW.heading("Description", text='Description')
        TREEVIEW.heading("Current_Stock", text="Current_Stock")

        P_NAME = Label(MARKET, text = "PRODUCT NAME", font=('Helvetica', 17, 'bold'), fg = 'ghost white',bg = "#303a73" )
        P_NAME.place(x = 1075, y = 265)

        E_NAME = Entry(MARKET, state= DISABLED,relief= RAISED, bd = 5, font=('Helvetica', 17, 'bold'))
        E_NAME.place(x = 1030, y= 305, width = 300, height = 40)

        S_NAME = Label(MARKET, text="SELLER NAME", font=('Helvetica', 17, 'bold'), fg='ghost white', bg="#303a73")
        S_NAME.place(x=1090, y=360)

        E_SNAME = Entry(MARKET, state=DISABLED, relief=RAISED, bd=5, font=('Helvetica', 17, 'bold'))
        E_SNAME.place(x=1030, y=405, width=300, height=40)

        QUANTITY = Label(MARKET, text="Enter Quantity", font=('Helvetica', 17, 'bold'), fg='ghost white', bg="#303a73")
        QUANTITY.place(x=1095, y=460)

        E_QUANTITY = Entry(MARKET, relief=RAISED, bd=5, font=('Helvetica', 17, 'bold'))
        E_QUANTITY.place(x=1030, y=505, width=300, height=40)

        COST= Label(MARKET, text="COST", font=('Helvetica', 17, 'bold'), fg='ghost white', bg="#303a73")
        COST.place(x=1000, y=575)

        E_COST = Entry(MARKET, relief=RAISED, bd=5, font=('Helvetica', 17, 'bold'), state= DISABLED)
        E_COST.place(x=1100, y=570, width=230, height=40)


        buyer_main.withdraw()

        #BUTTON 2


        BUT1 =  Button(MARKET, text = "ADD TO CART", font=('Helvetica', 11, 'bold'),bg= 'green', relief=RAISED, bd = 5)
        BUT1.config(command = ADD_CART)
        BUT1.place(x = 980, y= 630)

        BUT2 = Button(MARKET, text="SELECT ITEM", font=('Helvetica', 11, 'bold'), bg='#2c61d4', relief=RAISED, bd = 5)
        BUT2.config(command = SELECT)
        BUT2.place(x=1250, y=630)

        BUT3 = Button(MARKET, text="CHECK MARKET", font=('Helvetica', 15, 'bold'), bg='#2c61d4', relief=RAISED, bd = 5)
        BUT3.config(command = DISPLAY_MARKET)
        BUT3.place(x = 375, y =630)

        BUT4 = Button(MARKET, text = "CALCULATE",font=('Helvetica', 11, 'bold'),bg= 'khaki1', relief=RAISED, bd = 5)
        BUT4.config(command = CALCULATE)
        BUT4.place(x = 1123,y = 630)



    def manage_account():
        def BACK():
            manage.destroy()
            buyer_main.deiconify()


        manage = Tk()
        manage.geometry('800x500')

        ACC = Label(manage, text="My Profile", pady= 5,bg= 'gray46',font=('Helvetica', 30, 'bold'))
        ACC.pack(fill = "x")

        ACC = Label(manage, text="Manage and protect your account", pady=5, bg='gray46',font=('Helvetica', 11, 'bold'))
        ACC.pack(fill="x")

        LogoLabel = Label(manage, text="LULU SHOP", font=('Times New Roman', 20, 'bold'), bg='gray1',fg='ghost white', pady=5, padx=5)
        LogoLabel.place(x=7, y=6)

        Back = Button(manage, text="BACK", font=('Times New Roman', 20, 'bold'), bg='gray46',fg='ghost white', pady=5, padx=5, relief=RAISED, bd =5)
        Back.config(command = BACK)
        Back.place(x=630, y=6, width = 150, height = 60)

        USER_ID = Label(manage,text= f"Seller ID: {ID}",font=('Helvetica', 20, 'bold'))
        USER_ID.place(x = 100, y = 100)

        USER_NAME = Label(manage, text= f'Sellers Name: {Name}',font=('Helvetica', 20, 'bold'))
        USER_NAME.place(x = 100 , y = 180)

        USER_ADD = Label(manage, text = f'Seller Addres: {Address}',font=('Helvetica', 20, 'bold'))
        USER_ADD.place(x=100, y=260)

        USER_Phone = Label(manage, text=f'Seller Phone number: {Phone}',font=('Helvetica', 20, 'bold'))
        USER_Phone.place(x=100, y=340)

        USER_EM = Label(manage, text=f'Seller Email Address: {email}',font=('Helvetica', 20, 'bold'))
        USER_EM.place(x=100, y=420)

        buyer_main.withdraw()

    def Logout():
         buyer_main.destroy()

    buyer_main = Tk()
    buyer_main.resizable(False,False)
    buyer_main.geometry('1400x700')
    buyer_main.title(f'Welcome Seller {Name}')

    cover1 = Label(bg = "#2196f3",pady=10)
    cover1.place(x = 0 , width = 1400, height = 80)

    LogoLabel = Label(buyer_main, text="LULU SHOP", font=('Times New Roman', 30, 'bold'), bg='#2196f3', fg='ghost white',pady=5, padx=5)
    LogoLabel.place(x=7, y=6)

    logout_btn = Button(buyer_main, text="Log-out", bg="#f44336", fg="white", font=("Helvetica", 17, "bold"))
    logout_btn.config(command = Logout)
    logout_btn.place(x = 1250, y = 15)

    cover2 = Label(bg='#778599', pady=10, relief=RIDGE,bd = 5)
    cover2.place(x=0, y= 80, width=600, height=150)

    WELCOME = Label(buyer_main, text="Welcome to LULU",font=('Times New Roman', 30, 'bold'), bg = '#778599', fg='ghost white',pady=10, padx = 100)
    WELCOME.place(x = 40, y = 80 )

    SHOP_LABEL = Label(buyer_main, text="SHOP", font=('Times New Roman', 30, 'bold'), bg='#778599',fg='ghost white', pady=10, padx=207)
    SHOP_LABEL.place(x=40, y=149)

    cover2 = Label(bg='#f2f2f2', pady=10,  relief=RIDGE,bd = 5)
    cover2.place(x=0, y=230, width=600, height=470)

    WELCOME1 = Label(buyer_main, text=f"{Name}", font=('Times New Roman', 30, 'bold'), bg='#f2f2f2',fg='gray1', padx=75)
    WELCOME1.place(x=10, y=250)

    WELCOME2 = Label(buyer_main, text=f"Buyer", font=('Times New Roman', 30, 'bold'), bg='#f2f2f2', fg='gray1', padx=75)
    WELCOME2.place(x=150, y=300)

    TEXT1 = Label(buyer_main, text=f"Thank you for joining us", font=('Times New Roman', 20, 'bold'), bg='#f2f2f2', fg='gray1', padx=75)
    TEXT1.place(x=65, y=450)

    TEXT2 = Label(buyer_main, text=f"This is the main menu, navitage \n through the selection beside on \n what you want to do", font=('Times New Roman', 20, 'bold'), bg='#f2f2f2',fg='gray1', padx=75)
    TEXT2.place(x=20, y=500)



    cover3 = Label(bg='ghost white', pady=10)
    cover3.place(x=600, y=80, width=800, height=620)

    MAINLABEL = Label(buyer_main, text = 'MAIN MENU', bg ='ghost white',font=('Times New Roman', 40, 'bold'),fg='gray1')
    MAINLABEL.place(x = 850,  y = 120)
    # db8b5c

    BUT1 = Button(buyer_main,text = "MY ACCOUNT", font=('Times New Roman', 30, 'bold'),fg='ghost white')
    BUT1.config(bg ='#4caf50', relief=RAISED, bd = 5, activebackground="#a63f03")
    BUT1.config(command = manage_account)
    BUT1.place(x = 830,y = 230,width = 350)

    BUT2 = Button(buyer_main, text="SHOP NOW", font=('Times New Roman', 30, 'bold'), fg='ghost white')
    BUT2.config(bg='#03a9f4', relief=RAISED, bd=5, activebackground="#a63f03")
    BUT2.config(command = SHOPPING)
    BUT2.place(x=830, y=350,width = 350)

    BUT3 = Button(buyer_main, text="MY CART", font=('Times New Roman', 30, 'bold'), fg='ghost white')
    BUT3.config(bg='#ff9800', relief=RAISED, bd=5, activebackground="#a63f03")
    BUT3.config(command = CHECK_CART)
    BUT3.place(x=830, y=470, width = 350)

    BUT4 = Button(buyer_main, text="CHECK OUT", font=('Times New Roman', 30, 'bold'), fg='ghost white')
    BUT4.config(bg='#0288d1', relief=RAISED, bd=5, activebackground="#a63f03")
    BUT4.config(command = CHECK_OUT)
    BUT4.place(x=830, y=590,width = 350)

    buyer_win.destroy()

#=============================================================================BUYERRRR LOGIN========================================================
def login_buy():
    def create_buy():
        def creation(Name,Email,Phone,Password,Address):
            try:
                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                connect.autocommit = True
                cursor = connect.cursor()

                cursor.execute("SELECT MAX(buyer_ID) FROM Buyers")

                last_id = cursor.fetchone()[0]

                if last_id:
                    new_id = last_id + 1
                else:
                    new_id = 100001

                query_stmt = "INSERT INTO Buyers (buyer_ID,buyer_Address,phone_number,password,buyer_name,buyer_email) VALUES(?,?,?,?,?,?)"
                cursor.execute(query_stmt, new_id, Address, Phone, Password, Name, Email)
                NOTIF.config(text="Creation of Account is successful", fg = 'green')

            except pyodbc.Error as ex:
                print(f'Failed to create account {ex}')

        def check_create():
            Name = En_Name.get()
            Email = En_Email.get()
            Phone = En_Phone.get()
            Password = En_Password.get()
            Address = En_Address.get()

            if  Name == '' or Email == '' or Phone == '' or Password == '' or Address == '':
                NOTIF.config(text = 'all fields must be filled !!!!', fg = 'red')
                return
            else:
                creation(Name,Email,Phone,Password,Address)



        create_window = Tk()
        create_window.geometry('900x600')
        create_window.resizable(False,False)
        create_window.title('Create an Account')

        main_Label1 = Label(create_window, text='Create your account to start shopping!!', font=('Helvetica', 30, 'bold'), pady=10,
                            bg='misty rose')
        main_Label1.pack(fill="x")
        main_Label2 = Label(create_window, text='Fill up the needed details', font=('Helvetica', 15, 'bold'),
                            bg='misty rose')
        main_Label2.pack(fill="x")
        main_Label3 = Label(create_window, text='below and join us today!! \N{grinning face}',
                            font=('Helvetica', 15, 'bold'), bg='misty rose')
        main_Label3.pack(fill="x")

        NOTIF = Label(create_window, text='', font=('Helvetica', 15, 'bold'))
        NOTIF.pack(fill="x")

        FName = Label(create_window, text='Full Name (Lastname, Firstname):', font=('Helvetica', 17, 'bold'))
        FName.place(x=40, y=170)

        En_Name = Entry(create_window, font=('Helvetica', 15, 'bold'), relief=RIDGE, bd=5)
        En_Name.place(x=40, y=210, height=40, width=360)

        Phone = Label(create_window, text='Phone number:', font=('Helvetica', 17, 'bold'))
        Phone.place(x=500, y=170)

        En_Phone = Entry(create_window, font=('Helvetica', 15, 'bold'), relief=RIDGE, bd=5)
        En_Phone.place(x=500, y=210, height=40, width=360)

        Email = Label(create_window, text='Email address:', font=('Helvetica', 17, 'bold'))
        Email.place(x=40, y=270)

        En_Email = Entry(create_window, font=('Helvetica', 15, 'bold'), relief=RIDGE, bd=5)
        En_Email.place(x=40, y=310, height=40, width=360)

        Password = Label(create_window, text='Create Password:', font=('Helvetica', 17, 'bold'))
        Password.place(x=500, y=270)

        En_Password = Entry(create_window, font=('Helvetica', 15, 'bold'), relief=RIDGE, bd=5)
        En_Password.place(x=500, y=310, height=40, width=360)

        Address = Label(create_window, text='Full address', font=('Helvetica', 17, 'bold'))
        Address.place(x=375, y=380)

        En_Address = Entry(create_window, font=('Helvetica', 15, 'bold'), relief=RIDGE, bd=5)
        En_Address.place(x=40, y=420, height=40, width=800)

        main_Label4 = Label(create_window, text='Your details will be reviewed before your account is created,',font=('Helvetica', 12, 'bold'), bg='khaki2')
        main_Label4.place(x=0, y=550, width=900)

        main_Label5 = Label(create_window,text='you will receive emails whether your account is approve or not',font=('Helvetica', 12, 'bold'), bg='khaki2')
        main_Label5.place(x=0, y=570, width=900)

        Sign_But = Button(create_window, text='Sign up', font=('Helvetica', 22, 'bold'), relief=RAISED, bd=4, activebackground='green')
        Sign_But.place(x=380, y=470)
        Sign_But.config(command = check_create)

    def login(Email,Pass):
        try:
            connect = pyodbc.connect(
                'DRIVER={SQL SERVER};'
                'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
                'DATABASE=SHOPEE_FINAL;'
                'Trusted_Connection=yes;'
            )

            connect.autocommit = True
            cursor = connect.cursor()

            cursor.execute("SELECT * FROM Buyers WHERE buyer_email = ? and password = ?",(Email,Pass))

            buyer = cursor.fetchone()

            if buyer:
                ID = buyer[0]
                Address = buyer[1]
                Phone = buyer[2]
                Name = buyer[4]
                email = buyer[5]
                buyer_window(ID, Address, Phone, Name, email, buyer_win)
            else:
                INDICATOR.config(text ="Login Failed Incorrect INPUTS", fg = 'red' )


        except pyodbc.Error as ex:
            INDICATOR.config(text ="Failed to Login Account", fg = 'red' )
            print(ex)


    def check_login():
        Email = USER_ENTRY.get()
        Pass = PASS_ENTRY.get()

        if Pass == '' or Email == '':
            INDICATOR.config(text = 'all fields must be filled !!!!', fg = 'red')

        else:
            login(Email,Pass)

    buyer_win = Tk()
    buyer_win.geometry('800x500')
    buyer_win.title('Login as Seller')
    buyer_win.resizable(False,False)

    main_Label = Label(buyer_win, text='LOGIN AS BUYER', font=('Helvetica', 20, 'bold'), pady=20, bg='misty rose')
    main_Label.pack(fill="x")

    USER = Label(buyer_win, text='Login using email', font=('Helvetica', 20, 'bold'))
    USER.place(x=50, y=100)

    USER_ENTRY = Entry(buyer_win, font=('Helvetica', 20, 'bold'), relief=RAISED, bd=4)
    USER_ENTRY.place(x=50, y=150, height=60, width=400)

    PASS = Label(buyer_win, text='Enter Password', font=('Helvetica', 20, 'bold'))
    PASS.place(x=50, y=225)

    PASS_ENTRY = Entry(buyer_win, font=('Helvetica', 20, 'bold'), relief=RAISED, bd=4, show='*')
    PASS_ENTRY.place(x=50, y=275, height=60, width=400)

    LOG_BUT = Button(buyer_win, text='LOGIN', font=('Helvetica', 20, 'bold'), relief=RAISED, bd=5)
    LOG_BUT.config(activebackground='green')
    LOG_BUT.config(command = check_login)
    LOG_BUT.place(x=525, y=200, height=70, width=200)

    INDICATOR = Label(buyer_win, text='Status', font=('Helvetica', 20, 'bold'))
    INDICATOR.place(x=230, y=350)

    CRAETE_Label = Label(buyer_win, text='Not a member yet?', font=('Helvetica', 20, 'bold'))
    CRAETE_Label.place(x=150, y=425)

    CREATE_But = Button(buyer_win, text='Create ACCOUNT', font=('Helvetica', 20, 'bold'), relief=RAISED, bd=5,
                        bg='sky blue')
    CREATE_But.config(command = create_buy)
    CREATE_But.place(x=425, y=415)

    main_window.destroy()


main_window = Tk()
main_window.geometry('1400x700')
icon = PhotoImage(file = 'shopping.png')
main_window.title('Login in LULU SHOP')
main_window.resizable(False,False)
main_window.iconphoto(True,icon)
main_window.config(bg='ghost white')
main_Label = Label(main_window, text = 'Select Login', font = ('Helvetica',40,'bold'), pady = 40, bg = 'misty rose')
main_Label.pack(fill= "x")

Logo = Label(main_window, text = 'Welcome to LULU SHOP',image= icon, compound='top', bg= 'coral', pady= 50, font = ('Helvetica',20,'bold'))
Logo.place(x = 700, y = 145, height = 555, width = 700)


Indicator = Label(main_window, text = 'LOGIN AS', font = ('Helvetica',30, 'bold'), bg = 'ghost white')
Indicator.place(x = 230, y = 150, height = 100, width = 200)

LOGIN_SELLER = Button(main_window, text = 'Seller', font = ('Helvetica',30, 'bold'), bg = 'wheat', relief= RAISED, bd = 5)
LOGIN_SELLER.config(activebackground= 'light coral')
LOGIN_SELLER.config(command= login_sel)
LOGIN_SELLER.place(x = 175, y = 300, height = 100, width = 300)

LOGIN_BUYER = Button(main_window, text = 'Buyer', font = ('Helvetica',30, 'bold'), bg = 'wheat', relief= RAISED, bd = 5)
LOGIN_BUYER.config(activebackground= 'light coral')
LOGIN_BUYER.config(command = login_buy )
LOGIN_BUYER.place(x = 175, y = 450, height = 100, width = 300)

Credits = Label(main_window, text = 'Creators of this application: Hendricks, Adrian, Kurt',font = ('Arial',12, 'bold'), bg = 'ghost white')
Credits.place(x = 125, y = 600)
Credits1 = Label(main_window, text = 'Powered by: python and lucky day',font = ('Arial',12, 'bold'), bg = 'ghost white')
Credits1.place(x = 175, y = 650)



main_window.mainloop()