# You don't have to use this code
# this is just a sample code that I was provided
# it may not be the best for every project

import pygame
from pygame.locals import *

WHITE = [255, 255, 255]
BLACK = [  0,   0,   0]

class App:
    def __init__(self):
        self._running = True
        self.surface = None
        self.width = 640 # defines window width
        self.height = 400 # defines window height
        self.size = [self.width, self.height] # sets the window size
        self.clock = pygame.time.Clock()
        self.fps = 60 # sets the game's framerate (i.e. 'ticks' per second)

    def on_init(self):
        pygame.init()
        self.surface = pygame.display.set_mode(self.size)
        self._running = True

        # usable variables, this is where you initialize the game's
        # beginning conditions
        # should use attributes of self
        # i.e. self.character for the player's character

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
        pygame.quit()

    def on_execute(self):
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
