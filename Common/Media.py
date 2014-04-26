"""
LD29 Entry - Beneath The Surface
Space Farm
2014 Fiona Burrows fiona@justfiona.com
"""

# Standard library imports
import os

# Framework imports
from myrmidon import Game


class Media(object):
    """Loads all the media required for the game to run,
    graphics, fonts and sounds.
    """

    # Dictionaries containing the loaded files
    gfx = {}
    fonts = {}
    sfx = {}
    music = {}


    def __init__(self):
        self.gfx['tiles_ground'] = Game.load_image(os.path.join("assets", "tiles", "ground.png"))
        self.gfx['tiles_objects'] = Game.load_image(os.path.join("assets", "tiles", "objects.png"))
