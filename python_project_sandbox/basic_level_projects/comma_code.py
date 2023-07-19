# practice code for Comma Code game
'''
Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.
'''

spam = ['apples','bananas','tofu','cats']

#test code so far
#for x in spam:
#    print(x)

def transform_list(list):
    string1 = ''
    if len(list) == 0:
        print("empty")
    for x in list:
        string1 += str(x) +", "
    return string1

print(transform_list([1,2,3,4,"five"]))

    
