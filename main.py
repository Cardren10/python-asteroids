import pygame
import constants
import player
import asteroid
import asteroidfield

def main():
    # initialize pygame.
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode(size=(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create groups to manage game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)

    # instantiate player
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    p = player.Player(x, y)

    # instantiate asteroid field
    field = asteroidfield.AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        for game_object in updatable:
            game_object.update(dt)
        for game_object in drawable:
            game_object.draw(screen)
        pygame.display.flip()

        # Limit framerate to 60
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()