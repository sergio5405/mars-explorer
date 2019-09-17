from entities.crumb import Crumb
from entities.drawable_entity import DrawableEntity
from entities.explorer import Explorer
from entities.mars_base import MarsBase
from entities.obstacle import Obstacle
from entities.rock import Rock


class World(DrawableEntity):
    COLOR = '#804C1A'

    def __init__(self, width, height, num_rocks):
        self.width = width
        self.height = height

        self.entities = []
        self.rocks = []
        self.obstacles = []
        self.explorers = []
        self.crumbs = []
        self.mars_base = None
        self.num_rocks = num_rocks
        self.rocks_collected = 0

    def draw(self, canvas):
        canvas.configure(background=self.COLOR)

    def tick(self):
        for explorer in self.explorers:
            explorer.tick()

    def add_entity(self, entity):
        assert isinstance(entity, DrawableEntity)

        self.entities.append(entity)

        if isinstance(entity, Rock):
            self.rocks.append(entity)
        elif isinstance(entity, Obstacle):
            self.obstacles.append(entity)
        # Order matters here because Carrier < Explorer.
        elif isinstance(entity, Crumb):
            self.crumbs.append(entity)
        elif isinstance(entity, Explorer):
            self.explorers.append(entity)
        elif isinstance(entity, MarsBase):
            self.mars_base = entity

    def remove_entity(self, entity):
        assert isinstance(entity, DrawableEntity)

        self.entities.remove(entity)

        if isinstance(entity, Rock):
            self.rocks.remove(entity)
        elif isinstance(entity, Obstacle):
            self.obstacles.remove(entity)
        # Order matters here because Carrier < Explorer.
        elif isinstance(entity, Crumb):
            self.crumbs.remove(entity)
        elif isinstance(entity, Explorer):
            self.explorers.remove(entity)
        elif isinstance(entity, MarsBase):
            self.mars_base = None

    def is_done(self):
        return self.rocks_collected == self.num_rocks

    def rock_collected(self):
        self.rocks_collected += 1
