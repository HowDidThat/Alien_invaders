from operator import truediv
import sys
import pygame
from  random import randint
from time import sleep
from classes import Bullet
from classes_al import Bullet_alien
from classes_al import Alien

def check_events(ai_settings,screen,stats,play_button,ship,bullets):
    """What the mouse doing"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings,screen, ship ,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y)

def check_play_button(stats, play_button ,mouse_x,mouse_y) :
    """Start new game"""
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        stats.game_active = True


def check_keydown_event(event, ai_settings,screen,ship,bullets):
    # Move the ship Dumbass
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_UP:
        ship.move_up = True
    elif event.key == pygame.K_DOWN:
        ship.move_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_z:
        sys.exit()

def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_UP:
        ship.move_up = False
    elif event.key == pygame.K_DOWN:
        ship.move_down = False

def update_screen(ai_settings, screen,stats, ship,aliens,bullets,play_button,sb,bullets_aliens):
    """Updateja screen and move to the updated screen"""
    #   Redraw the screen in each pass
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    #redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    
    for bullet in bullets_aliens.sprites():
        bullet.draw_bullet()
    #draw the play button
    if not stats.game_active :
        play_button.draw_button()

    pygame.display.flip()

def update_bullets(ai_settings,screen,aliens,bullets,stats,sb,bullets_aliens,ship) :
    """update the pozition and the bullets on the screen""" 
    bullets.update()
   
    #get rid of old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0 :
            bullets.remove(bullet)
    
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions :
        for aliens in collisions.values() :

            stats.score += int (ai_settings.alien_points * ai_settings.alien_speed) * len(aliens)
            sb.prep_score()
    
    for bullet in bullets_aliens :
        if ship.rect.colliderect(bullet.rect):
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            bullets_aliens.empty()
    if len(aliens) == 0 :
        bullets.empty()
        sleep(0.5)
        ai_settings.increase_lvl()
        create_fleet(ai_settings,screen,aliens)

    
def update_bullets_aliens(ai_settings,screen,bullets_aliens):
    bullets_aliens.update()
    for bullet in bullets_aliens.copy():
        if bullet.rect.top >= ai_settings.screen_height:
            bullets_aliens.remove(bullet)

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets,bullets_aliens) :
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    update_bullets_aliens(ai_settings,screen,bullets_aliens)
    for alien in aliens.copy():
        fire_bullet_alien(ai_settings,screen,alien,bullets_aliens)
    #check for sip colission.
    if pygame.sprite.spritecollideany(ship,aliens):
        if stats.ship_left > 0 :
            print (stats.ship_left)
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
        else :
            sys.exit()

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets) :
    """Respond to ship hit"""
    stats.ship_left -= 1
    #reload everithing
    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings,screen,aliens)
    ship.center_ship()
    #a bit of pause for the fallen ones
    sleep(0.5)  

def fire_bullet(ai_settings,screen,ship,bullets) :

    """Fire a bullet if the linit is not reached yet"""
    # Create a new fired bullet
    if ai_settings.max_bullets > len(bullets) :
        new_bullet = Bullet(ai_settings, screen, ship) 
        bullets.add(new_bullet)


def fire_bullet_alien(ai_settings,screen,alien,bullets_aliens) :
    #fire an alien bullet if it is the case
    q = randint(0,ai_settings.bullet_chance)
    if q < 1 :
        
        new_bullet = Bullet_alien(ai_settings,screen,alien)
        bullets_aliens.add(new_bullet)



def get_number_aliens_x(ai_settings,alien_width):
    """determine the number of aliens that fit in a row"""
    aviable_space_x = ai_settings.screen_width - 4 * alien_width
    number_aliens_x = int (aviable_space_x / (1 * alien_width))
    return number_aliens_x

def get_number_of_rows(ai_settings,ship_height,alien_height) :
    aviable_space_y = (ai_settings.screen_height-(3 * alien_height) - ship_height)
    number_of_rows = int (aviable_space_y / (2 * alien_height))
    return number_of_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number) :
    """Create un instance of a alien"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 1 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien) 

def create_fleet(ai_settings, screen, aliens) :
    """create the full fleet of aliens"""
    # create aliens and the number of aliens
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_of_rows(ai_settings, alien.rect.height,alien.rect.height)

    #create the aliens
    for row_number in range (number_rows) :
        for alien_number in range(number_aliens_x) :
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def check_fleet_edges(ai_settings,aliens) :
    """if any alien reaches an edge revers the move direction"""
    for alien in aliens.sprites() :
        if alien.check_edges() :
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens) :
    """Drop the fleet"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


