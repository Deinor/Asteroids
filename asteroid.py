import pyglet
from pyglet.window import key
from game import load, gui, player, asteroid, menu, levels

#Game constants
version = str(0.01)
score = 0
number_of_asteroids_big = 0
number_of_asteroids_medium = 0
asteroids_big = []
asteroids_medium = []

number_of_lives = 3
event_stack_size = 0
game_objects = []
level_number = 0
game_on = False

#Create main batch
main_batch = pyglet.graphics.Batch()

#Set up game window(width, height)
game_window = pyglet.window.Window(1280, 720)

#Set up top static lables
version_label = pyglet.text.Label(text=version, x=10, y=700, batch=main_batch)
score_label = pyglet.text.Label(text="Score is: 0", x=200, y=700, batch=main_batch)
      
def reset_game():
    global number_of_asteroids_big, number_of_asteroids_medium, number_of_lives
    number_of_asteroids_big = 1
    number_of_asteroids_medium = 1
    number_of_lives = 3  

def init():
    main_menu()

def start_game():
    """
    Run main game loop.
    """
    main_menu_obj.remove()
    game_window.pop_handlers()
    run_game(number_of_lives, level_number)

def set_new_level():
    """
    After clearing level creates massage and sets up variables for next level.
    """
    global level_number
    for obj in game_objects:
        obj.delete()
    level_number += 1
    number_of_lives = 3
    main_menu_obj.remove()
    game_window.pop_handlers()
    run_game(number_of_lives, level_number)

def test_2():

    """
    Options.
    """
    print('options')

def exit_game():
    """
    Exit.
    """
    game_window.close()

def main_menu():
    global main_menu_obj
    #main_menu_obj = menu.NextLevel(set_new_level, test_3, main_batch)
    main_menu_obj = menu.MainMenu(start_game, test_2, exit_game, main_batch)
    game_window.push_handlers(main_menu_obj)

def game_over():
    menu.Banner('You got crushed by ateroids.', main_batch)

def run_game(number_of_lives, level_number):

    global player_ship, asteroids, game_objects, event_stack_size, player_live, game_on

    game_on = True

    asteroids = levels.levels(level_number)

    #Clean up stack of event handleres before new level
    while event_stack_size > 0:
        game_window.pop_handlers()
        event_stack_size -= 1       

    #Player live sprite
    player_live = gui.player_lives(number_of_lives, main_batch)

    global asteroids_big, asteroids_medium  
    #Load objects
    player_ship = player.Player(x=640, y=350, batch=main_batch)
    asteroids_big = load.asteroids_big(asteroids[0], player_ship.position, main_batch)
    asteroids_medium = load.asteroids_medium(asteroids[1], player_ship.position, main_batch)

    #List of game objects
    game_objects = [player_ship] + asteroids_big + asteroids_medium

    #Add event handler to the stack
    for obj in game_objects:
        for handler in obj.event_handlers:
            game_window.push_handlers(handler)
            event_stack_size += 1

#Seting up event handler on_draw
@game_window.event
def on_draw():
    #Clear the screen
    game_window.clear()
    
    #Draw objects
    main_batch.draw()

def update(dt):
    global score, number_of_lives

    player_dead = False

    #Sets up constant to check if are any asteroids left in game
    asteroids_alive = 0

    for i in range(len(game_objects)):
    #Nested loop to avoid checking collisions twice and ceckink collision with it self
        for j in range(i + 1 , len(game_objects)):
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]

            #Checks if objects are not already dead 
            if not obj_1.dead and not obj_2.dead:
                if obj_1.check_collision(obj_2):
                    obj_1.collision_action(obj_2)
                    obj_2.collision_action(obj_1)
    
    #List of objects added (spawned) while game is running, separete list to avoid changing the object list while iterating over it
    to_add = []

    #Function updating game objects
    for obj in game_objects:
       obj.update(dt)
       to_add.extend(obj.new_objects)
       obj.new_objects = []

       #Check if any asteroid is alive in game
       if (isinstance(obj, asteroid.AsteroidBig) or isinstance(obj, asteroid.AsteroidMedium)):
        asteroids_alive += 1       

    for remove_object in [obj for obj in game_objects if obj.dead]:

        #Remove object from batch
        remove_object.delete()
        #Remove object from game objects list
        game_objects.remove(remove_object)        

        #Score is added when asteroid obj gets destroyed
        if isinstance (remove_object, asteroid.AsteroidBig):
            #Check if deleted object is asteroid class
            score += 1
            score_label.text = f"Score is: {score}"
        
        if isinstance (remove_object, asteroid.AsteroidMedium):
            #Check if deleted object is asteroid class
            score += 1
            score_label.text = f"Score is: {score}"

        if remove_object == player_ship:
            player_dead = True

    game_objects.extend(to_add)

    if player_dead:
        number_of_lives -= 1
        if number_of_lives > 0:
            run_game(number_of_lives)
        else:
            game_over()

    global main_menu_obj

    if  asteroids_alive == 0 and game_on and not isinstance(main_menu_obj, menu.NextLevel):
        #Checks if wining conditions are fulfilled and lets player choose to start next level or exit game
        
        #TODO pop player handleres in menu
        #game_window.pop_handlers()
        
        main_menu_obj = menu.NextLevel(set_new_level, exit_game, main_batch)
        game_window.push_handlers(main_menu_obj)
        

if __name__ == '__main__':

    init()

    #Call update function
    pyglet.clock.schedule_interval(update, 1/120.0)

    #Run the window
    pyglet.app.run()