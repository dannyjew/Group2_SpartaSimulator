# we are trying to get an input from the user - we need the number of months and it has to be an integer
def my_input(prompt=''):
    try:
        return input(prompt)
    except NameError:
        return input(prompt)


def time_frame():
    try: # this is going to ask for the month to be inputted - but we will convert it to integer immediately
        user_month_input = int(my_input("How long would you like to run the simulation for? Enter in number (1, 2,.. etc) of months: "))
    except ValueError: # we know people do not do as asked so this deals with error incase an integer is not input
        print("Please input a number as a digit (eg. 10)")
        user_month_input = int(
                my_input("How long would you like to run the stimulation for? Enter in number (1, 2,.. etc) of months: "))

    return user_month_input # this just gives us the month as an integer that we can then use for the rest of our work



