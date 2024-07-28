import pygame

class TextWithBackground:
  def __init__(self, text, text_color, bg_color, font, padding=5):
    self.text = text
    self.text_color = text_color
    self.bg_color = bg_color
    self.font = font
    self.padding = padding
    self.create_surface()

  def create_surface(self):
    text_surface = self.font.render(self.text, True, self.text_color)
    text_rect = text_surface.get_rect()
    self.surface = pygame.Surface((text_rect.width + self.padding * 2, text_rect.height + self.padding * 2), pygame.SRCALPHA)

    self.surface.fill(self.bg_color)
    self.surface.blit(text_surface, (self.padding, self.padding))

