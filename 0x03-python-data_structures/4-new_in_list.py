#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list
    for i in range(len(my_list)):
        if idx < 0:
            return (my_list)
        elif idx == 1:
            new_list[0] = element
            return (new_list)
        elif idx > len(my_list):
            return (my_list)
        for i in range(len(my_list)):
            if i == idx:
                new_list[i] = element
            return (new_list)
