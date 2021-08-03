# here we are going to create a random number of students between 20 - 30 for each month
def trainee_gen():
    import random # we need function in this library
    number = random.randint(20, 30) # this is inclusive for 20 and 30
    return number # this will give us this random number to use for further work

