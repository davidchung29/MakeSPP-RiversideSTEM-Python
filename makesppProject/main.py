
####################################################
# This is the main file for the MakeSPP nodea team #
####################################################

import pygame
from pygame.locals import *
import sys, os, time
import math
import random

pygame.init()
fpsClock = pygame.time.Clock()
FPS = 60

W,H = 900, 1000
win = pygame.display.set_mode((W,H))
pygame.display.set_caption("Game")

bg = pygame.image.load(os.path.join('images','bg.jpg'))
bgX = int(0)
bgX2 = bg.get_width()

class player(object):       # created class for player
    img = pygame.image.load(os.path.join('images', 'player.png'))
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False

    def draw(self,win):
        #show player when player wants to move(left, right, or still)
        if self.left:
            win.blit(self.img, (self.x, self.y))
        elif self.right:
            win.blit(self.img, (self.x, self.y))
        else:
            win.blit(self.img, (self.x, self.y))
        if self.up:
            win.blit(self.img, (self.x, self.y))
        if self.down:
            win.blit(self.img, (self.x, self.y))
        self.hitbox = (self.x + 150 , self.y+100, self.width+210, self.height + 180)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class coin(object):
    img = pygame.image.load(os.path.join('images', 'coin.png'))
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 4

    def draw(self,win):
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(pygame.transform.scale(self.img, (64,64)), (self.x,self.y))

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

def redrawGameWindow():   #this function basicaly refreshes the screen to keep it updated
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))  # draws our first bg image# draws the second bg image   #draws the background at the center, or 0,0
    player.draw(win)           #draws the player in the window
    fpsClock.tick(FPS)    #refresehes every FPS
    for item in items:
        item.draw(win)
    win.blit(currentscore, (750, 40))
    pygame.display.update()     #checks for any inputs from user, then updates the program
def endcreen():
    win.blit(bg, (0, 0))

run = False # makes main run false
pygame.time.set_timer(USEREVENT+1, 500)
score = 0
player = player(190, 550, 40, 60)
items =[]

score = 0

font = pygame.font.SysFont('comicsans', 40) # creates a font object
currentscore = font.render('Score: '+ str(score),1,(255,255,255))

run = True
while run:
    for item in items:
        if item.collide(player.hitbox):
            score += 1
            print(score)
            currentscore = font.render('Score: ' + str(score), 1, (255, 255, 255))
            items.pop(items.index(item))

        if item.x < -64:
            items.pop(items.index(item))
        else:
            item.x -= 4
    bgX -= 4
    bgX2 -= 4
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()

    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pygame.event.get():  # checks for input
        if event.type == pygame.QUIT:  # if input is quit(the x at the top of the screen)
            pygame.quit()  # if program recieves quit input, closes program
        if event.type == USEREVENT + 1:
            if len(items) <13:
                rxcor = random.randrange(500, 800)
                rycor = random.randrange(200, 700)
                items.append(coin(rxcor, rycor, 64, 64))
    keys = pygame.key.get_pressed()  # making life easier

    if keys[pygame.K_LEFT] and player.x > player.vel:  # if player presses left key and player's horizontal positioin is greater than the velocity
        player.x -= player.vel
        player.left = True
        player.right = False

    elif keys[pygame.K_RIGHT] and player.x < 500 - player.vel - player.width:
        player.x += player.vel
        player.left = False
        player.right = True

    elif keys[pygame.K_UP]:
        player.y -= player.vel
        player.up = False
        player.down = True

    elif keys[pygame.K_DOWN]:
        player.y += player.vel
        player.up = True
        player.down = False

    elif keys[pygame.K_q]:
        pygame.quit()

    redrawGameWindow()



pygame.quit()
