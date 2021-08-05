def num_full(centers):
    """
    Takes the dictionary of centers and number of trainees and returns the number of full centers
    :param centers:
    :return:
    """
    full = 0
    num = centers.values()
    # Creates month list of trainees per centers
    for i in num:
    # iterates through the list
        if i == 100:
            full += 1
    return full
