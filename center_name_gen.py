def name_generator(list_of_centers, num_centers):
    for i in range(num_centers):
        if list_of_centers == {}:
            list_of_centers.update({"Center 1": 0})
        else:
            x = len(list_of_centers) + 1
            center_name = "Center " + str(x)
            list_of_centers.update({center_name: 0})
    return list_of_centers


