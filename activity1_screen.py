import pygame
import activity1_modules
from display import Display, get_font

pygame.init()

def activity1_screen(screen):
    # declare variables
    start_screen2 = True
    start_screen3 = True
    activity = 1
    screen_num = 1

    pygame.display.set_caption('Theory of Mind')
    font = pygame.font.Font('open-sans/OpenSans-Regular.ttf', 30)

    apple_box = activity1_modules.Apple_box()
    grape_box = activity1_modules.Grape_box()
    continue_button = activity1_modules.Continue_button(font)
    child = activity1_modules.Child()

    # static text (instructions, results, etc.)
    instructions1_1 = Display(pos=(400,60), text_input="Click on each box to see its contents.", 
                           font=get_font(30), base_color="Black")
    instructions1_2 = Display(pos=(400,100), text_input="Press continue when you know what is in each box.", 
                           font=get_font(30), base_color="Black")
    instructions2 = Display(pos=(400,60), text_input="Click on the box that has an apple inside it.", 
                           font=get_font(30), base_color="Black")    
    instructions2_correct = Display(pos=(400,100), text_input="Great! Now press continue.", 
                           font=get_font(30), base_color="Black")
    instructions3_1 = Display(pos=(400,60), text_input="This child just entered the room.", 
                           font=get_font(30), base_color="Black")
    instructions3_2 = Display(pos=(400,100), text_input="He does not know which box the apple is in.", 
                           font=get_font(30), base_color="Black")
    instructions3_3 = Display(pos=(400,140), text_input="Where would he most likely look for the apple?", 
                           font=get_font(30), base_color="Black")
    try_again = Display(pos=(400,170), text_input=" Try Again ", font=get_font(30), base_color="Red")
    correct = Display(pos=(400,170), text_input="You are correct!", font=get_font(30), base_color="Black")
    incorrect = Display(pos=(400,170), text_input="Sorry, that is incorrect!", font=get_font(30), base_color="Black")
    return_menu = Display(pos=(400,250), text_input=" Return to Main Menu ", font=get_font(30), base_color="Black")

    background = pygame.image.load('assets/game1/background.png')

    while True:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 3
            if event.type == pygame.MOUSEBUTTONUP:
                click = True

        # instruction screen
        if activity == 1:

            screen.blit(background, (0,0))

            if screen_num == 1:
                for element in [instructions1_1, instructions1_2]:
                    element.draw_text(screen)

                continue_button.draw(screen, continue_button)
                if continue_button.continue_screen(click, screen):
                    screen_num = 2

                apple_box.draw_change(click, screen)
                grape_box.draw_change(click, screen)

                pygame.display.update()

            elif screen_num == 2:
                # check why i cant use same variable for the start_screens
                if start_screen2:
                    apple_box_clicked = False
                    grape_box_clicked = False
                    start_screen2 = False
                else: 
                    instructions2.draw_text(screen)

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
                        instructions2_correct.draw_text(screen)
                        continue_button.draw(screen, continue_button)
                        if continue_button.continue_screen(click, screen):
                            screen_num = 3
                    elif apple_box_clicked:
                        try_again.draw_text(screen)
                     
                    pygame.display.update()

            elif screen_num == 3:
                if start_screen3:
                    apple_box_clicked = False
                    grape_box_clicked = False
                    start_screen3 = False
                else:
                    for element in [instructions3_1, instructions3_2, instructions3_3]:
                        element.draw_text(screen)
                    
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
                        incorrect.draw_text(screen)
                    elif apple_box_clicked:
                        correct.draw_text(screen)

                    return_menu.draw_button(screen)

                    mouse_pos = pygame.mouse.get_pos()
                    if click and return_menu.checkForInput(mouse_pos):
                        return 0
                    
                    pygame.display.update()