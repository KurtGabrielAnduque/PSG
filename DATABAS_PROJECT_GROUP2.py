

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyodbc

server = "DESKTOP-6AIOAKJ\\SQLEXPRESS"


# =============================================================================main seller window========================================================
def seller_window(ID, Address, Phone, Name, email, seller_win, server):
    def Logout():
        seller_main.destroy()

    def manage_market():

        def submit_market(P_ID, P_NAME, P_TEXT, P_PRICE, P_STOCK):
            try:
                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    f'SERVER={server};'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                cursor = connect.cursor()
                query_stmt = "INSERT INTO MARKET (product_ID,product_NAME,seller_id,description,price, current_stock) VALUES (?,?,?,?,?,?)"
                cursor.execute(query_stmt, (int(P_ID), P_NAME, int(ID), P_TEXT, int(P_PRICE), int(P_STOCK)))

                query_stmt2 = "DELETE FROM Inventory WHERE product_ID = ? and product_NAME = ?"
                cursor.execute(query_stmt2, (int(P_ID), P_NAME))
                messagebox.showinfo(title="WARNING",
                                    message=f'INSERTED TO MARKET SUCCESSFULY PLS click the check button to referesh treeview')

                connect.commit()

                for record in TREEVIEW.get_children():
                    TREEVIEW.delete(record)

            except pyodbc.Error as ex:
                messagebox.showwarning(title="WARNING", message=f'{ex}')

        def check_data():
            P_ID = Product_ID.get()
            P_NAME = Product_Name.get()
            P_STOCK = Stock_EN.get()
            P_PRICE = PRICE_EN.get()
            P_TEXT = DTEXT.get("1.0", END).strip()

            if P_ID == "" or P_NAME == "" or P_STOCK == "" or P_PRICE == "" or P_TEXT == "":
                messagebox.showwarning(title="WARNIGN",
                                       message="PLS FILL THE NECESSARY FIELDS BEFORE SUBMIT TO THE MARKET")

            else:
                submit_market(P_ID, P_NAME, P_TEXT, P_PRICE, P_STOCK)

        def select_data():
            Product_ID.config(state=NORMAL)
            Product_Name.config(state=NORMAL)
            Stock_EN.config(state=NORMAL)

            selected = TREEVIEW.focus()
            values = TREEVIEW.item(selected, 'values')

            Product_ID.delete(0, END)
            Product_Name.delete(0, END)
            Stock_EN.delete(0, END)
            PRICE_EN.delete(0, END)
            DTEXT.delete('1.0', END)

            Product_ID.insert(0, values[0])
            Product_Name.insert(0, values[1])
            Stock_EN.insert(0, values[2])

            Product_ID.config(state=DISABLED)
            Product_Name.config(state=DISABLED)
            Stock_EN.config(state=DISABLED)

        def update_stock():
            try:

                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    f'SERVER={server};'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                cursor = connect.cursor()
                query_stmt = "SELECT * FROM Inventory"

                cursor.execute(query_stmt)
                products = cursor.fetchall()

                for item in TREEVIEW.get_children():
                    TREEVIEW.delete(item)

                counter = 0

                for product in products:
                    counter += 1
                    TREEVIEW.insert('', 'end', text=f'{counter}',
                                    values=(f'{product[1]}', f'{product[2]}', f'{product[3]}'))


            except pyodbc.Error as ex:
                messagebox.showwarning(title="WARNING", message=f"Failed to load Products {ex}")

        def BACK():
            market.destroy()
            seller_main.deiconify()

        market = Tk()
        market.geometry('1400x700')
        market.title(f'Mange your market')
        market.resizable(False, False)
        market.config(bg='peach puff')

        Welcome = Label(market, text="Manage Market", font=('Helvetica', 30, 'bold'), padx=20, bg='peach puff')
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

        # LABELS

        Product = Label(market, text="Product ID:", font=('Times New Roman', 20, 'bold'), fg='gray1',
                        bg='gray65')
        Product.place(x=20, y=140)

        Product_ID = Entry(market, font=('Times New Roman:', 20, 'bold'), relief=RAISED, bd=5)
        Product_ID.config(state=DISABLED)
        Product_ID.place(x=210, y=140, width=350, height=40)

        PName = Label(market, text="Product Name:", font=('Times New Roman', 20, 'bold'), fg='gray1', bg='gray65')
        PName.place(x=20, y=210)

        Product_Name = Entry(market, font=('Times New Roman', 20, 'bold'), relief=RAISED, bd=5)
        Product_Name.config(state=DISABLED)
        Product_Name.place(x=210, y=210, width=350, height=40)

        Stock = Label(market, text="Current Stock:", font=('Times New Roman', 20, 'bold'), fg='gray1', bg='gray65')
        Stock.place(x=20, y=280)

        Stock_EN = Entry(market, font=('Times New Roman', 20, 'bold'), relief=RAISED, bd=5)
        Stock_EN.config(state=DISABLED)
        Stock_EN.place(x=210, y=280, width=350, height=40)

        PRICE = Label(market, text="PRICE:", font=('Times New Roman', 20, 'bold'), fg='gray1', bg='gray65')
        PRICE.place(x=20, y=350)

        PRICE_EN = Entry(market, font=('Times New Roman', 20, 'bold'), relief=RAISED, bd=5)
        PRICE_EN.place(x=210, y=350, width=350, height=40)

        DESCP = Label(market, text="Description:", font=('Times New Roman', 20, 'bold'), fg='gray1', bg='gray65')
        DESCP.place(x=20, y=400)

        DTEXT = Text(market, font=('Arial', 11), relief=RAISED, bd=5)
        DTEXT.place(x=20, y=440, width=550, height=200)

        BUT1 = Button(market, text="Search", font=('Helvetica', 15, "bold"), relief=RAISED, bd=5)
        BUT1.config(bg='SkyBlue1', activebackground='cyan')
        BUT1.config(command=select_data)
        BUT1.place(x=40, y=650, width=200, height=40)

        BUT2 = Button(market, text="Submit", font=('Helvetica', 15, "bold"), relief=RAISED, bd=5)
        BUT2.config(bg='green', activebackground='lawn green')
        BUT2.config(command=check_data)
        BUT2.place(x=350, y=650, width=200, height=40)

        cover2 = Label(market, bg="gray1")
        cover2.place(x=600, y=130, width=800, height=590)

        TREEVIEW = ttk.Treeview(market)
        TREEVIEW.place(x=625, y=150, width=750, height=480)

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
        BUT3.config(command=update_stock)
        BUT3.place(x=900, y=650, width=200, height=40)

        seller_main.withdraw()

    def manage_profits():

        def Refresh():
            for item in PROFIT_TREE.get_children():
                PROFIT_TREE.delete(item)

            for item in MARKET_TREE.get_children():
                MARKET_TREE.delete(item)

            try:

                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    f'SERVER={server};'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                cursor = connect.cursor()

                query_stmt1 = "SELECT buyer_ID, product_ID, quantity, cost FROM Billing WHERE seller_ID = ?"

                query_stmt2 = "SELECT product_ID,product_NAME,price,current_stock FROM MARKET WHERE seller_ID = ?"

                total_profit = 0
                total_sold = 0

                sales = cursor.execute(query_stmt1, (ID,)).fetchall()
                in_sale = cursor.execute(query_stmt2, (ID,)).fetchall()

                counter2 = 0
                counter = 0
                for sale in sales:
                    counter += 1
                    get_buyer_name = cursor.execute("SELECT buyer_name FROM Buyers WHERE buyer_ID = ?",
                                                    (sale[0])).fetchone()
                    get_product_name = cursor.execute("SELECT product_NAME FROM MARKET WHERE product_ID = ?",
                                                      (sale[1])).fetchone()

                    PROFIT_TREE.insert('', 'end', text=f'{counter}', values=(
                        f'{get_buyer_name[0]}', f'{get_product_name[0]}', f'{sale[2]}',
                        f'{sale[3]}'))
                    total_sold += int(sale[2])
                    total_profit += int(sale[3])

                Sum_Item.config(state=NORMAL)
                Sum_Item.delete(0, END)
                Sum_Item.insert(0, total_sold)
                Sum_prof.config(state="readonly")

                Sum_prof.config(state=NORMAL)
                Sum_prof.delete(0, END)
                Sum_prof.insert(0, f'₱ {total_profit}')
                Sum_prof.config(state="readonly")

                for product in in_sale:
                    MARKET_TREE.insert('', 'end', text=f'{counter}', values=(
                        f'{product[0]}', f'{product[1]}', f'{product[2]}',
                        f'{product[3]}'))


            except pyodbc.Error as ex:
                messagebox.showwarning(title="WARNING", message=f"Failed to load Products {ex}")

        def BACK():
            profits.destroy()
            seller_main.deiconify()

        profits = Tk()
        profits.geometry('1400x700')
        profits.title(f'Seller {Name} Profits')
        profits.resizable(False, False)

        cover1 = Label(profits, bg="#374151", relief=RIDGE, bd=5)
        cover1.place(x=0, width=1400, height=120)

        cover2 = Label(profits, bg="#595959", relief=RIDGE, bd=5)
        cover2.place(x=0, y=120, width=600, height=580)

        cover3 = Label(profits, bg="ghost white", relief=RIDGE, bd=5)
        cover3.place(x=20, y=140, width=560, height=540)

        cover4 = Label(profits, bg="#595959", relief=RIDGE, bd=5)
        cover4.place(x=600, y=120, width=800, height=290)

        MAR_COVER = Label(profits, bg="#1f1f1f")
        MAR_COVER.place(x=610, y=130, width=780, height=60)

        MAR_LABEL = Label(profits, text="ITEMS CURRENTLY IN MARKET", font=('Times New Roman', 30, 'bold'),
                          fg='ghost white', bg="#1f1f1f")
        MAR_LABEL.place(x=685, y=135)

        MARKET_TREE = ttk.Treeview(profits)
        MARKET_TREE.place(x=610, y=190, width=780, height=200)

        MARKET_TREE['columns'] = ('Product_ID', 'Product_Name', 'Price', 'Remaining Stock')
        MARKET_TREE.column("#0", width=40, minwidth=50)
        MARKET_TREE.column("Product_ID", anchor=W, width=120, minwidth=120)
        MARKET_TREE.column("Product_Name", anchor=W, width=120, minwidth=120)
        MARKET_TREE.column("Price", anchor=W, width=120, minwidth=120)
        MARKET_TREE.column("Remaining Stock", anchor=W, width=120, minwidth=120)

        MARKET_TREE.heading("#0", text="row")
        MARKET_TREE.heading("Product_ID", text='Product_ID')
        MARKET_TREE.heading("Product_Name", text='Product_Name')
        MARKET_TREE.heading("Price", text='Price')
        MARKET_TREE.heading("Remaining Stock", text="Remaining Stock")

        cover5 = Label(profits, bg="#595959", relief=RIDGE, bd=5)
        cover5.place(x=600, y=410, width=800, height=290)

        PRO_COVER = Label(profits, bg="#1f1f1f")
        PRO_COVER.place(x=610, y=420, width=780, height=60)

        PRO_LABEL = Label(profits, text="SALES RECORD", font=('Times New Roman', 30, 'bold'), fg='ghost white',
                          bg="#1f1f1f")
        PRO_LABEL.place(x=850, y=425)

        PROFIT_TREE = ttk.Treeview(profits)
        PROFIT_TREE.place(x=610, y=470, width=780, height=210)

        PROFIT_TREE['columns'] = ('Buyer Name', 'Product Name', 'Amount Bought', 'Total cost')
        PROFIT_TREE.column("#0", width=40, minwidth=50)
        PROFIT_TREE.column('Buyer Name', anchor=W, width=120, minwidth=120)
        PROFIT_TREE.column('Product Name', anchor=W, width=120, minwidth=120)
        PROFIT_TREE.column('Amount Bought', anchor=W, width=120, minwidth=120)
        PROFIT_TREE.column('Total cost', anchor=W, width=120, minwidth=120)

        PROFIT_TREE.heading("#0", text="row")
        PROFIT_TREE.heading('Buyer Name', text='Buyer Name')
        PROFIT_TREE.heading('Product Name', text='Product Name')
        PROFIT_TREE.heading('Amount Bought', text='Amount Bought')
        PROFIT_TREE.heading('Total cost', text='Total cost')

        LogoLabel = Label(profits, text="SHOP", font=('Times New Roman', 30, 'bold'), bg='gray1', fg='ghost white',
                          pady=5, padx=5)
        LogoLabel.place(x=7, y=6)

        Back = Button(profits, text="BACK", font=('Times New Roman', 20, 'bold'), bg='gray46', fg='ghost white', pady=5,
                      padx=5, relief=RAISED, bd=5)
        Back.place(x=1200, y=30, width=150, height=60)
        Back.config(command=BACK)

        INFO1 = Label(profits, bg="#374151", text="Manage Profits", font=('Arial', 30, 'bold'), fg="ghost white")
        INFO1.place(x=200, y=10)

        INFO2 = Label(profits, bg="#374151", text="This is a detailed page of your profits", font=('Arial', 20),
                      fg="ghost white")
        INFO2.place(x=200, y=60)

        MAIN_LABEL = Label(profits, text='PROFITS DETAILS', font=('Arial', 30, 'bold'), fg="gray1", bg="ghost white")
        MAIN_LABEL.place(x=130, y=150)

        Item_label = Label(profits, text='Total amount of\nItems sold:', font=('Arial', 20, 'bold'), fg="gray1",
                           bg="ghost white")
        Item_label.place(x=190, y=210)

        Sum_Item = Entry(profits, font=('Arial', 15), relief=RIDGE, bd=5)
        Sum_Item.config(state="readonly")
        Sum_Item.place(x=150, y=280, width=300, height=40)

        notif_sold = Label(profits, text='total items has been sold', font=('Arial', 15), fg="gray1", bg="ghost white")
        notif_sold.place(x=190, y=320)

        prof_label = Label(profits, text='Total profit gained\nfrom sales:', font=('Arial', 20, 'bold'), fg="gray1",
                           bg="ghost white")
        prof_label.place(x=175, y=380)

        Sum_prof = Entry(profits, font=('Arial', 15), relief=RIDGE, bd=5)
        Sum_prof.config(state="readonly")
        Sum_prof.place(x=150, y=450, width=300, height=40)

        notif_prof = Label(profits, text='has been obtained from sales', font=('Arial', 15), fg="gray1",
                           bg="ghost white")
        notif_prof.place(x=170, y=490)

        yap = Label(profits, text="Keep up the good work!", font=('Arial', 20, 'bold'), fg="gray1", bg="ghost white")
        yap.place(x=140, y=540)

        REFRESH = Button(profits, text="REFRESH PROFITS", font=('Arial', 20, 'bold'), relief=RAISED, bd=5, bg="green",
                         fg="ghost white")
        REFRESH.config(command=Refresh)
        REFRESH.place(x=150, y=600, height=50, width=300)

        seller_main.withdraw()

    def check_inv():

        def SELECTED(e):

            selected = TREEVIEW.focus()
            values = TREEVIEW.item(selected, 'values')
            if not values or len(values) < 3:
                return  # Prevents IndexError

            Product_ID.delete(0, END)
            Product_Name.delete(0, END)
            Stock_EN.delete(0, END)

            Product_ID.insert(0, values[0])
            Product_Name.insert(0, values[1])
            Stock_EN.insert(0, values[2])

            Product_ID.config(state=DISABLED)
            Product_Name.config(state=DISABLED)

        def view():
            try:
                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    f'SERVER={server};'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                cursor = connect.cursor()
                query_stmt = "SELECT * FROM Inventory WHERE seller_ID = ?"
                cursor.execute(query_stmt,(ID,))
                products = cursor.fetchall()

                counter = 1

                Product_ID.config(state=NORMAL)
                Product_Name.config(state=NORMAL)
                Stock_EN.config(state=NORMAL)

                for item in TREEVIEW.get_children():
                    TREEVIEW.delete(item)

                for product in products:
                    counter += 1
                    TREEVIEW.insert('', 'end', text=f'{counter}', values=(
                        f'{product[1]}',f'{product[2]}', f'{product[3]}'))


            except pyodbc.Error as ex:
                status.config(text="FAILE TO COLLECT Products", fg='red')
                print(ex)

        def update(merch_ID, merch_name, current_stock):
            try:
                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    f'SERVER={server};'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                cursor = connect.cursor()
                query_stmt = "UPDATE Inventory SET current_stock = ? WHERE product_ID = ? and product_NAME = ?"

                cursor.execute(query_stmt, (int(current_stock), int(merch_ID), merch_name))
                connect.commit()

                if cursor.rowcount > 0:
                    status.config(text="Product Updated Successfully", fg='green')
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


        def ADD(merch_ID, merch_name, current_stock):
            try:
                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    f'SERVER={server};'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                connect.autocommit = True
                cursor = connect.cursor()
                # INSERT INTO ITEM (Item_ID,Item_name,Item_value,Item_quatity) VALUES (?,?,?,?)
                quert_stmt = "INSERT INTO Inventory (seller_ID,product_ID,product_NAME,current_stock) VALUES (?,?,?,?)"
                cursor.execute(quert_stmt, (ID, int(merch_ID), merch_name, int(current_stock)))
                connect.commit()

                if cursor.rowcount > 0:
                    status.config(text="Product Added Successfully", fg='green')
                    Product_ID.delete(0, END)
                    Product_Name.delete(0, END)
                    Stock_EN.delete(0, END)
                else:
                    status.config(text="Failed to Add product")

            except pyodbc.Error as ex:
                status.config(text="Failed to Add product")
                print(ex)

        def ADD_check():
            merch_ID = Product_ID.get()
            merch_name = Product_Name.get()
            current_stock = Stock_EN.get()

            if merch_ID == "" or merch_name == "" or current_stock == "":
                status.config(text="PLS FILL ALL FIELDS!!!")

            else:
                ADD(merch_ID, merch_name, current_stock)

        def BACK():
            inventory.destroy()
            seller_main.deiconify()

        inventory = Tk()
        inventory.geometry('1400x700')
        inventory.title(f'Seller {Name} inventory')
        inventory.resizable(False, False)
        inventory.config(bg='peach puff')

        Welcome = Label(inventory, text="Welcome to the Inventory", font=('Helvetica', 30, 'bold'), padx=20,
                        bg='peach puff')
        Welcome.place(x=0, y=20)
        description = Label(inventory,
                            text="This is where your items are listed. You can add stocks or remove your products",
                            font=('Helvetica', 15, 'bold'), padx=20, bg='peach puff')
        description.place(x=0, y=80)

        Back = Button(inventory, text="BACK", font=('Times New Roman', 20, 'bold'), bg='gray46', fg='ghost white',
                      pady=5, padx=5, relief=RAISED, bd=5)
        Back.config(command=BACK)
        Back.place(x=1200, y=15, width=150, height=60)

        cover_update = Label(inventory, bg='#2b2d40')
        cover_update.place(x=0, y=130, width=550, height=590)

        status = Label(inventory, text="", font=('Times New Roman', 25, 'bold'), fg='ghost white', bg='#2b2d40')
        status.place(x=100, y=140)

        desc1 = Label(inventory, text="Add or Update Products", font=('Times New Roman', 30, 'bold'), fg='ghost white',
                      bg='#2b2d40')
        desc1.place(x=70, y=190)

        Product = Label(inventory, text="Product ID", font=('Times New Roman', 25, 'bold'), fg='ghost white',
                        bg='#2b2d40')
        Product.place(x=180, y=270)

        Product_ID = Entry(inventory, font=('Times New Roman', 25, 'bold'), relief=RAISED, bd=5)
        Product_ID.place(x=70, y=320, width=400, height=40)

        PName = Label(inventory, text="Product Name", font=('Times New Roman', 25, 'bold'), fg='ghost white',
                      bg='#2b2d40')
        PName.place(x=160, y=370)

        Product_Name = Entry(inventory, font=('Times New Roman', 25, 'bold'), relief=RAISED, bd=5)
        Product_Name.place(x=70, y=420, width=400, height=40)

        Stock = Label(inventory, text="Current Stock", font=('Times New Roman', 25, 'bold'), fg='ghost white',
                      bg='#2b2d40')
        Stock.place(x=160, y=470)

        Stock_EN = Entry(inventory, font=('Times New Roman', 25, 'bold'), relief=RAISED, bd=5)
        Stock_EN.place(x=70, y=520, width=400, height=40)

        # 3 BUTTONS

        BUT1 = Button(inventory, text="ADD", font=('Times New Roman', 20, 'bold'), bg="green", relief=RAISED, bd=5)
        BUT1.config(command=ADD_check)
        BUT1.place(x=20, y=600, width=225)


        BUT3 = Button(inventory, text="Update", font=('Times New Roman', 20, 'bold'), bg="#424ec2", relief=RAISED, bd=5)
        BUT3.config(command=check_update)
        BUT3.place(x=300, y=600, width=225)

        cover2 = Label(inventory, bg="#353354")
        cover2.place(x=550, y=130, width=850, height=590)

        cover3 = Label(inventory, bg='#0a0a0a')
        cover3.place(x=550, y=130, width=850, height=100)

        desc4 = Label(inventory, text="CURRENT INVENTORY", font=('Times New Roman', 25, 'bold'), fg='ghost white',
                      bg='#0a0a0a')
        desc4.place(x=780, y=160)




        TREEVIEW = ttk.Treeview(inventory)
        TREEVIEW.place(x=575, y=250, width=800, height=380)

        TREEVIEW['columns'] = ('product_ID', 'product_NAME', 'current_stock')


        TREEVIEW.column("#0", width=150, minwidth=150)
        TREEVIEW.column("product_ID", width=200, minwidth=150)
        TREEVIEW.column("product_NAME", width=200, minwidth=150)
        TREEVIEW.column("current_stock", width=200, minwidth=150)

        TREEVIEW.heading("#0", text="Number")
        TREEVIEW.heading("product_ID", text="Product ID")
        TREEVIEW.heading("product_NAME", text="Product Name")
        TREEVIEW.heading("current_stock", text="current stock")

        TREEVIEW.bind("<ButtonRelease-1>", SELECTED)

        UPDATE_BUT = Button(inventory, text="VIEW INVENTORY", font=('Times New Roman', 20, 'bold'), bg="#424ec2",
                            relief=RAISED, bd=5)
        UPDATE_BUT.config(command=view)
        UPDATE_BUT.place(x=850, y=640, width=300, height=50)

        seller_main.withdraw()

    def manage_account():

        def BACK():
            manage.destroy()
            seller_main.deiconify()

        manage = Tk()
        manage.geometry('800x500')

        ACC = Label(manage, text="My Profile", pady=5, bg='gray46', font=('Helvetica', 30, 'bold'))
        ACC.pack(fill="x")

        ACC = Label(manage, text="Manage and protect your account", pady=5, bg='gray46', font=('Helvetica', 11, 'bold'))
        ACC.pack(fill="x")

        LogoLabel = Label(manage, text="Ziti Zitti SHOP", font=('Times New Roman', 20, 'bold'), bg='gray1', fg='ghost white',
                          pady=5, padx=5)
        LogoLabel.place(x=7, y=6)

        Back = Button(manage, text="BACK", font=('Times New Roman', 20, 'bold'), bg='gray46', fg='ghost white', pady=5,
                      padx=5, relief=RAISED, bd=5)
        Back.config(command=BACK)
        Back.place(x=630, y=6, width=150, height=60)

        USER_ID = Label(manage, text=f"Seller ID: {ID}", font=('Helvetica', 20, 'bold'))
        USER_ID.place(x=100, y=100)

        USER_NAME = Label(manage, text=f'Sellers Name: {Name}', font=('Helvetica', 20, 'bold'))
        USER_NAME.place(x=100, y=180)

        USER_ADD = Label(manage, text=f'Seller Addres: {Address}', font=('Helvetica', 20, 'bold'))
        USER_ADD.place(x=100, y=260)

        USER_Phone = Label(manage, text=f'Seller Phone number: {Phone}', font=('Helvetica', 20, 'bold'))
        USER_Phone.place(x=100, y=340)

        USER_EM = Label(manage, text=f'Seller Email Address: {email}', font=('Helvetica', 20, 'bold'))
        USER_EM.place(x=100, y=420)

        seller_main.withdraw()

    seller_main = Tk()
    seller_main.resizable(False, False)
    seller_main.geometry('1400x700')
    seller_main.title(f'Welcome Seller {Name}')
    seller_main.config(bg='#3A3A3A')

    # =============================== GUI DESIGN ===================================================
    taskbar = Label(seller_main, bg='#374151', relief=RIDGE, bd=5)
    taskbar.place(x=0, width=1400, height=80)

    welcome = Label(seller_main, bg='#E5E7EB', relief=RIDGE, bd=5)
    welcome.place(x=0, y=80, width=600, height=620)

    cover1 = Label(seller_main, bg="#475569", relief=RIDGE, bd=5)
    cover1.place(x=0, y=80, width=600, height=80)

    welcome1 = Label(seller_main, text="WELCOME TO YOUR SHOP", font=('Times New Roman', 30, 'bold'), bg="#475569",
                     fg="ghost white")
    welcome1.place(x=30, y=95)

    logout_btn = Button(seller_main, text="Log-out", bg="#f44336", fg="white", font=("Helvetica", 17, "bold"))
    logout_btn.config(command=Logout)
    logout_btn.place(x=1250, y=15)

    welcome3 = Label(seller_main, text=f"Seller\n{Name}", font=('Times New Roman', 35), fg="gray1", bg="#E5E7EB")
    welcome3.place(x=50, y=200)

    INFO1 = Label(seller_main, text="Thank you for being part of\nour selling community", font=('Times New Roman', 25),
                  fg="gray1", bg="#E5E7EB")
    INFO1.place(x=110, y=350)

    INFO2 = Label(seller_main,
                  text="This is the main menu,\nnavigate through the\n selection on the side to\n get started",
                  font=('Times New Roman', 25),
                  fg="gray1", bg="#E5E7EB")
    INFO2.place(x=140, y=500)

    LogoLabel = Label(seller_main, text="Ziti Zitti SHOP", font=('Times New Roman', 30, 'bold'), bg='gray1', fg='ghost white',
                      pady=5, padx=5)
    LogoLabel.place(x=7, y=6)

    MAINLABEL = Label(seller_main, text="MAIN MENU", font=('Times New Roman', 40, 'bold'), bg='#3A3A3A', pady=5, padx=5,
                      fg='ghost white')
    MAINLABEL.place(x=850, y=90)

    # ======================================================================
    # =========================== 3 BUTTONS ================================
    # ======================================================================

    BUT1 = Button(seller_main, text='MY ACCOUNT', font=('Times New Roman', 30, 'bold'), bg='#475569', fg='ghost white',
                  relief=RAISED, bd=5)
    BUT1.config(activebackground="SlateBlue3")
    BUT1.config(command=manage_account)
    BUT1.place(x=800, y=190, height=70, width=420)

    BUT2 = Button(seller_main, text='CHECK INVENTORY', font=('Times New Roman', 30, 'bold'), bg='#475569',
                  fg='ghost white', relief=RAISED, bd=5)
    BUT2.config(activebackground="SlateBlue3")
    BUT2.config(command=check_inv)
    BUT2.place(x=800, y=290, height=70, width=420)

    BUT3 = Button(seller_main, text='MANAGE PROFITS', font=('Times New Roman', 30, 'bold'), bg='#475569',
                  fg='ghost white', relief=RAISED, bd=5)
    BUT3.config(activebackground="SlateBlue3")
    BUT3.config(command=manage_profits)
    BUT3.place(x=800, y=390, height=70, width=420)

    BUT4 = Button(seller_main, text='MANAGE MARKET', font=('Times New Roman', 30, 'bold'), bg='#475569',
                  fg='ghost white', relief=RAISED, bd=5)
    BUT4.config(activebackground="SlateBlue3")
    BUT4.config(command=manage_market)
    BUT4.place(x=800, y=490, height=70, width=420)

    seller_win.destroy()


