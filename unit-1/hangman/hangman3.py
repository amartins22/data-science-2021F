import random
    
#guess letter
def guess():
    g = input("Guess Letter: ")
    return g
        
#check letter and change the word
def check(word,letter,displayWord,isAlphabet):
    isCorrectLetter = False
    for i in range(len(word)):
        x = word[i]
        if letter.isalpha() == False:
            isAlphabet = False  
        elif x == letter :
            displayWord[i] = x
            isCorrectLetter = True    
    note(letter,isCorrectLetter,isAlphabet)
       
#print whether it is correct or not
def note(letter, isCorrectLetter,isAlphabet):
    if isAlphabet == False:
        print(letter + " is not a valid response.")
    elif isCorrectLetter == True:
        print("""
Yes, """ + letter + """ is in the word!""")
    else:
        print("""
No, """ + letter  + """ is not in the word.""")

#make the displayed word a string and not a list
def displayString(displayWord):
    displayString = ""
    for x in displayWord:
        displayString += x 
    return displayString

#game setup
def gameSetup(word,displayWord,string):
    wordLength = len(word)
    titleMessage = """Welcome to Hangman. 
The secret word has """ + str(wordLength) + """ letters and the theme is colors.
"""
    print(titleMessage)
    print(word)    
    print(string)

#tracking the letters that were guessed
def guessTracker(letter,numGuesses,alreadyGuessed,isAlphabet):
    if letter not in alreadyGuessed and isAlphabet == True:
        alreadyGuessed.append(letter)
        print("""So far you have guessed: 
""" + str(alreadyGuessed))
    else:
            print("You have already guessed that letter")
            numGuesses = increaseNumGuesses(numGuesses)

def increaseNumGuesses(numGuesses):
    numGuesses = numGuesses + 1
    return numGuesses
    
def playGame():  
    #variables
    wordList = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black", "brown", "gray", "white"] 
    word = random.choice(wordList)
    alreadyGuessed = []
    isAlphabet = True
    numGuesses = 8
    displayWord = ["*" for x in word]
    string = displayString(displayWord)
    gameOver = False

    gameSetup(word,displayWord,string)
     
    while gameOver == False:
        if "*" in displayWord:
            if numGuesses > 0 :    
                numGuesses = numGuesses - 1
                letter = guess()
                check(word,letter,displayWord,isAlphabet)
                print(displayWord)
                guessTracker(letter,numGuesses,alreadyGuessed,isAlphabet)
                print("You have " + str(numGuesses) + " guesses left.")
            else :
                gameOver = True
                print("You ran out of turns, you lose!")
        else:
            gameOver = True
            print("You've guessed the word!")
    
    
playGame()