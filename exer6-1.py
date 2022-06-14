def multiplicationTable(arg1, arg2=0):
    if arg2 == 0:
        arg2 = arg1

    for num_1 in range(1, arg1 + 1):
        new_list = []
        for num_2 in range(1, arg2 + 1):
            new_list.append(num_1 * num_2)
        print(new_list)


multiplicationTable(4, 2)
