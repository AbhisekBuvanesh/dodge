import pygame
import random
from constants import*
class Snake(pygame.sprite.Sprite):
    def __init__(self,p):
        super().__init__()
        self.rect = pygame.Rect(1,1,SNAKE_WIDTH,SNAKE_HEIGHT)
        self.image = pygame.image.load("zombie.png")
        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
        self.image = pygame.transform.flip(self.image, True, False)
        self.speedx= SNAKE_SPEED
        self.speedy= 0
        #This is how the snake appears in the beggining. 
    def update(self,p):
        if self.rect.x >= SCREEN_WIDTH:
            self.rect.y +=20
            self.speedx = -self.speedx
            self.image = pygame.transform.flip(self.image,True,False)
        if self.rect.x <= 0:
            self.rect.y += 20
            self.speedx= -self.speedx
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect.x += self.speedx
        self.rect.y +=self.speedy
        #This is how the snake zig zags across the screen