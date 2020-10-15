#-----------------------------------------------------------------------------
# Name:        Word Guessing Game.py
# Purpose:     Make a hangman type game
#
# Author:      Daniel
# Created:     07-Oct-2020
# Updated:     14-Oct-2020
#-----------------------------------------------------------------------------
# I think this project deserves a 4 because...
#
#Features Added:
#Added a twist to the triditional hangman, when the user guesses a correct letter they gain back a life and the
#hang man animation will lose a body part. (while I'm writting this I realized gaining body parts for losing makes no sense
#I'm going to change it so they lost a body part if they guess wrong and gain back one if they are correct...makes more sense.
#Played around with unicode so I didn't need to type out every letter.
#Added an AI for the user to compete with (if these brackets are here I may have forgot to edit this and I have not
# been able to add an AI -> if the case ignore this feature)
#
#

WIDTH = 800 #these are constant values so we use all ca
HEIGHT = 600
import random
gameState = ''
run = True
imageStatus = 0
letter = ''
guessedLetter = []
lives = 7
xDisplayWord = 80

#colors
yellow = (246,255,59)
purple = (169,111,224)
lightgreen = (105,230,145)
sand = (239,160,105)


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

hangman = Actor("hangman0")
hangman.pos = (600,150)
hangman.frame = 0



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
    
    
def updateHangman():
    '''updates the hangman image'''
    global hangman
    
    
    if hangman.frame > 6:
        hangman.frame = 0
        
    hangman.image = 'hangman' + str(hangman.frame)


def on_key_down(unicode):
    global letter, numLettersInWordList, secretWord, guessedLetter, lives, gameState, hangman
    '''this function checks the player input (gussed letter)'''

    
    if gameState == 'game':
        if unicode.isalpha():
            if unicode in (secretWord):
                if unicode in (guessedLetter):
                    '''avoid printing the same letter twice on the list'''
                    print("You already guessed that letter")
                    letter = unicode
                    
                else:
                    ''' check to see if the letter chosen is in the word'''
                    #guessedLetter = (unicode)
                    print("correct!")
                    guessedLetter.append(unicode)
                    print(unicode)
                    print(guessedLetter)
                    letter = unicode
                    
                    '''gives an extra life for correct guesses, but they can't have more than 7 lives '''
                    if lives < 7:
                        lives += 1
                        hangman.frame -= 1
                        updateHangman()


            else:
                if unicode in (guessedLetter):
                    '''avoid printing the same letter twice on the list'''
                    print("You already guessed that letter")
                    letter = unicode
                else:
                    '''finally if the letter is not in the word, we tell them to try again and we
                    add the letter to the list aswell to avoid duplications'''
                    print("That letter in not in the word, please try again")
                    guessedLetter.append(unicode)
                    letter = unicode
                    lives -= 1
                    hangman.frame += 1
                    updateHangman()
                    if lives == 0:
                        gameState = 'end'
                        
        else:
            print("Opps, numbers and symbols are not valid")
            
        
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



#Draw
def draw():
    global gameState, numLettersInWordList, guessedLetter, unicode, letter, yellow, lives, xDisplayWord
    
    if gameState == 'start screen':
        '''landing page'''
        if gameState == "start screen":
            screen.clear()
            screen.fill((212, 235, 250))
            screen.draw.text("Hello, Welcome To My Program", center=(WIDTH/2, HEIGHT/2), color="hotpink", fontsize=45)
            screen.draw.text("Still In The Making Though...", center=(WIDTH/2, 330), color="red")
            screen.draw.filled_rect(button1Rect, button1Color)
            screen.draw.text("Click To Start", center=(400,425), color="blue", fontsize = 32)
            screen.draw.filled_rect(button3Rect, button3Color)
            screen.draw.text("Rules", center=(400,480), color=(255,102,102), fontsize = 32)
    
    
    elif gameState == 'game':
        letterDisplay = " "
        '''the actual game'''
        screen.clear()
        screen.fill((173, 230, 187))
        hangman.draw()
        screen.draw.filled_rect(button2Rect, button2Color)
        screen.draw.text("Exit", center=(720,575), color="Red", fontsize = 32)
        screen.draw.text(numLettersInWordList*'_  ', (100,300), color="black", fontsize=80)
        screen.draw.text((str(guessedLetter)), center=(200,100), color="Red", fontsize = 20)
        screen.draw.text("Lives left: " + (str(lives)), center=(100,50), color="hotpink", fontsize = 40)
        '''printing correctly gussed letters on screen'''
        
        for i in range(len(secretWord)):
            '''displaying correctly guessed letters on screen'''
            if secretWord[i] in guessedLetter:
                #print the letter
                letterDisplay += secretWord[i] + "  "
                screen.draw.text(letterDisplay , (xDisplayWord,290), color = "black", fontsize = 80)
                if letterDisplay == secretWord:
                    screen.draw.text(" You Won!", (400,300), color = "black", fontsize = 80) 
            else:
                screen.draw.text(" ", (100,305), color = "black", fontsize = 32) 
            
        
