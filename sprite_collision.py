import pygame

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
DARKGREEN= (  10,  89,  14)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
BROWN    = ( 153,  83,   9)
DARKPURPLE=(  60,  18,  76)
YELLOW   = ( 255, 233,   0)
LIGHTGRAY= ( 214, 213, 205)
ORANGE   = ( 255, 161,   0)
MAGENTA  = ( 219, 138, 242)
LIGHTBLUE= (  12, 170, 249)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = 0

    def x_move(self, speed):
        self.x_speed = speed

    def update(self):
        if self.x_speed != 0:
            self.rect.x = self.rect.x + self.x_speed

# Initialize game
pygame.init()

# Create a group of sprites so they can all be updated on every frame
all_sprites = pygame.sprite.Group()

# Set up the display
screen = pygame.display.set_mode((320, 240))

# Set game clock
clock = pygame.time.Clock()

# Create player sprite instance
player = Player(0, 100) # Create the player

# Add player sprite to the group of all sprites
# !!!!!! IMPORTANT !!!!!!
all_sprites.add(player);

# Run game loop
done = False
while not done:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_move(-5)
            elif event.key == pygame.K_RIGHT:
                player.x_move(5)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.x_move(0)
            elif event.key == pygame.K_RIGHT:
                player.x_move(0)


    # Update every sprite !!!!!! IMPORTANT !!!!!!
    all_sprites.update()

    # Draw the scene
    screen.fill(BLACK)

    # Draw all the sprites
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()
