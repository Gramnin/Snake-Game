import pygame
from pygame.locals import *

WHITE = [255, 255, 255]
BLACK = [  0,   0,   0]

class App:
    def __init__(self):
        # the __init__ function creates the object and sets up the INITial
        # parameters, you probably won't have to change this function other
        # than for the width, height, and framerate, any variables you need
        # should be added to the on_init function
        self._running = True
        self.surface = None
        self.width = 640 # defines window width
        self.height = 400 # defines window height
        self.size = [self.width, self.height] # sets the window size
        self.clock = pygame.time.Clock()
        self.fps = 60 # sets the game's framerate (i.e. 'ticks' per second)

    def on_init(self):
        # this game's setup function, sets up pygame and any variables the
        # developer needs for the game to work properly
        pygame.init()
        self.surface = pygame.display.set_mode(self.size)
        self._running = True

        # usable variables, this is where you initialize the game's
        # beginning conditions
        # should use attributes of self
        # i.e. self.character for the player's character

        # ^ add here ^

    def on_event(self, event):
        # things that happen when the user does something
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        # things that happen every 'tick' of the game
        pass

    def on_render(self):
        # the actual drawing of the screen
        self.surface.fill(WHITE)
        
        #drawing goes here
        
        pygame.display.flip()

    def on_cleanup(self):
        # this should only be changed if there are things that need to be
        # cloased after the user quits the game, things like files
        pygame.quit()

    def on_execute(self):
        # this calls the other functions in the game and doesn't need to be
        # changed by the developer
        if self.on_init() == False:
            self._running = False

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self.clock.tick(self.fps)
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
