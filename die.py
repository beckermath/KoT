import pygame

class Die(object):
    def __init__(self, value, font, text_color, rect, idle_color, hover_color, callback_function):
        self.value = value
        self.font = font
        self.text_color = text_color
        self.label = font.render(value, False, text_color)
        self.rect = pygame.Rect(rect)
        self.label_rect = self.label.get_rect(center = self.rect.center)
        self.idle_color = idle_color
        self.hover_color = hover_color
        self.hovered = False
        self.kept = False
        self.callback = callback_function

    def update(self, mouse_pos):
        self.hovered = False
        if self.rect.collidepoint(mouse_pos):
            self.hovered = True
        
    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.hovered:
                self.flipDie()
        
    def draw(self, surface):
        color = self.hover_color if self.hovered else self.idle_color
        pygame.draw.rect(surface, color, self.rect)
        surface.blit(self.label, self.label_rect)
    
    def updateLabel(self, newtext):
        if not self.kept:
            self.label = self.font.render(newtext, False, self.text_color)
            self.text = newtext 
        
    def flipDie(self):
        if self.kept:
            self.idle_color = (0, 204, 0)
            self.kept = False
        else:
            self.idle_color = self.hover_color
            self.kept = True
    