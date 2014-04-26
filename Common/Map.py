"""
LD29 Entry - Beneath The Surface
Space Farm
2014 Fiona Burrows fiona@justfiona.com
"""

# Standard lib imports
import json

# Framework imports
from myrmidon import Game, Entity


class Map(Entity):
    """Loads tilemap information from a json file exported by
    Tiled, is also responsible for drawing the tilemap.
    """
    # Data loaded directly from the tilemap.
    _raw_values = {}
    
    def execute(self, window, map_file):
        self.window = window

        # Get the json in
        try:
            with open(map_file, 'r') as f:
                self._raw_values = json.load(f)
        except IOError:
            print("Error loading map file ", map_file)
            self.window.quit_game()
            return

        print(self._raw_values)
        
        while True:
            yield
