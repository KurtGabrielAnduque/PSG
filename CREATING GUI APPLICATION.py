from tkinter import *

counter=  0
def cat_clicker():
        global counter

        counter += 1

        cat_clicked = f'MEOW {counter}'
        LABEL1.config(text = cat_clicked)



window = Tk()
window.title('TNGINA PANGILAN MO NA TO!!!')
window.geometry('1000x800')
icon = PhotoImage(file ='cat.png')
window.iconphoto(True,icon)
window.config(background='bisque')


Label1 = Label(window,text = 'HELLOW WORLD',font = ('Arial',20,'bold'),fg = 'black',bg = 'bisque',relief= GROOVE,bd = 10,padx= 40,pady= 40)
Label1.grid(row = 0, column = 0)

BUTTON = Button(window, text = 'Click me', command=cat_clicker)
BUTTON.config(font = ('Ink Free',40, 'bold'), bg = 'salmon', activebackground='bisque')
BUTTON.config(image = icon, compound= 'right')
BUTTON.grid(row = 0 , column = 1)


LABEL1 = Label(window, text = counter)
LABEL1.grid(row = 1, column  = 1)






window.mainloop()
