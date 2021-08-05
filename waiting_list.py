# so to do this you basically want to do:
# num of trainees from random gen - num of trainees being accepted in centre

wait_list = []

def wl():
    import trainee_generation
    x = 15 # stand in until Conner makes trainee being taken in
    return trainee_generation.trainee_gen() - x

print(wl())

# test = can append to list if required