import pygame
from Constants import *

pygame.init()

DESKTOP_GAME_TEXT_SIZE = SCREEN_AREA / 8000
DESKTOP_GAME_FONT = pygame.font.SysFont(FONT, int(DESKTOP_GAME_TEXT_SIZE))
DESKTOP_GAME_TEXT = DESKTOP_GAME_FONT.render(MAINMENU, True, WHITE)
DESKTOP_GAME_RECT = DESKTOP_GAME_TEXT.get_rect()
DESKTOP_GAME_RECT.center = (CX, SCREEN_HEIGHT / 7)

GAME_BUTTONS_PER_ROW = 4

GAME_BUTTON_WIDTH = SCREEN_WIDTH / (GAME_BUTTONS_PER_ROW + 1)
GAME_BUTTON_HEIGHT = SCREEN_HEIGHT / 8

GAME_BUTTON_TEXT_SIZE = GAME_BUTTON_WIDTH / (GAME_BUTTONS_PER_ROW * 0.4 + 5.2)
GAME_BUTTON_SPACING = GAME_BUTTON_WIDTH / (GAME_BUTTONS_PER_ROW + 1)

GAME_BUTTON_FONT = pygame.font.SysFont(FONT, int(GAME_BUTTON_TEXT_SIZE))

GAME_BUTTON_WIDTH_SPACE = GAME_BUTTON_WIDTH + GAME_BUTTON_SPACING
GAME_BUTTON_HEIGHT_SPACE = GAME_BUTTON_HEIGHT + GAME_BUTTON_SPACING

GAME_BASE_CX = GAME_BUTTON_WIDTH * 1 / 2 + GAME_BUTTON_SPACING
GAME_BASE_CY = GAME_BUTTON_HEIGHT_SPACE * 2