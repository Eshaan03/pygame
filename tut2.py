import pygame
import random
import os
pygame.init()
# Window Creation
screen_width = 900
screen_height = 600
# Colours
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
orange = (200, 34, 34)
random_colour = (57, 57, 90)
gameWindow = pygame.display.set_mode((screen_height, screen_height))
pygame.display.set_caption("Game Project")
pygame.display.update()
# Game Variables

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, colour, snake_list, snake_size):
    for x, y in snake_list:
     pygame.draw.rect(gameWindow, colour, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(orange)
        text_screen("Welcome!", black, 210, 200)
        text_screen("Press SpaceBar to play", black, 100, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(30)



def gameloop():
    exit_game = False
    game_over = False
    snake_x = 55
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size = 10
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    fps = 30
    snake_list = []
    snake_length = 1
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(black)
            text_screen("Game Over!", white, 10, 50)
            text_screen("Press Enter to continue.", white, 10, 100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 5
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - 5
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - 5
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = 5
                        velocity_x = 0
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score = score + 10
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snake_length = snake_length + 1
            if score > int(highscore):
                highscore = score

            gameWindow.fill(random_colour)
            text_screen("Score: " + str(score)+"  High score"+str(highscore), red, 5, 5)
            pygame.draw.rect(gameWindow, white, [food_x, food_y, snake_size, snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True


            plot_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()