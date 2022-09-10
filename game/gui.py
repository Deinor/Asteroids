#Modul to settup game gui
import pyglet
from . import resources

def player_lives(number_of_lives, batch=None):
    """
    Defines the gui generating live icons.
    """
    sprite_player_lives = []

    for i in range(number_of_lives):
        new_sprite_player_lives = pyglet.sprite.Sprite(img=resources.player_image, x=1200 - i * 50, y=680, batch=batch)
        new_sprite_player_lives.scale = 0.4
        sprite_player_lives.append(new_sprite_player_lives)
    return sprite_player_lives