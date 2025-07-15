import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

time = pygame.time.Clock()
dt = 0
updatable_group = pygame.sprite.Group()
drawable_group = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()
shot_group = pygame.sprite.Group()
Player.containers = (updatable_group, drawable_group)
Shot.containers = (updatable_group, drawable_group, shot_group)
Asteroid.containers = (updatable_group, drawable_group, asteroid_group)
AsteroidField.containers = (updatable_group)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt =time.tick(60)/1000
        screen.fill(BLACK)
        updatable_group.update(dt)
        for i in drawable_group:
            i.draw(screen)
        for asteroid in asteroid_group:
            for shot in shot_group:
                if shot.collision(asteroid) == True:
                    shot.kill()
                    asteroid.split()
        for asteroid in asteroid_group:
            if player.collision(asteroid) == True:
                print("Game over!")
                sys.exit()
        pygame.display.flip()

if __name__ == "__main__":
    main()
