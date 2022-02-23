import pygame

import pygame.font

from pygame.sprite import Sprite

class Ship():
    def __init__(self,ai_settings,screen):
        """Initialize the ship and set its starting point"""

        self.screen = screen

        # Load Ship

        self.image = pygame.image.load('Images/Ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        # Start each new ship
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #MOvement flags , because why not
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False


        self.center = float(self.rect.centerx)
        self.height = float(self.rect.centery)


    def update(self):
        """Update the ship's pozition based on the movement flag"""
        if self.move_right and self.ai_settings.screen_width:
            self.center += self.ai_settings.ship_speed
        if self.move_left and self.center >0: 
            self.center -= self.ai_settings.ship_speed
        if self.move_up and self.height > 0:
            self.height -= self.ai_settings.ship_speed
        if self.move_down and self.height < self.ai_settings.screen_height :
            self.height += self.ai_settings.ship_speed
        #update the pozition
        self.rect.centerx = self.center
        self.rect.centery = self.height
    def blitme(self):
        """Draw sip"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self) :
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx
        self.height = self.screen_rect.bottom

class Bullet(Sprite) :
    """Bullets bitch"""
    def __init__ (self,ai_settings,screen,ship):
        """Crate za bullet"""
        super(Bullet,self).__init__()
        self.screen = screen

        # Make bullet at 0,0 and then adjust to preference
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top
        
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move za bullet up to the great beyond"""
        self.y -= self.speed_factor 
        self.rect.y = self.y
    
    def draw_bullet(self) :
        """Draw za bullet"""
        pygame.draw.rect(self.screen,self.color,self.rect)



class Scoreboard() :
    """A class to keep track of the score of the game"""

    def __init__(self,ai_settings,screen,stats) :
        """Initialize the scoreboard atributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        #Font settings
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 40)

        self.prep_score()
    
    def prep_score(self) :
        """Make a image out of the score"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,self.ai_settings.bg_color)

        # Display the score
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    def show_score(self) :
        self.screen.blit(self.score_image, self.score_rect)