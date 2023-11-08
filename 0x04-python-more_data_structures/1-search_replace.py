#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i_list = list(my_list)
    for x in range(len(i_list)):
        if i_list[x] == search:
            i_list[x] = replace
    return i_list
