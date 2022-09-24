import pyglet
from pyglet.window import key

class Overlay():
    def update(self, dt):
        pass

    def draw(self):
        pass

class Banner(Overlay):
    """
    Creates Banner over existing screen with intendet massage - Lable.
    """
    def __init__(self, label):
        self.text = pyglet.text.Label(label,
                                      font_name='Arial',
                                      font_size=36,
                                      x=50, 
                                      y=50,
                                      anchor_x='center',
                                      anchor_y='center')

    def draw(self):
        self.text.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == self.key.SPACE:
            print('Space')

class Menu(Overlay):
    """
    Base class of menu. Creates title and un and down navigation (key events) in menu.
    """
    def __init__(self, title, batch=None):
        self.items = []
        self.selected_index = 0
        self.title_text = pyglet.text.Label(title, 
                                            font_name='Arial',
                                            font_size=36,
                                            x=640, 
                                            y=550,
                                            anchor_x='center',
                                            anchor_y='center',
                                            batch=batch)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.DOWN:
            self.selected_index += 1
        elif symbol == key.UP:
            self.selected_index -= 1
        #Sets the min index to 0 and max index to len of items in menu
        self.selected_index = min(max(self.selected_index, 0), len(self.items) - 1)
        print(self.selected_index)

    def reset_selected_index(self):
        # Reset selected index to 0 - first place in menu
        self.selected_index = 0

    def on_key_release(self, symbol, modifiers):
        self.items[self.selected_index].on_key_release(symbol, modifiers)
        print('Enter1')

class MenuItem():
    """
    Creates items in menu with selection of item
    """
    def __init__(self, y, lable, execute_function, batch=None):
        self.y = y
        self.execute_function = execute_function
        self.text = pyglet.text.Label(lable, 
                                        font_name='Arial',
                                        font_size=26,
                                        x=640, 
                                        y=y,
                                        anchor_x='center',
                                        anchor_y='center',
                                        batch=batch)
    def on_key_release(self, symbol, modifier):
        if symbol == key.ENTER:
            self.execute_function()
            print('Enter2')

class MainMenu(Menu):
    """
    Creates the main menu.
    """
    def __init__(self, start_game_function, options_function, exit_function, batch=None):
        super().__init__('Asteroids', batch)

        self.items.append(MenuItem(350, 'Start game', start_game_function, batch=batch))
        self.items.append(MenuItem(300, 'Options', options_function, batch=batch))
        self.items.append(MenuItem(250, 'Exit', exit_function, batch=batch))
        #Reset selected index while menu is created
        self.reset_selected_index()
    
    def remove(self):
        for item in self.items:
            item.remove()