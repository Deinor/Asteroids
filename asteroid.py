import pyglet
from game import resources, load, gui, physycalobjects, player

#Game constants
version = str(0.01)
score = str(0)
number_of_asteroids = 10
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
game_objects = asteroids + [player_ship]

#Player object responds to key handlers
game_window.push_handlers(player_ship.key_handler)

#Seting up event handler on_draw
@game_window.event
def on_draw():
    #Clear the screen
    game_window.clear()
    
    #Draw objects
    main_batch.draw()

def update(dt):
    #Function updating game objects
    for obj in game_objects:
       obj.update(dt)


if __name__ == '__main__':

    #Call update function
    pyglet.clock.schedule_interval(update, 1/120.0)

    #Run the window
    pyglet.app.run()