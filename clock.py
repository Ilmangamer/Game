import tkinter as tk
from datetime import datetime, timedelta



# Get a clock in tkinter GUI
# Imports 
# Size and geometry
# create a label with font. Display it
# Create a function where you create strftime
# Configure that variable to your existing label
# tell it to display after 1000 ms, then show time




root = tk.Tk()
root.geometry("250x100")


def moving_time():
    now = datetime.now()
    a = (now.strftime("%H:%M:%S %p"))
    ab = (now + timedelta(seconds =+1)).strftime("%H:%M:%S %p")
    return ab

clock_label = tk.Label(root, text= moving_time(), font=("ds-digital", 80), background="black", foreground="green")
clock_label.pack(anchor="center")

root.configure(bg="black")


def update():
    clock_label['text'] = moving_time()
    root.after(1000, update)

update()

# tkinter way of updating variables
""""
clock_label["text"] = moving_time()
What it does is that it updates the text variable objec to what the moving_time function returns
"""
# normal way of updating variables
"""
my_obeject.my_value = new_value
"""
root.mainloop()


