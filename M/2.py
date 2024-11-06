from tkinter import *
from tkinter import ttk


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Special Midterm Exam in OOP")
        self.geometry("400x300")
        self.initUI()

    def initUI(self):
        self.button = Button(self, text="Click to Change Color", command=self.change_color)
        self.button.pack(pady=110)

    def change_color(self):
        self.button.config(bg="yellow")


if __name__ == '__main__':
    app = App()
    app.mainloop()