#        if letter in secretWord:
#            if numLettersInWordList in range(len(secretWord)):
#               print(numLettersInWordList[i])
#            screen.draw.text(letter, (100,305), color = "black", fontsize = 32)
#        elif lives == 0:
#            gameState == 'end'

        
        #images = []
        #for i in range(5):
            #image = image.load("witch" + str(i) + ".png")
            #images.append(image)

        
    elif gameState == 'end':
        '''take users to this screen if they lost'''
        screen.clear()
        screen.fill((173, 230, 187))
        screen.draw.filled_rect(button2Rect, button2Color)
        screen.draw.text("Exit", center=(720,575), color="Red", fontsize = 32)
        screen.draw.text("Oh No!", center=(400,100), color="red", fontsize = 100)
        screen.draw.text("Looks Like You've Run Out Of Lives", center=(400,170), color="orange", fontsize = 60)
        screen.draw.text("Click the exit button to restart", center=(400,250), color=(yellow), fontsize = 70)
        
    elif gameState == 'win':
        '''take user to this screen if they win'''
        screen.clear()
        screen.fill(lightgreen)
        screen.draw.filled_rect(button2Rect, button2Color)
        screen.draw.text("Exit", center=(720,575), color="Red", fontsize = 32)
        screen.draw.text("Oh No!", center=(400,100), color="red", fontsize = 100)
        screen.draw.text("Looks Like You've Run Out Of Lives", center=(400,170), color="orange", fontsize = 60)
        screen.draw.text("Click the exit button to restart", center=(400,250), color=(yellow), fontsize = 70)

    elif gameState == 'rules':
        '''rules screen'''
        screen.clear()
        screen.fill(purple)  
        screen.draw.filled_rect(button2Rect, button2Color)
        screen.draw.text("Exit", center=(720,575), color="Red", fontsize = 32)
        screen.draw.text("The Rules Are Simple", center=(400,100), color=(yellow), fontsize = 80)
        screen.draw.text ("Guess The Secret Word...", center=(WIDTH/2, 200), color=(lightgreen))
        screen.draw.text ("Before The AI Gusses Your Word!", center=(WIDTH/2, 230), color=(lightgreen))
        screen.draw.text ("You May Use Any Word, Or Even A Mix Of Letters", center=(WIDTH/2, 260), color=(lightgreen))
        screen.draw.text ("However, You Can Only Use Up To 6 Letters", center=(WIDTH/2, 290), color=(lightgreen))
        screen.draw.text ("In Addition To Who Guesses The Word The Fastest", center=(WIDTH/2, 320), color=(lightgreen))
        screen.draw.text ("If You Guess 5 Wrong Letters You Will Automatically Lose", center=(WIDTH/2, 350), color=(lightgreen))
        screen.draw.text ("Numbers And Symbols Are Not Valid", center=(WIDTH/2, 380), color=(lightgreen))
        screen.draw.text("Good Luck!", center=(400,500), color=(sand), fontsize = 80)

    else: 
        '''check for errors'''
        screen.fill((255, 204, 203))
        screen.draw.text ("Something is wrong", center=(WIDTH/2, HEIGHT/2), color="red")

#need help with making the whole game into a loop        
print (secretWord)

startUp()
