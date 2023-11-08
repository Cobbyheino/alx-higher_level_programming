#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        return (sum(i * x for i, x in my_list) / sum(x for i, x in my_list))
