import pygame

class Display():
    def __init__(self, pos, text_input, font, base_color):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def draw_text(self, screen):
        screen.blit(self.text, self.rect)

    def draw_button(self, screen):
        pygame.draw.rect(screen, "White", self.rect)
        screen.blit(self.text, self.rect)
        pygame.draw.rect(screen, "Black", self.rect, 3, 5)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
def get_font(size):
    return pygame.font.Font('open-sans/OpenSans-Regular.ttf', size)