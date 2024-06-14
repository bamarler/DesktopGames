import pygame
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from src.constants.MainMenuConstants import *
from src.classes.Button import *
from src.games.FeedingFrenzy import *
from src.games.SnakeGame import *
from src.games.TemplateGame import *

def main_menu():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Main Menu')
    clock = pygame.time.Clock()
    
    gameNames = [FEEDINGFRENZY, SNAKEGAME, TEMPLATEGAME, TEMP_GAME_NAME, TEMP_GAME_NAME]

    buttons = list()

    for i in range(0, len(gameNames)):
        buttons.append(Button(screen, GAME_BUTTON_WIDTH, GAME_BUTTON_HEIGHT, gameNames[i], GAME_BUTTON_FONT, 
                              GAME_BASE_CX + GAME_BUTTON_WIDTH_SPACE * (i % GAME_BUTTONS_PER_ROW), 
                              GAME_BASE_CY + GAME_BUTTON_HEIGHT_SPACE * math.floor(i / GAME_BUTTONS_PER_ROW)))

    # Main menu loop
    running = True
    while running:
        screen.fill(CHARCOAL)

        screen.blit(DESKTOP_GAME_TEXT, DESKTOP_GAME_RECT)

        for button in buttons:
            button.draw()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(0, len(buttons)):
                    if (buttons[i].clicked(event.pos)):
                        running = False
                        return gameNames[i]
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):
                    running = False
                    return QUIT
        clock.tick(TICK_SPEED)

    pygame.quit()

def main():
    pygame.init()

    current_screen = MAINMENU
    running = True

    while running:
        if (current_screen == MAINMENU):
            current_screen = main_menu()
        if (current_screen == TEMP_GAME_NAME):
            current_screen = main_menu()
        elif (current_screen == FEEDINGFRENZY):
            feedingFrenzy = FeedingFrenzy()
            current_screen = feedingFrenzy.run()
        elif (current_screen == SNAKEGAME):
            snakeGame = SnakeGame()
            current_screen = snakeGame.run()
        elif (current_screen == TEMPLATEGAME):
            templateGame = TemplateGame()
            current_screen = templateGame.run()
        elif (current_screen == QUIT):
            running = False

if __name__ == "__main__":
    main()