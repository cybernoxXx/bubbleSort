def bubbleSort(my_list):
    # Cycling to all the list
    for i in range(0, len(my_list)-1):
        # Cycling to all the list starting after i
        for j in range(i+1, len(my_list)):
            # Swapping elements
            if my_list[i] > my_list[j]:
                tmp = my_list[j]
                my_list[j] = my_list[i]
                my_list[i] = tmp
    return my_list


assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]
