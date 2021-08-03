def time_frame():
    try:
        user_month_input = int(input("How long would you like to run the stimulation for? Enter in number (1, 2,.. etc) of months: "))
    except ValueError:
        print("Please input a number as a digit (eg. 10)")
        user_month_input = int(
                input("How long would you like to run the stimulation for? Enter in number (1, 2,.. etc) of months: "))

    return user_month_input
    print(f"This stimulation will show you what Sparta will look like in {time_frame()} months.")


