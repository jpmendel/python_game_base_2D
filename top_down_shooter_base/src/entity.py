# Entity Class

from tkinter import *
from .vector_2D import *

""" A class to represent any element in the game with a position and velocity
    relative to the environment. """

class Entity:
    def __init__(self, x, y):
        self.pos = Vector2D(x, y)
        self.vel = Vector2D(0, 0)
        self.visible = True
