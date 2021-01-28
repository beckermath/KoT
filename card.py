import pygame

class Card(object):
    def __init__(self, text, name, cost, vp, hearts, energy, font, text_color, rect, idle_color, hover_color, callback_function, show):
        self.name = name
        self.cost = cost
        self.vp = vp
        self.hearts = hearts
        self.energy = energy
        self.text = text
        self.font = font
        self.label = font.render(text, False, text_color)
        self.rect = pygame.Rect(rect)
        self.label_rect = self.label.get_rect(center = self.rect.center)
        self.idle_color = idle_color
        self.hover_color = hover_color
        self.hovered = False
        self.callback = callback_function
        self.show = show

    def update(self, mouse_pos):
        self.hovered = False
        if self.rect.collidepoint(mouse_pos):
            self.hovered = True
        
    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.hovered:
                self.callback()
        
    def draw(self, surface):
        if self.hovered:
            self.show = True
        else:
            self.show = False

        color = self.hover_color if self.hovered else self.idle_color
        pygame.draw.rect(surface, color, self.rect)
        surface.blit(self.label, self.label_rect)
    
    def updateLabel(self, newtext):
        self.label = self.font.render(newtext, False, (0, 0, 0))
        self.text = newtext