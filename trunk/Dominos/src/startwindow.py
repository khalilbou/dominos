#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit
from main import *
from os import environ


class splashWindow(object):
 
    def __init__(self):
        """
        __init__(self)
            this function will initiate the startwindow
        """
        environ['SDL_VIDEO_CENTERED']='1'
        pygame.init()
        seticon('images/icon.png')
        start_screen = pygame.display.set_mode((498,501),NOFRAME,32)
        init_background = pygame.image.load("images/init_bg.png").convert()
        pygame.display.set_caption("Dominoes!")
        onQuite_clicked_img = pygame.image.load("images/onclicked1.png")
        onenjoy_clicked_img = pygame.image.load("images/onclicked2.png")
        
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                     
                if event.type == MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    if x >= 172 and x <= 320 and y >= 435 and y<=480:
                        start_screen.blit(onenjoy_clicked_img,(190,438))
                        pygame.display.update()
                        pygame.time.wait(500)
                        main()
                    
                    elif x >= 324 and x <= 423 and y >= 327 and y<=369:
                        start_screen.blit(onQuite_clicked_img,(317,322))
                        pygame.display.update()
                        exit()
            
            start_screen.blit(init_background,(0,0))
            pygame.display.update()

if __name__ == '__main__':
    splashWindow()
            
        
        