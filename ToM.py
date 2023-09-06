import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill('Black')
pygame.display.flip()

pygame.display.set_caption('Theory of Mind')

font = pygame.font.Font('open-sans/OpenSans-Regular.ttf', 40)

question_surf = font.render('What do you think is in the bag?', True, 'White')
question_rect = question_surf.get_rect(center = (400, 60))

answer1_surf = font.render(' apple ', False, 'White')
answer1_rect = answer1_surf.get_rect(center = (200, 140))

answer2_surf = font.render(' pizza ', False, 'White')
answer2_rect = answer2_surf.get_rect(center = (400, 140))

answer3_surf = font.render(' bread ', False, 'White')
answer3_rect = answer3_surf.get_rect(center = (600, 140))

bag_surf = pygame.image.load('sprites/applebag.png').convert_alpha()
bag_surf = pygame.transform.rotozoom(bag_surf, 0, 0.8)
bag_rect = bag_surf.get_rect(center = (400, 380))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEBUTTONDOWN():
            

    # question screen
    screen.blit(question_surf, question_rect)
    screen.blit(answer1_surf, answer1_rect)
    pygame.draw.rect(screen, 'White', answer1_rect, 3, 5)
    screen.blit(answer2_surf, answer2_rect)
    pygame.draw.rect(screen, 'White', answer2_rect, 3, 5)
    screen.blit(answer3_surf, answer3_rect)
    pygame.draw.rect(screen, 'White', answer3_rect, 3, 5)
    screen.blit(bag_surf, bag_rect)
    pygame.display.update()
        # if incorrect, prompt until correct answer (apple), ask to base off on the image on the bag

    # check answer to question, then prompt player to click on the bag to check its contents

    # now ask the player what is in the bag, same choices

        # if incorrect (not bread), show the contents again -> loop until correct

    # now introduce figure (has not seen inside the bag yet)

    # ask what the figure would think is in the bag
