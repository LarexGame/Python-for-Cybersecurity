# third tkinter script
# Get people in space
# Create by Garcia 12/01

# Import tkinter
import requests
import tkinter

# Functions
def people_in_space():
    url = "http://api.open-notify.org/astros.json"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    # Convert to Python object
    astros = response.json()
    num_people = astros['number']
    lbl_main.configure(
        text = f"There are currently {num_people} people in space"
    )

# Create the GUI main window
root = tkinter.Tk()

# Add widgets
lbl_main = tkinter.Label(
    root,
    text = "People in Space",
    font = ("Arial Bold", 50)
)

btn_update = tkinter.Button(
    root,
    text = "Click to update",
    command = people_in_space
)
btn_update.pack()
lbl_main.pack()
# Enter the main event loop
root.mainloop()