#!/bin/python3

import math
import os
import random
import re
import sys



import operator
#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def findSubstring(s, k):
    if not s:
        return 
    
    if k == 0: 
        return('Not found!')   
   
        
    l = []
    vowels = 0
    for x in range(0, len(s)): 
        if s[x] == 'a' or s[x] == 'e' or s[x] == 'i' or s[x] == 'o' or s[x] == 'u': 
            l.append(1)
            vowels += 1 
        else: 
            l.append(0)
            
    if vowels == 0: 
        return('Not found!')
    
    # make a new dict
    substrings = {}
    
    # look at all sections of k length within s 
    for i in range(0, len(s) - k + 1): 
        # count number of vowels 
        substrings[s[i:i+k]] = sum(l[i:i+k])
    
    print(substrings)
    return max(substrings.items(), key = operator.itemgetter(1))[0]

    

if __name__ == '__main__':