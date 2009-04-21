#!/usr/bin/env python

#------------------IMPORTS------------------------
import pygame
from pygame.locals import *
from random import randrange
from sys import exit
from time import sleep
from computer import *
from Tile import *

#------------------Constants----------------------
main_window_resolution = (800, 600)
outer_color = (140,95,22)
bg_image = pygame.image.load("images/bg.png")

#-------------------Variables--------------------------
__PASS__ = 0
NUMBER_OF_PLAYERS = 2

HUMAN_TILES = []
COMPUTER_TILES = []

PLAYED_TILES = []

#----------------------------------------------------------------------------

def seticon(iconname):
    """
    give an iconname, a bitmap sized 32x32 pixels, black (0,0,0) will be alpha channel
    
    the windowicon will be set to the bitmap, but the black pixels will be full alpha channel
     
    can only be called once after pygame.init() and before somewindow = pygame.display.set_mode()
    """
    icon=pygame.Surface((32,32))
    icon.set_colorkey((0,0,0))
    rawicon=pygame.image.load(iconname)
    for i in range(0,32):
        for j in range(0,32):
            icon.set_at((i,j), rawicon.get_at((i,j)))
    pygame.display.set_icon(icon)

#----------------------------------------------------------------------------

def generate_tiles():
    """ generate_tiles()
        this function takes nothing and returns a complete dominos list of 28 elements
    each element of this list is a "tuple".
    """
	# TODO (DONE) make two loops instead of this mess :D
    temp = []
    for i in range(0,7):
        for j in range(i,7):
            temp.append((i,j))
    return temp

#----------------------------------------------------------------------------

