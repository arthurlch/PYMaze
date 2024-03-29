import pygame as pg

"""  all constants VAR and data are stored in this file constants.py 
constants are recognizable in the other file with UPPERCASE letters
"""

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

# game settings / screen sized
WIDTH = 960   #  shown on the screen 960
HEIGHT = 960  #shown on the screen
FPS = 60 # Frame Per Second
TITLE = "Macgyver Escaping the Maze"
BGCOLOR = BROWN
FONT_NAME = 'arial'

# Map settings
TILESIZE = 80
"""  the number of tile is 15/15 and their size is 80 px by 80 px """
""" the number of tile is verifiable in the map.tmx """

# Wall
WALL_IMG = 'wall.png'

# Player settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'macgyver.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
PLAYER_HEALTH = 1000
PLAYER_POINT = 0
MAX_PLAYER_POINT = 3
BAR_LENGTH = 100
BAR_HEIGHT = 20

# Guardian/Mobs/Objects settings
GUARDIAN_IMG = 'guardian.png'
GUARDIAN_HIT_RECT = pg.Rect(0, 0, 3, 3)
GUARDIAN_DAMMAGE = 15
GUARDIAN_HEALTH = 100


# Items
ITEMS_IMAGE = {'item1': 'item1.png', 'item2': 'item2.png','item3': 'item3.png' }
ITEMS_LIST = [*ITEMS_IMAGE]
ITEM1_POINT_AMOUNT = 1
ITEM2_POINT_AMOUNT = 1
ITEM3_POINT_AMOUNT = 1
