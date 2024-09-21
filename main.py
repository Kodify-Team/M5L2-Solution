#Copy this code to Mu Editor

WIDTH = 600 # Window width
HEIGHT = 300 # Window height

TITLE = "Alien Runner" # Title for the game window
FPS = 30 # Number of frames per second

# Objects
alien = Actor('alien', (50, 240))
background = Actor("background")
box = Actor('box', (550, 265))

def draw():
    background.draw()
    alien.draw()
    box.draw()
    
def update(dt):

    # Box movement
    if box.x > -20:
        box.x = box.x - 5
        box.angle = box.angle + 5
    else:
        box.x = WIDTH + 20
        
    # Controls
    if keyboard.left and alien.x > 20:
        alien.x = alien.x - 5
        alien.image = 'left'
    
    elif keyboard.right and alien.x < 580:
        alien.x = alien.x + 5
        alien.image = 'right'

    else:
        alien.image = 'alien'
        

def on_key_down(key):
    # Jump
    if keyboard.space or keyboard.up or keyboard.w:
        alien.y = 100
        animate(alien, tween='bounce_end', duration=2, y=240)
