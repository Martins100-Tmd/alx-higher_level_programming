#!/usr/bin/python3
def no_c(my_string):
    strList=list()
    sr=''
    for i in range(len(my_string)):
        strList.append(my_string[i])
    if 'C' in strList:
        strList.remove('C')
    elif 'c' in strList:
        strList.remove('c')
    for i in range(len(strList)):
        sr += strList[i]
    return sr
