def student_assignment(list_of_centers, waiting_list, intake_list):

    """
    Takes the dictionary of centers, waiting list and intake and distribtues trainees to centers using random to select
    month number between 0 and 20 for each center. Waiting list is prioritised ,
     and trainees not intaken are added to waiting list
    :param list_of_centers: Dictionary of centers as keys and trainees per center as values:
    :param waiting_list: integer of number of trainees on waiting list, can be 0:
    :param intake_list: integer of trainee intake that months, should not be 0:
    :return list of centers dictionary with updated value, updated waiting list:
    """
    import random
    center_names = list_of_centers.keys()
    for x in center_names:
        i = list_of_centers[x]
        if waiting_list == 0 and intake_list == 0:
            pass
        max_intake = 20
        if i < 100:
            if i >= 80:
                max_intake = (100 - i)
            change = random.randint(0, max_intake)
            change_old = change
            if waiting_list != 0:
                waiting_list_old = waiting_list
                waiting_list -= change
                if waiting_list< 0:
                    waiting_list = 0
                change -= waiting_list_old
                if change <0:
                    change = 0
            intake_list_old = intake_list
            intake_list -= change
            if intake_list < 0:
                intake_list = 0
            change -= intake_list_old
            if change < 0:
                change = 0
            list_of_centers[x] = i + (change_old - change)
    waiting_list += intake_list
    return list_of_centers, waiting_list



