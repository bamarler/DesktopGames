import pygame
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from src.constants.MainMenuConstants import *
from src.classes.Button import *

from src.games.TemplateGame import *
from src.games.ComingSoon import *

from src.games.FeedingFrenzy import *
from src.games.SnakeGame import *


import math

def main_menu():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Main Menu')
    clock = pygame.time.Clock()
    
    singleGameNames = [FEEDINGFRENZY, SNAKEGAME, MINESWEEPER, TWENTYFOURTYEIGHT, SUDOKU, TETRIS, FLAPPYBIRD]
    multiGameNames = [CHESS, TICTACTOE, TANKGAME]

    MULTIPLAYER_TEXT_Y = SINGLE_PLAYER_TEXT_Y + GAME_BUTTON_SPACING + GAME_BUTTON_HEIGHT_SPACE * (math.ceil(len(singleGameNames) / GAME_BUTTONS_PER_ROW))
    MULTIPLAYER_GAME_CY = MULTIPLAYER_TEXT_Y + GAME_BUTTON_HEIGHT

    singleButtons = list()

    for i in range(0, len(singleGameNames)):
        singleButtons.append(Button(screen, GAME_BUTTON_WIDTH, GAME_BUTTON_HEIGHT, singleGameNames[i], GAME_BUTTON_FONT, 
                              SINGLE_PLAYER_GAME_CX + GAME_BUTTON_WIDTH_SPACE * (i % GAME_BUTTONS_PER_ROW), 
                              SINGLE_PLAYER_GAME_CY + GAME_BUTTON_HEIGHT_SPACE * math.floor(i / GAME_BUTTONS_PER_ROW)))
        
    multiButtons = list()

    for i in range(0, len(multiGameNames)):
        multiButtons.append(Button(screen, GAME_BUTTON_WIDTH, GAME_BUTTON_HEIGHT, multiGameNames[i], GAME_BUTTON_FONT, 
                              MULTIPLAYER_GAME_CX + GAME_BUTTON_WIDTH_SPACE * (i % GAME_BUTTONS_PER_ROW), 
                              MULTIPLAYER_GAME_CY + GAME_BUTTON_HEIGHT_SPACE * math.floor(i / GAME_BUTTONS_PER_ROW)))

    # Main menu loop
    running = True
    while running:
        screen.fill(CHARCOAL)

        screen.blit(DESKTOP_GAME_TEXT, DESKTOP_GAME_RECT)

        screen.blit(SINGLE_PLAYER_TEXT, (SINGLE_PLAYER_TEXT_X, SINGLE_PLAYER_TEXT_Y))
        for button in singleButtons:
            button.draw()

        screen.blit(MULTIPLAYER_TEXT, (MULTIPLAYER_TEXT_X, MULTIPLAYER_TEXT_Y))
        for button in multiButtons:
            button.draw()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(0, len(singleButtons)):
                    if (singleButtons[i].clicked(event.pos)):
                        running = False
                        return singleGameNames[i]
                for i in range(0, len(multiButtons)):
                    if (multiButtons[i].clicked(event.pos)):
                        running = False
                        return multiGameNames[i]
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
        else:
            comingSoon = ComingSoon()
            current_screen = comingSoon.run()

if __name__ == "__main__":
    main()