'''
Created on Apr 7, 2009

@author: Mohamed Elemam
'''

__PASS__ = 0
HUMAN_TILES_COUNT = 0
COMPUTER_TILES_COUNT = 0
NUMBER_OF_PLAYERS = 2

#----------------------------------------------------------------------------

from random import randrange
from computer import *

def generate_newgame():
    """ generate_newgame()
        this function takes nothing and returns a complete dominos list of 28 elements
    each element of this list is a "tuple".
    examples :-
    
    >>> x=generate_newgame()
    >>> print x
    [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 3), (3, 4), (3, 5), (3, 6), (4, 4), (4, 5), (4, 6), (5, 5), (5, 6), (6, 6)]
    
    >>> print len(x)
    28
    """
    return [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 3), (3, 4), (3, 5), (3, 6), (4, 4), (4, 5), (4, 6), (5, 5), (5, 6), (6, 6)]

#----------------------------------------------------------------------------

def destribute_tiles(tiles_set):
    """ destribute_tiles(tiles_set)
        this function takes a complete list of dominos tiles (list of tuples) and 
    returns one list that contains two lists, each list of them consists of seven tuples
    examples:-
    
    >>> x=generate_newgame()
    >>> result=destribute_tiles(x)
    >>> print len(result[0])
    7
    >>> print len(result[1])
    7
    """
    first_player_tiles=[]
    second_player_tiles=[]
    for i in range(0, 7):
        #add a tile for the first player, then remove it from the tiles list
        random_number = randrange(0, len(tiles_set))
        first_player_tiles.append(tiles_set[random_number])
        del(tiles_set[random_number])
        
        #add a tile for the second player, then remove it from the tiles list
        random_number = randrange(0, len(tiles_set))
        second_player_tiles.append(tiles_set[random_number])
        del(tiles_set[random_number])
    
    return [first_player_tiles, second_player_tiles]

#----------------------------------------------------------------------------

def END_GAME():
    pass

#----------------------------------------------------------------------------

def reverse(tile):
    square1 = tile[0]
    square2 = tile[1]
    reverse_tile = (square2,square1)
    return reverse_tile

#----------------------------------------------------------------------------

if __name__ == '__main__':
    complete_tiles_set = generate_newgame()
    played_tiles=[]
    
    both_players_tiles = destribute_tiles(complete_tiles_set)
    human_list = both_players_tiles[0][:]
    auto_player_list = both_players_tiles[1][:]
    
    HUMAN_TILES_COUNT = 7
    COMPUTER_TILES_COUNT = 7
    
    auto_player = computer(auto_player_list)
    
    
    
    
    while (HUMAN_TILES_COUNT != 0):
        
        print "human" ,human_list
        print "computer" ,auto_player_list
        print "please enter a tile index"
        
        user_choise=raw_input()
        if user_choise == "PASS":
            if __PASS__ == 1:
                print "GAME ENDED"
                break
            else:
                __PASS__ = 1
        else :
            tile = int(user_choise)
        
        if len(played_tiles) == 0 :
            played_tiles.append(human_list[tile])
            human_list.pop(tile)
        elif __PASS__ == 1 :
            pass
        else :
            if human_list[tile][1] == played_tiles[0][0]:
                played_tiles.insert(0, human_list[tile])
            elif human_list[tile][0] == played_tiles[-1][1]:
                played_tiles.insert(len(played_tiles), human_list[tile])
            elif human_list[tile][0] == played_tiles[0][0]:
                new_tile = reverse(human_list[tile])
                played_tiles.insert(0, new_tile)
            elif human_list[tile][1] == played_tiles[-1][1]:
                new_tile = reverse(human_list[tile])
                played_tiles.insert(len(played_tiles), new_tile)
            
            human_list.pop(tile)
        
        print played_tiles
        
        auto_tile = auto_player.play(played_tiles)
        if auto_tile == "PASS" :
            if __PASS__ == 1:
                print "GAME ENDED"
                break
            else:
                __PASS__ = 1
                continue
        
        if auto_tile[1] == played_tiles[0][0]:
            played_tiles.insert(0, auto_tile)
        elif auto_tile[0] == played_tiles[-1][1]:
            played_tiles.insert(len(played_tiles), auto_tile)
        elif auto_tile[0] == played_tiles[0][0]:
            new_tile = reverse(auto_tile)
            played_tiles.insert(0, new_tile)
        elif auto_tile[1] == played_tiles[-1][1]:
            new_tile = reverse(auto_tile)
            played_tiles.insert(len(played_tiles), new_tile)
        
        print played_tiles
        
        HUMAN_TILES_COUNT -= 1


#----------------------------------------------------