def distribute_tiles(tiles_set, players_count):
    """
    distribute_tiles(tiles_set, players_count)
        Takes a complete dominos list and returns a list of lists
        each list contains 7 tiles as Tuples.
        WARNING! "players_count" should be less than 4.

        in this function we faced type of lists called list of lists
        for more clarify i will put example
        >>> count = 3
        >>> list = [[] for x in range(count)]
        >>> print list
        [[], [], []]
        this list were contain 3 lists each list for one player :D
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
            # TODO (DONE) use the 'pop' method instead of the following active two lines            
            final_list[j].append(tiles_set.pop(random_number))

    return final_list

#----------------------------------------------------------------------------

def initialize(screen):
    """
    initialize(screen)
        This function takes a "display" and creates the tiles sets for
        the players then displays them on the "display"
    """
    #Generate two random Tile lists
    complete_tiles_set = generate_tiles()
    both_players_tiles = distribute_tiles(complete_tiles_set, NUMBER_OF_PLAYERS)

    #Constructing the Human Tiles list
    identifier = 0

    x_start = main_window_resolution[0]/2 - 273
    x_end = x_start + 514
    y_start = main_window_resolution[1] - (main_window_resolution[1]/8) - 34

    for i in range(x_start, x_end, 80):
        HUMAN_TILES.append([both_players_tiles[0][identifier], (i, y_start)])
        identifier += 1


    #Constructing the Computer Tiles list
    identifier = 0
    y_start = (main_window_resolution[1] / 8) - 34

    for i in range(x_start, x_end, 80):
        COMPUTER_TILES.append([both_players_tiles[1][identifier], (i, y_start)])
        identifier += 1


    #draw the background and dominos tiles on the screen
    draw_bg(screen)
    draw_tiles(screen)

#----------------------------------------------------------------------------

def draw_bg(screen):
    """
    draw_bg()
        drawing the board background 
    """
    screen.blit(bg_image,(0,0))
    pygame.display.flip()

#----------------------------------------------------------------------------

def draw_tiles(screen):
    """
    draw_tiles()
        this function draws both computer's and human's tiles
    """

    #Print the human Tiles on the screen
    for i in range(len(HUMAN_TILES)):
        current_tile = HUMAN_TILES[i][0]
        current_position = HUMAN_TILES[i][1]
        temp_tile = Tile(current_tile[0], current_tile[1], screen, current_position[0], current_position[1])
        temp_tile.show_vertical()

    #Print the Computer Tiles (up-side-down)
    # TODO (DONE) changing the Computer tiles image
    for i in range(len(COMPUTER_TILES)):
        current_position = COMPUTER_TILES[i][1]
        temp_tile = Tile(9, 8, screen, current_position[0], current_position[1])
        temp_tile.show_vertical()

#----------------------------------------------------------------------------

def clicked_on_tile(mouse_position, tile_position):
    """
    clicked_on_tile(mouse_position, tile_position)
        takes two positions as "tuples", and returns True if the
        mouse is on the tile, and returns False otherwise.
    """
    if mouse_position[0] > tile_position[0]\
    and mouse_position[0] < (tile_position[0] + 34)\
    and mouse_position[1] > tile_position[1]\
    and mouse_position[1] < (tile_position[1] + 68) :
        return True
    else :
        return False

#----------------------------------------------------------------------------

def tile_check(tile):
    """
    human_tile_check(tile)
        Takes a tile as a tuple, and returns a tuple of (tile, position)
        which "tile" is the suitable tile, and position is "left"
        or "right" or None (if this is the first tile).

        syntax:
        >>> [[(tilex,tiley),(posx,posy)],[(tilex,tiley),(posx,posy)],[(tilex,tiley),(posx,posy)]]
        
        example for last tile played on the right
        >>> b=[[(0,1),(100,200)],[(0,2),(300,400)],[(0,3),(500,600)]]
        >>> print b[-1][0][1]
        3
        represented the tiley (second_tile_value) for the last tile played on the right
        
        example for last tile played on the left
        >>> print b[0][0][0]
        0
        represented the tilex (first_tile_value) for the last tile played on the left
    """

    #If this is the first tile to be played
    if len(PLAYED_TILES) == 0 :
        return tile, None

    #check if the tile can be played on the right
    elif tile[0] == PLAYED_TILES[-1][0][1] :
        return tile, "right"
    elif tile[1] == PLAYED_TILES[-1][0][1] :
        return (tile[1], tile[0]), "right"

    #check if the tile can be played on the left
    elif tile[1] == PLAYED_TILES[0][0][0] :
        return tile, "left"
    elif tile[0] == PLAYED_TILES[0][0][0] :
        return (tile[1], tile[0]), "left"

    #If the tile isn't suitable
    else :
        return None

#----------------------------------------------------------------------------
# TODO Add animation SOMEHOW!!!
# TODO make the can be played left and can be played right in the same turn
#ask the player where to play his tiles 
def play(tile, screen, place = None):
    """
    play(tile, screen, place)
        this function takes a tile as a "tuple", display
        and a place ("left" or "right"). then draws the tile on the screen.
                
        example for the x_position to the last tile played on the left
        >>> b=[[(0,1),(100,200)],[(0,2),(300,400)],[(0,3),(500,600)]]
        >>> print b[0][1][0]
        100
        
        example for the y_position to the last tile played on the left
        >>> print b[0][1][1]
        200
        
        example for the x_position to the last tile played on the right
        >>> print b[-1][1][0]
        500
        
        example for the y_position to the last tile played on the right
        >>> print b[-1][1][1]
        600 
    """

    #Initialize the place of the tile
    tile_x = 0
    tile_y = 0

    #check if this tile is the first tile to be played
    if len(PLAYED_TILES) == 0 :

        #check if the tile is DUO, then place it in the right place
        if tile[0] == tile[1]:
            tile_x = main_window_resolution[0]/2 - 17
            tile_y = main_window_resolution[1]/2 - 34
            PLAYED_TILES.append([tile,(tile_x, tile_y)])
        else :
            tile_x = main_window_resolution[0]/2 - 34
            tile_y = main_window_resolution[1]/2 - 17
            PLAYED_TILES.append([tile,(tile_x, tile_y)])

    #If this tile is not the first played tile, check if the user
    #passed the place or not ("left" or "right")
    elif place is not None :

        #if the tile is DUO
        if tile[0] == tile[1]:

            #if the tile is DUO and going to be placed on the left side
            if place == "left" :
                tile_x = PLAYED_TILES[0][1][0] - 34
                tile_y = PLAYED_TILES[0][1][1] - 17
                PLAYED_TILES.insert(0, [tile, (tile_x, tile_y)])

            #if the tile is DUO and going to be placed on the right side
            elif place == "right" :
                tile_x = PLAYED_TILES[-1][1][0] + 68
                tile_y = PLAYED_TILES[-1][1][1] - 17
                PLAYED_TILES.append([tile, (tile_x, tile_y)])

        #If the tile is not DUO
        else :

            #if the tile is not DUO and going to be placed on the left side
            if place == "left" :

                #check if the previous tile was DUO
                if PLAYED_TILES[0][0][0] == PLAYED_TILES[0][0][1] :
                    tile_x = PLAYED_TILES[0][1][0] - 68
                    tile_y = PLAYED_TILES[0][1][1] + 17
                    PLAYED_TILES.insert(0, [tile, (tile_x, tile_y)])

                #If the previous was't DUO
                else :
                    tile_x = PLAYED_TILES[0][1][0] - 68
                    tile_y = PLAYED_TILES[0][1][1]
                    PLAYED_TILES.insert(0, [tile, (tile_x, tile_y)])

            #if the tile is not DUO and going to be placed on the right side
            elif place == "right" :

                #If the previous tile was DUO
                if PLAYED_TILES[-1][0][0] == PLAYED_TILES[-1][0][1] :
                    tile_x = PLAYED_TILES[-1][1][0] + 34
                    tile_y = PLAYED_TILES[-1][1][1] + 17
                    PLAYED_TILES.append([tile, (tile_x, tile_y)])

                #If the previous tile wasn't DUO
                else :
                    tile_x = PLAYED_TILES[-1][1][0] + 68
                    tile_y = PLAYED_TILES[-1][1][1]
                    PLAYED_TILES.append([tile, (tile_x, tile_y)])

    #Create a Tile object
    temp_tile = Tile(tile[0], tile[1], screen, tile_x, tile_y)

    #Check if this tile is DUO
    if tile[0] == tile[1]:

        #If the tile is DUO, then it will be placed vertically
        temp_tile.show_vertical()

    else :

        #If the tile is not DUO, then it will be placed horizontally
        temp_tile.show_horizontal()

#----------------------------------------------------------------------------

def hide_tile(x, y, screen):
    hiding_rectangle = Rect(x, y, 34, 68)
    pygame.draw.rect(screen, outer_color, hiding_rectangle)

#----------------------------------------------------------------------------

def END_GAME():
    pass

#----------------------------------------------------------------------------

if __name__ == '__main__':

    #Initialize PyGame    
    pygame.init()
    
    # TODO (DONE) adding game icon
    
    seticon('images/icon.png')
    
    #Create the Main Window
    screen = pygame.display.set_mode(main_window_resolution, 0, 32)
    pygame.display.set_caption("Dominos!")

    #initialize the game
    initialize(screen)
    auto_player = computer(COMPUTER_TILES)

#####################  MAIN LOOP  #######################

    while True:

        #Handling PyGame events
        event = pygame.event.wait()

        #Handling the QUIT signal
        if event.type == QUIT:
            exit()

        #Handling the Mouse Events (Checking whether the user clicked on a tile)
        elif event.type == MOUSEBUTTONDOWN :
            for tile in HUMAN_TILES :

                #if the human clicked on a tile
                if clicked_on_tile(event.pos, tile[1]):
                    result = tile_check(tile[0])
                    if result is not None :
                        play(result[0], screen, result[1])
                        HUMAN_TILES.remove(tile)
                        hide_tile(tile[1][0], tile[1][1], screen)

                    # TODO add a PASS button
                    #Ask the computer to play
                    chosen_tile = auto_player.play(PLAYED_TILES)
                    if chosen_tile != "PASS" :
                        final_tile = tile_check(chosen_tile[0])
                        play(final_tile[0], screen, final_tile[1])
                        hide_tile(chosen_tile[1][0], chosen_tile[1][1], screen)

                    #if the computer said "PASS"
                    else :

                        #If the human said "PASS" last time, End the game
                        if __PASS__ == 1 :
                            END_GAME()

                        #If the human didn't say "ASS" last time, set __PASS__ to 1
                        else :
                            __PASS__ = 1





        pygame.display.update()

