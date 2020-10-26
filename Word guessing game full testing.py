#-----------------------------------------------------------------------------
# Name:        Word Guessing Game.py
# Purpose:     Make a hangman type game
#
# Author:      Daniel
# Created:     07-Oct-2020
# Updated:     15-Oct-2020
#-----------------------------------------------------------------------------
# I think this project deserves a 4+ because...
# Unaware of the extension I spent every free moment working on this coding during thanks giving
# And hontestly the end result was not what I had planned at the beginning but it turned out 10 times better than I imagined
# A lot of the code I use I learnt on the way while coding the game, which is why there's so many surprises
# For example, more than half the code in here I wouldn't have know were possible or exists if it weren't for my curiosity to
# search it up.
#
#Features Added and reasoning together:
#Added a twist to the triditional hangman, when the user guesses a correct letter they gain back a life and the
#hang man animation will lose a body part. (while I'm writting this I realized gaining body parts for losing makes no sense
#I changed it so they lost a body part if they guess wrong and gain back one if they are correct...makes more sense.
# ^ I didn't like an 'actual' hanging man, so I changed it to a strawberry plant
#Played around with unicode so I didn't need to type out every letter.
#Added an AI for the user to compete with (if these brackets are here I may have forgot to edit this and I have not
# been able to add an AI -> if the case ignore this feature)
#Made a custom screen for every gameState and helped a few other friends make a custom main screen too
# I edited a few of the sprites, like the hangman guy who use to have a frown now has a smile, and some candy (on lose screen)

#I made sure to add a function description for everything, even if I wasn't sure it needed one. Because I lost
#all my marks there last time.
#Learnt by width and height are in caps in the progress
#Learnt that I could set color names with a certain color code as a variable, and added a few to my game
#Made the discorvery of centering text and rectangles, makes life easy.

#I didn't add a quit game button so they user can never leave, 200IQ
#I added I bunch of sounds and music to match certain events, and a buttoned click sound because who doesn't
#like clicky buttons. and it turns out adding sound and images is sooo simple... I've spent half a day searching it up to no
#sucess...because I had an error with thonny or pgzero. Waste of time but atleast I know how to fix it next time.

#overall very proud of this, even got my family to play it. Now off to the emerging technologies assignment

WIDTH = 800 #these are constant values so we use all caps
HEIGHT = 600
import random
gameState = ''
run = True
imageStatus = 0
letter = ''
guessedLetter = []
correctLetter = []
lives = 5

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

# def pickWord(wordListIn):
#     return (random.choice(wordListIn))
# 
# secretWord = pickWord(wordList)

numLettersInWordList = len(secretWord)
print (secretWord)
print (numLettersInWordList)

'''creating plant'''
plant = Actor("plant-1")
plant.pos = (600,200)
plant.frame = 1

'''creating end screen layout'''
endScreen = Actor("youlost")
endScreen.pos = (WIDTH/2, HEIGHT/2)

'''creating start screen'''
startScreen = Actor("startscreen")
startScreen.pos = (WIDTH/2, HEIGHT/2)

'''creating game background'''
background = Actor ("gamebackground")
background.pos = (WIDTH/2, HEIGHT/2)

'''creating rules screen'''
rule = Actor ("rules")
rule.pos = (WIDTH/2, HEIGHT/2)

'''win screen'''
winScreen = Actor("winscreen")
winScreen.pos = (WIDTH/2, HEIGHT/2)



#start button
button1Draw = [102, 270, 210, 138]
button1Rect = Rect(button1Draw) 
button1Value = False  
button1Color = 'green'

#game page exit button
button2Draw = [680, 560, 80, 30]
button2Rect = Rect(button2Draw) 
button2Value = False  
button2Color = (230,187,173)

#rules button
button3Draw = [488, 270, 210, 138]
button3Rect = Rect(button3Draw) 
button3Value = False  
button3Color = (255, 250, 205)

#exit button on lose screen
button4Draw = [348, 443, 58, 70]
button4Rect = Rect(button4Draw) 
button4Value = False  
button4Color = (230,187,173)

#play again button on win screen
button5Draw = [280, 450, 220, 90]
button5Rect = Rect(button5Draw) 
button5Value = False  
button5Color = (230,187,173)


#start-up
def startUp():
    '''Run this to get the program ready to run'''
    global gameState
    
    gameState = 'start screen'
        
#def secretWord():
    #global wordList, numLettersInWordList
    
    
def updatePlant():
    '''updates the hangman image'''
    global plant, gameState
    
    '''restart the image frame when it reaches the last one'''
    if plant.frame > 5 and plant.frame != 0:
        plant.frame = 1
    
        
    '''this is what changes the plant image'''
    plant.image = 'plant-' + str(plant.frame)