# =============================================================================SELLER LOGIN========================================================
def login_sel(server):
    def create_sel():

        def creation(Name, Email, Phone, Password, Address):
            try:
                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    f'SERVER={server};'
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
                NOTIF.config(text="Creation of Account is successful", fg='green')

            except pyodbc.Error as ex:
                print(f'Failed to create account {ex}')

        def check_create():
            Name = En_Name.get()
            Email = En_Email.get()
            Phone = En_Phone.get()
            Password = En_Password.get()
            Address = En_Address.get()

            if Name == '' or Email == '' or Phone == '' or Password == '' or Address == '':
                NOTIF.config(text='all fields must be filled !!!!', fg='red')
                return
            else:
                creation(Name, Email, Phone, Password, Address)

        create_window = Tk()
        create_window.geometry('900x600')
        create_window.resizable(False, False)
        create_window.title('Create an Account')

        main_Label1 = Label(create_window, text='Welcome new seller!', font=('Helvetica', 30, 'bold'), pady=10,
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

        main_Label4 = Label(create_window, text='Your details will be reviewed before your account is created,',
                            font=('Helvetica', 12, 'bold'), bg='khaki2')
        main_Label4.place(x=0, y=550, width=900)

        main_Label5 = Label(create_window, text='you will receive emails whether your account is approve or not',
                            font=('Helvetica', 12, 'bold'), bg='khaki2')
        main_Label5.place(x=0, y=570, width=900)

        Sign_But = Button(create_window, text='Sign up', font=('Helvetica', 22, 'bold'), relief=RAISED, bd=4,
                          activebackground='green')
        Sign_But.place(x=380, y=470)
        Sign_But.config(command=check_create)

    def login(Email, Pass):
        try:
            connect = pyodbc.connect(
                'DRIVER={SQL SERVER};'
                f'SERVER={server};'
                'DATABASE=SHOPEE_FINAL;'
                'Trusted_Connection=yes;'
            )

            connect.autocommit = True
            cursor = connect.cursor()

            cursor.execute(f"SELECT * FROM Sellers Where seller_email =? and password =?", (Email, Pass))

            seller = cursor.fetchone()

            if seller:
                ID = seller[0]
                Address = seller[1]
                Phone = seller[2]
                Name = seller[4]
                email = seller[5]
                seller_window(ID, Address, Phone, Name, email, seller_win, server)

            else:
                INDICATOR.config(text="Login Failed Incorrect INPUTS", fg='red')


        except pyodbc.Error as ex:
            INDICATOR.config(text="Failed to Login Account", fg='red')
            print(f'{ex}')

    def check_login():
        Email = USER_ENTRY.get()
        Pass = PASS_ENTRY.get()

        if Pass == '' or Email == '':
            INDICATOR.config(text='all fields must be filled !!!!', fg='red')

        else:
            login(Email, Pass)

    seller_win = Tk()
    seller_win.geometry('800x500')
    seller_win.title('Login as Seller')
    seller_win.resizable(False, False)

    main_Label = Label(seller_win, text='LOGIN AS SELLER', font=('Helvetica', 20, 'bold'), pady=20, bg='misty rose')
    main_Label.pack(fill="x")

    USER = Label(seller_win, text='Login using email', font=('Helvetica', 20, 'bold'))
    USER.place(x=50, y=100)

    USER_ENTRY = Entry(seller_win, font=('Helvetica', 20, 'bold'), relief=RAISED, bd=4)
    USER_ENTRY.place(x=50, y=150, height=60, width=400)

    PASS = Label(seller_win, text='Enter Password', font=('Helvetica', 20, 'bold'))
    PASS.place(x=50, y=225)

    PASS_ENTRY = Entry(seller_win, font=('Helvetica', 20, 'bold'), relief=RAISED, bd=4, show='*')
    PASS_ENTRY.place(x=50, y=275, height=60, width=400)

    LOG_BUT = Button(seller_win, text='LOGIN', font=('Helvetica', 20, 'bold'), relief=RAISED, bd=5)
    LOG_BUT.config(activebackground='green')
    LOG_BUT.config(command=check_login)
    LOG_BUT.place(x=525, y=200, height=70, width=200)

    INDICATOR = Label(seller_win, text='Status', font=('Helvetica', 20, 'bold'))
    INDICATOR.place(x=230, y=350)

    CRAETE_Label = Label(seller_win, text='Not a member yet?', font=('Helvetica', 20, 'bold'))
    CRAETE_Label.place(x=150, y=425)

    CREATE_But = Button(seller_win, text='Create ACCOUNT', font=('Helvetica', 20, 'bold'), relief=RAISED, bd=5,
                        bg='sky blue')
    CREATE_But.config(command=create_sel)
    CREATE_But.place(x=425, y=415)

    main_window.destroy()


# =============================================================================MAIN BUYER WINDOW========================================================
def buyer_window(ID, Address, Phone, Name, email, buyer_win, server):
    def CHECK_OUT(CART_ID, QUANTITY, COST, NAME, CCART):

        def PAY():
            method = E_PAYMENT.get()
            print(method)

            if not method:
                messagebox.showwarning("Warning", "Please select a payment method.")
                return

            to_pay = EntryCost.get()

            payment_status = ''
            if method == "CASH ON DELIVERY":
                payment_status = "Pending"
            else:
                payment_status = "Paid"

            try:
                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    f'SERVER={server};'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                cursor = connect.cursor()

                # cart_ID = cursor.execute("SELECT MAX(cart_ID) FROM Cart").fetchone()[0]
                Bill_ID = cursor.execute("SELECT MAX(billing_ID) FROM  Billing").fetchone()[0]

                query_stmt = "SELECT product_ID FROM Cart WHERE cart_ID = ?"

                product_id = cursor.execute(query_stmt, (CART_ID,)).fetchone()[0]

                query_stmt2 = "SELECT seller_ID FROM MARKET WHERE product_ID = ?"

                seller_id = cursor.execute(query_stmt2, (product_id,)).fetchone()[0]

                query_stmt3 = "SELECT seller_Address, phone_number FROM Sellers WHERE seller_ID = ?"

                seller_info = cursor.execute(query_stmt3, (seller_id,)).fetchone()

                sel_add = seller_info[0]
                sel_number = seller_info[1]

                if Bill_ID:
                    Bill_ID = Bill_ID + 1
                else:
                    Bill_ID = 7001

                query_stmt6 = "SELECT current_stock FROM MARKET WHERE product_ID = ?"

                check_quantity = cursor.execute(query_stmt6, (product_id,)).fetchone()[0]

                if int(QUANTITY) > int(check_quantity):
                    messagebox.showwarning(title="WARNING",
                                           message="NO MORE AVAILABLE stock in the market pls. remove it from your cart or lessen your quantity")
                    return

                content = f'''
                         🧾 Marketplace Receipt

                    Billing ID: {Bill_ID}
                    Payment Mode: {method}
                    Payment Status: {payment_status}

                    -----------------------------------------
                    Buyer Information:
                    - Buyer ID: {ID}
                    - Address: {Address}
                    - Phone Number: {Phone}

                    Seller Information:
                    - Seller ID: {seller_id}
                    - Address: {sel_add}
                    - Phone Number: {sel_number}

                    -----------------------------------------
                    Product Details:
                    - Product ID: {product_id}
                    - Product Name:{NAME}
                    - Quantity: {QUANTITY}
                    - Cost: {COST} ₱
                    - Shipping fee : 70 ₱
                    - Total Amount to be paid: {to_pay} ₱

                    -----------------------------------------
                    Thank you for shopping with us!



                '''
                TEXT.config(state="normal")
                TEXT.delete("1.0", "end")
                TEXT.insert("1.0", content)
                TEXT.config(state="disabled")

                query_stmt4 = "INSERT INTO Billing (buyer_ID,buyer_Address,buyer_phone_num,seller_ID,seller_Address,seller_phone_num,product_ID,quantity,billing_ID,payment_mode,payment_status,cost) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"

                cursor.execute(query_stmt4, (
                    int(ID), Address, Phone, int(seller_id), sel_add, sel_number, int(product_id), int(QUANTITY),
                    int(Bill_ID), method, payment_status, int(COST)))
                cursor.commit()
                # update the quantity of the market

                query_stmt5 = "UPDATE MARKET set current_stock = current_stock - ? WHERE product_ID = ?"

                cursor.execute(query_stmt5, (int(QUANTITY), product_id))
                cursor.commit()

                query_stmt9 = "SELECT current_stock FROM MARKET WHERE product_ID = ?"

                check_quantity = cursor.execute(query_stmt9, (product_id,)).fetchone()[0]

                if int(check_quantity) <= 0:
                    query_stmt7 = "DELETE FROM MARKET WHERE product_ID = ?"
                    cursor.execute(query_stmt7, (product_id,))
                    cursor.commit()

                # update the profit of the seller
                query_stmt8 = "INSERT INTO Profit (Seller_ID,billing_ID,product_ID,quantity,cost) VALUES(?,?,?,?,?)"
                cursor.execute(query_stmt8, (int(seller_id), int(Bill_ID), int(product_id), int(QUANTITY), int(COST)))

                cursor.commit()

                # loading screeen
                messagebox.showinfo(title="payment notice",
                                    message="PAYMENT PROCESSING SUCCESSFULY please wait for your product to deliver")




            except pyodbc.Error as ex:
                messagebox.showwarning(title="WARNING", message=f"{ex}")

        def BACK():
            Billing.destroy()
            CCART.deiconify()

        Billing = Tk()
        Billing.title("Payment menu")
        Billing.geometry("1400x700")
        Billing.resizable(False, False)
        cover1 = Label(Billing, bg="#c3e8c1", relief=RIDGE, bd=5)
        cover1.place(x=0, width=1400, height=120)
        LogoLabel = Label(Billing, text="SHOP", font=('Times New Roman', 30, 'bold'), bg='gray1', fg='ghost white',
                          pady=5, padx=5)
        LogoLabel.place(x=7, y=6)
        INFO1 = Label(Billing, bg="#c3e8c1", text="Pending payment for product", font=('Arial', 30, 'bold'))
        INFO1.place(x=200, y=20)
        INFO2 = Label(Billing, bg="#c3e8c1", text="Items that are pending payment are lister here",
                      font=('Arial', 15, "bold"))
        INFO2.place(x=200, y=70)


        cover2 = Label(Billing, bg="#0f0f0f", relief=RAISED, bd=5)
        cover2.place(x=0, y=120, width=950, height=580)

        cover3 = Label(Billing, bg="#1d3852", relief=RIDGE, bd=3)
        cover3.place(x=950, y=630, width=450, height=80)
        LABEL3 = Label(Billing, text="Please pay on time to avoid problems", font=('Arial', 17, "bold"),
                       fg='ghost white', bg="#1d3852")
        LABEL3.place(x=965, y=650)

        cover4 = Label(Billing, bg="#235b82", relief=RIDGE, bd=3)
        cover4.place(x=950, y=530, width=450, height=100)

        cover5 = Label(Billing, bg="#A6CAEC", relief=RIDGE, bd=5)
        cover5.place(x=950, y=180, width=450, height=350)

        cover7 = Label(Billing, text="", bg="#E3F2FD", bd=3, relief=RAISED)
        cover7.place(x=965, y=195, width=420, height=320)

        cover6 = Label(Billing, bg="#235b82", relief=RIDGE, bd=3)
        cover6.place(x=950, y=120, height=60, width=450)

        LABEL4 = Label(Billing, text="TOTAL AMOUNT TO PAID: ", fg="ghost white", font=("Arial", 15, "bold"),
                       bg="#235b82")
        LABEL4.place(x=960, y=540)

        EntryCost = Entry(Billing, font=("Helvetica", 15, "bold"), relief=RIDGE, bd=5)
        EntryCost.insert(0, f'{int(COST) + 70}')
        EntryCost.configure(state="readonly")
        EntryCost.place(x=1030, y=580, height=40, width=300)

        MAINLABEL = Label(Billing, text="Select Payment Method", font=("Helvetica", 22, "bold"), bg="#235b82",
                          fg="ghost white")
        MAINLABEL.place(x=1010, y=130)

        LABEL1 = Label(Billing, text="Selected Item:", bg="#E3F2FD", font=("Helvetica", 15, "bold"))
        LABEL1.place(x=980, y=220)

        LABEL2 = Label(Billing, text="Total quantity:", bg="#E3F2FD", font=("Helvetica", 15, "bold"))
        LABEL2.place(x=980, y=270)

        LABEL2 = Label(Billing, text="Total Cost:", bg="#E3F2FD", font=("Helvetica", 15, "bold"))
        LABEL2.place(x=980, y=320)

        E_NAME = Entry(Billing, font=("Helvetica", 17, "bold"), relief=RIDGE, bd=5)
        E_NAME.insert(0, NAME)
        E_NAME.config(state="readonly")
        E_NAME.place(x=1150, y=215, width=210, height=40)

        E_QUAN = Entry(Billing, font=("Helvetica", 17, "bold"), relief=RIDGE, bd=5)
        E_QUAN.insert(0, QUANTITY)
        E_QUAN.config(state="readonly")
        E_QUAN.place(x=1150, y=265, width=210, height=40)

        E_COST = Entry(Billing, font=("Helvetica", 17, "bold"), relief=RIDGE, bd=5)
        E_COST.insert(0, COST)
        E_COST.config(state="readonly")
        E_COST.place(x=1150, y=315, width=210, height=40)


        options = ["G-CASH", "PAY MAYA", "7-ELEVEN", 'BDO', "CASH ON DELIVERY", "BPI"]


        E_PAYMENT = ttk.Combobox(Billing,value = options, state="readonly")
        E_PAYMENT.config(font=("Helvetica", 15, "bold"))
        E_PAYMENT.current(0)
        E_PAYMENT.place(x=1075, y=390, width=200, height=40)




        PAYNOW = Button(Billing, text="PAY NOW!", font=("Helvetica", 15, "bold"), relief=RAISED, bd=5, bg="#3F51B5",fg="ghost white")
        PAYNOW.config(command=PAY)
        PAYNOW.place(x=1120, y=450)

        Back = Button(Billing, text="BACK", font=('Times New Roman', 20, 'bold'), bg='gray46', fg='ghost white', pady=5,
                      padx=5, relief=RAISED, bd=5)
        Back.place(x=1200, y=15, width=150, height=60)
        Back.config(command=BACK)

        cover8 = Label(Billing, bg="#233b61", relief=RIDGE, bd=3)
        cover8.place(x=20, y=140, height=100, width=908)

        LABEL5 = Label(Billing, text="RECEIPT", font=('Times New Roman', 40, 'bold'), bg="#233b61", fg="ghost white")
        LABEL5.place(x=370, y=155)

        TEXT = Text(Billing, bg="ghost white", relief=RIDGE, bd=5, font=("Helvetica", 12, "bold"), state=DISABLED)
        TEXT.place(x=20, y=240, height=435, width=908)

        CCART.withdraw()

    def CHECK_CART():



        def GET_ID():
            E_NAME.config(state=NORMAL)
            E_COST.config(state=NORMAL)
            E_QUAN.config(state=NORMAL)
            E_CART.config(state=NORMAL)

            CART_ID = E_CART.get()
            QUANTITY = E_QUAN.get()
            COST = E_COST.get()
            NAME = E_NAME.get()

            if CART_ID == "" or QUANTITY == "" or COST == "" or E_CART == "":
                messagebox.showwarning(title="WARNING", message="PLS SELECT PRODUCTS BEFORE CHECK OUT")
                return
            else:
                E_CART.config(state=DISABLED)
                CHECK_OUT(CART_ID, QUANTITY, COST, NAME, CCART)

        def REMOVE():
            E_CART.config(state=NORMAL)
            CART_ID = E_CART.get()
            E_CART.config(state=DISABLED)

            try:

                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    f'SERVER={server};'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                cursor = connect.cursor()
                query_stmt = "DELETE FROM Cart WHERE cart_ID  = ?"

                cursor.execute(query_stmt, (int(CART_ID),))
                connect.commit()

                messagebox.showinfo(title="NOTICE", message="SUCCESSFULY REMOVE FROM THE CART")
            except pyodbc.Error as ex:
                messagebox.showwarning(title="WARNING", message=f"Failed to load Products {ex}")

        def SELECTED(e):
            E_NAME.config(state=NORMAL)
            E_QUAN.config(state=NORMAL)
            E_COST.config(state=NORMAL)
            E_CART.config(state=NORMAL)

            selected = TREEVIEW.focus()
            values = TREEVIEW.item(selected, 'values')

            if not values or len(values) < 6:
                return

            E_NAME.delete(0, END)
            E_QUAN.delete(0, END)
            E_COST.delete(0, END)
            E_CART.delete(0, END)

            E_NAME.insert(0, values[1])
            E_QUAN.insert(0, values[4])
            E_COST.insert(0, values[5])
            E_CART.insert(0, values[3])

            E_NAME.config(state=DISABLED)
            E_QUAN.config(state=DISABLED)
            E_COST.config(state=DISABLED)
            E_CART.config(state=DISABLED)

        def DISPLAY_CART():
            try:

                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    f'SERVER={server};'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                cursor = connect.cursor()
                query_stmt = "SELECT * FROM Cart WHERE buyer_ID  = ?"

                cursor.execute(query_stmt, (ID))
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
        CCART.config(bg="peach puff")

        Back = Button(CCART, text="BACK", font=('Times New Roman', 20, 'bold'), bg='gray46', fg='ghost white', pady=5,
                      padx=5, relief=RAISED, bd=5)
        Back.config(command=BACK)
        Back.place(x=1200, y=15, width=150, height=60)

        cover1 = Label(CCART, bg='gray1', pady=10, relief=RIDGE, bd=5)
        cover1.place(x=0, y=130, width=950, height=570)
        cover2 = Label(CCART, bg="gray46", relief=RIDGE, bd=5)
        cover2.place(x=950, y=130, width=450, height=570)

        LogoLabel = Label(CCART, text="Ziti Zitti SHOP", font=('Times New Roman', 30, 'bold'), bg='gray1', fg='ghost white',
                          pady=5, padx=5)
        LogoLabel.place(x=7, y=6)

        WELCOME3 = Label(CCART, text="SHOPPING CART", font=('Helvetica', 30, 'bold'), bg='peach puff',
                         fg='gray1', pady=5, padx=5)
        WELCOME3.place(x=530, y=10)

        WELCOME4 = Label(CCART, text="This is where you will be managing\nthe items in your cart",
                         font=('Helvetica', 17, 'bold'), bg='peach puff', fg='gray1', pady=5, padx=5)
        WELCOME4.place(x=500, y=60)

        cover3 = Label(CCART, bg="#131e61")
        cover3.place(x=970, y=150, width=410, height=100)

        cover4 = Label(CCART, bg="#131e61")
        cover4.place(x=970, y=150, width=410, height=100)
        cover5 = Label(CCART, bg="#303a73")
        cover5.place(x=970, y=250, width=410, height=430)

        SELECT_LABEL = Label(CCART, text="Select Items in cart \nthat you want to checkout",
                             font=('Helvetica', 20, 'bold'), fg='ghost white', bg="#131e61")
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

        BUT3 = Button(CCART, text="REFRESH CART", font=('Helvetica', 15, 'bold'), bg='#2c61d4', relief=RAISED, bd=5)
        BUT3.config(command=DISPLAY_CART)
        BUT3.place(x=375, y=630)

        TREEVIEW.bind("<ButtonRelease-1>", SELECTED)

        # patuloy ng mga buttons kulang parin
        # pati design bai

        LABEL1 = Label(CCART, text="Selected Item:", bg="#303a73", font=("Helvetica", 15, "bold"), fg="ghost white")
        LABEL1.place(x=980, y=270)

        LABEL2 = Label(CCART, text="Total quantity:", bg="#303a73", font=("Helvetica", 15, "bold"), fg='ghost white')
        LABEL2.place(x=980, y=320)

        LABEL3 = Label(CCART, text="Total Cost:", bg="#303a73", font=("Helvetica", 15, "bold"), fg='ghost white')
        LABEL3.place(x=980, y=370)

        LABEL4 = Label(CCART, text="Cart ID:", bg="#303a73", font=("Helvetica", 15, "bold"), fg='ghost white')
        LABEL4.place(x=980, y=420)
        # entries disable
        E_NAME = Entry(CCART, font=("Helvetica", 17, "bold"), relief=RIDGE, bd=5, state=DISABLED)
        E_NAME.place(x=1150, y=265, width=210, height=40)

        E_QUAN = Entry(CCART, font=("Helvetica", 17, "bold"), relief=RIDGE, bd=5, state=DISABLED)
        E_QUAN.place(x=1150, y=315, width=210, height=40)

        E_COST = Entry(CCART, font=("Helvetica", 17, "bold"), relief=RIDGE, bd=5, state=DISABLED)
        E_COST.place(x=1150, y=365, width=210, height=40)

        E_CART = Entry(CCART, font=("Helvetica", 17, "bold"), relief=RIDGE, bd=5, state=DISABLED)
        E_CART.place(x=1150, y=415, width=210, height=40)

        BUT1 = Button(CCART, text='CHECK OUT\n ITEM', bg='green', font=("Helvetica", 15, "bold"), fg="ghost white",
                      relief=RAISED, bd=5)
        BUT1.place(x=980, y=600, width=180)
        BUT1.config(command=GET_ID)

        BUT2 = Button(CCART, text='REMOVE FROM\n CART', bg='red', font=("Helvetica", 15, "bold"), fg="ghost white",
                      relief=RAISED, bd=5)
        BUT2.place(x=1195, y=600)
        BUT2.config(command=REMOVE)

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
                messagebox.showwarning(title="WARNING",
                                       message="PLS FILL THE QUANTITY YOU WANT TO BUY BEFORE CALCULATE")

            try:

                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    f'SERVER={server};'
                    'DATABASE=SHOPEE_FINAL;'
                    'Trusted_Connection=yes;'
                )

                cursor = connect.cursor()

                query_stmt = "SELECT seller_ID FROM Sellers WHERE seller_name = ?"
                seller_result = cursor.execute(query_stmt, (Seller_Name,)).fetchone()
                seller_id = seller_result[0]

                query_stmt1 = "SELECT product_ID, current_stock FROM MARKET WHERE product_NAME = ? and seller_ID = ?"
                product_result = cursor.execute(query_stmt1, (product_Name, seller_id)).fetchone()
                product_ID, current_stock = product_result

                if int(QUANTITY) > current_stock:
                    messagebox.showwarning(
                        title="WARNING",
                        message=f"Not enough stock. Only {current_stock} item(s) left in stock."
                    )
                    return

                # cursor.execute("SELECT MAX(buyer_ID) FROM Buyers")
                cart_ID = cursor.execute("SELECT MAX(cart_ID) FROM Cart").fetchone()[0]

                if cart_ID:
                    new_cart_ID = cart_ID + 1
                else:
                    new_cart_ID = 30000
                # "INSERT INTO Buyers (buyer_ID,buyer_Address,phone_number,password,buyer_name,buyer_email) VALUES(?,?,?,?,?,?)"
                query_stmt3 = "INSERT INTO Cart (product_ID,buyer_ID,cart_ID,quantity,total_cost) VALUES (?,?,?,?,?)"
                cursor.execute(query_stmt3, (product_ID, ID, new_cart_ID, QUANTITY, COST))
                connect.commit()

                messagebox.showinfo(title="NOTIFICATION",
                                    message="SUCCESSFULY ADDED TO CART PLS CHECK YOUR CART TO VERIFY")

            except pyodbc.Error as ex:
                messagebox.showwarning(title="WARNING", message=f"FAILED TO MOVE PRODUCTS TO CART {ex}")

        def DISPLAY_MARKET():
            try:

                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    f'SERVER={server};'
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
                    seller_result = cursor.execute(get_name_seller, (product[2])).fetchone()
                    seller_name = seller_result[0] if seller_result else "UNKNOWN"

                    counter += 1
                    TREEVIEW.insert('', 'end', text=f'{counter}', values=(
                    f'{product[0]}', f'{product[1]}', f'{seller_name}', f'{product[4]}', f'{product[3]}',
                    f'{product[5]}'))


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
            E_COST.delete(0, END)
            E_QUANTITY.delete(0, END)

            E_NAME.insert(0, values[1])
            E_SNAME.insert(0, values[2])
            E_COST.insert(0, values[3])

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
                messagebox.showwarning(title="WARNING",
                                       message="PLS FILL THE QUANTITY YOU WANT TO BUY BEFORE CALCULATE")
            else:
                TOTAL_COST = (int(QUANTITY) * int(COST))
                E_COST.config(state=NORMAL)

                E_COST.delete(0, END)

                E_COST.insert(0, TOTAL_COST)

                E_COST.config(state=DISABLED)

        MARKET = Tk()
        MARKET.geometry("1400x700")
        MARKET.title("WELCOME TO MAIN MARKET")
        MARKET.resizable(False, False)
        MARKET.config(bg="peach puff")

        Back = Button(MARKET, text="BACK", font=('Times New Roman', 20, 'bold'), bg='gray46', fg='ghost white', pady=5,
                      padx=5, relief=RAISED, bd=5)
        Back.config(command=BACK)
        Back.place(x=1200, y=25, width=150, height=60)

        cover1 = Label(MARKET, bg='gray1', pady=10, relief=RIDGE, bd=5)
        cover1.place(x=0, y=130, width=950, height=570)
        cover2 = Label(MARKET, bg="gray46", relief=RIDGE, bd=5)
        cover2.place(x=950, y=130, width=450, height=570)

        LogoLabel = Label(MARKET, text="Ziti Zitti SHOP", font=('Times New Roman', 30, 'bold'), bg='gray1', fg='ghost white',
                          pady=5, padx=5)
        LogoLabel.place(x=7, y=6)

        WELCOME3 = Label(MARKET, text="Welcome to the market", font=('Helvetica', 30, 'bold'), bg='peach puff',
                         fg='gray1', pady=5, padx=5)
        WELCOME3.place(x=300, y=20)

        WELCOME4 = Label(MARKET, text="Browse for items you want yo buy", font=('Helvetica', 17, 'bold'),
                         bg='peach puff', fg='gray1', pady=5, padx=5)
        WELCOME4.place(x=300, y=70)

        cover3 = Label(MARKET, bg="#131e61")
        cover3.place(x=970, y=150, width=410, height=100)

        cover4 = Label(MARKET, bg="#131e61")
        cover4.place(x=970, y=150, width=410, height=100)
        cover5 = Label(MARKET, bg="#303a73")
        cover5.place(x=970, y=250, width=410, height=430)

        SELECT_LABEL = Label(MARKET, text="Select Items in market \nto add in your cart",
                             font=('Helvetica', 20, 'bold'), fg='ghost white', bg="#131e61")
        SELECT_LABEL.place(x=1020, y=165)

        TREEVIEW = ttk.Treeview(MARKET)
        TREEVIEW.place(x=25, y=165, width=900, height=450)

        TREEVIEW['columns'] = ('Product_ID', 'Product_Name', 'Seller_Name', 'Price', 'Description', 'Current_Stock')
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

        P_NAME = Label(MARKET, text="PRODUCT NAME", font=('Helvetica', 17, 'bold'), fg='ghost white', bg="#303a73")
        P_NAME.place(x=1075, y=265)

        E_NAME = Entry(MARKET, state=DISABLED, relief=RAISED, bd=5, font=('Helvetica', 17, 'bold'))
        E_NAME.place(x=1030, y=305, width=300, height=40)

        S_NAME = Label(MARKET, text="SELLER NAME", font=('Helvetica', 17, 'bold'), fg='ghost white', bg="#303a73")
        S_NAME.place(x=1090, y=360)

        E_SNAME = Entry(MARKET, state=DISABLED, relief=RAISED, bd=5, font=('Helvetica', 17, 'bold'))
        E_SNAME.place(x=1030, y=405, width=300, height=40)

        QUANTITY = Label(MARKET, text="Enter Quantity", font=('Helvetica', 17, 'bold'), fg='ghost white', bg="#303a73")
        QUANTITY.place(x=1095, y=460)

        E_QUANTITY = Entry(MARKET, relief=RAISED, bd=5, font=('Helvetica', 17, 'bold'))
        E_QUANTITY.place(x=1030, y=505, width=300, height=40)

        COST = Label(MARKET, text="COST", font=('Helvetica', 17, 'bold'), fg='ghost white', bg="#303a73")
        COST.place(x=1000, y=575)

        E_COST = Entry(MARKET, relief=RAISED, bd=5, font=('Helvetica', 17, 'bold'), state=DISABLED)
        E_COST.place(x=1100, y=570, width=230, height=40)

        buyer_main.withdraw()

        # BUTTON 2

        BUT1 = Button(MARKET, text="ADD TO CART", font=('Helvetica', 11, 'bold'), bg='green', relief=RAISED, bd=5)
        BUT1.config(command=ADD_CART)
        BUT1.place(x=980, y=630)

        BUT2 = Button(MARKET, text="SELECT ITEM", font=('Helvetica', 11, 'bold'), bg='#2c61d4', relief=RAISED, bd=5)
        BUT2.config(command=SELECT)
        BUT2.place(x=1250, y=630)

        BUT3 = Button(MARKET, text="CHECK MARKET", font=('Helvetica', 15, 'bold'), bg='#2c61d4', relief=RAISED, bd=5)
        BUT3.config(command=DISPLAY_MARKET)
        BUT3.place(x=375, y=630)

        BUT4 = Button(MARKET, text="CALCULATE", font=('Helvetica', 11, 'bold'), bg='khaki1', relief=RAISED, bd=5)
        BUT4.config(command=CALCULATE)
        BUT4.place(x=1123, y=630)

    def manage_account():
        def BACK():
            manage.destroy()
            buyer_main.deiconify()

        manage = Tk()
        manage.geometry('800x500')

        ACC = Label(manage, text="My Profile", pady=5, bg='gray46', font=('Helvetica', 30, 'bold'))
        ACC.pack(fill="x")

        ACC = Label(manage, text="Manage and protect your account", pady=5, bg='gray46', font=('Helvetica', 11, 'bold'))
        ACC.pack(fill="x")

        LogoLabel = Label(manage, text="Ziti Zitti SHOP", font=('Times New Roman', 20, 'bold'), bg='gray1', fg='ghost white',
                          pady=5, padx=5)
        LogoLabel.place(x=7, y=6)

        Back = Button(manage, text="BACK", font=('Times New Roman', 20, 'bold'), bg='gray46', fg='ghost white', pady=5,
                      padx=5, relief=RAISED, bd=5)
        Back.config(command=BACK)
        Back.place(x=630, y=6, width=150, height=60)

        USER_ID = Label(manage, text=f"Buyer ID: {ID}", font=('Helvetica', 20, 'bold'))
        USER_ID.place(x=100, y=100)

        USER_NAME = Label(manage, text=f'Buyer Name: {Name}', font=('Helvetica', 20, 'bold'))
        USER_NAME.place(x=100, y=180)

        USER_ADD = Label(manage, text=f'Buyer Address: {Address}', font=('Helvetica', 20, 'bold'))
        USER_ADD.place(x=100, y=260)

        USER_Phone = Label(manage, text=f'Buyer Phone number: {Phone}', font=('Helvetica', 20, 'bold'))
        USER_Phone.place(x=100, y=340)

        USER_EM = Label(manage, text=f'Buyer Email Address: {email}', font=('Helvetica', 20, 'bold'))
        USER_EM.place(x=100, y=420)

        buyer_main.withdraw()

    def Logout():
        buyer_main.destroy()

    buyer_main = Tk()
    buyer_main.resizable(False, False)
    buyer_main.geometry('1400x700')
    buyer_main.title(f'Welcome Seller {Name}')

    cover1 = Label(bg="#2196f3", pady=10)
    cover1.place(x=0, width=1400, height=80)

    LogoLabel = Label(buyer_main, text="Ziti Zitti SHOP", font=('Times New Roman', 30, 'bold'), bg='#2196f3',
                      fg='ghost white', pady=5, padx=5)
    LogoLabel.place(x=7, y=6)

    logout_btn = Button(buyer_main, text="Log-out", bg="#f44336", fg="white", font=("Helvetica", 17, "bold"))
    logout_btn.config(command=Logout)
    logout_btn.place(x=1250, y=15)

    cover2 = Label(bg='#778599', pady=10, relief=RIDGE, bd=5)
    cover2.place(x=0, y=80, width=600, height=150)

    WELCOME = Label(buyer_main, text="Welcome to Ziti Zitti", font=('Times New Roman', 30, 'bold'), bg='#778599',
                    fg='ghost white', pady=10, padx=100)
    WELCOME.place(x=40, y=80)

    SHOP_LABEL = Label(buyer_main, text="SHOP", font=('Times New Roman', 30, 'bold'), bg='#778599', fg='ghost white',
                       pady=10, padx=207)
    SHOP_LABEL.place(x=40, y=149)

    cover2 = Label(bg='#f2f2f2', pady=10, relief=RIDGE, bd=5)
    cover2.place(x=0, y=230, width=600, height=470)

    WELCOME1 = Label(buyer_main, text=f"{Name}", font=('Times New Roman', 30, 'bold'), bg='#f2f2f2', fg='gray1',
                     padx=75)
    WELCOME1.place(x=10, y=250)

    WELCOME2 = Label(buyer_main, text=f"Buyer", font=('Times New Roman', 30, 'bold'), bg='#f2f2f2', fg='gray1', padx=75)
    WELCOME2.place(x=150, y=300)

    TEXT1 = Label(buyer_main, text=f"Thank you for joining us", font=('Times New Roman', 20, 'bold'), bg='#f2f2f2',
                  fg='gray1', padx=75)
    TEXT1.place(x=65, y=450)

    TEXT2 = Label(buyer_main,
                  text=f"This is the main menu, navitage \n through the selection beside on \n what you want to do",
                  font=('Times New Roman', 20, 'bold'), bg='#f2f2f2', fg='gray1', padx=75)
    TEXT2.place(x=20, y=500)

    cover3 = Label(bg='ghost white', pady=10)
    cover3.place(x=600, y=80, width=800, height=620)

    MAINLABEL = Label(buyer_main, text='MAIN MENU', bg='ghost white', font=('Times New Roman', 40, 'bold'), fg='gray1')
    MAINLABEL.place(x=850, y=120)
    # db8b5c

    BUT1 = Button(buyer_main, text="MY ACCOUNT", font=('Times New Roman', 30, 'bold'), fg='ghost white')
    BUT1.config(bg='#4caf50', relief=RAISED, bd=5, activebackground="#a63f03")
    BUT1.config(command=manage_account)
    BUT1.place(x=830, y=230, width=350)

    BUT2 = Button(buyer_main, text="SHOP NOW", font=('Times New Roman', 30, 'bold'), fg='ghost white')
    BUT2.config(bg='#03a9f4', relief=RAISED, bd=5, activebackground="#a63f03")
    BUT2.config(command=SHOPPING)
    BUT2.place(x=830, y=350, width=350)

    BUT3 = Button(buyer_main, text="MY CART", font=('Times New Roman', 30, 'bold'), fg='ghost white')
    BUT3.config(bg='#ff9800', relief=RAISED, bd=5, activebackground="#a63f03")
    BUT3.config(command=CHECK_CART)
    BUT3.place(x=830, y=470, width=350)

    buyer_win.destroy()


