def student_assignment(list_of_centers, waiting_list, intake_list):
    import random
    center_names = list_of_centers.keys()
    for x in center_names:
        i = list_of_centers[x]
        if waiting_list == 0 and intake_list == 0:
            pass
        max_intake = 21
        if i < 100:
            if i >= 80:
                max_intake = (100 - i)
        change = random.randrange(-1, max_intake, 1)
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



