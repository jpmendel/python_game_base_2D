# Vector2D Class

""" A two-dimensional vector class that can be used to represent various
    elements of a 2D game, such as position and velocity of an entity."""

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(vector):
        self.x += vector.x
        self.y += vector.y

    def sub(vector):
        self.x -= vector.x
        self.y -= vector.y

    def mult(vector):
        self.x *= vector.x
        self.y *= vector.y

    def div(vector):
        self.x /= vector.x
        self.y /= vector.y
