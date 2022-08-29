#!/usr/bin/python3
def no_c(my_string):
    strList=list()
    sr = ""
    for i in range(len(my_string)):
        strList.append(my_string[i])
    for i in range(len(strList)):
        if strList[i] != 'C' and strList[i] != 'c':
            sr+=strList[i];
    return (sr)
