# Background Class

from tkinter import *
from .entity import *
from .player import *
from .sprite import *
from .constants import *

class Background(Entity):
    def __init__(self, map_file):
        Entity.__init__(self, 0, 0)
        self.width = 0
        self.height = 0
        self.tiles = self.generate_map(map_file)
        self.player = Player(300, 225)

    def render(self, window):
        """ Renders the background on the screen. """
        self.draw_map(window)
        self.player.draw(window)

    def update(self):
        """ Updates the status of the entities on the background. """
        self.player_move()

    def draw_map(self, window):
        """ Draws each of the tiles currently visible on the map. """
        window.create_rectangle(0, 0, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT,
        fill = "black", outline = "black")
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[0])):
                if self.pos.x + (x * Constants.TILE_SIZE) > (-2 * Constants.TILE_SIZE) \
                and self.pos.x + (x * Constants.TILE_SIZE) < Constants.SCREEN_WIDTH + (2 * Constants.TILE_SIZE) \
                and self.pos.y + (y * Constants.TILE_SIZE) > (-2 * Constants.TILE_SIZE) \
                and self.pos.y + (y * Constants.TILE_SIZE) < Constants.SCREEN_HEIGHT + (2 * Constants.TILE_SIZE):
                    self.tiles[y][x].draw(window, self.pos.x + (x * Constants.TILE_SIZE),
                    self.pos.y + (y * Constants.TILE_SIZE))

    def generate_map(self, map_file):
        """ Generates a 2D array of tiles from a whitespace-delimited text file
            and returns the array. """
        open_map_file = open(map_file, "r")
        file_data = open_map_file.readlines()
        open_map_file.close()
        map_data = []
        for line in file_data:
            map_data.append(line.split(" "))
        self.width = len(map_data[0]) * Constants.TILE_SIZE
        self.height = len(map_data) * Constants.TILE_SIZE
        map_sprites = []
        for line in map_data:
            map_line = []
            for tile in line:
                sprite = self.get_sprite(int(tile))
                map_line.append(sprite)
            map_sprites.append(map_line)
        return map_sprites

    def get_sprite(self, sprite_id):
        """ Gets a Sprite object based on a given sprite_id read from the map
            file. """
        if sprite_id == Sprite.NONE:
            return Sprite(sprite_id, False, False, False)
        elif sprite_id == Sprite.BLOCK:
            return Sprite(sprite_id, True, False, False)
        return Sprite(Sprite.ERROR, False, False, False)

    def player_move(self):
        """ Moves the player around the screen. """
        if self.player.move_state[Constants.UP] \
        and not self.player.collision[Constants.UP]:
            self.pos.y += self.player.speed
        elif self.player.move_state[Constants.DOWN] \
        and not self.player.collision[Constants.DOWN]:
            self.pos.y -= self.player.speed
        if self.player.move_state[Constants.LEFT] \
        and not self.player.collision[Constants.LEFT]:
            self.pos.x += self.player.speed
        elif self.player.move_state[Constants.RIGHT] \
        and not self.player.collision[Constants.RIGHT]:
            self.pos.x -= self.player.speed
        self.player_boundary()
        self.player_collision()

    def player_collision(self):
        """ Checks collisions between the player and any solid tiles. """
        bx = int((self.player.pos.x - self.pos.x) / Constants.TILE_SIZE)
        by = int((self.player.pos.y - self.pos.y) / Constants.TILE_SIZE)
        up = int((self.player.pos.y + (Constants.TILE_SIZE / 2) - self.pos.y) / Constants.TILE_SIZE)
        down = int((self.player.pos.y - (Constants.TILE_SIZE / 2) - self.pos.y) / Constants.TILE_SIZE)
        left = int((self.player.pos.x + (Constants.TILE_SIZE / 2) - self.pos.x) / Constants.TILE_SIZE)
        right = int((self.player.pos.x - (Constants.TILE_SIZE / 2) - self.pos.x) / Constants.TILE_SIZE)
        if self.tiles[up - 1][bx].solid:
            if not self.player.collision[Constants.UP]:
                self.player.collision[Constants.UP] = True
                self.pos.y -= self.player.speed
        else:
            self.player.collision[Constants.UP] = False
        if self.tiles[down + 1][bx].solid:
            if not self.player.collision[Constants.DOWN]:
                self.player.collision[Constants.DOWN] = True
                self.pos.y += self.player.speed
        else:
            self.player.collision[Constants.DOWN] = False
        if self.tiles[by][left - 1].solid:
            if not self.player.collision[Constants.LEFT]:
                self.player.collision[Constants.LEFT] = True
                self.pos.x -= self.player.speed
        else:
            self.player.collision[Constants.LEFT] = False
        if self.tiles[by][right + 1].solid:
            if not self.player.collision[Constants.RIGHT]:
                self.player.collision[Constants.RIGHT] = True
                self.pos.x += self.player.speed
        else:
            self.player.collision[Constants.RIGHT] = False

    def player_boundary(self):
        """ Blocks the player from moving past the boundaries of the map. """
        if self.player.pos.x <= (self.pos.x + Constants.TILE_SIZE / 2):
            self.pos.x -= self.player.speed
        if self.player.pos.x >= (self.pos.x + self.width - Constants.TILE_SIZE / 2):
            self.pos.x += self.player.speed
        if self.player.pos.y <= (self.pos.y + Constants.TILE_SIZE / 2):
            self.pos.y -= self.player.speed
        if self.player.pos.y >= (self.pos.y + self.height - Constants.TILE_SIZE / 2):
            self.pos.y += self.player.speed