def on_key_down(unicode):
    global letter, numLettersInWordList, secretWord, guessedLetter, lives, gameState, plant, win, winScreen, correctLetter
    '''this function checks the player input (gussed letter)'''


    if gameState == 'game':
        if unicode.isalpha():
            '''checks if the letter pressed by the user is in the secret word'''
            if unicode in (secretWord):

                if unicode in (guessedLetter):
                    '''avoid printing the same letter twice on the list'''
                    print("You already guessed that letter")
                    letter = unicode
                    music.play_once('invalid')
                    
                else:
                    ''' check to see if the letter chosen is in the word'''
                    #guessedLetter = (unicode)
                    print("correct!")
                    guessedLetter.append(unicode)
                    correctLetter.append(unicode)
                    print(unicode)
                    print(guessedLetter)
                    letter = unicode
                    music.play_once('correctanswer')
                    
                    
                    '''gives an extra life for correct guesses, but they can't have more than 7 lives '''
                    '''also added 'and plant.frame <= 1' because the game would break if plant.frame = 0'''
                    if lives < 5:
                        lives += 1
                        plant.frame -= 1
                        updatePlant()
                


            else:
                if unicode in (guessedLetter):
                    '''avoid printing the same letter twice on the list'''
                    print("You already guessed that letter")
                    letter = unicode
                    music.play_once('invalid')
                    
                else:
                    '''finally if the letter is not in the word, we tell them to try again and we
                    add the letter to the list aswell to avoid duplications'''
                    print("That letter in not in the word, please try again")
                    guessedLetter.append(unicode)
                    letter = unicode
                    lives -= 1
                    plant.frame += 1
                    updatePlant()
                    music.play_once('wronganswer')
                    
                    if lives == 0:
                        gameState = 'end'
        
        else:
            print("Opps, numbers and symbols are not valid")
            print("In addition, shift and caps lock are invalid keys, thus don't use Upper Case")
            music.play_once('invalid')
        
        
        '''when all the letters in the secretword has been guessed the player wins and is taken to the win screen'''
        winGame = True
        for i in secretWord:
            if i not in correctLetter:
                winGame = False
                break
            
        if winGame == True: 
            gameState = 'win'
                
                    
            
        
#buttons
def on_mouse_up(pos, button):
    '''Pygame Special Event Hook - Runs when the mouse button is released'''
    
    import random
    global button1Color
    global button1Value
    global button2Value
    global button2Color
    global button3Color
    global button3Value
    global button4Color
    global button4Value
    '''I didn't bother converting the above globals into a single line. But when I found out i could just use commas
    I did that for the rest of the game, like below. Also something I learnt on the way'''
    global gameState, lives, guessedLetter, letter, imageStatus, numLettersInWordList, secretWord, button5Color, button5Value
    global plant
    
     
    if gameState == 'start screen':
        if button1Rect.collidepoint(pos):
            '''Start game button and rules button. turns out I can't have two gameState == 'startScreen's in one
            function so I put the both together here'''
            gameState = 'game'
            button1Value = True
            music.play_once('buttonclicked')

            #start screen button
            if  button1Value == True:
                button1Color = 'light green'
            else:
                button1Color == 'green'
                
                
        #rules button
        elif button3Rect.collidepoint(pos):
            if  button3Value == True:
                button3Color = (255, 250, 205)
                button3Value = False
                gameState = 'rules'
                music.play_once('buttonclicked')

            else:
                button3Value = True
                gameState = 'rules'
                music.play_once('buttonclicked')

    elif gameState == 'game' or gameState == 'rules':
          if button2Rect.collidepoint(pos):
            '''Exit game button'''
            
            if  button2Value == True:
                button2Color = (230,187,173)
                button2Value = False
                gameState = 'start screen'
                music.play_once('buttonclicked')

            else:
                button2Value = True
                gameState = 'start screen'
                music.play_once('buttonclicked')
            

    elif gameState == 'end':
          if button4Rect.collidepoint(pos):
            '''restart button on end screen'''
        
            if  button4Value == True:
                button4Color = (230,187,173)
                button4Value = False
                gameState = 'start screen'
                lives = 5
                imageStatus = 0
                plant.frame = 1
                letter = ''
                guessedLetter = []
                secretWord = (random.choice(wordList))
                numLettersInWordList = len(secretWord)
                print (secretWord)
                print (numLettersInWordList)
                music.play_once('buttonclicked')
                
            else:
                button2Value = True
                gameState = 'start screen'
                gameState = 'start screen'
                lives = 5
                imageStatus = 0
                plant.frame = 1
                letter = ''
                guessedLetter = []
                secretWord = (random.choice(wordList))
                numLettersInWordList = len(secretWord)
                print (secretWord)
                print (numLettersInWordList)
                music.play_once('buttonclicked')
     
    elif gameState == 'win':
          if button5Rect.collidepoint(pos):
            '''restart button on win screen'''
        
            if  button5Value == True:
                button5Color = (230,187,173)
                button5Value = False
                gameState = 'start screen'
                lives = 5
                imageStatus = 0
                plant.frame = 1
                letter = ''
                guessedLetter = []
                secretWord = (random.choice(wordList))
                numLettersInWordList = len(secretWord)
                print (secretWord)
                print (numLettersInWordList)
                music.play_once('buttonclicked')
                
            else:
                button2Value = True
                gameState = 'start screen'
                gameState = 'start screen'
                lives = 5
                imageStatus = 0
                plant.frame = 1
                letter = ''
                guessedLetter = []
                secretWord = (random.choice(wordList))
                numLettersInWordList = len(secretWord)
                print (secretWord)
                print (numLettersInWordList)
                music.play_once('buttonclicked')

