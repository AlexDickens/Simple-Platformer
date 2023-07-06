import pygame
from sys import exit
import requests
import time
import json
import pyautogui
from homeScreen import homescreen


class runner:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 400
        self.screen = pygame.display.set_mode((self.width , self.height))
        self.clock = pygame.time.Clock()
        self.score = 0
        self.font = pygame.font.Font("font/Pixeltype.ttf", 50)
        self.gameActive = False
        self.high_score = False



        self.sky = pygame.image.load("sprites/Sky.png").convert()
        self.ground = pygame.image.load("sprites/ground.png").convert()

        #enemy
        self.enemy = pygame.image.load("sprites/snail/snail1.png").convert_alpha()
        self.enemy_rect = self.enemy.get_rect(bottomleft = (700,300))

        #player
        self.player = pygame.image.load("sprites/Player/player_walk_1.png").convert_alpha()
        self.player_rect = self.player.get_rect(bottomleft = (50,300))
        self.playerGravity = 0


        self.home = homescreen()

    def game_loop(self):

        while True:

            self.event_loop()
            self.render_graphics()


            self.clock.tick(60)
            pygame.display.update()

    def event_loop(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit
                exit()

            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE and self.gameActive == True:
                    if self.player_rect.bottom == 300:
                        self.playerGravity = -20
                if events.key == pygame.K_SPACE and self.gameActive == False:
                    self.gameActive = True
                    self.enemy_rect.x = 800
                    

    def render_graphics(self):
        if (self.gameActive == True):    

        

            self.screen.blit(self.sky , (0,0))
            self.screen.blit(self.ground, (0,300))
            self.screen.blit(self.enemy, self.enemy_rect)
            self.screen.blit(self.player, self.player_rect)
            #currentTime()


            #moving snail
            self.enemy_rect.x -= 4

            if (self.enemy_rect.x < -50):
                self.enemy_rect.x = 850

            #allowJumping 
            self.playerGravity += 1
            self.player_rect.y += self.playerGravity

            if self.player_rect.bottom >= 300:
                self.player_rect.bottom = 300


            #collisiom

            if self.player_rect.colliderect(self.enemy_rect):
                self.gameActive = False

        elif (self.gameActive == False):
            self.home.homeScreen(self.screen, self.font)

    


game = runner()
game.game_loop()







