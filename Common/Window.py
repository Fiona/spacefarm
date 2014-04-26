"""
LD29 Entry - Beneath The Surface
Space Farm
2014 Fiona Burrows fiona@justfiona.com
"""

# Standard lib imports
import os, sys, json

# Framework imports
from myrmidon import Game, Entity
from myrmidon.consts import *

# Application imports
from Common.Consts import Consts
from Common.Media import Media
from Common.Map import Map


class Window(Entity):
    """The primary window Entity is the entry point for
    the application, it holds everything that should be global to the game
    like game state, media etc.
    It sets up the state machine and starts the first state.
    """

    def execute(self):
        self.media = Media()
        self.map = Map(self, os.path.join('maps', Consts.default_map_file))
        while True:
            if Game.keyboard_key_released(K_q):
                self.quit_game()
            yield


    def quit_game(self):
        """Immediately closes the application
        """
        sys.exit()

