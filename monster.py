import pygame

class Monster:
    def __init__(self, name, hearts, vp, energy, sprite, x, y, color, alive, in_tokyo):
        self.name = name
        self.hearts = hearts
        self.vp = vp
        self.energy = energy
        self.sprite = sprite
        self.x = x
        self.y = y
        self.color = color
        self.alive = True
        self.in_tokyo = in_tokyo
        self.status_text = str(self.vp) + "vp " + str(self.hearts) + "h " + str(self.energy) + "e"
        self.cards = []

    def draw(self, surface):
        surface.blit(self.sprite, (self.x, self.y))
        

    def move(self, x, y):
        self.x = x
        self.y = y

    def give_card(self, card):
        self.cards.append(card)