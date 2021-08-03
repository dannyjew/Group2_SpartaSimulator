# Things to do in the meeting:

user_month_input = input("How long would you like to run the stimulation for? Enter in number (1, 2,.. etc) of months: ")

def time_frame(month):
    while month.isdigit() != True:
        print("Please input a number as a digit (eg. 10)")
        user_month_input = input(
            "How long would you like to run the stimulation for? Enter in number (1, 2,.. etc) of months: ")
        month = user_month_input
    else:
        print(f"This stimulation will show you what Sparta will look like in {month} months.")


time_frame(user_month_input)