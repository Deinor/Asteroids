import pyglet
from . import physycalobjects, resources

class Laser(physycalobjects.PhysycalObjects):
    """
    Laser object. Fired by player
    """

    def __init__(self, *args, **kwargs):
        super().__init__(resources.laser_image, *args, **kwargs)

        self.is_laser = True
        self.react_to_laser = False

        #Timer to delete bullet
        pyglet.clock.schedule_once(self.die, 0.5)

    def die(self, dt):
        self.dead = True