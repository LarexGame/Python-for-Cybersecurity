import tkinter
from tkinter import messagebox

# Funtion
def login_clicked():
    username = entry_user.get()
    password = entry_pass.get()
    remember_me = keep_logged_in.get()
    message = f"Login details:\n"
    message += f"Username: '{username}'\n"
    message += f"Password: '{password}'\n"
    messagebox.showinfo("Title here", message) 
    if remember_me == 1:
        message += "Remember me: Checked"
    else:
        message += "Remember me: unchecked"
    

# Create main window
root = tkinter.Tk()
root.title("Example Login Form")
keep_logged_in = tkinter.IntVar()

# Create widget
lbl_user = tkinter.Label(root, text = "Username")
lbl_pass = tkinter.Label(root, text = "Password")
entry_user = tkinter.Entry(root)
entry_pass = tkinter.Entry(root, show = "$$$")
chk_loggedin = tkinter.Checkbutton(root, text = "Keep me logged", variable=keep_logged_in)
btn_login = tkinter.Button(root, text = "Login", command=login_clicked)

# Place Widgets
lbl_user.grid(row=0, column=0, columnspan=2)
entry_user.grid(row=0, column=2, columnspan=2)
lbl_pass.grid(row=1, column=0, columnspan=2)
entry_pass.grid(row=1, column=2, columnspan=2)
chk_loggedin.grid(row=2, column=1, columnspan=2)
btn_login.grid(row=2, column=3, columnspan=2)

# Mainloop
root.mainloop()