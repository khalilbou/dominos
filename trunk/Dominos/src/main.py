#!/usr/bin/env python
'''
Created on Apr 7, 2009

@author: Mohamed Elemam
'''

#------------------IMPORTS------------------------
import pygame
from pygame.locals import *

from random import randrange
from sys import exit
from time import sleep

from computer import *
from Tile import *

#------------------Constants----------------------
main_window_resolution = (800,600)
light_green = (0,200,15)
dark_green = (0,140,15)

#-------------------Variables--------------------------
__PASS__ = 0
NUMBER_OF_PLAYERS = 2

LEFT_TILE_PLACE = []
RIGHT_TILE_PLACE = []

HUMAN_TILES = []
COMPUTER_TILES = []

#----------------------------------------------------------------------------

def generate_tiles():
    """ generate_tiles()
        this function takes nothing and returns a complete dominos list of 28 elements
    each element of this list is a "tuple".
    examples :-
    
    >>> x=generate_newgametiles()
    >>> print x
    [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 3), (3, 4), (3, 5), (3, 6), (4, 4), (4, 5), (4, 6), (5, 5), (5, 6), (6, 6)]
    """
    return [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 3), (3, 4), (3, 5), (3, 6), (4, 4), (4, 5), (4, 6), (5, 5), (5, 6), (6, 6)]

#----------------------------------------------------------------------------

def draw_rectangles(screen):
    """
    init_game()
        Initialize the game graphics by creating a new display
        and returns that display
    """
    
    screen.fill(dark_green)
    
    center_rectangle_start = (0, main_window_resolution[1]/4)
    center_rectangle_size = (main_window_resolution[0], main_window_resolution[1]/2)
    center_rectangle = Rect(center_rectangle_start, center_rectangle_size)
    
    pygame.draw.rect(screen, light_green, center_rectangle)
    
    pygame.display.update()
    

def distribute_tiles(tiles_set, players_count):
    """
    distribute_tiles(tiles_set, players_count)
        Takes a complete dominos list and returns a list of lists
        each list contains 7 tiles as Tuples.
        WARNING! "players_count" should be less than 4.
    """
    #check the validity of the number of players
    if players_count > 4 :
        raise ValueError
    
    #create an empty list of lists, to hold the players' tiles
    final_list=[ [] for x in range(players_count) ]
    
    #fill the "final_list" with random tiles
    for i in range(0, 7):
        for j in range(players_count):
            random_number = randrange(0, len(tiles_set))
            final_list[j].append(tiles_set[random_number])
            del(tiles_set[random_number])
    
    return final_list

#----------------------------------------------------------------------------

def END_GAME():
    pass

#----------------------------------------------------------------------------

if __name__ == '__main__':
    
    #Initialize PyGame
    pygame.init()
    
    #Initialize the Main Window
    screen = pygame.display.set_mode(main_window_resolution, 0, 32)
    pygame.display.set_caption("Dominos!")
    
    #Generate two randome Tile lists
    complete_tiles_set = generate_tiles()
    both_players_tiles = distribute_tiles(complete_tiles_set, NUMBER_OF_PLAYERS)
    
#    #Constructing Computer's Tiles
#    COMPUTER_TILES = both_players_tiles[0][:]
    
    #Constructing the Human Tiles list
    identifier = 0
    for i in range(80, 700, 100):
        HUMAN_TILES.append([both_players_tiles[1][identifier], (i, 480)])
        identifier += 1
    
    #Constructing the Computer Tiles list
    identifier = 0
    for i in range(80, 700, 100):
        COMPUTER_TILES.append([both_players_tiles[0][identifier], (i, 50)])
        identifier += 1
    
    #Draw Rectangles in the Main Window
    draw_rectangles(screen)
    
#####################  MAIN LOOP  #######################
    
    while True:
        
        #Print the human Tiles on the screen
        for i in range(len(HUMAN_TILES)):
            current_tile = HUMAN_TILES[i][0]
            current_position = HUMAN_TILES[i][1]
            temp_tile = Tile(current_tile[0], current_tile[1], screen, current_position[0], current_position[1])
            temp_tile.show_vertical()
        
        #Print the Computer Tiles (up-side-down)
        for i in range(len(COMPUTER_TILES)):
            current_position = COMPUTER_TILES[i][1]
            temp_tile = Tile(0, 0, screen, current_position[0], current_position[1])
            temp_tile.show_vertical()
        
        #Handling PyGame events
        for event in pygame.event.get():
            
            #Handling the QUIT signal
            if event.type == QUIT:
                exit()
            
            #Handling the Mouse Events (Checking whether the user clicked on a tile)
            elif event.type == MOUSEBUTTONDOWN :
                for tile in HUMAN_TILES :
                    tile_position = tile[1]
                    mouse_position = event.pos
                    if mouse_position[0] > tile_position[0]\
                    and mouse_position[0] < (tile_position[0] + 34)\
                    and mouse_position[1] > tile_position[1]\
                    and mouse_position[1] < (tile_position[1] + 68) :
                        print tile[0]
        
        
        
#        event = pygame.event.wait()
#        if event.type == QUIT:
#            exit()
#        elif event.type == MOUSEBUTTONDOWN :
#            print "test"
#            if event.pos[0] > 480 and event.pos[0] < 548 and event.pos[1] > 80 and event.pos[1] < 148 :
#                print "hiiiii"
        
        
        
        
        
        #pygame.display.update()
        
        