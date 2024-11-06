import tkinter as tk

class FullNameDisplayApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Midterm in OOP")
        self.geometry("450x250")

        self.label = tk.Label(self, text="Enter your fullname:", fg="red")
        self.label.place(x=20, y=60)

        self.name_input = tk.Entry(self)
        self.name_input.place(x=240, y=60, width = 150, height = 25)

        self.button = tk.Button(self, text="Click to display your Fullname", command=self.display_name, fg="red")
        self.button.place(x=20, y=120)

        self.output = tk.Entry(self, state='readonly')
        self.output.place(x=240, y=120, width = 150, height = 25)

    def display_name(self):
        name = self.name_input.get()
        self.output.config(state='normal')
        self.output.delete(0, tk.END)
        self.output.insert(0, name)
        self.output.config(state='readonly')

if __name__ == "__main__":
    app = FullNameDisplayApp()
    app.mainloop()