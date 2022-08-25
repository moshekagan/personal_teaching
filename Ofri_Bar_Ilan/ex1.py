def extend_list_x(list_x, list_y):
    new_list = []

    for i in list_y:
        new_list.append(i)

    for i in list_x:
        new_list.append(i)

    list_x = new_list
    return list_x
