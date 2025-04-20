from tkinter import *
from tkinter import ttk




main = Tk()
main.geometry('800x500')
main.title('treeeview partis')


label = Label(main, text = "SAMPLE TREE", font=('Arial',20,'bold'))
label.place(x = 480, y = 20)
puno = ttk.Treeview(main,)
puno.place(x = 380 ,y= 75, width = 400, height = 400)


puno['columns'] = ('Product_ID','Product_Name','Stock')
puno.column("#0",width=40, minwidth=50)
puno.column("Product_ID",anchor=W, width = 120,minwidth=120)
puno.column("Product_Name",anchor=W, width = 120,minwidth=120)
puno.column("Stock",anchor=W, width = 120,minwidth=120)


puno.heading("#0",text="box")
puno.heading("Product_ID",text = 'Product_ID')
puno.heading("Product_Name",text = 'Product_Name')
puno.heading("Stock",text = "Stocks")

puno.insert('', 'end', text='1', values=('P001', 'Milk', '50'))
puno.insert('', 'end', text='2', values=('P002', 'Bread', '120'))
puno.insert('', 'end', text='3', values=('P003', 'Eggs', '30'))

main.mainloop()