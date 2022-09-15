import pyglet
from game import load, gui, player

#Game constants
version = str(0.01)
score = str(0)
number_of_asteroids = 5
number_of_lives = 3

#Create main batch
main_batch = pyglet.graphics.Batch()

#Set up game window(width, height)
game_window = pyglet.window.Window(1280, 720)

#Set up top lables
version_label = pyglet.text.Label(text=version, x=10, y=700, batch=main_batch)
score_label = pyglet.text.Label(text="Score is: " + score, x=200, y=700, batch=main_batch)

#Load player live icons

player_live = gui.player_lives(number_of_lives, main_batch)

#Load objects
player_ship = player.Player(x=640, y=350, batch=main_batch)
asteroids = load.asteroids(number_of_asteroids,player_ship.position, main_batch)

#List of game objects
game_objects = [player_ship] + asteroids

#Player object responds to key handlers
game_window.push_handlers(player_ship.key_handler)

#Add event handler to the stack
for obj in game_objects:
    for handler in obj.event_handlers:
        game_window.push_handlers(handler)

#Seting up event handler on_draw
@game_window.event
def on_draw():
    #Clear the screen
    game_window.clear()
    
    #Draw objects
    main_batch.draw()

def update(dt):
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

    game_objects.extend(to_add)

if __name__ == '__main__':

    #Call update function
    pyglet.clock.schedule_interval(update, 1/120.0)

    #Run the window
    pyglet.app.run()