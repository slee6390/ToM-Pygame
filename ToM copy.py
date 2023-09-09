import pygame
from sys import exit

background_screen_num = 1
screen_num = 1
apple_box_index = 0
grape_box_index = 0

pygame.init()
screen = pygame.display.set_mode((800, 600))

# font = pygame.font.Font('open-sans/OpenSans-Regular.ttf', 40)

class Apple_box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        apple_closed = pygame.image.load('sprites/box_apple_pic.png').convert_alpha()
        apple_closed = pygame.transform.rotozoom(apple_closed, 0, 0.6)
        apple_open = pygame.image.load('sprites/apple pic box.png').convert_alpha()
        apple_open = pygame.transform.rotozoom(apple_open, 0, 0.5)

        self.apple_box = [apple_closed, apple_open]
        self.image = self.apple_box[apple_box_index]
        self.rect = self.image.get_rect(center = (200, 450))

        self.clicked = False
    
    def draw_change(self):
        mouse_pos = pygame.mouse.get_pos()
        if click and self.rect.collidepoint(mouse_pos):
            if self.image == self.apple_box[0]: self.image = self.apple_box[1]
            else: self.image = self.apple_box[0]
        
        screen.blit(self.image, self.rect)

    def draw_static(self):
        self.image = self.apple_box[0]
        screen.blit(self.image, self.rect)

    def display_try_again(self):
        mouse_pos = pygame.mouse.get_pos()
        try_again_surf = pygame.image.load('sprites/try again.png').convert_alpha()
        try_again_surf = pygame.transform.rotozoom(try_again_surf, 0, 1)
        try_again_rect = instructions2_surf.get_rect(center = (500, 170))

        if self.clicked:
            screen.blit(try_again_surf, try_again_rect)
        
        if click and self.rect.collidepoint(mouse_pos):
            if not self.clicked: 
                self.clicked = True
            else: self.clicked = False      

class Grape_box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        grape_closed = pygame.image.load('sprites/box_grape_pic.png').convert_alpha()
        grape_closed = pygame.transform.rotozoom(grape_closed, 0, 0.6)
        grape_open = pygame.image.load('sprites/grape pic box.png').convert_alpha()
        grape_open = pygame.transform.rotozoom(grape_open, 0, 0.5)

        self.grape_box = [grape_closed, grape_open]
        self.image = self.grape_box[grape_box_index]
        self.rect = self.image.get_rect(center = (600, 450))

        self.clicked = False
    
    def draw_change(self):
        mouse_pos = pygame.mouse.get_pos()
        if click and self.rect.collidepoint(mouse_pos):
            if self.image == self.grape_box[0]: self.image = self.grape_box[1]
            else: self.image = self.grape_box[0]

        screen.blit(self.image, self.rect)

    def draw_static(self):
        self.image = self.grape_box[0]
        screen.blit(self.image, self.rect)

    def display_continue(self):
        mouse_pos = pygame.mouse.get_pos()
        continue2_surf = pygame.image.load('sprites/continue2.png').convert_alpha()
        continue2_surf = pygame.transform.rotozoom(continue2_surf, 0, 1)
        continue2_rect = instructions2_surf.get_rect(center = (400, 30))

        if self.clicked:
            screen.blit(continue2_surf, continue2_rect)
        
        if click and self.rect.collidepoint(mouse_pos):
            if not self.clicked: 
                self.clicked = True
            else: self.clicked = False   
    

class Answer_apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('sprites/apple_text.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 1)
        self.rect = self.image.get_rect(center = (300, 170))
        # self.image = font.render(' apple ', False, 'Black')

    '''def apple_box_open(self):
        mouse_pos = pygame.mouse.get_pos()
        if click:
            if self.rect.collidepoint(mouse_pos):
                return True'''

    def draw(self):
        screen.blit(self.image, self.rect)

class Answer_grape(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('sprites/grape_text.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 1)
        # self.image = font.render(' grapes ', False, 'Black')
        self.rect = self.image.get_rect(center = (500, 170)) 
    
    '''def grape_box_open(self):
        mouse_pos = pygame.mouse.get_pos()
        if click:
            if self.rect.collidepoint(mouse_pos):
                return True'''

    def draw(self):
        screen.blit(self.image, self.rect)

class Continue_button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('sprites/continue.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 1)
        self.rect = self.image.get_rect(center = (400, 250))

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if click and self.rect.collidepoint(mouse_pos):
            global screen_num
            screen_num = 2
        screen.blit(self.image, self.rect)

class Child(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('sprites/child.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.38)
        self.rect = self.image.get_rect(center = (400, 300))

    def draw(self):
        screen.blit(self.image, self.rect)

apple_box = Apple_box()
grape_box = Grape_box()
answer_apple = Answer_apple()
answer_grape = Answer_grape()
continue_button = Continue_button()

child = Child()

pygame.display.set_caption('Theory of Mind')

# question_surf = font.render('What do you think is in the first box?', True, 'Black')
# question_rect = question_surf.get_rect(center = (400, 60))

instructions1_surf = pygame.image.load('sprites/instructions_1.png').convert_alpha()
instructions1_surf = pygame.transform.rotozoom(instructions1_surf, 0, 0.9)
instructions1_rect = instructions1_surf.get_rect(center = (400, 100))

instructions2_surf = pygame.image.load('sprites/instructions_2.png').convert_alpha()
instructions2_surf = pygame.transform.rotozoom(instructions2_surf, 0, 1)
instructions2_rect = instructions2_surf.get_rect(center = (400, 50))

# pointer_surf = pygame.image.load('sprites/arrow.png').convert_alpha()
# pointer_surf = pygame.transform.rotozoom(pointer_surf, 0, 0.6)
# pointer_rect = pointer_surf.get_rect(center = (200, 270))

background = pygame.image.load('sprites/background.png')
# clock = pygame.time.Clock()

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
    if background_screen_num == 1:
        screen.blit(background, (0,0))
        if screen_num == 1:
            screen.blit(instructions1_surf, instructions1_rect)
            # screen.blit(pointer_surf, pointer_rect)

            continue_button.draw()
            apple_box.draw_change()
            grape_box.draw_change()
            pygame.display.update()

        elif screen_num == 2:
            # print(apple_box.clicked)
            screen.blit(instructions2_surf, instructions2_rect)
            # answer_apple.draw()
            # answer_grape.draw()
            apple_box.draw_static()
            apple_box.display_try_again()
            grape_box.draw_static()
            grape_box.display_continue()
                
            pygame.display.update()
            # clock.tick(60)
        # if incorrect, prompt until correct answer (grapes), ask to base off on the image on the box


    # check answer to question, then prompt player to click on the box to check its contents:
        # animation where grapes comes out of apple box

    # now ask the player what is in the box, same choices

        # if incorrect (not grapes), show the contents again -> loop until correct

    # now introduce figure (has not seen inside the box yet)
    # child.draw(screen)

    # ask what the figure would think is in the box
