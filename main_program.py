import sys
import pygame 
from pygame.sprite import Group


from settings import Settings
from classes import Ship
from settings import GameStats
from classes import Scoreboard
from settings import Button
import game_functions as gf


def run_game():
    #in==Initialize game and create the screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings,screen,"Play")
    
    stats = GameStats(ai_settings)
    #make a ship
    ship = Ship(ai_settings,screen)
    #make the bullets group
    bullets = Group()
    #make the aliens 
    aliens = Group()
    bullets_aliens = Group()
    sb = Scoreboard(ai_settings,screen,stats)
    #create the fleet of aliens
    
    gf.create_fleet(ai_settings,screen,aliens)
    ship.update()
    gf.update_bullets(ai_settings,screen,aliens,bullets,stats,sb,bullets_aliens,ship)
    gf.update_aliens(ai_settings, stats, screen, ship, aliens ,bullets,bullets_aliens)
    gf.update_screen(ai_settings, screen, stats,ship, aliens ,bullets,play_button,sb,bullets_aliens)


    #Start the main loop for the game.
    while True:
        
        gf.check_events(ai_settings,screen,stats,play_button,ship,bullets)
        if stats.game_active == True :
            ship.update()
            gf.update_bullets(ai_settings,screen,aliens,bullets,stats,sb,bullets_aliens,ship)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens ,bullets,bullets_aliens)
            gf.update_screen(ai_settings, screen, stats,ship, aliens ,bullets,play_button,sb,bullets_aliens)

run_game()