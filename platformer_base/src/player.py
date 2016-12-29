# Player Class

from tkinter import *
from .entity import *
from .constants import *

class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self, x, y)
        self.x_speed = 0.4
        self.max_x_speed = 8.0
        self.friction = 0.8
        self.gravity = 0.5
        self.max_y_speed = 10
        self.move_state = {Constants.LEFT:False, Constants.RIGHT:False}
        self.jump_state = Constants.NOT_JUMPING
        self.collision = {Constants.UP:False, Constants.DOWN:False,
                          Constants.LEFT:False, Constants.RIGHT:False}

    def draw(self, window):
        if self.visible:
            window.create_rectangle(self.pos.x - Constants.TILE_SIZE / 2, self.pos.y - Constants.TILE_SIZE / 2,
            self.pos.x + Constants.TILE_SIZE / 2, self.pos.y + Constants.TILE_SIZE / 2, fill = "blue", outline = "blue")
