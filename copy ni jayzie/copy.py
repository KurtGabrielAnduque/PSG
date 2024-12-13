from tkinter import *
from tkinter import ttk, messagebox
import csv
import os
from datetime import datetime

# Initialize main GUI
GUI = Tk()
GUI.geometry('800x500')
GUI.title("HOME PAGE")

# Path for CSV file
csv_file_path = 'inventory.csv'

def read_csv_data():
    """Reads data from the CSV file and returns it as a list of dictionaries."""
    if not os.path.exists(csv_file_path):
        return []
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def write_to_csv(product_name, expiry_date, quantity):
    """Writes a new product entry to the CSV file."""
    header_exists = os.path.exists(csv_file_path)
    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Product', 'Expiry Date', 'Quantity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not header_exists:
            writer.writeheader()
        writer.writerow({'Product': product_name, 'Expiry Date': expiry_date, 'Quantity': quantity})

def GROCERY_PRESSED():
    """Handles the GROCERY window and displays products based on expiration."""
    GROCERY_SCREEN = Toplevel(GUI)
    GROCERY_SCREEN.geometry("1000x600")
    GROCERY_SCREEN.title("GROCERY")

    # UI Elements
    Grocery_LABEL = Label(GROCERY_SCREEN, bd=10, text="GROCERY LIST", font=('Helvetica bold', 20), bg='gray')
    Grocery_LABEL.place(x=0, y=0, width=1000, height=50)

    Main_Label1 = Label(GROCERY_SCREEN, text="Enter the Date today (YYYY-MM-DD):", font=('Helvetica bold', 20))
    Main_Label1.place(x=50, y=60, width=500, height=50)
    Main_Entry = Entry(GROCERY_SCREEN, font=('Arial', 15), bg='old lace', bd=3)
    Main_Entry.place(x=560, y=67, width=200, height=40)

    Frame1 = Frame(GROCERY_SCREEN, bd=5, relief=RIDGE, bg='white')
    Frame1.place(x=10, y=120, width=550, height=460)
    F1_LABEL = Label(GROCERY_SCREEN, text="DISPLAY PRODUCTS", font=('Helvetica bold', 20), bg="light pink")
    F1_LABEL.place(x=15, y=125, width=542, height=50)

    F1_TEXTBOX = Text(GROCERY_SCREEN, font=('Arial', 15), bg='old lace', bd=3)
    F1_TEXTBOX.place(x=15, y=175, width=542, height=403)

    Frame2 = Frame(GROCERY_SCREEN, bd=5, relief=RIDGE, bg='white')
    Frame2.place(x=565, y=120, width=430, height=460)
    F2_LABEL = Label(GROCERY_SCREEN, text="LIST OF EXPIRED PRODUCTS", font=('Helvetica bold', 20), bg="SteelBlue2")
    F2_LABEL.place(x=570, y=125, width=422, height=50)

    F2_TEXTBOX = Text(GROCERY_SCREEN, font=('Arial', 15), bg='linen', bd=3)
    F2_TEXTBOX.place(x=570, y=175, width=422, height=403)

    def check_products():
        """Checks and displays expired/non-expired products."""
        try:
            current_date = datetime.strptime(Main_Entry.get(), '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")
            return

        products = read_csv_data()
        non_expired = []
        expired = []

        for product in products:
            product_name = product['Product']
            expiry_date = datetime.strptime(product['Expiry Date'], '%Y-%m-%d')
            quantity = product['Quantity']

            if expiry_date >= current_date:
                non_expired.append(product)
            else:
                expired.append(f"{product_name} - Expiry: {expiry_date.date()} - Qty: {quantity}")

        # Update CSV with non-expired products
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Product', 'Expiry Date', 'Quantity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(non_expired)

        # Display products in respective frames
        F1_TEXTBOX.delete(1.0, END)
        F2_TEXTBOX.delete(1.0, END)

        for product in non_expired:
            F1_TEXTBOX.insert(END,
                              f"{product['Product']} - Expiry: {product['Expiry Date']} - Qty: {product['Quantity']}\n")

        F2_TEXTBOX.insert(END, "\n".join(expired))

        if expired:
            messagebox.showinfo("Expired Products", "Expired products have been removed from the inventory.")

    # Button to check products
    Button(GROCERY_SCREEN, text="Check Products", font=('Helvetica bold', 15), command=check_products, bg = 'bisque2').place(x=770, y=67, width=180, height=40)

def INVENTORY_PRESSED():
    """Handles the INVENTORY window for adding and checking products."""
    INVENTOTY_SCREEN = Toplevel(GUI)
    INVENTOTY_SCREEN.geometry("1000x600")
    INVENTOTY_SCREEN.title("SHOP INVENTORY")

    INV_LABEL = Label(INVENTOTY_SCREEN, bd=10, text="INVENTORY STOCK", font=('Helvetica bold', 20), bg='gray')
    INV_LABEL.place(x=0, y=0, width=1000, height=50)

    Frame1 = Frame(INVENTOTY_SCREEN, bd=5, relief=RIDGE, bg='white')
    Frame1.place(x=10, y=60, width=550, height=520)
    F1_LABEL = Label(INVENTOTY_SCREEN, text="DISPLAY PRODUCTS", font=('Helvetica bold', 20), bg="light pink")
    F1_LABEL.place(x=15, y=65, width=542, height=50)

    F1_TEXTBOX = Text(INVENTOTY_SCREEN, font=('Arial', 15), bg='old lace', bd=3)
    F1_TEXTBOX.place(x=15, y=115, width=542, height=463)

    Frame2 = Frame(INVENTOTY_SCREEN, bd=5, relief=RIDGE, bg='white')
    Frame2.place(x=565, y=60, width=430, height=520)
    F2_LABEL = Label(INVENTOTY_SCREEN, text="ADD PRODUCTS", font=('Helvetica bold', 20), bg="SteelBlue2")
    F2_LABEL.place(x=570, y=65, width=422, height=50)

    Label1 = Label(INVENTOTY_SCREEN, text="Product", font=('Helvetica bold', 20), bg="white")
    Label1.place(x=693, y=140, width=180, height=50)
    Entry1 = Entry(INVENTOTY_SCREEN, font=('Arial', 15), bg='old lace', bd=3)
    Entry1.place(x=660, y=200, width=250, height=50)

    Label2 = Label(INVENTOTY_SCREEN, text="Expiration Date (YYYY-MM-DD)", font=('Helvetica bold', 20), bg="white")
    Label2.place(x=590, y=260, width=400, height=50)
    Entry2 = Entry(INVENTOTY_SCREEN, font=('Arial', 15), bg='old lace', bd=3)
    Entry2.place(x=660, y=320, width=250, height=50)

    Label3 = Label(INVENTOTY_SCREEN, text="Quantity", font=('Helvetica bold', 20), bg="white")
    Label3.place(x=693, y=375, width=180, height=50)
    Entry3 = Entry(INVENTOTY_SCREEN, font=('Arial', 15), bg='old lace', bd=3)
    Entry3.place(x=660, y=435, width=250, height=50)

    def add_product():
        """Adds a product to the CSV file."""
        product_name = Entry1.get().strip()
        expiry_date = Entry2.get().strip()
        quantity = Entry3.get().strip()

        # Validate input
        if not product_name or not expiry_date or not quantity:
            messagebox.showwarning("Input Error", "All fields are required.")
            return

        try:
            datetime.strptime(expiry_date, '%Y-%m-%d')  # Validate date format
            int(quantity)  # Validate quantity is a number
        except (ValueError, TypeError):
            messagebox.showerror("Invalid Input", "Enter a valid date (YYYY-MM-DD) and numeric quantity.")
            return

        write_to_csv(product_name, expiry_date, quantity)
        messagebox.showinfo("Success", f"Product '{product_name}' added successfully.")
        Entry1.delete(0, END)
        Entry2.delete(0, END)
        Entry3.delete(0, END)

    def display_products():
        """Displays all products from the CSV file."""
        products = read_csv_data()
        F1_TEXTBOX.delete(1.0, END)

        for product in products:
            F1_TEXTBOX.insert(END, f"{product['Product']} - Expiry: {product['Expiry Date']} - Qty: {product['Quantity']}\n")

    # Buttons
    Button1 = Button(INVENTOTY_SCREEN, text="ADD", font=('Helvetica bold', 20), bg="tan1", command=add_product)
    Button1.place(x=575, y=510, width=200, height=50)

    Button2 = Button(INVENTOTY_SCREEN, text="Check", font=('Helvetica bold', 20), bg="SlateBlue2", command=display_products)
    Button2.place(x=785, y=510, width=200, height=50)

# Main GUI components
Main_Label = Label(GUI, bd=10, text="INVENTORY SYSTEM", font=('Helvetica bold', 20), bg="gray")
Main_Label.place(x=0, y=0, width=800, height=100)

Main_btn1 = Button(GUI, bd=3, text="INVENTORY", font=('Helvetica bold', 20), bg="RosyBrown1", command=INVENTORY_PRESSED)
Main_btn1.place(x=250, y=150, width=300, height=100)

Main_btn2 = Button(GUI, bd=3, text="GROCERY", font=('Helvetica bold', 20), bg="coral", command=GROCERY_PRESSED)
Main_btn2.place(x=250, y=325, width=300, height=100)

GUI.mainloop()
