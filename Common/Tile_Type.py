"""
LD29 Entry - Beneath The Surface
Space Farm
2014 Fiona Burrows fiona@justfiona.com
"""

class Tile_Type(object):
    """Just holds tile information
    """
    image = None
    tile_data = {}
    blocking = False

    def __init__(self, image, tile_data, palette_pos = 1):
        self.image = image
        self.tile_data = tile_data
        self.palette_pos = palette_pos
        if 'block' in self.tile_data and self.tile_data['block'] == "1":
            self.blocking = True
