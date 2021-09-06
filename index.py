import os
guessesLeft = 11
guesses = ["this is a placeholder"]

clear = lambda: os.system('cls')

word = input("What's your sentence/word? ")
clear()
word = word.lower()
wordHidden = word.split(" ")
string = ""
count = -1

def hasObject(string, array):
    count = 0
    for i in array:
        count += 1
        if (string.lower() == i.lower()):
            return True
        elif (count == len(array)):
            return False


for i in wordHidden:
    count += 1
    if (count == 0):
        string = string + "_" * len(wordHidden[count])
    else:
        string = string + " " + "_" * len(wordHidden[count])
wordHidden = string
print(wordHidden)
win = False
while guessesLeft > 0 and win == False:
    guess = input("Guess a letter! ")
    if (len(guess) == 1 and not guess.isnumeric() and hasObject(guess, guesses) == False and not guess == " "):
        if (hasObject("this is a placeholder", guesses)):
            guesses[0] = guess
        else:
            guesses.append(guess)
        if (guess in word):
            count1 = -1
            for i in word:
                count1 += 1
                if (guess == i):
                    string = wordHidden
                    position = count1
                    new_character = guess

                    wordHidden = string[:position] + new_character + string[position+1:]
        else:
            guessesLeft -= 1
                    
        print(wordHidden)
        print(guesses)
        print("Guesses Remaining: " + str(guessesLeft))

        if (wordHidden.find("_") == -1):
            win = True
            print("You won!")
    else:
        print("Invalid Guess! Guess again!")
