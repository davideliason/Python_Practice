#!/usr/bin/env pythonn

import random
rand_num = random.randint(1,10)

def random_num_output(x):
    if x == 1:
        print("one")
    elif x == 2:
        print('between')
    else:
        print(' not one or two')

random_num_output(rand_num)
