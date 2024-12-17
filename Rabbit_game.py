import pygame
import random
def game_intro():

    intro = True
    font = pygame.font.SysFont('comicsansms', 115)
    text_surface = font.render('Rabbit Jump', True, white)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (display_width / 2, display_height / 2)
    game_display.blit(text_surface, text_rectangle)
    game_display.blit(carrot_image, (300, 20))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        button('Play', 150, 450, 100, 50, green, bright_green, game_loop)
        button('Quit', 550, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(15)

def rabbit(x, y):
    game_display.blit(rabbit_image, (x, y))
def carrot(x, y):
    game_display.blit(carrot_image, (x, y))
def obstacle(x, y, width, height, color):
    pygame.draw.rect(game_display, color, [x, y, width, height])
def you_win():
    pygame.mixer.music.stop()

    font = pygame.font.SysFont('comicsansms', 50)
    text_surface = font.render('You Won!', True, black)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (display_width/2, display_height/2)
    game_display.blit(text_surface, text_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        button('Play again', 150, 450, 100, 50, green, bright_green, game_loop)
        button('Quit', 550, 450, 100,50,red, bright_red, quit_game)
        pygame.display.update()
        clock.tick(15)
def gameover():
    pygame.mixer.music.stop()
    font = pygame.font.SysFont('comicsansms', 50)
    text_surface = font.render('Game Over', True, black)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (display_width/2, display_height/2)
    game_display.blit(text_surface, text_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        button('Play again', 150, 450, 100, 50, green, bright_green, game_loop)
        button('Quit', 550, 450, 100,50,red, bright_red, quit_game)
        pygame.display.update()
        clock.tick(15)
def quit_game():
    pygame.quit()
    quit()

def game_loop():
    game_over = False
    pygame.mixer.music.load('jazz.mp3')
    pygame.mixer.music.play(-1)
    rabbit_x = display_width * 0.45
    rabbit_y = display_height * 0.8
    obstacle_y = rabbit_y + 80
    obstacle_x = -600
    obstacle_width = 200
    obstacle_height = 37.5
    rabbit_width = 73
    rabbit_height = 92
    obstacle_speed = 15
    y_change = 0
    obstacle_count = 0
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pygame.mixer.Sound.play(jump_sound)
                jumpMax = 55
                jumpCount = 55
                rabbit_y -= jumpCount
                if jumpCount > -jumpMax:
                    jumpCount -= 2
            if event.type == pygame.KEYUP:
                rabbit_y += jumpCount/4
                obstacle_count += 1
                pygame.draw.rect(game_display, gray, [obstacle_x, obstacle_y, 37.5, 200])
                if jumpCount > -jumpMax/4:
                    jumpCount -= 2
                    if rabbit_bottom <= obstacle_top and obstacle_left <= 560 and obstacle_right >= 160 and obstacle_left > 160 and obstacle_right < 560:
                        obstacle_speed = 0
                elif jumpCount <= -jumpMax/4 and obstacle_left <= 560 and obstacle_right >= 160 and obstacle_left > 160 and obstacle_right < 560:
                    rabbit_y - 30
                    game_over = True
                    gameover()
                else:
                    jump = False
        
        rabbit_y += y_change
        obstacle_x += obstacle_speed

        if obstacle_x > display_width:
            obstacle_x = -100
            obstacle_y = rabbit_y + rabbit_height - 15       
        game_display.fill(white)
        carrot(300, 5)
        rabbit(rabbit_x, rabbit_y)
        obstacle(obstacle_x, obstacle_y, obstacle_width, obstacle_height, gray)
        if rabbit_y <= 25:
            you_win()

        # Collision with an obstacle
        rabbit_left = rabbit_x
        rabbit_right = rabbit_x + rabbit_width
        rabbit_top = rabbit_y
        rabbit_bottom = rabbit_y + rabbit_height
        obstacle_left = obstacle_x
        obstacle_right = obstacle_x + obstacle_width
        obstacle_top = obstacle_y
        obstacle_bottom = obstacle_y - obstacle_height
        if rabbit_bottom >= obstacle_top and rabbit_top <= obstacle_bottom and rabbit_left < obstacle_right and rabbit_right > obstacle_left:
            if rabbit_right >= obstacle_left and rabbit_left <= obstacle_left:
                # collision from the left
                game_over = True
                gameover()
            elif rabbit_left <= obstacle_right and rabbit_right >= obstacle_right:
                # collision from the right
                game_over = True
                gameover()
        pygame.display.update()
        clock.tick(60)

def button(message, x, y, width, height, inactive_color, active_color, action=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(game_display, inactive_color, (x,y,width, height))
    font = pygame.font.SysFont('comicsansms', 20)
    text_surface = font.render(message, True, white)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (x + width/2, y + height/2)
    game_display.blit(text_surface, text_rectangle)

    #check if mouse is on top of the button
    if mouse_x in range (x,x+width+1) and mouse_y in range(y,y+height+1):
        pygame.draw.rect(game_display, active_color, (x,y,width, height))
        #print('mouse on the button')
        #check if user clicked button
        if click[0] and action != None:
            action()
    else:
        pygame.draw.rect(game_display, inactive_color, (x,y,width, height))
        font = pygame.font.SysFont('comicsansms', 20)
        text_surface = font.render(message, True, white)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (x + width/2, y + height/2)
        game_display.blit(text_surface, text_rectangle)

####MAIN BODY####
pygame.init()

display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Rabbit Jump')

clock = pygame.time.Clock()
rabbit_image = pygame.image.load('rabbit3.png')
carrot_image = pygame.image.load('carrot.png')
jump_sound = pygame.mixer.Sound('jump_sound.mp3')
crash_sound = pygame.mixer.Sound('crash.wav')

white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)
red = (100, 0, 0)
bright_red = (255, 0, 0)
green = (0, 100, 0)
bright_green = (0, 255, 0)
gray = (100,100,100)
game_intro()



#Sound Effect from <a href="https://pixabay.com/sound-effects/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=6462">Pixabay</a>