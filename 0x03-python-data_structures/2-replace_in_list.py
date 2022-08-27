#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx <0:
        return (my_list)
    elif idx == 1:
        my_list[0]=element;
        return my_list
    elif idx > len(my_list):
        return (my_list)
    for i in range(len(my_list)):
        if i == idx -1:
            my_list[i]=element;
    return my_list
