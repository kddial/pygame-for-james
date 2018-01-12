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

pygame.init()
def player(level):
    player = level
    if level == "title":
        pygame.draw.ellipse(screen,BLACK,[sscreen_x,sscreen_y,50,50])
def titleScreen1():
    try:
        title = font_1.render("Ellipse Adventure",True,BLACK)
        start_text = font_1.render("Start Game",True,BLACK)
        screen.blit(title,[275,100])
        screen.blit(start_text,[300,200])
    except:
        pass
    pygame.draw.rect(screen,DARKGREEN,[0,450,700,50])
def button(x,y):
    pygame.draw.rect(screen,RED,[x,y,300,100])
titleScreen = True
sscreen_x = 100
sscreen_y = 200
initial_jump = False
during_jump = False
can_jump = True
x_speed = 0
y_speed = 0
font_1 = pygame.font.Font(None,25)
font_2 = pygame.font.Font(None,60)
click = False
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -5
            elif event.key == pygame.K_RIGHT:
                x_speed = 5
            elif event.key == pygame.K_UP:
                if can_jump:
                    initial_jump = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            elif event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_SPACE:
                x_speed *= 0.5

    # --- Game logic should go here
    # i.e calculations for positions, variable updates
    #player jumping function
    pos = pygame.mouse.get_pos()
    x_mouse = pos[0]
    y_mouse = pos[1]
    print pos
    if x_mouse >= 200 and x_mouse <= 500 and y_mouse >= 160 and y_mouse <= 260 and click:
        print "ayy"
    if initial_jump:
        y_speed = -25
        initial_jump = False
        during_jump = True
        can_jump = False
    if during_jump:
        y_speed += 1
    sscreen_x += x_speed
    sscreen_y += y_speed
    if sscreen_x <= 0:
        x_speed = 0
    elif sscreen_x >= 600:
        x_speed = 0
    if sscreen_y >= 400:
        y_speed = 0
        sscreen_y = 400
        during_jump = False
        can_jump = True
    else:
        during_jump = True
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    if titleScreen:
        player("title")
        button(200,160)
        titleScreen1()
    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
