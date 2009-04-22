import pygame
from pygame.locals import *
from sys import exit
from main import seticon

class splashWindow(object):
 
    def __init__(self):
        """
        __init__(self)
            this function will initiate the startwindow
        """
        pygame.init()
        seticon('images/icon.png')
        start_screen = pygame.display.set_mode((498,501),NOFRAME)
        init_background = pygame.image.load("images/init_bg.png").convert()
        ###
        #TODO: MAKE CENTER IS THE DEFAULT POSITION
        ###
        while True:
            for event in pygame.event.get(): 
                if event.type == MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    if x >= 172 and x <= 320 and y >= 435 and y<=480:
                        pass
                        ###
                        #TODO:INITIATE THE BOARD WINDOW
                        ###
                    else:
                        if x >= 324 and x <= 423 and y >= 327 and y<=369:
                            exit()
            
            start_screen.blit(init_background,(0,0))
            pygame.display.update()

splashWindow()
            
        
        