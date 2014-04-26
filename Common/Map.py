"""
LD29 Entry - Beneath The Surface
Space Farm
2014 Fiona Burrows fiona@justfiona.com
"""

# Standard lib imports
import json

# Framework imports
from myrmidon import Game, Entity

# Game imports
from Common.Map_Layer import Map_Layer
from Common.Tile_Type import Tile_Type


class Map(Entity):
    """Loads tilemap information from a json file exported by
    Tiled, is also responsible for drawing the tilemap.
    """
    # Data loaded directly from the tilemap.
    _raw_values = {}

    # List of Map_Layer objects, which in turn holds tile data
    map_layers = []    

    # Dictionary of tile IDs to Tile_Type objects
    tile_types = {}
    
    # Width/height of map in tiles
    width = 0
    height = 0
    
    def execute(self, window, map_file):
        self.window = window
        self.map_layers = []    
        self.tile_types = {}
        
        # Get the json in
        try:
            with open(map_file, 'r') as f:
                self._raw_values = json.load(f)
        except IOError:
            print("Error loading map file ", map_file)
            self.window.quit_game()
            return

        self.width = self._raw_values['width']
        self.height = self._raw_values['height']

        # Load in all the different tile types
        for tileset_data in self._raw_values['tilesets']:
            map_tile_id = tileset_data['firstgid']
            palette_pos = 1
            num_tiles = int((tileset_data['imagewidth'] / self._raw_values['tilewidth']) * (tileset_data['imageheight'] / self._raw_values['tileheight']))
            for tile_num in range(num_tiles):
                tile_data = tileset_data['tileproperties'][tile_num] if tile_num in tileset_data['tileproperties'] else {}
                self.tile_types[map_tile_id] = Tile_Type(self.window.media.gfx['tiles_' + tileset_data['name']], tile_data, palette_pos = palette_pos)
                map_tile_id += 1
                palette_pos += 1

        # Create Map_Layer objects for each layer to draw
        for layer_data in self._raw_values['layers']:
            self.map_layers.append(Map_Layer(self.window, layer_data))

        #print(self._raw_values)
        
        while True:
            yield
