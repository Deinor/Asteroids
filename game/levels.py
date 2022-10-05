def levels(n):
    """
    Sets up number of objects to load at start of the game based on level input.
    """

    levels_object_list = []
    
    #[level_1[number_of_asteroids_big, number_of_asteroids_medium], level_2[number_of_asteroids_big, number_of_asteroids_medium] ...]
    levels_object_list = [[0, 1], [0, 2], [3, 2], [3, 3]]
    curent_level = levels_object_list[n]
    return curent_level

