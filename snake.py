import pygame, sys
from pygame.locals import *
import math, random

# set up pygame
pygame.init()

# set up the window

pygame.display.set_caption('Hello world! Play snake yohoo')
'''
# set up the colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# set up fonts
basicFont = pygame.font.SysFont(None, 48)

# set up the text
text = basicFont.render('Hello world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# draw the white background onto the surface
windowSurface.fill(WHITE)

# draw a green polygon onto the surface
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# draw some blue lines onto the surface
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# draw a blue circle onto the surface
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# draw a red ellipse onto the surface
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# draw the text's background rectangle onto the surface
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# get a pixel array of the surface
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

# draw the text onto the surface
windowSurface.blit(text, textRect)

# draw the window onto the screen
'''

#random object appearing


"""""""""def get_random_point(radius):
    while True:
        # Generate the random point
        x = random.randint(-radius, radius)
        y = random.randint(-radius, radius)
        # Check that it is inside the circle
        if math.sqrt(x ** 2 + y ** 2) < radius:
            # Return it
            return (x, y)
            """""""""
   

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

x = 1
y = 1
speed = 10
# x, y ,w ,h
lijst = [grid.size_width, grid.size_height,15,15]
clock = pygame.time.Clock()

class Grid:
    height = 20
    width = 35
    
    size_height = 15
    size_width = 15
    
grid = Grid()
    
    
windowSurface = pygame.display.set_mode((grid.width * grid.size_width , grid.height * grid.size_height ), 0, 32)
    
class Snack:

    # Class Attribute
    color = 'red'
    height = 15
    width = 15
    x_coo = 0
    y_coo = 0
    
    
    def random(self):
        self.x_coo = random.randint(0,100)
        self.y_coo = random.randint(0,100)
        
    
    # Initializer / Instance Attributes
    def __init__(self, color):
        self.color = color
        self.random()
        

snack = Snack('green')
dir = 'down'

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            

    
    
    clock.tick(2)
    pygame.event.pump()
    # a key has been pressed
    keyinput = pygame.key.get_pressed()
    
    if keyinput[pygame.K_ESCAPE]:
        raise SystemExit

    
    
    if keyinput[pygame.K_LEFT]:
        dir = 'left'
    elif keyinput[pygame.K_RIGHT]:
        dir = 'right'
    elif keyinput[pygame.K_UP]:
        dir = 'up'
    elif keyinput[pygame.K_DOWN]:
        dir = 'down'
    
    if dir == 'left':
        lijst[0] -= speed
    elif dir == 'right':
        lijst[0] += speed
    elif dir == 'up':
        lijst[1] -= speed
    elif dir == 'down':
        lijst[1] += speed
        
    #achtergrond zwart
    windowSurface.fill(BLACK)
    #snack (surface,x,y,h,w)
    pygame.draw.rect(windowSurface, BLUE, (snack.x_coo, snack.y_coo, snack.height, snack.width))
    #snake
    pygame.draw.rect(windowSurface,RED,lijst)
    
    #
    pygame.display.update()





  
#TO DO
#als random blokje geraakt wordt: verdwijnen nieuw blokje verschijnen
    
# denk na over de matrix (voorstelling, bewegen erin) coordinaten of 1,1 ->10,10; 2,2 -> 20,20 

#random kleur verschijnend bloktje
    
# ander blokje vergroot
            
# Faye's hoofd wordt snake
            
            
            
            
