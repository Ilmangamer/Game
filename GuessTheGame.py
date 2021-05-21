import sys 

try:
    import random
except ImportError as Ie: # if random fails to load, it will show: 
    print("could not load random") # this


# Making variables

number = 37
last_option = 150
running = True
count = 0
def input_integer(number): # making a func which has number as parameter
    while True:
        try:
            guess = int(input("Enter an integer: ")) # gettting input
            adjusted_integer(guess, number) # Adjusting the input, if a certain condition is met
            return guess # returning the value to function
        except ValueError as ve: # raising exception if input is not integer
            print("Only integers please, (Error is:", str(ve), "Please try again")

def adjusted_integer(guess, number): # adjusting the output
    if guess < number:
        print("It is a little higher than that")

    elif guess >= last_option:
        print("Max number" "\ninvalid option")

    if guess > number and  guess < last_option:
         print("No, it is lower than that")

#adjusted_integer(number)
while running: # bool ---> True
    guess = input_integer(37) # Assignment to  variable guess
    if guess == number: # comparing it to number
        print(guess) # to se it's value
        print(f"This is for : {​​​​​​​guess}​​​​​​​") # formating guess to see it in the output, without writing it as a string
        print("You have guessed the number")
        print("Game over")
        exit("You Won!") # Exiting the program when the numbar has been guessed
