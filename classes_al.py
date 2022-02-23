import pygame
from pygame.sprite import Sprite

class Alien(Sprite) :
    """A class to represent a alien"""
    
    def __init__(self,ai_settings, screen)  :
        """Initialize the alien and its pozition"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Loat the allien
        self.image = pygame.image.load('Images/Alien.bmp')
        self.rect = self.image.get_rect()

        #Start alien at the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien poz
        self.x = float (self.rect.x)

    def blitme(self):
        """Draw alien"""
        self.screen.blit(self.image,self.rect)
    
    def check_edges(self) :
        """Return True if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0 :
            return True

    def update(self) :
        """Move the alien-s"""
        self.x += (self.ai_settings.alien_speed * self.ai_settings.fleet_direction)
        self.rect.x = self.x