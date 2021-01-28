import pygame

class Button(object):
    def __init__(self, text, font, text_color, rect, idle_color, hover_color, callback_function):
        self.text = text
        self.font = font
        self.text_color = text_color
        self.label = font.render(text, False, text_color)
        self.rect = pygame.Rect(rect)
        self.label_rect = self.label.get_rect(center = self.rect.center)
        self.idle_color = idle_color
        self.hover_color = hover_color
        self.hovered = False
        self.callback = callback_function

    def update(self, mouse_pos):
        self.hovered = False
        if self.rect.collidepoint(mouse_pos):
            self.hovered = True
        
    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.hovered:
                self.callback()
        
    def draw(self, surface):
        color = self.hover_color if self.hovered else self.idle_color
        pygame.draw.rect(surface, color, self.rect)
        surface.blit(self.label, self.label_rect)
    
    def updateLabel(self, newtext):
        self.label = self.font.render(newtext, False, self.text_color)
        self.label_rect = self.label.get_rect(center = self.rect.center)
        self.text = newtext
    