#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = []
    if my_list:
        for i in my_list:
            newlist.append(False if num % 2 else True)
        return newlist
