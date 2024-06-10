import pygame
from GamesConstants import *

pygame.init()

# name of this game
TEMPLATEGAME_TEXT = GAMENAME_TEXT_FONT.render(TEMPLATEGAME, True, GAMENAME_TEXT_COLOR)

# score constants
SCORE_SIZE = SCREEN_WIDTH / 30
SCORE_FONT = pygame.font.Font(None, int(SCORE_SIZE))
SCORE_COLOR = (255, 255, 255)

SIZE_TO_SCORE = SCREEN_AREA / 250000

# unique constants for this game