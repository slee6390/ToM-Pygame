import pygame
from sys import exit
from button import Button
import activity1

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Theory of Mind')

def get_font(size):
    return pygame.font.Font('open-sans/OpenSans-Regular.ttf', size)

def activity1_screen():
    # declare variables
    start_screen2 = True
    start_screen3 = True
    activity = 1
    screen_num = 1

    pygame.display.set_caption('Theory of Mind')
    font = pygame.font.Font('open-sans/OpenSans-Regular.ttf', 30)

    apple_box = activity1.Apple_box()
    grape_box = activity1.Grape_box()
    continue_button = activity1.Continue_button(font)
    child = activity1.Child()

    # static text (instructions, results, etc.)
    try_again_surf = font.render(' Try Again ', True, 'Red')
    try_again_rect = try_again_surf.get_rect(center = (400, 170))

    instructions1_1_surf = font.render('Click on each box to see its contents.', True, 'Black')
    instructions1_1_rect = instructions1_1_surf.get_rect(center = (400, 60))

    instructions1_2_surf = font.render('Press continue when you know what is in each box.', True, 'Black')
    instructions1_2_rect = instructions1_2_surf.get_rect(center = (400, 100))

    instructions2_surf = font.render('Click on the box that has an apple inside it.', True, 'Black')
    instructions2_rect = instructions2_surf.get_rect(center = (400, 60))

    instructions2_correct_surf = font.render('Great! Now press continue.', True, 'Black')
    instructions2_correct_rect = instructions2_correct_surf.get_rect(center = (400, 100))

    instructions3_1_surf = font.render('This child just entered the room.', True, 'Black')
    instructions3_1_rect = instructions3_1_surf.get_rect(center = (400, 60))

    instructions3_2_surf = font.render('He does not know which box the apple is in.', True, 'Black')
    instructions3_2_rect = instructions3_2_surf.get_rect(center = (400, 100))

    instructions3_3_surf = font.render('Where would he most likely look for the apple?', True, 'Black')
    instructions3_3_rect = instructions3_3_surf.get_rect(center = (400, 140))

    correct_surf = font.render('You are correct!', True, 'Black')
    correct_rect = correct_surf.get_rect(center = (400, 170))

    incorrect_surf = font.render('Sorry, that is incorrect!', True, 'Black')
    incorrect_rect = incorrect_surf.get_rect(center = (400, 170))

    return_surf = font.render(' Return to Main Menu ', True, 'Black')
    return_rect = return_surf.get_rect(center = (400, 250))

    background = pygame.image.load('assets/game1/background.png')

    while True:
        click = False
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                click = True

        # instruction screen
        if activity == 1:
            screen.blit(background, (0,0))

            if screen_num == 1:
                screen.blit(instructions1_1_surf, instructions1_1_rect)
                screen.blit(instructions1_2_surf, instructions1_2_rect)

                continue_button.draw(screen, continue_button)
                if continue_button.continue_screen(click, screen):
                    screen_num = 2

                apple_box.draw_change(click, screen)
                grape_box.draw_change(click, screen)

                pygame.display.update()

            elif screen_num == 2:
                if start_screen2:
                    apple_box_clicked = False
                    grape_box_clicked = False
                    start_screen2 = False
                else: 
                    screen.blit(instructions2_surf, instructions2_rect)

                    apple_box.draw_static(screen)
                    if apple_box.clicked(click):
                        if apple_box_clicked is False:
                            apple_box_clicked = True
                        else: apple_box_clicked = False

                    grape_box.draw_static(screen)
                    if grape_box.clicked(click):
                        if grape_box_clicked is False:
                            grape_box_clicked = True
                    
                    if grape_box_clicked: 
                        screen.blit(instructions2_correct_surf, instructions2_correct_rect)
                        continue_button.draw(screen, continue_button)
                        if continue_button.continue_screen(click, screen):
                            screen_num = 3
                    elif apple_box_clicked:
                        screen.blit(try_again_surf, try_again_rect)
                     
                    pygame.display.update()

            elif screen_num == 3:
                if start_screen3:
                    apple_box_clicked = False
                    grape_box_clicked = False
                    start_screen3 = False
                else:
                    screen.blit(instructions3_1_surf, instructions3_1_rect)
                    screen.blit(instructions3_2_surf, instructions3_2_rect)
                    screen.blit(instructions3_3_surf, instructions3_3_rect)
                    
                    apple_box.draw_static(screen)
                    grape_box.draw_static(screen)

                    if apple_box.clicked(click):
                        apple_box_clicked = True
                    if grape_box.clicked(click):
                        grape_box_clicked = True

                    child.draw(screen)

                    pygame.display.update()

                    if grape_box_clicked or apple_box_clicked:
                        screen_num = 4

            elif screen_num == 4:
                    if grape_box_clicked: 
                        screen.blit(incorrect_surf, incorrect_rect)
                    elif apple_box_clicked:
                        screen.blit(correct_surf, correct_rect)

                    pygame.draw.rect(screen, 'White', return_rect, 0)
                    pygame.draw.rect(screen, 'Black', return_rect, 3, 5)
                    screen.blit(return_surf, return_rect)

                    mouse_pos = pygame.mouse.get_pos()
                    if click and return_rect.collidepoint(mouse_pos):
                        main_menu()
                    pygame.display.update()

# def activity2():

def main_menu():
    while True:
        screen.blit(pygame.image.load('assets/background.png'), (0,0))
        menu_mouse_pos = pygame.mouse.get_pos()

        menu_surf = get_font(100).render("Main Menu", True, "Black")
        menu_rect = menu_surf.get_rect(center = (400, 100))

        # def __init__(self, pos, text_input, font, base_color):
        activity1_button = Button(pos=(400,250), text_input=" Activity 1 ", font=get_font(70), base_color="Black")
        activity2_button = Button(pos=(400,360), text_input=" Activity 2 ", font=get_font(70), base_color="Black")
        quit_button = Button(pos=(400,470), text_input=" Quit ", font=get_font(70), base_color="Black")

        screen.blit(menu_surf, menu_rect)

        for button in [activity1_button, activity2_button, quit_button]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if activity1_button.checkForInput(menu_mouse_pos):
                    activity1_screen()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    exit()

        pygame.display.update()

main_menu()