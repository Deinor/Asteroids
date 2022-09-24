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

def game_over_label(batch=None):
    game_over_label = pyglet.text.Label("YOU DIED, GAME OVER", 
                                        font_name='Times New Roman', 
                                        font_size=36, x=640, y=360, 
                                        anchor_x='center', 
                                        anchor_y='center', 
                                        batch=batch)
    return game_over_label

def restart_game_label(batch=None):
    restart_game_label = pyglet.text.Label("Press Enter to restart level, or ESC to end game", 
                                        font_name='Times New Roman', 
                                        font_size=24, x=640, y=300, 
                                        anchor_x='center', 
                                        anchor_y='center', 
                                        batch=batch)
    return restart_game_label