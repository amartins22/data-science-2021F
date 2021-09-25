import random
    
#guess letter
def guess():
    g = input("Guess Letter: ")
    return g

        
#check letter and change the word
def check(word,letter,displayWord):
    isCorrectLetter = False
    for i in range(len(word)):
        x = word[i]
        if letter.isalpha() == False:
            print("not a valid response")
        elif x == letter :
            displayWord[i] = x
            isCorrectLetter = True     
    note(letter,isCorrectLetter)
 
       
#print whether it is correct or not
def note(letter, isCorrectLetter):
    if isCorrectLetter == True:
        print("Yes, " + letter + " is in the word!")
    else:
        print("No, " + letter  + " is not in the word.")


#game setup
def gameSetup(word, displayWord):
    wordLength = len(word)
    titleMessage = """Welcome to Hangman. 
The secret word has """ + str(wordLength) + """ letters and the theme is colors.
"""
    print(titleMessage)
    print(word)    
    displayWord = ["*" for x in word]
    print(displayWord)

#tracking the letters that were guessed
def guessTracker(letter,numGuesses,alreadyGuessed):
    if letter not in alreadyGuessed:
        alreadyGuessed.append(letter)
        print("So far you have guessed " + str(alreadyGuessed))
    else:
            print("You have already guessed that letter")
            numGuesses = numGuesses + 1

def playGame():  
    #variables
    wordList = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black", "brown", "gray", "white"] 
    word = random.choice(wordList)
    alreadyGuessed = []
    numGuesses = 8
    displayWord = ["*" for x in word]
    gameOver = False

    gameSetup(word, displayWord)
     
    while gameOver == False:
        if "*" in displayWord:
            if numGuesses > 0 :    
                numGuesses = numGuesses - 1
                letter = guess()
                check(word,letter,displayWord)
                print(displayWord)
                guessTracker(letter, numGuesses, alreadyGuessed)
                print("You have " + str(numGuesses) + " guesses left.")
            else :
                gameOver = True
                print("You ran out of turns, you lose!")
        else:
            gameOver = True
            print("You've guessed the word!")
    
    
playGame()