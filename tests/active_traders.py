#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'mostActive' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY customers as parameter.
#

def mostActive(customers):
    # create a dictionary where value is number of occurences of each customer 
    cust = {} 
    n = len(customers)
    for i in range(0, n):
        if customers[i] in cust: 
            cust[customers[i]] = cust[customers[i]] + 1
        else: 
            cust[customers[i]] = 1
        
    # create a sorted list with only customers of top 5% trades 
    top_l = list()
    for key in cust: 
        if cust[key] / n >= 0.05: 
            top_l.append(key)
            
    return sorted(top_l)

if __name__ == '__main__':