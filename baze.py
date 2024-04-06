from typing import Any
from pygame import *
import pygame
pygame.init()
font.init()
mixer.init()

W,H = 1000,600
window = pygame.display.set_mode((W,H))
background = transform.scale(image.load("fon.png"),(1000,600))
window.blit(background,(0,0))

Game = True
Fin = False

class GameSprite(sprite.Sprite):
  
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and  self.rect.y > 0:
            self.rect.y -= 10
        if keys[pygame.K_DOWN] and self.rect.y < 400:
            self.rect.y += 10

    def update2(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and  self.rect.y > 0:
            self.rect.y -= 10
        if keys[pygame.K_s] and self.rect.y < 400:
            self.rect.y += 10
    
class Ball(GameSprite):

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        pass

ball = Ball("img/ball.png.png", 200, 200, 2, 50, 50)

p1 = GameSprite("img/lat.png", 15,0,1,50,200)
p2 = GameSprite("img/lat.png", 940,0,1,50,200)

clock = pygame.time.Clock()

dx = 3
dy = 3
        
while Game:
    window.blit(background,(0,0))
    p2.reset()
    p1.reset()
    ball.reset()
    p2.update()
    p1.update2()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            Game = False
            Fin = True        

    ball.rect.x += dx
    ball.rect.y += dy
    if ball.rect.y > 550:
        dy *= -1
    
    if ball.rect.y < 0:
        dy *= -1
    
    if ball.rect.colliderect(p2.rect):
        dx *= -1
    
    if ball.rect.colliderect(p1.rect):
        dx *= -1
    
    pygame.display.update()
    clock.tick(60)        