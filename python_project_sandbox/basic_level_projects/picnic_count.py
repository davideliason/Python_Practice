#!/usr/bin/env python3

# This program uses a dictionary, containing other dictionaries, to calculate the total number of an item being brought by all the guests.

allGuest = {'Alice': {'apples': 5, 'pretzels': 12}, 
           'Bob': {'ham sandwiches': 3, 'apples': 2},
           'Carol': {'cups': 3, 'apple pies':1}}

def getItem(dict, item):
    totalNumOfItem = 0 # sum of specific item by all persons
    for k, v in dict.items():
        totalNumOfItem =totalNumOfItem + v.get(item, 0) # get method returns 0 if item does not exist as a key)
    return totalNumOfItem

print('Number of things being brought: ')
print(' - Apples       ' + str(getItem(allGuest, 'apples')))

