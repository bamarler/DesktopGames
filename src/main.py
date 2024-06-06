import pygame
import sys
from MainMenuConstants import *
from FeedingFrenzy import *
from Button import *

def main_menu():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Main Menu')
    clock = pygame.time.Clock()
    
    buttons = [
        Button(screen, B1_NAME, BUTTON_FONT, B1_CX, B1_CY, B1_LX, B1_RX, B1_LY, B1_RY),
        Button(screen, B2_NAME, BUTTON_FONT, B2_CX, B2_CY, B2_LX, B2_RX, B2_LY, B2_RY),
        Button(screen, B3_NAME, BUTTON_FONT, B3_CX, B3_CY, B3_LX, B3_RX, B3_LY, B3_RY),
        Button(screen, B4_NAME, BUTTON_FONT, B4_CX, B4_CY, B4_LX, B4_RX, B4_LY, B4_RY)
    ]

    # Main menu loop
    running = True
    while running:
        screen.fill(CHARCOAL)

        for button in buttons:
            button.draw()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (buttons[0].clicked(event.pos)):
                    running = False
                    return B1_NAME
                elif (buttons[1].clicked(event.pos)):
                    running = False
                    return MAINMENU
                elif (buttons[2].clicked(event.pos)):
                    running = False
                    return MAINMENU
                elif (buttons[3].clicked(event.pos)):
                    running = False
                    return MAINMENU
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
        elif (current_screen == B1_NAME):
            feedingFrenzy = FeedingFrenzy()
            current_screen = feedingFrenzy.run()
        elif (current_screen == QUIT):
            running = False

if __name__ == "__main__":
    main()