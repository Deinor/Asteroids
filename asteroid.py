import pyglet
from pyglet.window import key
from game import load, gui, player, asteroid, menu

#Game constants
version = str(0.01)
score = 0
number_of_asteroids = 0
number_of_lives = 3
event_stack_size = 0
game_objects = []

#Create main batch
main_batch = pyglet.graphics.Batch()

#Set up game window(width, height)
game_window = pyglet.window.Window(1280, 720)

#Set up top static lables
version_label = pyglet.text.Label(text=version, x=10, y=700, batch=main_batch)
score_label = pyglet.text.Label(text="Score is: 0", x=200, y=700, batch=main_batch)
      
def reset_game():
    global number_of_asteroids, number_of_lives
    number_of_asteroids = 1
    number_of_lives = 3  

def init():
    main_menu()

def start_game():
    """
    Run main game loop.
    """
    main_menu_obj.remove()
    run_game()

def test_2():
    """
    Options.
    """
    print('options')


def test_3():
    """
    Exit.
    """
    print('exit')

def main_menu():
    global main_menu_obj
    main_menu_obj = menu.MainMenu(start_game, test_2, test_3, main_batch)
    game_window.push_handlers(main_menu_obj)

def run_game():
    #Add event handler to the stack
    for obj in game_objects:
        for handler in obj.event_handlers:
            game_window.push_handlers(handler)
            event_stack_size += 1

    global number_of_asteroids

    number_of_asteroids = 3
    reset_level(number_of_lives)    
 
def reset_level(number_of_lives):
    global player_ship, asteroids, game_objects, event_stack_size, player_live

    #Clean up stack of event handleres before new level
    while event_stack_size > 0:
        game_window.pop_handlers()
        event_stack_size -= 1       

    #Player live sprite
    player_live = gui.player_lives(number_of_lives, main_batch)

    #Load objects
    player_ship = player.Player(x=640, y=350, batch=main_batch)
    asteroids = load.asteroids(number_of_asteroids,player_ship.position, main_batch)

    #List of game objects
    game_objects = [player_ship] + asteroids

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

    for remove_object in [obj for obj in game_objects if obj.dead]:

        #Remove object from batch
        remove_object.delete()
        #Remove object from game objects list
        game_objects.remove(remove_object)               

        #Score is added when asteroid obj gets destroyed
        if isinstance (remove_object, asteroid.Asteroid):
            #Check if deleted object is asteroid class
            score += 1
            score_label.text = f"Score is: {score}"

        if remove_object == player_ship:
            player_dead = True

    game_objects.extend(to_add)

    if player_dead:
        number_of_lives -= 1
        if number_of_lives > 0:
            reset_level(number_of_lives)
        else:
            pass

if __name__ == '__main__':

    init()

    #Call update function
    pyglet.clock.schedule_interval(update, 1/120.0)

    #Run the window
    pyglet.app.run()