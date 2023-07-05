import pygame
from sys import exit

pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode((width , height))
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font("font/Pixeltype.ttf", 50)
gameActive = False

def homeScreen():
   
 

    screen.fill((0,153,153))
    text1 = font.render("Alex Dickens Runner", False, (0,102,102))
    text1_rect = text1.get_rect(center = (width * 0.5, 100))
    
    
    homeImage = pygame.image.load("sprites/Player/player_walk_1.png")
    homeImage_rect = homeImage.get_rect(center = (width * 0.5, height * 0.5))
    restart = font.render("Press space to run", False, (0,102,102))
    restart_rect = restart.get_rect(center = (width * 0.5, 300))

    screen.blit(text1, text1_rect)
    
    screen.blit(homeImage, homeImage_rect)
    screen.blit(restart, restart_rect)


#scene
sky = pygame.image.load("sprites/Sky.png").convert()
ground = pygame.image.load("sprites/ground.png").convert()

#enemy
enemy = pygame.image.load("sprites/snail/snail1.png").convert_alpha()
enemy_rect = enemy.get_rect(bottomleft = (700,300))

#player
player = pygame.image.load("sprites/Player/player_walk_1.png").convert_alpha()
player_rect = player.get_rect(bottomleft = (50,300))
playerGravity = 0


fly = pygame.image.load("sprites/Fly/Fly1.png")


while True:

   
    
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit
            exit()

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_SPACE and gameActive == True:
                if player_rect.bottom == 300:
                    playerGravity = -20
            if events.key == pygame.K_SPACE and gameActive == False:
                gameActive = True
            

        
        
    if (gameActive == True):    

        screen.blit(sky , (0,0))
        screen.blit(ground, (0,300))
        screen.blit(enemy, enemy_rect)
        screen.blit(player, player_rect)


        #moving snail
        enemy_rect.x -= 4

        if (enemy_rect.x < -50):
            enemy_rect.x = 850

        #allowJumping 
        playerGravity += 1
        player_rect.y += playerGravity

        if player_rect.bottom >= 300:
            player_rect.bottom = 300


        #collisiom

        if player_rect.colliderect(enemy_rect):
            gameActive = False

    elif (gameActive == False):
        homeScreen()


    clock.tick(60)
    pygame.display.update()