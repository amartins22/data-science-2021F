import random

#display the secret word
def createDisplay(displayWord, word):
    for x in word:
        displayWord.append("*")
    return displayWord
    
#guess letter
def guess(numGuesses):
    g = input("Guess Letter: ")
    print("You guessed " + g)
    numGuesses = numGuesses - 1
    return g
    
        
#check letter
def check(word,letter,displayWord):
    for i in range(len(word)):
        x = word[i]
        if x == letter :
            displayWord[i] = x
            print("Yes, " + letter + " is in the word!")
    print(displayWord)    

def playGame():  
    #variables
    wordList = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black", "brown", "gray", "white"] 
    word = random.choice(wordList)
    wordLength = len(word)
    numGuesses = 10
    displayWord = []
    
    titleMessage = """Welcome to Hangman. 
The secret word has """ + str(wordLength) + """ letters and the theme is colors.
"""
   

    print(titleMessage)
    print(word)    
    createDisplay(displayWord, word)
    print(displayWord)
    
    if "*" in displayWord:
       if numGuesses > 0 :    
           letter = guess(numGuesses)
           check(word,letter,displayWord)
       else :
           print("You ran out of turns, you lose!")
    else: 
        print("You've guessed the word!")
    
    
playGame()