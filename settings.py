WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY
FT_FILE = "fastesttime.txt"
FONT_NAME = 'arial'

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_ACC = 2.0
PLAYER_GRAV = 0.8
PLAYER_FRICTION = -0.12
PLAYER_JUMP = 20

#  Mob settings - soon^TM

# Items
ITEM_IMAGES = {'speed': 'speed_boost.png'}
SPEED_BOOST_AMOUNT = 50.0

# Sounds
BG_MUSIC = 'espionage.ogg'
EFFECTS_SOUNDS = {'jump': 'Jump7.wav'}
PLAYER_HIT_SOUNDS = ['Explosion7.wav']

