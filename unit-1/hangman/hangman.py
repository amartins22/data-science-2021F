import random
def playGame():  
    #variables
    wordList = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black", "brown", "gray", "white"] 
    word = random.choice(wordList)
    wordLength = len(word)
    numGuesses = 0
    titleMessage = """Welcome to Hangman. 
The secret word has """ + str(wordLength) + """ letters and the theme is colors."""
   
    
    def createDisplay():
        displayWord = []
        
        for x in word:
            displayWord.append("*")
        
        print(displayWord)
    
    
    
    print(titleMessage)
    print(word)    
    createDisplay()
    
    
playGame()