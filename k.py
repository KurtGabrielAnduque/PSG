from tkinter import *

# Colors
top_bar_color = "#2196f3"
logout_button_color = "#f44336"
left_panel_color = "#f2f2f2"
button_colors = {
    "My Account": "#4caf50",
    "Shop Now": "#03a9f4",
    "My Cart": "#ff9800",
    "Checkout": "#0288d1",
}

# Main window
buyer_main = Tk()
buyer_main.title("Welcome Seller user1")
buyer_main.geometry("800x600")
buyer_main.resizable(False, False)

# Top Bar
top_bar = Frame(buyer_main, bg=top_bar_color, height=60)
top_bar.pack(fill="x")

app_title = Label(top_bar, text="DA GAE SHOP", font=("Helvetica", 20, "bold"), bg=top_bar_color, fg="white")
app_title.pack(side="left", padx=20, pady=10)

logout_btn = Button(top_bar, text="Log-out", bg=logout_button_color, fg="white", font=("Helvetica", 12, "bold"))
logout_btn.pack(side="right", padx=20, pady=10)

# Main Frame
main_frame = Frame(buyer_main)
main_frame.pack(fill="both", expand=True)

# Left Panel
left_panel = Frame(main_frame, bg=left_panel_color, width=400)
left_panel.pack(side="left", fill="y")

welcome_label = Label(left_panel, text="Welcome, user1!", bg=left_panel_color, font=("Helvetica", 16))
welcome_label.pack(pady=30, padx=20)

instruction_label = Label(left_panel, text="Select an option from the menu to get started.",
                          bg=left_panel_color, font=("Helvetica", 12), wraplength=300)
instruction_label.pack(pady=10, padx=20)

# Right Panel
right_panel = Frame(main_frame, bg="#f8f8ff")
right_panel.pack(side="right", fill="both", expand=True)

for text, color in button_colors.items():
    btn = Button(right_panel, text=text, bg=color, fg="white", font=("Helvetica", 15, "bold"), width=25, height=2)
    btn.pack(pady=20)

buyer_main.mainloop()