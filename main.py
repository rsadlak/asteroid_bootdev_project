import pygame
from constants import *
from logger import log_state
from logger import log_event
from player import *
from asteroid import *
from asteroidfield import *
from sys import exit

def main():
    print(f"Starting Asteroids with pygame version {pygame.version.ver}!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    AsteroidField()

    while SCREEN_WIDTH == 1280:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')

        for u in updatable:
            u.update(dt)
        for a in asteroids:
            
            for s in shots:
                if a.collides_with(s):
                    log_event("asteroid_shot")
                    a.split()

            if a.collides_with(player):
                log_event("player_hit")
                print('Game over!')
                sys.exit()
        
        for d in drawable:
            d.draw(screen)



        pygame.display.flip()     
        dt = clock.tick(60)/1000
        print(dt)

if __name__ == "__main__":
    main()
