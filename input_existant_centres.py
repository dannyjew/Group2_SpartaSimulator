def centre_input():
    """
    Requests an input of number of initial centers
    :return: a dictionary of centers with 0 trainees
    """
    import center_name_gen
    correct_input = False
    while not correct_input:
        center_num = input("Please state the number of already existing centers ")
        try:
            center_num = int(center_num)
            correct_input = True
            return center_name_gen.name_generator({}, center_num)
        except:
            print("Please input an integer value for the total number of existing centres ")

