import pyglet

import pyglet
from pyglet.window import key
from . import resources
    
class Overlay():
    def update(self, dt):
        pass

    def draw(self):
        pass

class Banner(Overlay):
    """
    Creates Banner over existing screen with intendet massage - Lable.
    """
    def __init__(self, label, batch=None):
        self.text = pyglet.text.Label(label,
                                      font_name='Baskerville_Old_Face',
                                      font_size=36,
                                      x=640, 
                                      y=370,
                                      anchor_x='center',
                                      anchor_y='center',
                                      batch=batch)

        #Game starts to recognise key handlers
        self.key_handler = key.KeyStateHandler()
        self.event_handlers_menu = [self, self.key_handler]

    def draw(self):
        self.text.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == self.key.SPACE:
            print('Space')


class Menu(Overlay):
    """
    Base class of menu. Creates title and un and down navigation (key events) in menu.
    """
    def __init__(self):
        #Create list of items in menu (labels)
        self.items = []
        #Create a list of functions coresponding to list of labels 
        self.active_functions = []
        self.selected_index = 0
        #Game starts to recognise key handlers
        self.key_handler = key.KeyStateHandler()
        self.event_handlers_menu = [self, self.key_handler]

        #Set up y position of labels and pointer
        self.y_positions = [(400 - self.y * 80) for self.y in range(3)]

        #Set up initioal position of pointer
        self.y_pointer = self.y_positions[0 + self.selected_index]

    def on_key_press(self, symbol, modifiers):
        if symbol == key.DOWN:
            self.selected_index += 1        

        elif symbol == key.UP:
            self.selected_index -= 1

        #Sets the min index to 0 and max index to len of items in menu
        self.selected_index = min(max(self.selected_index, 0), len(self.items) - 1)

        #Updates pointer position
        #TODO error list out of range
        self.y_pointer = self.y_positions[self.selected_index]
    
    def reset_selected_index(self):
        # Reset selected index to 0 - first place in menu
        self.selected_index = 0

class MainMenu(Menu, pyglet.text.Label):
    """
    Creates the intractive main menu.
    """
    #TODO Change coulour of labels to gl with some gradient etc.

    def __init__(self, start_game_function, options_function, exit_function, batch=None):
        super(MainMenu, self).__init__()

        #Set up main menu labels and pointer
        self.label_start_game = pyglet.text.Label('Start Game', 
                                        font_name='Baskerville_Old_Face',
                                        font_size=28,
                                        bold=True,
                                        color=(0, 245, 255, 180),
                                        x=640, 
                                        y = self.y_positions[0],
                                        anchor_x='center',
                                        anchor_y='center',
                                        batch=batch)
        self.label_options = pyglet.text.Label('Options', 
                                        font_name='Baskerville_Old_Face',
                                        font_size=28,
                                        bold=True,
                                        color=(0, 245, 255, 180),
                                        x=640,
                                        y = self.y_positions[1],
                                        anchor_x='center',
                                        anchor_y='center',
                                        batch=batch)
        self.label_exit = pyglet.text.Label('Exit', 
                                        font_name='Baskerville_Old_Face',
                                        font_size=28,
                                        bold=True,
                                        color=(0, 245, 255, 180),
                                        x=640, 
                                        y = self.y_positions[2],
                                        anchor_x='center',
                                        anchor_y='center',
                                        batch=batch)
        self.pointer = MenuPointer(x=490, y=self.y_pointer, batch=batch)

        #Create list of main menu labels
        self.items.append(self.label_start_game)
        self.items.append(self.label_options)
        self.items.append(self.label_exit)
        self.items.append(self.pointer)

        #Create function list of main menu functions executed by presing enter on label
        self.active_functions.append(start_game_function)
        self.active_functions.append(options_function)
        self.active_functions.append(exit_function)


    def on_key_release(self, symbol, modifiers):
        #Activate function from function list
        if symbol == key.ENTER:
            self.active_function = self.active_functions[self.selected_index]
            self.active_function()

    def on_key_press(self, symbol, modifiers):
        super ().on_key_press(symbol, modifiers)
        self.pointer.update(y=self.y_pointer)

    def remove(self):
        """
        Remove labels from batch.
        """
        for item in self.items:
            item.delete()
        self.items.clear()
        self.active_functions.clear()

class NextLevel(Menu, pyglet.text.Label):
    """
    Creates the intractive main menu.
    """
    #TODO Change coulour of labels to gl with some gradient etc.

    def __init__(self, start_game_function, exit_function, batch=None):
        super(NextLevel, self).__init__()

        #Set up main menu labels and pointer
        self.label_start_game = pyglet.text.Label('Start Game', 
                                        font_name='Baskerville_Old_Face',
                                        font_size=28,
                                        bold=True,
                                        color=(0, 245, 255, 180),
                                        x=640, 
                                        y = self.y_positions[0],
                                        anchor_x='center',
                                        anchor_y='center',
                                        batch=batch)
        self.label_exit = pyglet.text.Label('Exit', 
                                        font_name='Baskerville_Old_Face',
                                        font_size=28,
                                        bold=True,
                                        color=(0, 245, 255, 180),
                                        x=640, 
                                        y = self.y_positions[1],
                                        anchor_x='center',
                                        anchor_y='center',
                                        batch=batch)
        self.pointer = MenuPointer(x=490, y=self.y_pointer, batch=batch)

        #Create list of main menu labels
        self.items.append(self.label_start_game)
        self.items.append(self.label_exit)
        self.items.append(self.pointer)

        #Create function list of main menu functions executed by presing enter on label
        self.active_functions.append(start_game_function)
        self.active_functions.append(exit_function)


    def on_key_release(self, symbol, modifiers):
        #Activate function from function list
        if symbol == key.ENTER:
            self.active_function = self.active_functions[self.selected_index]
            self.active_function()

    def on_key_press(self, symbol, modifiers):
        super ().on_key_press(symbol, modifiers)
        self.pointer.update(y=self.y_pointer)

    def remove(self):
        """
        Remove labels from batch.
        """
        for item in self.items:
            item.delete()
        self.items.clear()
        self.active_functions.clear()

class MenuPointer (pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.player_image, *args, **kwargs)
        self.scale = 0.7
        self.rotation = 90