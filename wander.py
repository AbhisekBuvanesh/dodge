import pygame
import random
from constants import*
class Wander(pygame.sprite.Sprite):
    def __init__(self,p):
        super().__init__()
        x = random.randint(0,SCREEN_WIDTH-WANDER_WIDTH)
        y = random.randint(0,SCREEN_HEIGHT-WANDER_HEIGHT)
        while(abs(p.rect.x-x)+abs(p.rect.y-y)<200):
            x = random.randint(0, SCREEN_WIDTH - WANDER_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT - WANDER_HEIGHT)
        self.rect = pygame.Rect(x,y,WANDER_WIDTH,WANDER_HEIGHT)
        self.image = pygame.image.load("wander.png")
        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
        self.speedx= random.randint(MIN_WANDER_SPEED,MAX_WANDER_SPEED)
        self.speedy= random.randint(MIN_WANDER_SPEED,MAX_WANDER_SPEED)
        #This is how the Wander gets it apperance and make sures that it is still on the screen.
    def update(self,p):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x < 0:
            self.speedx = -self.speedx
        if self.rect.y < 0:
            self.speedy=-self.speedy
        if self.rect.x+self.rect.width > SCREEN_WIDTH:
            self.speedx= -self.speedx
        if self.rect.y + self.rect.height > SCREEN_HEIGHT:
            self.speedy = -self.speedy
        #This is how the wander moves.
