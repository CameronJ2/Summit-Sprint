import pygame as pg
import os

pg.init()

# Sets screen resolution
screen_width = 960
screen_height = 640

screen = pg.display.set_mode((screen_width, screen_height))

# Define game variables 
tile_size = 32
tile_folder = 'Refactored/level_editor/Tiles/1_Tiles'

# Load tiles from tile_folder directory
def load_tiles(tile_folder):
    tile_images = []
    for i in range(1, 61):
        tile_path = os.path.join(tile_folder, f'Tile_{i:02d}.png')
        tile_image = pg.image.load(tile_path).convert_alpha()
        tile_images.append(tile_image)
    return tile_images

# Load level from a file
def load_level(level_path, cols, rows):
    level_data = [[0 for x in range(cols)] for y in range(rows)]
    with open(level_path, 'r') as f:
        for row, line in enumerate(f):
            tile_indices = line.strip().split(',')
            for col, tile_index in enumerate(tile_indices):
                level_data[row][col] = int(tile_index)
    return level_data