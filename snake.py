import pygame
import random

score = 0

pygame.init()

window = pygame.display.set_mode((800, 600))
window.fill((255,255,255))
pygame.display.set_caption("Snake Game")

player = pygame.surface.Surface((100,100))
player.fill((0,255,0))

adder = pygame.surface.Surface((100,50))
adder.fill((0,0,255))

player_x=0
player_y=0

player_vel_x=0
player_vel_y=0

adder_x = -100
adder_y = 0

falling_object = pygame.surface.Surface((50,50))
falling_object.fill((0,0,0))

falling_object_x = 0
falling_object_y = 0
falling_object_vel_x = 0
falling_object_vel_y = 0

def collision_detection():
    return (player_x <= (falling_object_x + int(falling_object.width)) and
            (player_x + player.width) >= falling_object_x and
            player_y <= (falling_object_y + falling_object.height + 5) and 
            (player_y + player.height) >= falling_object_y)

game_state = 1

while True:
    #take input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_vel_x = -0.5
                player_vel_y = 0
            if event.key == pygame.K_RIGHT:
                player_vel_x = 0.5
                player_vel_y = 0
            if event.key == pygame.K_UP:
                player_vel_y = -0.5
                player_vel_x = 0
            if event.key == pygame.K_DOWN:
                player_vel_y = 0.5
                player_vel_x = 0
            if event.key == pygame.K_ESCAPE:
                game_state = 2
        else: 
            player_vel_x = 0
            player_vel_y = 0

    if collision_detection():
        falling_object_y = random.randint(0, window.width - 50)
        falling_object_x = random.randint(0, window.width - 50)
        score += 50

    if falling_object_y >= 600:
        falling_object_y = 100
        
    #output
    window.fill((255,255,255))
    if game_state == 1:
        player_x += player_vel_x
        player_y += player_vel_y

        window.blit(player, (player_x,player_y))


        falling_object_x += falling_object_vel_x
        falling_object_y += falling_object_vel_y
        window.blit(falling_object, (falling_object_x,falling_object_y))

    elif game_state == 2:
        print("Game Over")
        print(f"Score: {score}")
    pygame.display.flip()




    