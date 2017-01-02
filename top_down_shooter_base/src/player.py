# Player Class

from tkinter import *
from .entity import *
from .constants import *

class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self, x, y)
        self.move_state = {Constants.UP:False, Constants.DOWN:False,
                           Constants.LEFT:False, Constants.RIGHT:False}
        self.collision = {Constants.UP:False, Constants.DOWN:False,
                           Constants.LEFT:False, Constants.RIGHT:False}
        self.speed = 5
    def draw(self, window):
        if self.visible:
            window.create_rectangle(self.pos.x - Constants.TILE_SIZE / 2, self.pos.y - Constants.TILE_SIZE / 2,
            self.pos.x + Constants.TILE_SIZE / 2, self.pos.y + Constants.TILE_SIZE / 2, fill = "blue", outline = "blue")
