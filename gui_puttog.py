import tkinter
from tkinter import *
import tkinter.font as tkfont
import webbrowser
root = Tk()
root.title('Sparta Simulation')  # Sets the window title
root.iconphoto(True, tkinter.PhotoImage(file="sparta_logo.png"))  # Adds the favicon logo to the window
window_height = 1024
window_width = 1280
window_geometry = str(window_width) + "x" + str(window_height)  # Setting the height and width to use for the window
root.geometry(window_geometry)  # Applying the height and width

# Define font styles
fontStyle = tkfont.Font(family="Raleway", size=10)
titleStyle = tkfont.Font(family="Raleway", size=50)

# Images used within application
submit_button = PhotoImage(file="SubmitButton.png")
centre_label = PhotoImage(file="CentreLabel.png")
month_label = PhotoImage(file="MonthLabel.png")
SG_logo = PhotoImage(file="SGLogo.png")

# Creating the primary frame - where everything will be in
main_frame = Frame(root, highlightthickness=10, highlightcolor="#E23761", highlightbackground="#E23761",
                   width=window_width, height=window_height, bg="white")
main_frame.pack(fill="both", expand=True)

# Creating the secondary frames - which will separate the user input boxes, labels and submit button from the logo
# first frame is the input frame for the input boxes, labels and submit button frames
input_frame = Frame(main_frame, width=window_width, height=window_height-100, bg="White")
input_frame.pack(side=BOTTOM, expand=True, fill="both")

# second frame is where the logo will be
menu_frame = Frame(main_frame, width=window_width, height=50, bg="#00181A")
menu_frame.pack(side=TOP, expand=True, fill="both")
# Function to open a web browser


def hyper(url):
    webbrowser.open_new(url)


# Adding the logo and menu label
logo1 = Label(menu_frame, image=SG_logo, fg="White", bg="#00181A", cursor="hand2")
# placing the logo within thi grid
logo1.grid(row=0, column=0, padx=75, pady=100)
logo1.grid_propagate(False)  # Ensures that the frame doesn't fit only around the logo
# Binds the logo to a button that calls upon the function above to open a browser and the link specified below
logo1.bind("<Button-1>", lambda e: hyper("https://www.spartaglobal.com"))

title_label = Label(menu_frame, text="Sparta Simulation", fg="White", bg="#00181A", font=titleStyle)
title_label.grid(row=0, column=1, padx=100)
title_label.grid_propagate(False)

# Creating the tertiary frames - which will separate the user inputs and labels from the submit button
# first frame is the entries frame for the user inputs and labels to go
entries_frame = Frame(input_frame, width=window_width, height=window_height, bg="White")
entries_frame.pack(side=TOP)
# second frame is the submit frame for the submit button to go
submit_frame = Frame(input_frame, width=window_width, height=window_height, bg="White")
submit_frame.pack(side=BOTTOM)

# Defining the labels
# this calls upon the label images that are referenced earlier
label1 = Label(entries_frame, image=centre_label, fg="Black", bg="White")
label2 = Label(entries_frame, image=month_label, fg="Black", bg="White")
# Place the labels in the grid
label1.grid(row=0, column=0, sticky=W, pady=102)
label2.grid(row=1, column=0, sticky=W, pady=102)

# Defining the user input boxes
# User input text boxes
centre_entry = Entry(entries_frame, width=40, font=fontStyle, bd=2)
centre_entry.grid(row=0, column=1, pady=2, ipady=10)
centre_entry.configure(highlightcolor="#E23761")

month_entry = Entry(entries_frame, width=40, font=fontStyle, bd=2)
month_entry.grid(row=1, column=1, pady=2, ipady=10)
month_entry.configure(highlightcolor="#E23761")

# Defining a function to be called once the submit button is pressed


def submit():
    result = []
    center_num = centre_entry.get()
    user_month_input = month_entry.get()
    result.append(center_num)
    result.append(user_month_input)
    centre_entry.delete(0, "end")
    user_month_input.delete(0, "end")
    return result


# Creating the submit button
button1 = Button(submit_frame, image=submit_button, command=submit, bg="White", fg="white", border=0)
# Placing the button into the frame
button1.pack()
root.mainloop()
