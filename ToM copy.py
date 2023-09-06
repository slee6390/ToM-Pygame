import pygame
from sys import exit

screen_num = 1
apple_box_index = 0

pygame.init()
screen = pygame.display.set_mode((800, 600))

font = pygame.font.Font('open-sans/OpenSans-Regular.ttf', 40)

class Apple_box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        apple_closed = pygame.image.load('sprites/box_apple_pic.png').convert_alpha()
        apple_open = pygame.image.load('sprites/apple pic box.png').convert_alpha()
        self.apple_box = [apple_closed, apple_open]

        self.image = self.apple_box[apple_box_index]
        self.image = pygame.transform.rotozoom(self.image, 0, 0.25)
        self.rect = self.image.get_rect(center = (200, 450))

class Grape_box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('sprites/box_grape_pic.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.25)
        self.rect = self.image.get_rect(center = (600, 450))

class Answer_apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('sprites/apple_text.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 1)
        # self.image = font.render(' apple ', False, 'Black')
        self.rect = self.image.get_rect(center = (300, 140))
        pygame.draw.rect(screen, 'White', self.rect, 10, 5)

    def player_input(self):
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(mouse_pos):
                apple_box_index = 1

    def update(self):
        self.player_input()

class Answer_grape(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('sprites/grape_text.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 1)
        # self.image = font.render(' grapes ', False, 'Black')
        self.rect = self.image.get_rect(center = (500, 140))

    def draw(self):
        pygame.draw.rect(screen, 'Blue', self.rect, 10, 5)

class Child(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('sprites/child.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.38)
        self.rect = self.image.get_rect(center = (400, 380))

apple_box = pygame.sprite.GroupSingle()
apple_box.add(Apple_box())

grape_box = pygame.sprite.GroupSingle()
grape_box.add(Grape_box())

answer_apple = pygame.sprite.GroupSingle()
answer_apple.add(Answer_apple())

answer_grape = pygame.sprite.GroupSingle()
answer_grape.add(Answer_grape())

child = pygame.sprite.GroupSingle()
child.add(Child())

pygame.display.set_caption('Theory of Mind')

# question_surf = font.render('What do you think is in the first box?', True, 'Black')
# question_rect = question_surf.get_rect(center = (400, 60))

question_surf = pygame.image.load('sprites/first_box_text.png').convert_alpha()
question_surf = pygame.transform.rotozoom(question_surf, 0, 0.9)
question_rect = question_surf.get_rect(center = (400, 60))

pointer_surf = pygame.image.load('sprites/arrow.png').convert_alpha()
pointer_surf = pygame.transform.rotozoom(pointer_surf, 0, 0.6)
pointer_rect = pointer_surf.get_rect(center = (200, 270))

background = pygame.image.load('sprites/background.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # question screen
    if screen_num == 1:
        print(screen)
        screen.blit(background, (0,0))

        screen.blit(question_surf, question_rect)
        screen.blit(pointer_surf, pointer_rect)

        answer_apple.draw(screen)
        answer_apple.update()

        answer_grape.draw(screen)
        answer_grape.update()

        apple_box.draw(screen)
        grape_box.draw(screen)

        pygame.display.update()

        # if incorrect, prompt until correct answer (grapes), ask to base off on the image on the box


    # check answer to question, then prompt player to click on the box to check its contents:
        # animation where grapes comes out of apple box

    # now ask the player what is in the box, same choices

        # if incorrect (not grapes), show the contents again -> loop until correct

    # now introduce figure (has not seen inside the box yet)
    # child.draw(screen)

    # ask what the figure would think is in the box
