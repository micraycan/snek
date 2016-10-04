import pygame
import random

pygame.init()

# window dimensions
display_width = 800
display_height = 600

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('snek v0.2')
clock = pygame.time.Clock()
FPS = 15

# snek variables
block_size = 10


def snek(block_size, sneklist):
    for XnY in sneklist:
        pygame.draw.rect(gameDisplay, black, [XnY[0], XnY[1], block_size, block_size])


def text_objects(msg, font):
    textSurface = font.render(msg, True, red)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color):
    largeText = pygame.font.SysFont("comicsansms", 15)
    TextSurf, TextRect = text_objects(msg, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)


def game_loop():
    # game variables
    running = True
    game_over = False

    # snek lead variables
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0
    snek_list = []
    snek_length = 1

    # apple stuff
    rand_apple_x = round(random.randrange(0, display_width - block_size * 2) / 10) * 10
    rand_apple_y = round(random.randrange(0, display_height - block_size * 2) /10) * 10


    while running:

        # game over check and menu
        while game_over:
            gameDisplay.fill(white)
            message_to_screen('snek is rip. press F to pay respeks or Q to quit', red)
            pygame.display.update()

            # game over event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        game_loop()

                    if event.key == pygame.K_q:
                        running = False
                        game_over = False

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if lead_x_change != block_size:
                        lead_y_change = 0
                        lead_x_change = -block_size
                elif event.key == pygame.K_RIGHT:
                    if lead_x_change != -block_size:
                        lead_y_change = 0
                        lead_x_change = block_size
                elif event.key == pygame.K_UP:
                    if lead_y_change != block_size:
                        lead_x_change = 0
                        lead_y_change = -block_size
                elif event.key == pygame.K_DOWN:
                    if lead_y_change != -block_size:
                        lead_x_change = 0
                        lead_y_change = block_size

        # snek speed
        lead_x += lead_x_change
        lead_y += lead_y_change

        # outter boundaries
        if (lead_x > display_width - block_size or
            lead_x < 0 or
            lead_y > display_height - block_size or
            lead_y < 0):
            
            game_over = True

        # draw and updoot
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [rand_apple_x, rand_apple_y, block_size, block_size])

        snek_head = []
        snek_head.append(lead_x)
        snek_head.append(lead_y)
        snek_list.append(snek_head)

        # prevent snek from increasing length constantly
        if len(snek_list) > snek_length:
            del snek_list[0]

        for each_segment in snek_list[:-1]:
            if each_segment == snek_head:
                game_over = True

        snek(block_size, snek_list)

        pygame.display.update()

        # snek eat apple
        if lead_x == rand_apple_x and lead_y == rand_apple_y:
            rand_apple_x = round(random.randrange(0, display_width - block_size * 2) / 10) * 10
            rand_apple_y = round(random.randrange(0, display_height - block_size * 2) /10) * 10
            snek_length += 5

        clock.tick(FPS)

game_loop()
pygame.quit()
quit()