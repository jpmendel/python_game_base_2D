# Python Simple Platformer Demo
# By Jacob Mendelowitz

from tkinter import *
from src.background import *

class Game:
    TITLE = "Platformer Example"
    ICON = "res/icon.ico"
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 450
    FRAME_RATE = 60
    USING_MOUSE = False
    USING_KEYBOARD = True
    def __init__(self, window):
        self.window = window
        self.background = Background("res/map.txt")
        
    def render(self):
        self.background.render(self.window)

    def update(self):
        self.background.update()

    def mouse_motion(self, x_pos, y_pos):
        pass
    def l_mouse_pressed(self, x_pos, y_pos):
        pass
    def r_mouse_pressed(self, x_pos, y_pos):
        pass

    def key_pressed(self, character, symbol):
        if character == "w":
            if self.background.player.jump_state == Constants.NOT_JUMPING:
                self.background.player.collision[Constants.DOWN] = False
                self.background.player.jump_state = Constants.RISING
        elif character == "a":
            self.background.player.move_state[Constants.LEFT] = True
            self.background.player.move_state[Constants.RIGHT] = False
        elif character == "d":
            self.background.player.move_state[Constants.RIGHT] = True
            self.background.player.move_state[Constants.LEFT] = False

    def key_released(self, character, symbol):
        if character == "w":
            if self.background.player.jump_state == Constants.RISING:
                self.background.player.jump_state = Constants.FALLING
                self.background.player.vel.y = 0
        elif character == "a":
            self.background.player.move_state[Constants.LEFT] = False
        elif character == "d":
            self.background.player.move_state[Constants.RIGHT] = False

##############################################################################

############# SETUP CODE AND HELPER FUNCTIONS BELOW THIS LINE ################

##############################################################################

def mouse_motion(event):
    game.mouse_motion(event.x, event.y)

def l_mouse_pressed(event):
    game.l_mouse_pressed(event.x, event.y)

def r_mouse_pressed(event):
    game.r_mouse_pressed(event.x, event.y)

def key_pressed(event):
    game.key_pressed(event.char, event.keysym)

def key_released(event):
    game.key_released(event.char, event.keysym)

def main_function():
    refresh_GUI()
    delay = 1000 // Game.FRAME_RATE
    game.window.after(delay, main_function)

def refresh_GUI():
    game.window.delete(ALL)
    game.update()
    game.render()

def init():
    global tk
    global game
    tk = Tk() # Makes the tk object into the window application.
    canvas = Canvas(tk, width=Game.SCREEN_WIDTH, height=Game.SCREEN_HEIGHT)
    canvas.pack() # Adds a canvas for drawing on the window.
    tk.resizable(width=0, height=0)
    tk.title(Game.TITLE) # Creates title in top bar of window.
    if Game.ICON:
        tk.iconbitmap(Game.ICON) # Creates icon in top left of window.
    if Game.USING_MOUSE:
        tk.bind("<Motion>", mouse_motion) # Checks for mouse motion.
        tk.bind("<Button-1>", l_mouse_pressed) # Checks for left mouse press.
        tk.bind("<Button-3>", r_mouse_pressed) # Checks for right mouse press.
    if Game.USING_KEYBOARD:
        tk.bind("<KeyPress>", key_pressed) # Checks for any key press.
        tk.bind("<KeyRelease>", key_released) # Checks for any key release.
    game = Game(canvas)

def run():
    init()
    main_function()
    tk.mainloop() # Launch program.

run()
