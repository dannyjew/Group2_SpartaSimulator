# from tkinter import *
#
# # create root widget - this creates basic window
# root = Tk()
#
# # to create everything - you have to create it and define it (tell which widget it is)
# # Creating a label widget
# myLabel = Label(root, text="Hellow World!")
# # have to pack this label into the root - so show it on the screen
# myLabel.pack()
#
# # have to create an event loop - that how long the loop is open
# root.mainloop()  # this is main loop of the program
#
# # now get into this directory in terminal and type : python <file name>
# # when you close window, it closes the main loop


# ***** TUT 2 *****
# we do not have a lot of control above so will be using a grid system
# imagine the grids as columns and rows

# from tkinter import *
# root = Tk()
# myLabel1 = Label(root, text="Sparta Simulation")
# myLabel2 = Label(root, text="How long would you like to run your simulation?")
# # no longer need a pack - use grid to put on screen
# myLabel1.grid(row = 1, column = 0)
# myLabel2.grid(row = 2, column = 0)
# # these are relative to each other - so every widget in the grid is
# root.mainloop()

# now get into this directory in terminal and type : python <file name>
# when you close window, it closes the main loop


# try and attach input and function

import Tkinter as tk


# def TestMath():
#     global result # to return calculation
#
#     result = int(entry.get())
#     result += 4
#
#     print result
#
# result = 0

# def month():
#     global value
#     num = int(entry.get())
#     value += num
#     print(value)
#     return value

def time_frame():
    #try:
    user_month_input = int(entry.get())
    # except ValueError:
    #     print("Please input a number as a digit (eg. 10)")
    #     user_month_input = int(
    #             input("How long would you like to run the stimulation for? Enter in number (1, 2,.. etc) of months: "))
    print(user_month_input)
    return user_month_input

def centre_input():
    centre_num = int(entry1.get())
    print(centre_num)
    return centre_num

# def centre_input():
#     import center_name_gen
#     correct_input = False
#     while not correct_input:
#         center_num = input("Please state the number of already existing centers ")
#         try:
#             center_num = int(center_num)
#             correct_input = True
#             return center_name_gen.name_generator({}, center_num)
#         except:
#             print("Please input an integer value for the total number of existing centres ")


root = tk.Tk()

entry = tk.Entry(root)
entry.pack()
entry.insert(0, "Enter duration of simulation in months (eg. 7): ")

entry1 = tk.Entry(root)
entry1.pack()
entry1.insert(0, "Enter the existing number of centres: ")


button = tk.Button(root, text="Run Simulation", command=time_frame)
#button = tk.Button(root, text="Centre", command=centre_input)
button.pack()



root.mainloop()

