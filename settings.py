class Settings:
    #A class to store all settings for Alien Invasion

    def __init__(self):
        #Initialise the game's static settings

        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 5, 45)

        #Ship settings
        self.ship_limit = 3

        #Bullets settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (0, 255, 200)
        self.bullets_allowed = 10

        #Alien settings
        self.fleet_drop_speed = 5

        #How quickly the game speeds up
        self.speedup_scale = 1.2

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        #Initialise settings that change trhoughout the game
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.2
        
        # Fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        #Increase speed settings
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale