import random

from entities.drawable_entity import DrawableEntity
from utils import rect_in_world, rects_are_overlapping


class Crumb(DrawableEntity):
    SIZE = 10
    COLOR = 'yellow'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, canvas):
        top_left, bottom_right = self.get_bounds()
        canvas.create_oval(top_left.x,
                           top_left.y,
                           bottom_right.x,
                           bottom_right.y,
                           fill=self.COLOR)

    def has_room(self, world):
        """Checks whether self has room in world."""
        bounds = self.get_bounds()

        if not rect_in_world(bounds, world):
            return False

        for other in world.entities:
            # Rocks can be one on top of another, it doesn't matter.
            if isinstance(other, Crumb):
                continue

            if rects_are_overlapping(bounds, other.get_bounds()):
                return False

        return True

    @staticmethod
    def generate_many(num, world):

        crumbs = []
        while len(crumbs) < num:
            x = random.randint(0, world.width)
            y = random.randint(0, world.height)

            crumb = Crumb(x, y)
            if crumb.has_room(world):
                crumbs.append(crumb)

        return crumbs