# =============================================================================BUYERRRR LOGIN========================================================
def login_buy(server):
    def create_buy():
        def creation(Name, Email, Phone, Password, Address):
            try:
                connect = pyodbc.connect(
                    'DRIVER={SQL SERVER};'
                    f'SERVER={server};'
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
                NOTIF.config(text="Creation of Account is successful", fg='green')

            except pyodbc.Error as ex:
                print(f'Failed to create account {ex}')

        def check_create():
            Name = En_Name.get()
            Email = En_Email.get()
            Phone = En_Phone.get()
            Password = En_Password.get()
            Address = En_Address.get()

            if Name == '' or Email == '' or Phone == '' or Password == '' or Address == '':
                NOTIF.config(text='all fields must be filled !!!!', fg='red')
                return
            else:
                creation(Name, Email, Phone, Password, Address)

        create_window = Tk()
        create_window.geometry('900x600')
        create_window.resizable(False, False)
        create_window.title('Create an Account')

        main_Label1 = Label(create_window, text='Create your account to start shopping!!',
                            font=('Helvetica', 30, 'bold'), pady=10,
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

        main_Label4 = Label(create_window, text='Your details will be reviewed before your account is created,',
                            font=('Helvetica', 12, 'bold'), bg='khaki2')
        main_Label4.place(x=0, y=550, width=900)

        main_Label5 = Label(create_window, text='you will receive emails whether your account is approve or not',
                            font=('Helvetica', 12, 'bold'), bg='khaki2')
        main_Label5.place(x=0, y=570, width=900)

        Sign_But = Button(create_window, text='Sign up', font=('Helvetica', 22, 'bold'), relief=RAISED, bd=4,
                          activebackground='green')
        Sign_But.place(x=380, y=470)
        Sign_But.config(command=check_create)

    def login(Email, Pass):
        try:
            connect = pyodbc.connect(
                'DRIVER={SQL SERVER};'
                f'SERVER={server};'
                'DATABASE=SHOPEE_FINAL;'
                'Trusted_Connection=yes;'
            )

            connect.autocommit = True
            cursor = connect.cursor()

            cursor.execute("SELECT * FROM Buyers WHERE buyer_email = ? and password = ?", (Email, Pass))

            buyer = cursor.fetchone()

            if buyer:
                ID = buyer[0]
                Address = buyer[1]
                Phone = buyer[2]
                Name = buyer[4]
                email = buyer[5]
                buyer_window(ID, Address, Phone, Name, email, buyer_win, server)
            else:
                INDICATOR.config(text="Login Failed Incorrect INPUTS", fg='red')


        except pyodbc.Error as ex:
            INDICATOR.config(text="Failed to Login Account", fg='red')
            print(ex)

    def check_login():
        Email = USER_ENTRY.get()
        Pass = PASS_ENTRY.get()

        if Pass == '' or Email == '':
            INDICATOR.config(text='all fields must be filled !!!!', fg='red')

        else:
            login(Email, Pass)

    buyer_win = Tk()
    buyer_win.geometry('800x500')
    buyer_win.title('Login as Seller')
    buyer_win.resizable(False, False)

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
    LOG_BUT.config(command=check_login)
    LOG_BUT.place(x=525, y=200, height=70, width=200)

    INDICATOR = Label(buyer_win, text='Status', font=('Helvetica', 20, 'bold'))
    INDICATOR.place(x=230, y=350)

    CRAETE_Label = Label(buyer_win, text='Not a member yet?', font=('Helvetica', 20, 'bold'))
    CRAETE_Label.place(x=150, y=425)

    CREATE_But = Button(buyer_win, text='Create ACCOUNT', font=('Helvetica', 20, 'bold'), relief=RAISED, bd=5,
                        bg='sky blue')
    CREATE_But.config(command=create_buy)
    CREATE_But.place(x=425, y=415)

    main_window.destroy()


main_window = Tk()
main_window.geometry('1400x700')
icon = PhotoImage(file='shopping.png')
main_window.title('Login in Ziti Zitti SHOP')
main_window.resizable(False, False)
main_window.iconphoto(True, icon)
main_window.config(bg='ghost white')
main_Label = Label(main_window, text='Select Login', font=('Helvetica', 40, 'bold'), pady=40, bg='misty rose')
main_Label.pack(fill="x")

Logo = Label(main_window, text='Welcome to Ziti Zitti SHOP', image=icon, compound='top', bg='coral', pady=50,
             font=('Helvetica', 20, 'bold'))
Logo.place(x=700, y=145, height=555, width=700)

Indicator = Label(main_window, text='LOGIN AS', font=('Helvetica', 30, 'bold'), bg='ghost white')
Indicator.place(x=230, y=150, height=100, width=200)

LOGIN_SELLER = Button(main_window, text='Seller', font=('Helvetica', 30, 'bold'), bg='wheat', relief=RAISED, bd=5)
LOGIN_SELLER.config(activebackground='light coral')

LOGIN_SELLER.config(command=lambda: login_sel(server))
LOGIN_SELLER.place(x=175, y=300, height=100, width=300)

LOGIN_BUYER = Button(main_window, text='Buyer', font=('Helvetica', 30, 'bold'), bg='wheat', relief=RAISED, bd=5)
LOGIN_BUYER.config(activebackground='light coral')
LOGIN_BUYER.config(command=lambda: login_buy(server))
LOGIN_BUYER.place(x=175, y=450, height=100, width=300)

Credits = Label(main_window, text='Creators of this application: Hendricks, Adrian, Kurt', font=('Arial', 12, 'bold'),
                bg='ghost white')
Credits.place(x=125, y=600)
Credits1 = Label(main_window, text='Powered by: python and lucky day', font=('Arial', 12, 'bold'), bg='ghost white')
Credits1.place(x=175, y=650)


main_window.mainloop()
