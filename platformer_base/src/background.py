# Background Class

from tkinter import *
from .vector_2D import *
from .entity import *
from .player import *
from .sprite import *
from .constants import *

""" The background of a single level in the game. Contains a 2D array of
    Sprites that represent the map the player interacts with. The background
    also contains the player, and manages the player's movement. """

class Background(Entity):
    def __init__(self, map_file):
        Entity.__init__(self, -Constants.TILE_SIZE + 1, 0)
        self.width = 0
        self.height = 0
        self.tiles = self.generate_map(map_file)
        self.player = Player(200, 280)

    def render(self, window):
        """ Renders the background on the screen. """
        self.draw_map(window)
        self.player.draw(window)

    def update(self):
        """ Updates the status of the entities on the background. """
        self.player_move()
        self.player_jump()

    def draw_map(self, window):
        """ Draws each of the tiles currently visible on the map. """
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[0])):
                if self.pos.x + (x * Constants.TILE_SIZE) > (-2 * Constants.TILE_SIZE) \
                and self.pos.x + (x * Constants.TILE_SIZE) < Constants.SCREEN_WIDTH + (2 * Constants.TILE_SIZE):
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
        elif sprite_id == Sprite.SPRING:
            return Sprite(sprite_id, True, True, False)
        return Sprite(Sprite.ERROR, False, False, False)

    def player_move(self):
        """ Handles motion of the map and player. """
        if self.player.visible:
            if self.player.move_state[Constants.RIGHT]:
                if (not self.player.collision[Constants.RIGHT]) \
                and self.vel.x > -self.player.max_x_speed:
                    self.vel.x -= self.player.x_speed
            elif self.vel.x < 0:
                self.vel.x += self.player.friction
                if self.vel.x > 0:
                    self.vel.x = 0
            if self.player.move_state[Constants.LEFT]:
                if (not self.player.collision[Constants.LEFT]) \
                and self.vel.x < self.player.max_x_speed:
                    self.vel.x += self.player.x_speed
            elif self.vel.x > 0:
                self.vel.x -= self.player.friction
                if self.vel.x < 0:
                    self.vel.x = 0
            self.update_pos()
            self.player_collision()

    def update_pos(self):
        """ Updates the position of the map and player after movement. """
        if self.pos.x > -Constants.TILE_SIZE:
            self.player.pos.x -= self.vel.x
            if self.player.pos.x < Constants.TILE_SIZE / 2:
                self.player.pos.x = Constants.TILE_SIZE / 2
                self.vel.x = 0
            if self.player.pos.x > Constants.SCREEN_WIDTH / 2:
                self.pos.x = -Constants.TILE_SIZE
        elif self.pos.x < -self.width + Constants.SCREEN_WIDTH + Constants.TILE_SIZE:
            self.player.pos.x -= self.vel.x
            if self.player.pos.x > Constants.SCREEN_WIDTH - Constants.TILE_SIZE / 2:
                self.player.pos.x = Constants.SCREEN_WIDTH - Constants.TILE_SIZE / 2
                self.vel.x = 0
            if self.player.pos.x < Constants.SCREEN_WIDTH / 2:
                self.pos.x = -self.width + Constants.SCREEN_WIDTH + Constants.TILE_SIZE + 1
        else:
            self.pos.x += self.vel.x

    def player_collision(self):
        """ Checks collisions between the player and any solid tiles. """
        bx = int((self.player.pos.x - self.pos.x) / Constants.TILE_SIZE)
        by = int((self.player.pos.y - self.pos.y) / Constants.TILE_SIZE)
        up = int((self.player.pos.y - self.pos.y) / Constants.TILE_SIZE)
        down = int((self.player.pos.y - (Constants.TILE_SIZE / 2) - self.pos.y) / Constants.TILE_SIZE)
        left = int((self.player.pos.x + (Constants.TILE_SIZE / 2) - self.pos.x) / Constants.TILE_SIZE)
        right = int((self.player.pos.x - (Constants.TILE_SIZE / 2) - self.pos.x) / Constants.TILE_SIZE)
        if self.tiles[down + 1][bx].solid:
            if self.tiles[down + 1][bx].elastic:
                self.player.vel.y = -2.0 * self.player.vel.y
                if self.player.vel.y > self.player.max_y_speed:
                    self.player.vel.y = self.player.max_y_speed
            else:
                self.player.collision[Constants.DOWN] = True
                self.player.pos.y = (down * Constants.TILE_SIZE) + Constants.TILE_SIZE / 2
        else:
            self.player.collision[Constants.DOWN] = False
        if self.tiles[up - 1][bx].solid:
            if not self.player.collision[Constants.UP]:
                self.player.collision[Constants.UP] = True
        else:
            self.player.collision[Constants.UP] = False
        if self.tiles[by][left - 1].solid:
            if not self.player.collision[Constants.LEFT]:
                self.player.collision[Constants.LEFT] = True
                self.vel.x = 0
        else:
            self.player.collision[Constants.LEFT] = False
        if self.tiles[by][right + 1].solid:
            if not self.player.collision[Constants.RIGHT]:
                self.player.collision[Constants.RIGHT] = True
                self.vel.x = 0
        else:
            self.player.collision[Constants.RIGHT] = False

    def player_jump(self):
        """ Handles jumping and gravity of the player. """
        if self.player.visible:
            if self.player.jump_state == Constants.RISING:
                if self.player.vel.y < self.player.max_y_speed:
                    self.player.pos.y -= (self.player.max_y_speed + 2) - self.player.vel.y
                    self.player.vel.y += self.player.gravity
                elif self.player.vel.y >= self.player.max_y_speed:
                    self.player.jump_state = Constants.FALLING
                    self.player.vel.y = 0
                if self.player.collision[Constants.UP]:
                    self.player.jump_state = Constants.FALLING
                    self.player.vel.y = 0
            elif self.player.jump_state == Constants.FALLING:
                if not self.player.collision[Constants.DOWN]:
                    self.player.pos.y += self.player.vel.y
                    if self.player.vel.y < self.player.max_y_speed:
                        self.player.vel.y += self.player.gravity
                else:
                    self.player.jump_state = Constants.NOT_JUMPING
                    self.player.vel.y = 0
            elif self.player.jump_state == Constants.NOT_JUMPING:
                if not self.player.collision[Constants.DOWN]:
                    self.player.jump_state = Constants.FALLING
                    self.player.vel.y = 0
