# Sprite Class

from tkinter import *
from .constants import *

class Sprite:
    ERROR = -1
    NONE = 0
    BLOCK = 1
    SPRING = 2
    def __init__(self, sprite_id, solid, elastic, hazard):
        self.sprite_id = sprite_id
        self.solid = solid
        self.elastic = elastic
        self.hazard = hazard

    def draw(self, window, x, y):
        if self.sprite_id == Sprite.NONE:
            window.create_rectangle(x, y, x + Constants.TILE_SIZE,
            y + Constants.TILE_SIZE, fill = "white", outline = "white")
        elif self.sprite_id == Sprite.BLOCK:
            window.create_rectangle(x, y, x + Constants.TILE_SIZE,
            y + Constants.TILE_SIZE, fill = "black", outline = "black")
        elif self.sprite_id == Sprite.SPRING:
            window.create_rectangle(x, y, x + Constants.TILE_SIZE,
            y + Constants.TILE_SIZE, fill = "green", outline = "green")
        elif self.sprite_id == Sprite.ERROR:
            window.create_rectangle(x, y, x + Constants.TILE_SIZE,
            y + Constants.TILE_SIZE, fill = "red", outline = "red")
            window.create_text(x + Constants.TILE_SIZE / 2, y + Constants.TILE_SIZE / 2,
            text = "ERR", fill = "white", anchor = "center")
