WIDTH = 200
HEIGHT = 200


#Create the actor object
knight = Actor('knight_m_run_anim_f0')
#Give the actor a place on the screen to be
knight.pos = (100, 100)
#Set the starting image number
knight.frame = 0


def on_key_up(key):
    '''Check to see if a key has been released'''
    global knight
    
    if key == keys.A:
        #Increase the frame number
        knight.frame = knight.frame + 1
        
        #What do these lines fix?
        if knight.frame > 3:
            knight.frame = 0
            
        #Assign a new image name based on the updated frame number
        knight.image = 'knight_m_run_anim_f' + str(knight.frame)


def draw():
    '''Draw loop for all the graphical elements to display'''
    #Empty the screen for each animation frame
    screen.fill((255, 255, 255))
    #Draw the knight
    knight.draw()