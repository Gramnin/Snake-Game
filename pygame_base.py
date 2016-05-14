# You don't have to use this code
# this is just a sample code that I was provided
# it may not be the best for every project

import pygame
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.width = 640
        self.height = 400
        self.size = (self.width, self.height)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        # things that happen when the user does something
        if event.type == pygame.QUIT:
            self._running = False
   
    def on_loop(self):
        pass # things that happen every 'tick' of the game
   
    def on_render(self):
        pass # the actual drawing of the screen
   
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
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
