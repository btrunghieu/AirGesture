import pygame, sys, random
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
screen_wight = 1280
screen_hight = 720
screen = pygame.display.set_mode((screen_wight, screen_hight))
pygame.display.set_caption('Pong')

ball = pygame.Rect(screen_wight / 2 - 15, screen_hight/2 - 15, 30, 30)
player = pygame.Rect(screen_wight- 20, screen_hight/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_hight/2 - 70, 10, 140)

bg_color = pygame.Color('gray12')
light_grey = (200, 200, 200)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

def animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.left <=0 or ball.right >=screen_wight:
       reset_ball()
    if ball.top <=0 or ball.bottom >=screen_hight:
       ball_speed_y *=-1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *=-1
        
def player_animation():
    player.y +=player_speed
    if player.top <=0:
        player.top = 0
    if player.bottom >= screen_hight:
        player.bottom = screen_hight

def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.top -= opponent_speed
    if opponent.top <=0:
        opponent.top = 0
    if opponent.bottom >= screen_hight:
        opponent.bottom = screen_hight
  
def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_wight/ 2, screen_hight/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_a:
                player_speed +=7
            if event.key == K_d:
                player_speed -=7
        if event.type == KEYUP:
            if event.key == K_a:
                player_speed -=7
            if event.key == K_d:
                player_speed +=7
            
    animation()
    player_animation()
    opponent_animation()

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_wight/2, 0),(screen_wight/2, screen_hight))
    pygame.display.flip()
    clock.tick(60)
    