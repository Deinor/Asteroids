import random
from . import physycalobjects, resources

"""
Objects asteroid
"""

class AsteroidBig (physycalobjects.PhysycalObjects):
    """
    Defines asteroids spawned after colision.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(resources.asteroid_image_b1, *args, **kwargs)
        self.rotation_speed = random.random() * 80 - 50

    def update(self, dt):
        super(AsteroidBig, self).update(dt)
        self.rotation += self.rotation_speed * dt

    def collision_action(self, other_object):
        """
        Creates new asteroids 'childs' when asteroid gets destroyed.
        """

        super(AsteroidBig, self).collision_action(other_object)

        if self.dead and self.scale > 0.25:
            number_of_asteroids = random.randint(2, 3)
            for i in range(number_of_asteroids):
                new_asteroid = AsteroidBig(x=self.x, y=self.y, batch=self.batch)
                new_asteroid.rotation = random.randint(0, 360)
                new_asteroid.speed_x = (random.random() * 50 + self.speed_x)
                new_asteroid.speed_y = (random.random() * 50 + self.speed_y)
                new_asteroid.scale = self.scale * 0.5
                self.new_objects.append(new_asteroid)

class AsteroidMedium (physycalobjects.PhysycalObjects):
    """
    Defines asteroids spawned after colision.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(resources.asteroid_image_m1, *args, **kwargs)
        self.rotation_speed = random.random() * 80 - 50

    def update(self, dt):
        super(AsteroidMedium, self).update(dt)
        self.rotation += self.rotation_speed * dt

    def collision_action(self, other_object):
        """
        Creates new asteroids 'childs' when asteroid gets destroyed.
        """

        super(AsteroidMedium, self).collision_action(other_object)

        if self.dead and self.scale > 0.5:
            number_of_asteroids = random.randint(1, 1)
            for i in range(number_of_asteroids):
                new_asteroid = AsteroidMedium(x=self.x, y=self.y, batch=self.batch)
                new_asteroid.rotation = random.randint(0, 360)
                new_asteroid.speed_x = (random.random() * 50 + self.speed_x)
                new_asteroid.speed_y = (random.random() * 50 + self.speed_y)
                new_asteroid.scale = self.scale * 0.5
                self.new_objects.append(new_asteroid)