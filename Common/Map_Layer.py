"""
LD29 Entry - Beneath The Surface
Space Farm
2014 Fiona Burrows fiona@justfiona.com
"""

import sys

# Library imports
from OpenGL.GL import *

# Framework imports
from myrmidon import Game, Entity

# Game imports
from Common.Consts import Consts


class Map_Layer(Entity):
    """A single layer of a map.
    """
    # Dictionary containing types of tiles
    tile_types = {}
    
    # Flat list of values corresponding to tile type ids going from left-to-right,
    # top-to-bottom, denoting how the layer looks. 
    layer_data = []

    # width/height of the map
    width = 0
    height = 0
    
    def execute(self, window, layer_data):
        self.window = window
        self.width = layer_data['width']
        self.height = layer_data['height']
        self.layer_data = layer_data['data']
        self.layer_name = layer_data['name']
        self.tile_types = self.parent.tile_types
        self.tile_type_image = None
        self.build_vertex_data()
        while True:
            yield


    def build_vertex_data(self):       
        self.vertex_data = []
        self.text_coord_data = []
        x = 0.0
        y = 0.0
        for tile_num, tile_id in enumerate(self.layer_data):           
            # Vertex data assignment
            tile = [
                    x, y, 0.0,
                    x + float(Consts.tile_size), y, 0.0,
                    x + float(Consts.tile_size), y + float(Consts.tile_size), 0.0,
                    x, y + float(Consts.tile_size), 0.0,
                    ]

            x += float(Consts.tile_size)
            if not (tile_num + 1) % self.width:
                x = 0.0
                y += float(Consts.tile_size)

            if tile_id == 0:
                continue
            self.vertex_data.append(list(tile))

            # Texture coordinate assignment
            if self.tile_type_image is None:
                self.tile_type_image = self.tile_types[tile_id].image
                
            num_tiles_per_row = self.tile_type_image.width // Consts.tile_size
            tilepalette_width = self.tile_type_image.width
            tilepalette_height = self.tile_type_image.height

            row, col = divmod(self.tile_types[tile_id].palette_pos - 1, num_tiles_per_row)
            t_x, t_y = (col * Consts.tile_size) / tilepalette_width, (row * Consts.tile_size) / tilepalette_height
            t_x_w, t_y_w = ((col * Consts.tile_size) + Consts.tile_size) / tilepalette_width, ((row * Consts.tile_size) + Consts.tile_size) / tilepalette_height
            
            text_coords = [t_x, t_y, # top left
                           t_x_w, t_y, # top right
                           t_x_w, t_y_w, # bottom right
                           t_x, t_y_w] # bottom left
            
            self.text_coord_data.append(text_coords)

            
    def draw(self):
        glPushMatrix()

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.tile_type_image.surfaces[0])
        Game.engine['gfx'].last_image = self.tile_type_image.surfaces[0]
        glTexCoordPointer(2, GL_FLOAT, 0, self.text_coord_data)
        glVertexPointer(3, GL_FLOAT, 0, self.vertex_data)                               
        glColor4f(1.0, 1.0, 1.0, 1.0)
        glDrawArrays(GL_QUADS, 0, 4 * len(self.vertex_data))

        glPopMatrix()

        glBindTexture(GL_TEXTURE_2D, Game.engine['gfx'].last_image)
        glTexCoordPointer(2, GL_FLOAT, 0, Game.engine['gfx'].text_coords)
    
