
"""
    This program allows the user to play the game wordle. The player gets 6 tries to guess a random 5 letter word, 
    and if they get a letter in the correct spot, then that letter is printed green, if it's not in the right spot,
    then it's printed yellow, and if the letter is not in the word, it is printed as grey.
    Filename: wildproject2_awordgame_withcolor
    Author: Kragen Wild
    Date: 1-17-23
    Course: Programming II
    Assignment: Project 2 - A word game
    Collaborators: nada
    Internet Source: nada
"""


from random import randint


#this is a list of every letter in the alphabet, which i used to keep track of what letters were left in the guesses
alphabet = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


# print with yellow background
def print_yellow(s, end='\n'):
   print('\u001b[43;1m', end='')
   print(s, end=end)
   print('\033[0m', end='')

# print with grey background
def print_grey(s, end='\n'):
   print('\u001b[47;1m', end='')
   print(s, end=end)
   print('\033[0m', end='')

# print with green background
def print_green(s, end='\n'):
   print('\u001b[42;1m', end='')
   print(s, end=end)
   print('\033[0m', end='')


#creates an empty list to house all the words
words = []
#opens file containing all the words
with open(f"/Users/kragenwild/Downloads/Programming2023/projects/project2/usaWords.txt", "r") as a_file:
    #reads the file one line at a time, and repeats following code for each line
    for line in a_file:
        #creates a variable row, and saves the word in list form, split by line
        row = line.strip()
        #checks if the word is 5 letters long, if so, the word is appened to the list of possible words to be chosen 
        if len(row) == 5:
            words.append(row)


#instructions for non-color version of the game
print("Welcome to Wordle! You have six chances to guess the five-letter word.")


#chooses random word from list to be the word of interest that is to be guessed
word_of_interest = words[randint(0, len(words)-1)]
word_of_interest = "cares"

#keeps track of the guesses
guesses = 0

#keeps track of past guesses
guess_list = []
#keeps track of past results (if the word was a g,b, or y.)
results_list = []
#these two variables, when flipped, will end the game
winner = False
looser = False
#this while loop will run as long as the game is going
while not winner and not looser:
    #takes the user guess
    guess = input("What is your guess? ")

    #will repeatedly ask for guess until it is 5 letters long and in the list of words
    while guess not in words or len(guess) != 5:
        guess = input("Invalid Word.\nWhat is your guess? ")
    #sets a blank string as the result. The result is what keeps track of if each letter is in the word or in the correct spot
    results = ""

    #this word of interest list is created to store each letter of the word as a piece of the list
    woi_list = []
    for letter in word_of_interest:
        woi_list.append(letter)

    #this will repeat 5 times
    for i in range(5):
        #if the letter of the guess is in the same index as the word of interest, then this code runs, appends a G to the "results" variable,
        #and removes that letter from the word of interest list
        if word_of_interest[i] == guess[i]:
            # print("G",end="")
            results += "G"
            woi_list.pop(woi_list.index(guess[i]))

        #if the letter of the guess is inside of the list that holds all the letters of the word of interest, then a Y is appened to results
        # and that letter is removed from the woi list 
        elif guess[i] in woi_list:
            # print("Y",end="")
            results += "Y"
            woi_list.pop(woi_list.index(guess[i]))

        #this code runs if the letter is not in the word of interest, so that letter is removed from the alphabet as it is no longer a 
        # potential word 
        else:
            if guess[i] in alphabet:
                alphabet.pop(alphabet.index(guess[i]))
            # print("B",end="")
            results += "B"

    #the result code is appended to the list of results
    results_list.append(results)
    #the guess is appeneded to the list of results
    guess_list.append(guess)
    #guesses goes up by one
    guesses += 1


    #this code will run for however many guesses there are
    for j in range(guesses):
        #this code will for each guess, transversing each letter in the result
        for k in range(5):
            #if the letter looked at is a G, then the letter is in the right spot, and so the letter is printed green
            if results_list[j][k] == "G":
                print_green(f" {guess_list[j][k]} ", end='')
            #if the letter looked at is a Y, then the letter is in the word, and so the letter is printed yellow
            elif results_list[j][k] == "Y":
                print_yellow(f" {guess_list[j][k]} ", end='')
            #if the letter looked at is not a G or Y, then the letter is not in the word, and so the letter is printed grey
            else:
                print_grey(f" {guess_list[j][k]} ", end='')
        print("")
    print("")
    #this prints to the user the remaining possible letters
    print(f"The remaining letters are {alphabet}.")
    #this checks if the final index of the result list shows that the guess had all letters in the correct spot, meaning the user won.
    if results_list[-1] == "GGGGG":
        winner = True
    #if this isnt the case and the guess gets to 6, then the player looses.
    elif guesses == 6:
        looser = True

#final message display
if winner:
    print(f"Congrats, you won! It took {guesses} guesses.")
if looser:
    print(f"You loose, the word was not guessed in 6 tries. The word was {word_of_interest}")