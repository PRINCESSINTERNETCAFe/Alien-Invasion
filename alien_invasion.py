import sys
import pygame as pyg

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    #Overall class to manage game assets and behaviour

    def __init__(self):
        #Initialise the game and create its resources
        pyg.init()
        self.settings = Settings()
        self.screen = pyg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pyg.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pyg.sprite.Group()

        #Set background colour
        self.bg_color = self.settings.bg_color
    
    def run_game(self):
        #Start the main loop for the game
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()       
    
    def _check_events(self):
    #Reponds to keypresses and mouse events
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    sys.exit()
                elif event.type == pyg.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pyg.KEYUP:
                    self._check_keyup_events(event) 

    def _check_keydown_events(self, event):
        #Respond to key presses
        if event.key == pyg.K_RIGHT:
            #Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pyg.K_LEFT:
            #Move the ship to the left
            self.ship.moving_left = True
        elif event.key == pyg.K_ESCAPE:
            sys.exit()
        elif event.key == pyg.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        #Respond to key reeleases
        if event.key == pyg.K_RIGHT:
            #Stop moving the ship
            self.ship.moving_right = False
        elif event.key == pyg.K_LEFT:
            #Stop moving the ship
            self.ship.moving_left = False

    def _fire_bullet(self):
        #Create a new bullet and add it to the bullets group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
    #Get rid of bullets and get rid of bullets
            self.bullets.update()       

            #Get rid of bullets that have disappeared  
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

    def _update_screen(self):
    #Update images on the screen and flip to the new screen
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            # #Make the most recently drawn screen visible
            pyg.display.flip()

if __name__ == "__main__":
    #Make instance and run the game
    ai = AlienInvasion()
    ai.run_game()