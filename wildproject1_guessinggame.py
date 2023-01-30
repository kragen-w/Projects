# Docstring required at the beginning of every program:
"""
    This program allows the user to play the game "Pico Fermi Bagels" and will end once the user has won the game.
    The object of the game is to guess a three digit number. The computer will say Pico if one of your guessed numbers
    is in the target number. Fermi will display if one of your numbers is in the correct order. Bagels will show when
    none of your guessed numbers are in the target number.
    Filename: wildproject1_guessinggame.py
    Author: Kragen Wild
    Date: 1-9-23
    Course: Programming II
    Assignment: Project 1 - A Guessing Game (called Pico Fermi Bagels)
    Collaborators: nada
    Internet Source: nada
"""





from random import randint
def number_generator()->int:

    """
    This function creates a list of 3 random numbers 1-9 which don't repeat.
    parameters: None
    return: A list of 3 random numbers 1-9 which don't repeat.
    """
    #a list is created with the only number being a random 1-9
    lizt = [randint(1,9)]
    #this code will happen twice
    for i in range(2):
        #a new number is generated between 1-9
        targetnum = randint(1,9)
        #while this new number is the same as either the first or second number in the list, a new one will be made
        while targetnum == lizt[i] or targetnum == lizt[i-1]:
            #a new number is generated
            targetnum = randint(1,9)
        #the number that is unique is appended to the end of the list
        lizt.append(targetnum)
    #the list is returned
    return lizt


#a random 3 digit number is generated, in the form of a list
randomnum = (number_generator())
#this variable will track when the user gets 3 "fermi"s
correct = 0
#this variable will track how many tries it takes to guess correctly
guesses = 0
#this while loop will continue while the number of fermi's is not 3, which would break the loop and end the game
while correct != 3:
    #this takes the users input and determines if any of their numbers repeat
    #if so, the while loop continues and the user has to enter another guess
    userguess = input("What is your guess? ")
    while userguess[0] == userguess[1] or userguess[1] == userguess[2] or userguess[2] == userguess[0]:
        print("Invalid: no duplicate numbers.")
        userguess = input("What is your guess? ")


    #a new list is created
    userlist = []
    #this code happens three times
    for i in range(3):
        #the number in the user guess at index i is appended to the list
        userlist.append(int(userguess[i]))

    #"correct" is reset to 0
    correct = 0
    #these three variables represent the number of fermis and picos in the users guess
    #they both start at 0
    f = 0
    p = 0
    #this code repeats 3 times
    for i in range(3):
        #this if statement will run if the user guess and the target number have the same number at the same index,
        #incrimenting the number of fermi's and the correct variable by one
        if randomnum[i] == userlist[i]:
            f += 1
            correct += 1
        #this if statement will run if the user guess at index i is in the target number, and the number of picos goes
        # up by one
        elif randomnum.count(userlist[i]) == 1:
            p += 1
    #for however many fermis there are, fermi will be printed
    for i in range(f):
        print("Fermi! " , end="")
    #for however many picos there are, pico will be printed
    for i in range(p):
        print("Pico! " , end="")
    #if there are no fermis or picos, then that means that none of the numbers in the user guess are in the target
    #number, so bagels is printed
    if p == 0 and f == 0:
        print("Bagels! ", end="")
    #the number of guesses goes up by one
    guesses += 1

#this will print once the while loop is broken, meaning that the user guessed correctly, and the game is over
#the number of guesses is displayed too
print(f"that took you {guesses} tries.")

