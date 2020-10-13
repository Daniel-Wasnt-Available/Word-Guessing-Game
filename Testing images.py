WIDTH = 300
HEIGHT = 300
    

alien = Actor ('alien')
alien.pos = 0,56

def draw():
    screen.blit('alien',(10,10))
    alien.draw()