#Draw
def draw():
    '''Insert a header'''
    global gameState, numLettersInWordList, guessedLetter, unicode, letter, yellow, lives, plant, endScreen
    global startScreen, rule, winScreen, secretWord
    
    if gameState == 'start screen':
        '''landing page'''
        music.play_once('gamesound')
        if gameState == "start screen":
            screen.clear()
            startScreen.draw()
            #screen.draw.text("Hello, Welcome To My Program", center=(WIDTH/2, HEIGHT/2), color="hotpink", fontsize=45)
            #screen.draw.text("Still In The Making Though...", center=(WIDTH/2, 330), color="red")
            #screen.draw.filled_rect(button1Rect, button1Color)
            #screen.draw.text("Click To Start", center=(400,425), color="blue", fontsize = 32)
            #screen.draw.filled_rect(button3Rect, button3Color)
            #screen.draw.text("Rules", center=(400,480), color=(255,102,102), fontsize = 32)
    
    
    elif gameState == 'game':
        letterDisplay = " "
        '''the actual game'''
        screen.clear()
        background.draw()
        plant.draw()
        screen.draw.filled_rect(button2Rect, button2Color)
        screen.draw.text("Exit", center=(720,575), color="Red", fontsize = 32)
        screen.draw.text(numLettersInWordList*'_  ', (100,500), color="black", fontsize=80)
        screen.draw.text((str(guessedLetter)), center=(200,100), color="Red", fontsize = 20)
        screen.draw.text("Lives left: " + (str(lives)), center=(100,50), color="hotpink", fontsize = 40)
        '''printing correctly gussed letters on screen'''
        
        for i in range(len(secretWord)):
            '''displaying correctly guessed letters on screen'''
            if secretWord[i] in guessedLetter:
                #print the letter
                letterDisplay += secretWord[i] + "  "
                screen.draw.text(letterDisplay , (80,470), color = "black", fontsize = 80)
            else:
                screen.draw.text(" ", (80,440), color = "black", fontsize = 32)
                
        for i in secretWord:
            if i in letterDisplay:
                if len(secretWord) == len(letterDisplay):
                    gameState = 'win'

        

        
    elif gameState == 'end':
        '''take users to this screen if they lost'''
        screen.clear()
        endScreen.draw()
        music.play_once('gameoversound')
        #screen.draw.filled_rect(button2Rect, button2Color)
        #screen.draw.text("Exit", center=(720,575), color="Red", fontsize = 32)
        #screen.draw.text("Oh No!", center=(400,100), color="red", fontsize = 100)
        #screen.draw.text("Looks Like You've Run Out Of Lives", center=(400,170), color="orange", fontsize = 60)
        #screen.draw.text("Click the exit button to restart", center=(400,250), color=(yellow), fontsize = 70)
        
    elif gameState == 'win':
        '''take user to this screen if they win'''
        screen.clear()
        winScreen.draw()
        music.play_once('finalwinsound')
        #Need to match button cordinates with win screen


    elif gameState == 'rules':
        '''rules screen'''
        music.play('rulessound')
        screen.clear()
        rule.draw()
        screen.draw.filled_rect(button2Rect, button2Color)
        screen.draw.text("Exit", center=(720,575), color="Red", fontsize = 32)


    else: 
        '''check for errors, instead of the game breaking it would take me to this red screen'''
        screen.fill((255, 204, 203))
        screen.draw.text ("Something is wrong", center=(WIDTH/2, HEIGHT/2), color="red")

      
print (secretWord)

startUp()

'''Graded

I screwed up the video, so this is audio only...sorry.  Seems video editing/producing issues are contagious! 
Please look at the commit diff to see where I changed your program
https://drive.google.com/file/d/1J10OkRB3yrNXBLa5KFcizIQp18_D9qcV/view?usp=sharing

KA- 9.8/10
TC - 7/10
