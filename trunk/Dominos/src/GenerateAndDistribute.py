from random import randrange

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
    """
    #check the validity of the number of players
    if players_count > 4 :
        raise ValueError

    #create an empty list of lists, to hold the players' tiles
    final_list= [[] for x in range(players_count)]

    #fill the "final_list" with random tiles
    for i in range(0, 7):
        for j in range(players_count):
            random_number = randrange(0, len(tiles_set))
            # TODO (DONE) use the 'pop' method instead of the following active two lines
            final_list[j].append(tiles_set.pop(random_number))

    return final_list

#----------------------------------------------------------------------------
