# ZippityDooDah
## A Fun Guessing Game
## May 10, 2023

import random
NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
   print("ZippityDooDah: a guessing game. You get 10 guesses. Zippity: number is right but in wrong spot. Doo is right number in right spot. Dah is not right number or right spot")

   while True:
         secretNum = getSecretNum()
         print("I have a number")
         print(' You have {} guesses left!'.format(MAX_GUESSES))
main()  
