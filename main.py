import pygame
from sys import exit
from activity1_screen import activity1_screen
from display import Display, get_font

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Theory of Mind')

    while True:
        screen.blit(pygame.image.load('assets/background.png'), (0,0))
        menu_mouse_pos = pygame.mouse.get_pos()

        menu = Display(pos=(400,100), text_input=" Main Menu ", font=get_font(100), base_color="Black")
        activity1_button = Display(pos=(400,250), text_input=" Activity 1 ", font=get_font(70), base_color="Black")
        activity2_button = Display(pos=(400,360), text_input=" Activity 2 ", font=get_font(70), base_color="Black")
        quit_button = Display(pos=(400,470), text_input=" Quit ", font=get_font(70), base_color="Black")

        menu.draw_text(screen)
        for button in [activity1_button, activity2_button, quit_button]:
            button.draw_button(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if activity1_button.checkForInput(menu_mouse_pos):
                    activity1_screen(screen)
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    exit()

        pygame.display.update()

main()