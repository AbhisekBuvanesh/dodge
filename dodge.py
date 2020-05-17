import pygame
import pickle
from homing import *
from fast import *
import goal
import player
from wander import *
from constants import *
from snake import *
 # these are all the files needed in order to make this game
pygame.init()
def game():
    data = {}
    try:
        data = pickle.load(open("data","rb"))
    except:
        pass
    print(data)
    # This is to make sure that the score of the player is remembered
    name = input("Whats your name? ")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    p = player.Player()
    enemies= pygame.sprite.Group()
    enemies.add(Wander(p))
    g = goal.Goal(p)
    score = 0
    scoreFont = pygame.font.SysFont("Arial",24)
    gameOver = False
    gameOverFont = pygame.font.SysFont("Arial", 100)
    playing = True
    # This is creating the start of the game
    while playing:
        if gameOver == True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_e:
                        playing = False
                    if e.key == pygame.K_r:
                        gameOver = False
                        enemies = pygame.sprite.Group()
        # These are the keys for what happens after the game is over.
            screen.fill((255,0,0))
            gameOverText = gameOverFont.render("Game Over", False, (0,0,0))
            screen.blit(gameOverText, (300,200))
            restart = gameOverFont.render( " Press r to restart", False, (0,0,0))
            screen.blit(restart, (300, 300))
            exit = gameOverFont.render( " Press e to exit", False, (0,0,0))
            screen.blit(exit, (300,400))
            #These are the text that are going to display at the end of the game
            offset = 0
            scores = []
            for n in data:
                scores.append([data[n],n])
            scores = sorted(scores)
            for s in scores:
                score = scoreFont.render( s[1] + " - "+ str(s[0]),False, (0,255,0) )
                screen.blit(score, (10,10+offset))
                offset+=25

            pygame.display.update()
            continue
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    p.speedx = -PLAYER_SPEED
                if e.key == pygame.K_RIGHT:
                    p.speedx = PLAYER_SPEED
                if e.key == pygame.K_DOWN:
                    p.speedy = PLAYER_SPEED
                if e.key == pygame.K_UP:
                    p.speedy = -PLAYER_SPEED
                    #This code controls how the player moves.
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT and p.speedx == -PLAYER_SPEED:
                    p.speedx= 0
                if e.key == pygame.K_RIGHT and p.speedx == PLAYER_SPEED:
                    p.speedx = 0
                if e.key == pygame.K_DOWN and p.speedy  == PLAYER_SPEED:
                    p.speedy = 0
                if e.key == pygame.K_UP and p.speedy == -PLAYER_SPEED:
                    p.speedy = 0
                    #This code is to make sure that the player does not run  out of the screen.
        screen.fill(BACKGROUND_COLOR)
        #update
        p.update()
        for e in enemies:
            e.update(p)
            screen.blit(e.image,(e.rect.x,e.rect.y))
        #collisions
        if pygame.sprite.spritecollideany(p,enemies):
            gameOver = True
            if name not in data:
                data[name] = score
            elif data[name] < score:
                data[name]=score
            pickle.dump(data,open("data","wb"))
        if g.rect.contains(p.rect):
            score +=1
            g = goal.Goal(p)
            r = random.uniform(0,1)
            if r < WANDER_CHANCE:
                enemies.add(Wander(p))
            elif r < SNAKE_CHANCE:
                enemies.add(Snake(p))
            elif r < HOMING_CHANCE:
                enemies.add(Homing(p))
        #This code is responsible for which enemies form every point you earn.


        text = scoreFont.render("score: " + str(score), False, (255, 255, 255))
        screen.blit(text,(10,10))
        screen.blit(g.image, (g.rect.x, g.rect.y))
        screen.blit(p.image, (p.rect.x, p.rect.y))
        pygame.display.update()
        clock.tick(50)
        #This is the basic screen which we begin to draw on in the starting code.


game()