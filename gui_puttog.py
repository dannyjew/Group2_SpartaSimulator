import tkinter
from tkinter import *
import tkinter.font as tkfont
import webbrowser
from date_input import date
# from month_input import time_frame
# from input_existent_centres import centre_input
from opening_new_centre import monthly_centre
from trainee_generation import trainee_gen
from stu_assignment import student_assignment
from num_full_centers import num_full
from plotting import time_centers, time_trainees,  show
from center_name_gen import name_generator
#   Variables
month = 0
month_tick = 0
centers = {}
wait_list = 0

root = Tk()
root.title('Sparta Simulation')  # Sets the window title
root.iconphoto(True, tkinter.PhotoImage(file="sparta_logo.png"))  # Adds the favicon logo to the window
window_height = 1024
window_width = 1280
window_geometry = str(window_width) + "x" + str(window_height)  # Setting the height and width to use for the window
root.geometry(window_geometry)  # Applying the height and width

# Define font styles
fontStyle = tkfont.Font(family="Raleway", size=10)
outputStyle = tkfont.Font(family="Raleway", size=12)
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

# Function to open month web browser


def hyper(url):
    webbrowser.open_new(url)


# Defining month function to be called once the submit button is pressed


def submit():
    global centers
    global month
    global month_tick
    global wait_list
    centers = name_generator(centers, int(centre_entry.get()))
    month = int(month_entry.get())
    end_date = date(month)
    month_c = [0, ]
    centers_month = [len(centers, )]
    trainees_month = [0, ]
    months = [0, ]
    print(f"This simulation will show you what Sparta will look like in {month} months.")
    # this is to confirm the month or the user can re-start

    while date(month_tick) != end_date:
        month_tick += 1
        months.append(months[-1] + 1)
        if month_tick % 2 == 0 and month_tick != 0:
            month_c.append(month_c[-1] + 2)
            centers_month.append(centers_month[-1] + 1)
            # generates new centre every two month
            centers = monthly_centre(centers)
        intake = trainee_gen()
        trainees_month.append(trainees_month[-1] + intake)
        centers, wait_list = student_assignment(centers, wait_list, intake)

    time_centers(month_c, centers_month, months)
    time_trainees(months, trainees_month)

    output_x = f"There are {len(centers)} center(s), training {sum(centers.values())} trainees, " \
               f"{num_full(centers)} center(s) is/are full, and there are {wait_list} on the wait list."

    output.config(text=output_x)
    show()
    return


# Adding the logo and menu label
logo1 = Label(menu_frame, image=SG_logo, fg="White", bg="#00181A", cursor="hand2")
# placing the logo within thi grid
logo1.grid(row=0, column=0, padx=75, pady=100)
logo1.grid_propagate(False)  # Ensures that the frame doesn't fit only around the logo
# Binds the logo to month button that calls upon the function above to open month browser and the link specified below
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


# Creating the submit button and output label
button1 = Button(submit_frame, image=submit_button, command=submit, bg="White", fg="white", border=0)
output = Label(submit_frame, text="", bg="White", fg="Black", font=outputStyle)
# Placing the button and label into the frame
button1.grid(row=0, column=0, sticky=W)
output.grid(row=0, column=1)


root.mainloop()
