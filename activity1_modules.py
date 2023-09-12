import pygame

class Apple_box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        apple_closed = pygame.image.load('assets/game1/box_apple_pic.png').convert_alpha()
        apple_closed = pygame.transform.rotozoom(apple_closed, 0, 0.6)
        apple_open = pygame.image.load('assets/game1/apple pic box.png').convert_alpha()
        apple_open = pygame.transform.rotozoom(apple_open, 0, 0.5)

        self.apple_box = [apple_closed, apple_open]
        self.image = self.apple_box[0]
        self.rect = self.image.get_rect(center = (200, 450))
    
    def draw_change(self, click, screen):
        mouse_pos = pygame.mouse.get_pos()
        if click and self.rect.collidepoint(mouse_pos):
            if self.image == self.apple_box[0]: self.image = self.apple_box[1]
            else: self.image = self.apple_box[0]
        
        screen.blit(self.image, self.rect)

    def draw_static(self, screen):
        self.image = self.apple_box[0]
        screen.blit(self.image, self.rect)

    def clicked(self, click):
        mouse_pos = pygame.mouse.get_pos()
        if click and self.rect.collidepoint(mouse_pos):
            return True      
        return False   

class Grape_box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        grape_closed = pygame.image.load('assets/game1/box_grape_pic.png').convert_alpha()
        grape_closed = pygame.transform.rotozoom(grape_closed, 0, 0.6)
        grape_open = pygame.image.load('assets/game1/grape pic box.png').convert_alpha()
        grape_open = pygame.transform.rotozoom(grape_open, 0, 0.5)

        self.grape_box = [grape_closed, grape_open]
        self.image = self.grape_box[0]
        self.rect = self.image.get_rect(center = (600, 450))
    
    def draw_change(self, click, screen):
        mouse_pos = pygame.mouse.get_pos()
        if click and self.rect.collidepoint(mouse_pos):
            if self.image == self.grape_box[0]: self.image = self.grape_box[1]
            else: self.image = self.grape_box[0]

        screen.blit(self.image, self.rect)

    def draw_static(self, screen):
        self.image = self.grape_box[0]
        screen.blit(self.image, self.rect)

    def clicked(self, click):
        mouse_pos = pygame.mouse.get_pos()
        if click and self.rect.collidepoint(mouse_pos):
            return True      
        return False   

class Continue_button(pygame.sprite.Sprite):
    def __init__(self, font):
        super().__init__()
        self.image = font.render(' Continue ', True, 'Black')
        self.rect = self.image.get_rect(center = (400, 200))

    def continue_screen(self, click, screen):
        mouse_pos = pygame.mouse.get_pos()
        if click and self.rect.collidepoint(mouse_pos):
            return True
        screen.blit(self.image, self.rect)

    def draw(self, screen, continue_button):
        pygame.draw.rect(screen, 'White', continue_button, 0)
        pygame.draw.rect(screen, 'Black', continue_button, 3, 5)

class Child(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/game1/child.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.6)
        self.rect = self.image.get_rect(center = (400, 500))

    def draw(self, screen):
        screen.blit(self.image, self.rect)