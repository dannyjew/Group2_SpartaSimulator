# every 2 months, we want to open a new centre - this function should open a centre on command
def monthly_centre(list_of_centers): 
    import center_name_gen # we import the function that creates a new centre and gives it a name
    return center_name_gen.name_generator(list_of_centers, 1) # we specify that we want it to open exactly 1 centre and add it to existing centre list


