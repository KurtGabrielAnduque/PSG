from tkinter import *
from tkinter import ttk
import csv
import os

class Payroll:

    def search_employee(self):
        employee_id = self.F1_Entry1.get()
        if not employee_id:
            print("Please enter an Employee ID to search.")
            return

        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Employee ID"] == employee_id:
                        # Populate fields with employee data
                        self.F1_Entry2.delete(0, END)
                        self.F1_Entry2.insert(0, row["Name"])
                        self.F1_Entry3.delete(0, END)
                        self.F1_Entry3.insert(0, row["Age"])
                        self.F1_Combo.set(row["Gender"])
                        self.F1_Entry5.delete(0, END)
                        self.F1_Entry5.insert(0, row["Email"])
                        self.F1_Entry6.delete(0, END)
                        self.F1_Entry6.insert(0, row["DOB"])
                        self.F1_Entry7.delete(0, END)
                        self.F1_Entry7.insert(0, row["Contact No"])
                        self.F1_Entry8.delete(0, END)
                        self.F1_Entry8.insert(0, row["Status"])
                        self.F1_Entry9.delete("1.0", END)
                        self.F1_Entry9.insert("1.0", row["Address"])
                        self.F2_Entry1.delete(0, END)
                        self.F2_Entry1.insert(0, row["Department"])
                        self.F2_Entry2.delete(0, END)
                        self.F2_Entry2.insert(0, row["Days Worked"])
                        self.F2_Entry3.delete(0, END)
                        self.F2_Entry3.insert(0, row["Rate Per Day"])
                        self.F2_Entry5.delete(0, END)
                        self.F2_Entry5.insert(0, row["SSS"])
                        self.F2_Entry6.delete(0, END)
                        self.F2_Entry6.insert(0, row["Pagibig"])
                        self.F2_Entry7.delete(0, END)
                        self.F2_Entry7.insert(0, row["Philhealth"])
                        self.F2_Entry8.delete(0, END)
                        self.F2_Entry8.insert(0, row["Tax"])
                        self.F2_Entry4.config(state='normal')
                        self.F2_Entry4.delete(0, END)
                        self.F2_Entry4.insert(0, row["Net Salary"])
                        self.F2_Entry4.config(state='readonly')
                        print("Employee data loaded successfully.")
                        return
                print("Employee ID not found.")
        except FileNotFoundError:
            print("Employee data file not found.")
        except Exception as e:
            print(f"An error occurred while searching: {e}")


    def calculate_salary(self):
        try:
            # Collect inputs
            days = int(self.F2_Entry2.get())
            rate = float(self.F2_Entry3.get())
            sss = float(self.F2_Entry5.get())
            pagibig = float(self.F2_Entry6.get())
            philhealth = float(self.F2_Entry7.get())
            tax = float(self.F2_Entry8.get())

            # Calculations
            gross_salary = days * rate
            deductions = sss + pagibig + philhealth + tax
            net_salary = gross_salary - deductions

            # Update salary field
            self.F2_Entry4.config(state='normal')
            self.F2_Entry4.delete(0, END)
            self.F2_Entry4.insert(0, f"{net_salary:.2f}")
            self.F2_Entry4.config(state='readonly')

        except ValueError:
            print("Please fill out all required fields with valid numbers!")

    def save_employee(self):
        try:
            # Gather data dynamically from widgets
            employee_data = {
                "Employee ID": self.F1_Entry1.get(),
                "Name": self.F1_Entry2.get(),
                "Age": self.F1_Entry3.get(),
                "Gender": self.F1_Combo.get(),
                "Email": self.F1_Entry5.get(),
                "DOB": self.F1_Entry6.get(),
                "Contact No": self.F1_Entry7.get(),
                "Status": self.F1_Entry8.get(),
                "Address": self.F1_Entry9.get("1.0", END).strip(),
                "Department": self.F2_Entry1.get(),
                "Days Worked": self.F2_Entry2.get(),
                "Rate Per Day": self.F2_Entry3.get(),
                "SSS": self.F2_Entry5.get(),
                "Pagibig": self.F2_Entry6.get(),
                "Philhealth": self.F2_Entry7.get(),
                "Tax": self.F2_Entry8.get(),
                "Net Salary": self.F2_Entry4.get()
            }

            # Write to CSV
            file_exists = os.path.isfile(self.filename)
            with open(self.filename, mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=employee_data.keys())
                if not file_exists:
                    writer.writeheader()
                writer.writerow(employee_data)

            self.show_payslip(employee_data)
            print("Employee record saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving: {e}")


    # search person
    #remove from dataset
    #insert new dataset in the csv





    def clear_fields(self):
        # Clear all fields in the GUI
        for entry in [self.F1_Entry1, self.F1_Entry2, self.F1_Entry3, self.F1_Entry5,
                      self.F1_Entry6, self.F1_Entry7, self.F1_Entry8, self.F2_Entry1,
                      self.F2_Entry2, self.F2_Entry3, self.F2_Entry4,
                      self.F2_Entry5, self.F2_Entry6, self.F2_Entry7, self.F2_Entry8]:
            entry.delete(0, END)
        self.F1_Combo.set("Select Gender")
        self.F1_Entry9.delete("1.0", END)
        self.F4_textbox.delete("1.0", END)
        print("All fields cleared.")

    def show_payslip(self, employee_data):
        # Display the pay slip in the text box
        self.F4_textbox.delete("1.0", END)
        payslip = f"--- Pay Slip ---\n"
        for key, value in employee_data.items():
            payslip += f"{key}: {value}\n"
        payslip += "\n--- Thank You! ---"
        self.F4_textbox.insert(END, payslip)

    def update_employee(self):
        # Update employee data in CSV
        employee_id = self.F1_Entry1.get()
        if not employee_id:
            print("Please provide an Employee ID to update.")
            return

        updated = False
        updated_data = []
        with open(self.filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["Employee ID"] == employee_id:

                    row.update({
                        "Name": self.F1_Entry2.get(),
                        "Age": self.F1_Entry3.get(),
                        "Gender": self.F1_Combo.get(),
                        "Email": self.F1_Entry5.get(),
                        "DOB": self.F1_Entry6.get(),
                        "Contact No": self.F1_Entry7.get(),
                        "Status": self.F1_Entry8.get(),
                        "Address": self.F1_Entry9.get("1.0", END).strip(),
                        "Department": self.F2_Entry1.get(),
                        "Days Worked": self.F2_Entry2.get(),
                        "Rate Per Day": self.F2_Entry3.get(),
                        "SSS": self.F2_Entry5.get(),
                        "Pagibig": self.F2_Entry6.get(),
                        "Philhealth": self.F2_Entry7.get(),
                        "Tax": self.F2_Entry8.get(),
                        "Net Salary": self.F2_Entry4.get()
                    })

                    updated = True
                updated_data.append(row)

            self.F4_textbox.delete("1.0", END)
            payslip = f"--- Pay Slip ---\n"
            payslip += f"Name: {self.F1_Entry2.get()}\n"
            payslip += f"Age: {self.F1_Entry3.get()}\n"
            payslip += f"Gender: {self.F1_Combo.get()}\n"
            payslip += f"Email: {self.F1_Entry5.get()}\n"
            payslip += f"Date of Birth: {self.F1_Entry6.get()}\n"
            payslip += f"Contact No: {self.F1_Entry7.get()}\n"
            payslip += f"Status: {self.F1_Entry8.get()}\n"
            payslip += f"Address: {self.F1_Entry9.get("1.0", END).strip()}\n"
            payslip += f"Department: {self.F2_Entry1.get()}\n"
            payslip += f"Days Worked: {self.F2_Entry2.get()}\n"
            payslip += f"Rate Per Day: {self.F2_Entry3.get()}\n"
            payslip += f"SSS: {self.F2_Entry5.get()}\n"
            payslip += f"Pagibig: {self.F2_Entry6.get()}\n"
            payslip += f"Philhealth: {self.F2_Entry7.get()}\n"
            payslip += f"Tax: {self.F2_Entry8.get()}\n"
            payslip += f"Net Salary: {self.F2_Entry4.get()}\n"
            payslip += "--- Thank You! ---"
            self.F4_textbox.insert(END, payslip)

        if updated:


            with open(self.filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=row.keys())
                writer.writeheader()
                writer.writerows(updated_data)
            print("Employee record updated successfully.")

        else:
            print("Employee ID not found.")

    def delete_employee(self):
        try:
            # Validate Employee ID
            employee_id = self.F1_Entry1.get()
            if not employee_id:
                print("Please provide an Employee ID to delete.")
                return

            # Read CSV file
            updated_data = []
            deleted = False

            # Check if file exists and is not empty
            if os.path.isfile(self.filename) and os.stat(self.filename).st_size > 0:
                with open(self.filename, mode='r', newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row["Employee ID"] == employee_id:
                            deleted = True
                            continue  # Skip the employee to delete
                        updated_data.append(row)
            else:
                print("File is empty or does not exist.")
                return

            # Write updated data back to the CSV if deletion occurred
            if deleted:
                with open(self.filename, mode='w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=updated_data[0].keys())
                    writer.writeheader()
                    writer.writerows(updated_data)
                print(f"Employee with ID {employee_id} deleted successfully.")
                self.clear_fields()
            else:
                print(f"Employee ID {employee_id} not found.")
        except Exception as e:
            print(f"An error occurred while deleting: {e}")



    def __init__(self, GUI):
        self.GUI = GUI
        self.filename = "employee_data.csv"







        Main_Label = Label(self.GUI, bd=3, text="PAYROLL SYSTEM", font=('Arial bold', 20))
        Main_Label.pack(padx=20, pady=20)


        # mga label under frame1 ===================================================
        Frame1 = Frame(self.GUI, bd=5, relief=RIDGE, bg="white")
        Frame1.place(x=10, y=70, width=750, height=630)

        F1_Label = Label(self.GUI, text="Employee Details", font=('Arial bold', 20), bg='grey')
        F1_Label.place(x=12, y=70, width=748, height=50)

        F1_Label2 = Label(self.GUI, text='Employee I.D.: ', font= ('Arial bold', 15), bg= 'white')
        F1_Label2.place(x = 20 , y= 130, width = 200, height = 50)
        self.F1_Entry1 = Entry(self.GUI,font=('Arial',15), bg = 'old lace',bd =3)
        self.F1_Entry1.place(x = 200, y = 135, width = 200, height = 40)
        self.F1_Button1 = Button(self.GUI,text="Search", font = ('Arial',15),bg = 'lavender' ,bd =3)
        self.F1_Button1.place(x = 410,y = 135, width = 150, height = 40)
        self.F1_Button1.config(command=self.search_employee)


        F1_Label3 = Label(self.GUI, text='Name: ', font= ('Arial bold', 15), bg='white')
        F1_Label3.place(x = 20, y = 200, width = 150, height = 50 )
        self.F1_Entry2 = Entry(self.GUI, font=('Arial', 15), bg = 'old lace',bd =3)
        self.F1_Entry2.place(x = 150, y = 205 , width = 200 , height = 40)


        F1_Label4 = Label(self.GUI, text="Age: ", font = ('Arial bold', 15), bg= 'white')
        F1_Label4.place(x = 25, y = 265, width = 150, height = 50)
        self.F1_Entry3 = Entry(self.GUI,font=('Arial',15), bg = 'old lace',bd =3)
        self.F1_Entry3.place(x =150, y = 270, width = 200, height = 40)

        F1_Label5 = Label(self.GUI, text = "Gender: ", font = ('Arial bold', 15), bg ='white')
        F1_Label5.place(x = 25, y = 330, width = 150, height = 50)


        lst = ["Male", "Female"]


        self.F1_Combo = ttk.Combobox(self.GUI, value = lst, font=('Arial',15), background = 'old lace')
        self.F1_Combo.set("Select Gender")
        self.F1_Combo.place(x = 150, y =335, width = 200, height = 40)


        F1_Label6 = Label(self.GUI, text="Email: ", font= ('Arial bold', 15), bg= 'white')
        F1_Label6.place(x = 25, y = 390, width = 150, height = 50)
        self.F1_Entry5 = Entry(self.GUI, font = ('Arial', 15), bg = 'old lace',bd =3)
        self.F1_Entry5.place(x = 150, y = 395, width = 200, height = 40)


        F1_Label8 = Label(self.GUI, text="Date of Birth: ", font = ('Arial bold', 15), bg = 'white')
        F1_Label8.place(x = 400, y = 200, width = 150, height = 50)
        self.F1_Entry6 = Entry(self.GUI, font=('Arial',15), bg = 'old lace',bd =3)
        self.F1_Entry6.place(x = 540, y= 205, width = 200, height= 40)


        F1_Label9 = Label(self.GUI, text="Contact No : ", font = ('Arial bold', 15) ,bg= 'white')
        F1_Label9.place(x = 400, y= 265, width = 150, height = 50)
        self.F1_Entry7 = Entry(self.GUI, font = ('Arial', 15), bg = 'old lace',bd =3)
        self.F1_Entry7.place(x = 540, y = 270 , width = 200, height = 40)

        F1_Label10 = Label(self.GUI, text="Status: ", font = ('Arial bold', 15), bg = 'white')
        F1_Label10.place(x = 400, y = 330, width = 150, height = 50)
        self.F1_Entry8 = Entry(self.GUI,font = ('Arial', 15), bg = 'old lace',bd =3)
        self.F1_Entry8.place(x = 540, y = 335, width = 200, height = 40)

        F1_Label11 = Label(self.GUI, text="Address: ", font =('Arial bold', 15), bg = 'white')
        F1_Label11.place(x = 20,  y = 450, width = 150, height = 50)
        self.F1_Entry9 = Text(self.GUI, font = ('Arial',15), bg = 'old lace',bd =3)
        self.F1_Entry9.place(x = 150, y = 460, width = 590, height = 200)
        #==========================================================================================





        #MGA ELEMENT UNDER FRAME 2 DITO PAPASOK ===================================================
        Frame2 = Frame(self.GUI, bd=5, relief=RIDGE, bg='white')
        Frame2.place(x=770, y=70, width=610, height=420)
        F2_Label = Label(self.GUI, text="Employee Salary Details", font=('Arial bold', 20), bg='grey')
        F2_Label.place(x=772, y=70, width=608, height=50)

        #department
        F2_Label1 = Label(self.GUI, text="Department: ", font = ('Arial bold', 15), bg = 'white')
        F2_Label1.place(x = 780 , y = 130, width = 150 , height = 50)
        self.F2_Entry1 = Entry(self.GUI, font = ('Arial', 15), bg= 'old lace',bd =3)
        self.F2_Entry1.place(x = 920,  y = 135, width = 150, height = 40)

        #No of days
        F2_Label2 = Label(self.GUI, text="No. of days: ", font = ('Arial bold', 15), bg= 'white')
        F2_Label2.place(x = 780, y= 200, width = 150 , height = 50)
        self.F2_Entry2 = Entry(self.GUI, font=('Arial', 15), bg = 'old lace',bd =3)
        self.F2_Entry2.place(x = 920, y = 205, width = 150 , height = 40)

        #rate per day
        F2_Label3 = Label(self.GUI,text="Rate per day: ", font = ('Arial bold', 15), bg='white')
        F2_Label3.place(x = 1080, y = 130, width = 150, height = 50)
        self.F2_Entry3 = Entry(self.GUI, font=('Arial', 15), bg='old lace',bd =3)
        self.F2_Entry3.place(x = 1220, y = 135, width = 150, height = 40)


        #salary
        F2_Label4 = Label(self.GUI, text="Salary: ", font=('Arial bold', 15), bg = 'white')
        F2_Label4.place(x = 1080, y = 200, width = 150, height = 50)
        self.F2_Entry4 = Entry(self.GUI, font=('Arial', 15), bg='old lace', bd=3,state='readonly')
        self.F2_Entry4.place(x=1220, y=205, width=150, height=40)

        F2_Label5 = Label(self.GUI, text = "SSS: ", font= ('Arial bold', 15), bg = 'white')
        F2_Label5.place(x = 780, y= 260, width = 150, height = 50)
        self.F2_Entry5 = Entry(self.GUI, font=('Arial', 15), bg='old lace', bd = 3)
        self.F2_Entry5.place(x = 920, y = 265, width = 150, height = 40)


        F2_Label6 = Label(self.GUI, text = "PAG-IBIG: ", font = ('Arial bold', 15), bg = 'white')
        F2_Label6.place(x = 1080, y = 260, width = 150, height = 50)
        self.F2_Entry6 = Entry(self.GUI,font=('Arial', 15), bg='old lace', bd = 3)
        self.F2_Entry6.place(x = 1220, y = 265, width = 150, height = 40)


        F2_Label7 = Label(self.GUI, text = "PHILHEALTH: ", font = ('Arial bold', 15), bg = 'white')
        F2_Label7.place(x = 780, y = 310, width = 150, height = 50)
        self.F2_Entry7 = Entry(self.GUI, font=('Arial', 15), bg = 'old lace', bd= 3)
        self.F2_Entry7.place(x = 920, y = 315, width = 150, height = 40)

        F2_Label8 = Label(self.GUI, text= "TAX: ", font=('Arial bold', 15), bg='white')
        F2_Label8.place(x = 1080, y = 310, width = 150, height = 50)
        self.F2_Entry8 = Entry(self.GUI, font= ('Arial', 15),bg = 'old lace', bd = 3)
        self.F2_Entry8.place(x = 1220, y = 315, width = 150, height = 40)



        #BUTTONS
        # calculate
        self.F2_Button1 = Button(self.GUI, text=" CALCULATE ", font = ('Arial bold', 15), bg = 'coral',bd =3)
        self.F2_Button1.place(x = 800, y = 370, width = 180, height = 50)
        self.F2_Button1.config(command=self.calculate_salary)

        # save
        self.F2_Button2 = Button(self.GUI, text=" SAVE ", font = ('Arial bold', 15), bg = 'khaki1',bd=3)
        self.F2_Button2.place(x = 990, y = 370, width = 180, height = 50)
        self.F2_Button2.config(command=self.save_employee)

        #clear
        self.F2_Button3 = Button(self.GUI,text=" CLEAR ", font= ('Arial bold',15), bg = 'light pink', bd= 3)
        self.F2_Button3.place(x = 1180, y= 370 , width = 180, height = 50)
        self.F2_Button3.config(command=self.clear_fields)

        #update
        self.F2_Button4 = Button(self.GUI, text=" UPDATE ", font =('Arial bold',15), bg= 'plum1', bd =3 )
        self.F2_Button4.place(x = 799, y = 430, width = 270)
        self.F2_Button4.config(command=self.update_employee)

        #delete

        self.F2_Button5 = Button (self.GUI, text=" DELETE ", font=('Arial bold', 15), bg='RosyBrown1', bd = 3)
        self.F2_Button5.place(x = 1090, y = 430, width = 270)
        self.F2_Button5.config(command=self.delete_employee)
        # ==========================================================================================



        #Frame4 elements under =====================================================================
        Frame4 = Frame(self.GUI, bd=5, relief=RIDGE, bg='white')
        Frame4.place(x=770, y=500, width=610, height=200)
        F4_Label = Label(self.GUI, text="PAY SLIP", font=('Arial bold', 20), bg='grey')
        F4_Label.place(x=773, y=500, width=606, height=50)
        self.F4_textbox = Text(self.GUI, font=('Arial', 15), bg='old lace', bd=3)
        self.F4_textbox.place(x=773, y=550, width=606, height=150)


        #===========================================================================================