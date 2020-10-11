#-----------------------------------------------------------------------------
# Name:        Word Guessing Game.py
# Purpose:     Make a hangman type game
#
# Author:      Daniel
# Created:     07-Oct-2020
# Updated:     011-Oct-2020
#-----------------------------------------------------------------------------

WIDTH = 800 #these are constant values so we use all ca
HEIGHT = 600
import random
gameState = ''
run = True
imageStatus = 0
letter = ''
guessedLetter = ['Letters You Have Already Guessed',]


#picking a random word from my secret words lists
wordList = ["laptop", "blizzard" , "galaxy", "matrix" , "sunday", "mystify", "unknown", "yummy", "saturn", "canada", "oakville",
            "hospital", "computer", "firetruck", "github", "binder", "python", "october", "escape", "advanced", "monday", "pygame"]

#this did not work when I put it in a function
#I searched it up countless times and I was wasting a lot of time
#so I just left it here, out side of a function
secretWord = (random.choice(wordList))
numLettersInWordList = len(secretWord)
print (secretWord)
print (numLettersInWordList)

#start button
button1Draw = [300, 400, 200, 50]
button1Rect = Rect(button1Draw) 
button1Value = False  
button1Color = 'green'

#game page exit button
button2Draw = [680, 560, 80, 30]
button2Rect = Rect(button2Draw) 
button2Value = False  
button2Color = (230,187,173)

#rules button
button3Draw = [320, 460, 160, 40]
button3Rect = Rect(button3Draw) 
button3Value = False  
button3Color = (255, 250, 205)


#start-up
def startUp():
    '''Run this to get the program ready to run'''
    global gameState

    gameState = 'start screen'
        
#def secretWord():
    #global wordList, numLettersInWordList
    


def on_key_down(unicode):
    global letter, numLettersInWordList, secretWord
    global guessedLetter

    
    if gameState == 'game':
        if unicode in (secretWord):
            #guessedLetter = (unicode)
            print("correct!")
            guessedLetter.append(unicode)
            print(unicode)
            print(guessedLetter)
        else:
            print("try again")

#buttons
def on_mouse_up(pos, button):
    '''Pygame Special Event Hook - Runs when the mouse button is released'''

    global button1Color
    global button1Value
    global button2Value
    global button2Color
    global button3Color
    global button3Value
    global gameState
    
     
    if button1Rect.collidepoint(pos):
        '''Start game button'''

        if  button1Value == True:
            button1Color = 'light green'
            button1Value = False
            gameState = 'game'

        else:
            button1Color = 'green'
            button1Value = True
            gameState = 'game'

    elif button2Rect.collidepoint(pos):
        '''Exit game button'''
    
        if  button2Value == True:
            button2Color = (230,187,173)
            button2Value = False
            gameState = 'start screen'

        else:
            button2Value = True
            gameState = 'start screen'

    elif button3Rect.collidepoint(pos):
        '''Rules button'''
        
        if  button3Value == True:
            button3Color = (255, 250, 205)
            button3Value = False
            gameState = 'rules'

        else:
            button3Value = True
            gameState = 'rules'

def on_key_up(key):
    '''used key up to see if it gets released intead of pressed or held down'''
    global gameState
    
    

#Draw
def draw():
    global gameState, numLettersInWordList, guessedLetter, unicode
    
    if gameState == 'start screen':
        '''landing page'''
        if gameState == "start screen": #might change to kep pressed later
            screen.clear()
            screen.fill((212, 235, 250))
            screen.draw.text("Hello, Welcome To My Program", center=(WIDTH/2, HEIGHT/2), color="hotpink", fontsize=45)
            screen.draw.text("Still In The Making Though...", center=(WIDTH/2, 330), color="red")
            screen.draw.filled_rect(button1Rect, button1Color)
            screen.draw.text("Click To Start", center=(400,425), color="blue", fontsize = 32)
            screen.draw.filled_rect(button3Rect, button3Color)
            screen.draw.text("Rules", center=(400,480), color=(255,102,102), fontsize = 32)
    
    elif gameState == 'game':
        '''the actual game'''
        screen.clear()
        screen.fill((173, 230, 187))  
        screen.draw.filled_rect(button2Rect, button2Color)
        screen.draw.text("Exit", center=(720,575), color="Red", fontsize = 32)
        screen.draw.text(numLettersInWordList*'_ ', (100,300), color="black", fontsize=80)
        screen.draw.text((guessedLetter), center=(100,100), color="Red", fontsize = 32) #cant add guessedLetter also I'm having trouble
        #adding the images into my game. The code below is what I tried recently.
        
        #images = []
        #for i in range(5):
            #image = image.load("witch" + str(i) + ".png")
            #images.append(image)

        
    elif gameState == 'rules':
        '''rules screen'''
        screen.clear()
        screen.fill((240, 248, 255))  
        screen.draw.filled_rect(button2Rect, button2Color)
        screen.draw.text("Exit", center=(720,575), color="Red", fontsize = 32)

    else: 
        '''check for errors'''
        screen.fill((255, 204, 203))
        screen.draw.text ("Something is wrong", center=(WIDTH/2, HEIGHT/2), color="red") #use 'center=' to center text


        
print (secretWord)

startUp()