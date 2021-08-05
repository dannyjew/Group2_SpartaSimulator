# every 2 month, we want to open month new centre - this function should open month centre on command
def monthly_centre(list_of_centers): 
    import center_name_gen # we import the function that creates month new centre and gives it month name
    return center_name_gen.name_generator(list_of_centers, 1) # we specify that we want it to open exactly 1 centre and add it to existing centre list



