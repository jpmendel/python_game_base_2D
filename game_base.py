# Python Simple 2D Game Skeleton
# By Jacob Mendelowitz

from tkinter import *

class Game:
    TITLE = "My Game" # String of the title at the top bar of the window.
    ICON = None # Path to the icon image in the top left corner of the window.
    SCREEN_WIDTH = 600 # Width of the window.
    SCREEN_HEIGHT = 450 # Height of the window.
    FRAME_RATE = 30 # Frames per second refresh speed of the game.
    USING_MOUSE = True # Boolean to enable checking of mouse events.
    USING_KEYBOARD = True # Boolean to enable checking of keyboard events.
    def __init__(self, window):
        """ The class that controls everything in the game.
            If you want to have objects in your game, make them and set
            them to their classes here. Make sure they are self.something
            attributes, so they can be used throughout the Game class. """
        self.window = window
        # i.e. self.object = Class()
    def render(self):
        """ Put all drawing functions you want the game to run here.
            This function will run every '1000 / FRAME_RATE' milliseconds. """
        pass
    def update(self):
        """ Put all other functions you want the game to run here.
            This function will run every '1000 / FRAME_RATE' milliseconds. """
        pass
    def mouse_motion(self, x_pos, y_pos):
        """ When you move the mouse, this code runs.
            The function provides the x and y coordinates of the mouse at
            any given instant. """
        pass
    def l_mouse_pressed(self, x_pos, y_pos):
        """ When you press the left mouse button, this code runs.
            The function provides the x and y coordinates of the click when
            the mouse is pressed. """
        pass
    def r_mouse_pressed(self, x_pos, y_pos):
        """ When you press the right mouse button, this code runs.
            The function provides the x and y coordinates of the click when
            the mouse is pressed. """
        pass
    def key_pressed(self, character, symbol):
        """ When you press any key, this code runs.
            The function provides the character of the key
            ("a", "b", "c", "d", "e", " ", etc.)
            As well as the symbol which can be used for the arrow keys
            ("Up", "Down", "Left", "Right", "space", etc.) """
        pass
    def key_released(self, character, symbol):
        """ When you release any key, this code runs.
            The function provides the character of the key
            ("a", "b", "c", "d", "e", " ", etc.)
            As well as the symbol which can be used for the arrow keys
            ("Up", "Down", "Left", "Right", "space", etc.) """
        pass


class ImageDatabase:
    def __init__(self):
        """ A database to hold all the images.
            Load in new images to the game by inserting them below in the
            same form as the commented example below. """
        PATH = "res/images/"
        self.images = {}
        # self.images["Example"] = PhotoImage(file = PATH + "example.gif")
    def get_image(self, name):
        """ Use this to call an image from the database.
            Simply put: database.get_image("ImgName") to retrieve the image. """
        return self.images[name]


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
    """ Loops the refresh_GUI function over and over.
        The loop is executed every 'delay' milliseconds. """
    refresh_GUI()
    delay = 1000 // Game.FRAME_RATE
    game.window.after(delay, main_function)

def refresh_GUI():
    """ Deletes everything on the screen, changes data about the things in
        the game, then redraws them in their new locations.
        This function does three things:
        1. Deletes all graphics on the window.
        2. Runs update from the Game class.
        3. Runs render from the Game class. """
    game.window.delete(ALL)
    game.update()
    game.render()

def init():
    """ Sets up everything important. """
    global tk
    global game
    global database
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
    database = ImageDatabase()

def run():
    """ Runs the game. """
    init()
    main_function()
    tk.mainloop() # Launch program.

run()
