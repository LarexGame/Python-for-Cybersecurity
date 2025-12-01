# First tkinter script
# Create by Garcia 12/01

# Import tkinter
import tkinter

def button_clicked():
    tkinter.Label(
        root,
        text = "Button was Clicked"
).pack()
    # update my_label
    my_label.configure(
        text = "Python is AWESOME!!",
        font = ("Courier", 25),
        fg = "lightyellow",
        bg = "darkred"
    )

# Create the GUI main window
root = tkinter.Tk()

# Add widgets
my_label = tkinter.Label(
    root, 
    text = "Hello World",
    font = ("Arial Bold", 50)
    )
my_label.pack()

my_button = tkinter.Button(
    root,
    text = "Click ME",
    command = button_clicked
    )
my_button.pack()

# Enter the main event loop
root.mainloop()
