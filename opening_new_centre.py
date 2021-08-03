import centre_name_gen
import month_input

centres_open = {}

def monthly_centre():
    for m in range(month_input.month):
        return centre_name_gen.name_generator(centres_open, 1) # need to add list name

monthly_centre()
