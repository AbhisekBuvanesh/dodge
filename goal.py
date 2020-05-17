import pygame
import random
from constants import*
class Goal(pygame.sprite.Sprite):
    def __init__(self,p):
        super().__init__()
        x = random.randint(0,SCREEN_WIDTH-GOAL_WIDTH)
        y = random.randint(0,SCREEN_HEIGHT-GOAL_HEIGHT)
        while(abs(p.rect.x-x)+abs(p.rect.y-y)<200):
            x = random.randint(0, SCREEN_WIDTH - GOAL_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT - GOAL_HEIGHT)
        self.rect = pygame.Rect(x,y,GOAL_WIDTH,GOAL_HEIGHT)
        self.image = pygame.image.load("goal.jpg")
        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
                                                        
        #This is how the goal moves to random places in the screen while still staying on the screen.                                            

