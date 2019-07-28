import pygame as pg

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Macgyver Escape the Maze"
BGCOLOR = BROWN

# Map settings
TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Wall
WALL_IMG = 'wall.png'

# Player settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'macgyver.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
PLAYER_HEALTH = 10
BAR_LENGTH = 80 
BAR_HEIGHT = 20

# Guardian/Mobs/Objects settings
GUARDIAN_IMG = 'guardian.png'
GUARDIAN_HIT_RECT = pg.Rect(0, 0, 30, 30)
GUARDIAN_DAMMAGE = 0.5
GUARDIAN_ATTACK_TIMING = 300

