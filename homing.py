import pygame
import random
from constants import*
class Homing(pygame.sprite.Sprite):
    def __init__(self,p):
        super().__init__()
        x = random.randint(0,SCREEN_WIDTH-HOMING_WIDTH)
        y = random.randint(0,SCREEN_HEIGHT-HOMING_HEIGHT)
        while(abs(p.rect.x-x)+abs(p.rect.y-y)<200):
            x = random.randint(0, SCREEN_WIDTH - HOMING_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT - HOMING_HEIGHT)
        self.rect = pygame.Rect(x,y,HOMING_WIDTH,HOMING_HEIGHT)
        self.image = pygame.image.load("wander.png")
        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
        #This is how the homing appears and makes sure that it does not leave the screen
    def update(self,p):
        if p.rect.x<self.rect.x:
            self.rect.x -=2
        if p.rect.x > self.rect.x:
            self.rect.x +=2
        if p.rect.y > self.rect.y:
            self.rect.y +=2
        if p.rect.y < self.rect.y:
            self.rect.y -=2
            #This is the code to make the homing obstacle like a homing missle(It follows the target.)
