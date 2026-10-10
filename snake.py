import pygame
import random
import sys

score = 0
size = 40

pygame.init()

window = pygame.display.set_mode((800, 600))
window.fill((255,255,255))
pygame.display.set_caption("Snake Game")

player = pygame.surface.Surface((size, size))
player.fill((0,255,0))

adder = pygame.surface.Surface((size, size))
adder.fill((0,0,255))

snake_segments = [[size, size]]

move_timer = 0
delay = 200

player_vel_x=0
player_vel_y=0

object = pygame.surface.Surface((50,50))
object.fill((0,0,0))

object_x = random.randint(0, 800 - 100)
object_y = 0
object_vel_x = 0
object_vel_y = 0

player_x, player_y = snake_segments[0]

def collision_detection():
    player_x, player_y = snake_segments[0]
    return (player_x <= (object_x + int(object.get_width())) and
            (player_x + player.get_width()) >= object_x and
            player_y <= (object_y + object.get_height() + 5) and 
            (player_y + player.get_height()) >= object_y)

game_state = 1

clock = pygame.time.Clock()

while True:
    dt = clock.tick(60)
    #take input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player_vel_x == 0:
                player_vel_x = -size
                player_vel_y = 0
            if event.key == pygame.K_RIGHT and player_vel_x == 0:
                player_vel_x = size
                player_vel_y = 0
            if event.key == pygame.K_UP and player_vel_y == 0:
                player_vel_y = -size
                player_vel_x = 0
            if event.key == pygame.K_DOWN and player_vel_y == 0:
                player_vel_y = size
                player_vel_x = 0
            if event.key == pygame.K_ESCAPE:
                game_state = 2

    if collision_detection():
        object_y = random.randint(0, 800 - 100)
        object_x = random.randint(0, 800 - 100)
        score += 50

        last_segment = snake_segments[-1]
        snake_segments.append([last_segment[0], last_segment[1]])

    if object_y >= 600:
        object_y = 100
        
    #output
    window.fill((255,255,255))
    if game_state == 1:

        player_x, player_y = snake_segments[0]

        if player_x < 0 or player_x > 800 or player_y < 0 or player_y > 600:
            game_state = 2

        object_x += object_vel_x
        object_y += object_vel_y
        window.blit(object, (object_x,object_y))

        move_timer += dt
        if move_timer >= delay:
            move_timer = 0

            if player_vel_x != 0 or player_vel_y != 0:

                for i in range(len(snake_segments)-1,0,-1):
                    snake_segments[i][0] = snake_segments[i-1][0]
                    snake_segments[i][1] = snake_segments[i-1][1]

                snake_segments[0][0] += player_vel_x
                snake_segments[0][1] += player_vel_y

        for index, pos in enumerate(snake_segments):
            if index == 0:
                window.blit(player, (pos[0], pos[1]))
            else:
                window.blit(adder, (pos[0], pos[1]))

    elif game_state == 2:
        print("Game Over")
        print(f"Score: {score}")
        pygame.quit()
        sys.exit()

        
    pygame.display.flip()




    