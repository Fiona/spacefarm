"""
LD29 Entry - Beneath The Surface
Space Farm
2014 Fiona Burrows fiona@justfiona.com
"""

# Framework imports
from myrmidon import Game

# Application imports
from Common.Consts import Consts
from Common.Window import Window

# Start the game
Game.debug = True
Game.screen_resolution = Consts.screen_resolution
Game.full_screen = Consts.full_screen
Window()
