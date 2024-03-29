'''
Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.

Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)

Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.
'''
print('testing 123')

# main
def collatz(number):
    if number % 2 == 0:  # check even 
        print(number // 2)  # floor division 
        return number // 2
    else:
        print(3 * number + 1)
        return(3 * number + 1) 

# loop

#input value
try:
    input_value = int(input())
except ValueError:
    print('only number input')

#prep loop
int_val = collatz(input_value)
while int_val != 1:
    int_val = collatz(int_val)




