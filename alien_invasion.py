import sys

import pygame as pyg

class AlienInvasion:
    #Overall class to manage game assets and behaviour

    def __init__(self):
        #Initialise the game and create its resources
        pyg.init()
        self.screen = pyg.display.set_mode((1200, 800))
        pyg.display.set_caption("Alien Invasion")

        #Set background colour
        self.bg_color = (230, 230, 230)
    
    def run_game(self):
        #Start the main loop for the game
        while True:
            #Watch for keyboard and mouse events
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    sys.exit()
            
            #Redraw the screen during each pass trhough the loop
            self.screen.fill(self.bg_color)
            
            # #Make the most recently drawn screen visible
            pyg.display.flip()

if __name__ == "__main__":
    #Make instance and run the game
    ai = AlienInvasion()
    ai.run_game()