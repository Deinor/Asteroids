import pyglet
from . import util
#Modul handeling basic physics for object classes

class PhysycalObjects(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.speed_x, self.speed_y = 0.0, 0.0

        self.dead = False

    def update(self, dt):
        """
        Update position based on speed and time.
        """
        self.x += self.speed_x * dt
        self.y += self.speed_y * dt

        self.check_borders()

    def check_borders(self):
        """
        Defines where are the limits for borders and behaviour of obj on borders.
        """

        #Borders x and y position
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = 1280 + self.image.width / 2
        max_y = 720 + self.image.height / 2

        # Behaviour of object on borders - move object to oposite border
        if self.x < min_x:
            self.x = max_x
        if self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        if self.y > max_y:
            self.y = min_y

    def check_collision(self, other_object):
        """
        Check for collision of two objects.
        """
        #Find out colision distance
        collision_distance = self.image.width / 2 + other_object.image.width / 2
        #Load actual distance of two objects
        actual_distance = util.distance(self.position, other_object.position)
        return (actual_distance <= collision_distance)

    def collision_action(self, other_object):
        """
        After collision set up dead.
        """
        self.dead = True