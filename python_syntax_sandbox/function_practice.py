#!/usr/bin/env python3

import random
rand_num = random.randint(1,10)

def random_num_output(x):
    if x == 1:
        return("one")
    elif x == 2:
        return('between')
    else:
        return(' not one or two')

result = random_num_output(rand_num)
print(result)
