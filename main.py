from tkinter import *
from functions import Payroll


if __name__ == '__main__':
    GUI = Tk()
    GUI.geometry('1400x800')
    GUI.title("ACC SECURITY")
    mywin = Payroll(GUI)

    GUI.mainloop()