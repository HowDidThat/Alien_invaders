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

class Bullet_alien(Sprite):
    """Bullets bitch"""
    def __init__ (self,ai_settings,screen,alien):
        """Crate za bullet"""
        super(Bullet_alien,self).__init__()
        self.screen = screen

        # Make bullet at 0,0 and then adjust to preference
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width_alien,ai_settings.bullet_height_alien)
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom
        
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color_alien
        self.speed_factor_alien = ai_settings.bullet_speed_factor_alien

    def update(self):
        """Move za bullet up to the great beyond"""
        self.y += self.speed_factor_alien 
        self.rect.y = self.y

    
    def draw_bullet(self) :
        """Draw za bullet"""
        pygame.draw.rect(self.screen,self.color,self.rect)

