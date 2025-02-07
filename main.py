import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)

    while(True):
        screen.fill("Black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.draw(screen)
        
        player.update(dt)
        
        dt = clock.tick(60) / 1000
        

        pygame.display.flip()


if __name__ == "__main__":
    main()
