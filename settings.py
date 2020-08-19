class Settings:
    #A class to store all settings for Alien Invasion

    def __init__(self):
        #Initialise the game's settings

        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 5, 45)

        #Ship settings
        self.ship_speed = 2.5
        self.ship_limit = 3

        #Bullets settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 255, 255)
        self.bullets_allowed = 10

        #Alien settings
        self.alien_speed = 5
        self.fleet_drop_speed = 5
        # Fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1