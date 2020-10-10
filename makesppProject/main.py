####################################################
# This is the main file for the MakeSPP nodea team #
####################################################

import pygame
import sys, os, time
pygame.init()
fpsClock = pygame.time.Clock()
FPS = 120

W,H = 500, 700
win = pygame.display.set_mode((W,H))
pygame.display.set_caption("Game")

bg = pygame.image.load(os.path.join('images','bg.jpeg'))
bgY = int(0)
bgY2 = bg.get_height()

class player(object):       # created class for player
    img = pygame.image.load(os.path.join('images', 'rocket.png'))
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False

    def draw(self,win):
        #show player when player wants to move(left, right, or still)
        if self.left:
            win.blit(self.img, (self.x, self.y))
        elif self.right:
            win.blit(self.img, (self.x, self.y))
        else:
            win.blit(self.img, (self.x, self.y))

def redrawGameWindow():   #this function basicaly refreshes the screen to keep it updated
    win.blit(bg, (0, bgY2))
    win.blit(bg, (0, bgY))  # draws our first bg image# draws the second bg image   #draws the background at the center, or 0,0
    player.draw(win)           #draws the player in the window
    pygame.display.update()     #checks for any inputs from user, then updates the program
    fpsClock.tick(FPS)          #refresehes every FPS

      #draws player at 150,370 with width 40 and height 60
wait = True
intro = False #makes introduction true
starting = False
run = False # makes main run false

player = player(190, 540, 40, 60)
while wait:
    time.sleep(3) #waits 3 seconds
    wait = False #these 2 lines move on to the intro of the game
    intro = True
    while intro:
        for event in pygame.event.get():       #checks for input
            if event.type == pygame.QUIT:        # if input is quit(the x at the top of the screen)
                intro= False
                pygame.quit()

        player.y -= player.vel/2

        while player.y == 260:
            player.y-= player.vel

        if player.y == -50:
            wait = False
            starting = True
            print("max reached")
            while starting:
                player.x = 190
                player.y = 540
                starting = False
                run = True
                while run:
                    bgY -= player.vel
                    bgY2 -= player.vel
                    if bgY < bg.get_height() * -1:
                        bgY = bg.get_height()
                    if bgY2 < bg.get_height() * -1:
                        bgY2 = bg.get_height()

                    for event in pygame.event.get():  # checks for input
                        if event.type == pygame.QUIT:  # if input is quit(the x at the top of the screen)
                            pygame.quit()  # if program recieves quit input, closes program

                    keys = pygame.key.get_pressed()  # making life easier

                    if keys[
                        pygame.K_LEFT] and player.x > player.vel:  # if player presses left key and player's horizontal positioin is greater than the velocity
                        player.x -= player.vel
                        player.left = True
                        player.right = False

                    elif keys[pygame.K_RIGHT] and player.x < 500 - player.vel - player.width:
                        player.x += player.vel
                        player.left = False
                        player.right = True
                    elif keys[pygame.K_q]:
                        pygame.quit()

                    redrawGameWindow()

        redrawGameWindow()

pygame.quit()