#-----------------------------------------------------------------------------
# Name:        New File Generator (newFile.py)
# Purpose:     Generates a new file for use in the ICS3U course
#
# Author:      Mr. Brooks
# Created:     07-Oct-2020
# Updated:     07-Oct-2020
#-----------------------------------------------------------------------------

WIDTH = 800
HEIGHT = 600
import random
gameState = ''

#picking a random word from my secret words lists
wordList = ["laptop", "blizzard" , "galaxy", "matrix" , "sunday", "mystify", "unknown", "yummy", "saturn", "canada", "oakville"]
secretWord = (random.choice(wordList))

button1Draw = [300, 400, 200, 50]
button1Rect = Rect(button1Draw) 
button1Value = False  
button1Color = 'green'


#start-up
def startUp():
    '''Run this to get the program ready to run'''
    global gameState

    gameState = 'start screen'


#buttons
def on_mouse_up(pos, button):
    '''Pygame Special Event Hook - Runs when the mouse button is released'''

    global button1Color
    global button1Value
    global gameState
    
     
    if button1Rect.collidepoint(pos):

        if  button1Value == True:
            button1Color = 'light green'
            button1Value = False
            gameState = 'game'

        else:
            button1Color = 'green'
            button1Value = True
            gameState = 'game'

#Draw
def draw():
    global gameState
    if gameState == 'start screen': #landing page
        if gameState == "start screen":
            screen.clear()
            screen.fill((212, 235, 250))
            screen.draw.text("Hello, Welcome To My Program", center=(WIDTH/2, HEIGHT/2), color="hotpink", fontsize=45)
            screen.draw.text("Still In The Making Though...", center=(WIDTH/2, 330), color="red")
            screen.draw.filled_rect(button1Rect, button1Color)
            
    #word guessing game page
    elif gameState == 'game':
        screen.clear()
        screen.fill((173, 230, 187))  
    
    else: #to check 
        screen.fill((255, 204, 203))
        screen.draw.text ("Something is wrong", center=(WIDTH/2, HEIGHT/2), color="red") #use 'center=' to center text

print (secretWord)

startUp()