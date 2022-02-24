import pygame.font
import pygame

class Settings():
    """Setting for the python space invader game"""

    def __init__(self):
        """Values for the basic settings in the game"""
        
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        

        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.max_bullets = 100
        self.bullet_width_alien = 5
        self.bullet_height_alien = 20
        self.bullet_color_alien = 0,0,255
        #alien settings
        self.fleet_drop_speed = 10
        #fleet_direction = 1 -> right , -1 -> left
        self.ship_limit = 3
        self.speed_scale = 1.1
        self.initialize_dinamic_settings()
        self.bullet_chance = 10000
    def initialize_dinamic_settings(self):
        """All the game settings that change with time"""
        self.ship_speed = 1.5
        self.bullet_speed_factor = 3
        self.bullet_speed_factor_alien = 0.1
        self.alien_speed = .5
        self.fleet_direction = 1 
        self.ship_speed_factor = 1.06
        self.alien_points = 50
        
    def increase_lvl(self) :
        """Increase the speed by the lvl"""
        #self.ship_speed*= self.ship_speed_factor
        self.alien_speed *= self.ship_speed_factor

class GameStats() :

    """traks stats and other info"""
    def __init__(self,ai_settings) :
        """Initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #start the game in an inactive state
        self.game_active = False


    def reset_stats(self) :
        """Initialize statistics that change"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
class Button() :
    def __init__(self,ai_settings,screen,msg) :
        """Initialize button atributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #Set the dimesnions and propert of the buttons
        self.width , self.height = 200, 50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        #build the button
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        # The messege needs to be prepared only once.
        self.prep_msg(msg)


    def prep_msg(self,msg) :
        """Turn msg into a renerd img"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center 

    def draw_button(self) :
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


