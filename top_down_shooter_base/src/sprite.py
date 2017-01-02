# Sprite Class

from tkinter import *
from .constants import *

""" Represents a single tile on the background of the 2D game. Sprites can
    have various properties, such as being solid, elastic or hazardous. """

class Sprite:
    ERROR = -1
    NONE = 0
    BLOCK = 1
    def __init__(self, sprite_id, solid, elastic, hazard):
        self.sprite_id = sprite_id
        self.solid = solid # Player cannot pass through this.
        self.elastic = elastic # Player will bounce off of this.
        self.hazard = hazard # Player will be damaged by this.

    def draw(self, window, x, y):
        """ Draws the sprite on the screen. """
        if self.sprite_id == Sprite.NONE:
            window.create_rectangle(x, y, x + Constants.TILE_SIZE,
            y + Constants.TILE_SIZE, fill = "white", outline = "white")
        elif self.sprite_id == Sprite.BLOCK:
            window.create_rectangle(x, y, x + Constants.TILE_SIZE,
            y + Constants.TILE_SIZE, fill = "black", outline = "black")
        elif self.sprite_id == Sprite.ERROR:
            window.create_rectangle(x, y, x + Constants.TILE_SIZE,
            y + Constants.TILE_SIZE, fill = "red", outline = "red")
            window.create_text(x + Constants.TILE_SIZE / 2, y + Constants.TILE_SIZE / 2,
            text = "ERR", fill = "white", anchor = "center")
