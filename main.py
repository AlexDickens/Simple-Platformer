import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()


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


while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit
            exit()

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_SPACE:
                playerGravity = -20
            

        
        
            

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
        print("collision")


    clock.tick(60)
    pygame.display.update()