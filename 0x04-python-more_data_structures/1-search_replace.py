#!/usr/bin/python3
def search_replace(my_list, search, replace):
    listcopy = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            listcopy.append(replace)
        else:
            listcopy.append(my_list[i])
    return listcopy
