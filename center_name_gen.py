def name_generator(dict_of_centers, num_centers):
    """
    Appends empty centers to the original list
    :param dict_of_centers: dictionary containing centers and trainees
    :param num_centers: number of centers to be created
    :return:
    """
    for i in range(num_centers):
        x = len(dict_of_centers) + 1
        center_name = "Center " + str(x)
        dict_of_centers.update({center_name: 0})
    return dict_of_centers


