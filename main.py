import argparse

from entities.explorer import Explorer
from gui import GUI
from entities.mars_base import MarsBase
from entities.obstacle import Obstacle
from entities.rock import Rock
from entities.world import World


def init_entities(num_obstacles, num_rocks, num_explorers):
    world = World(800, 600, num_rocks)

    mars_base = MarsBase(world.width, world.height)
    world.add_entity(mars_base)

    for _ in range(num_explorers):
        explorer = Explorer(mars_base.x + mars_base.SIZE,
                            mars_base.y + mars_base.SIZE,
                            world)
        world.add_entity(explorer)

    obstacles = Obstacle.generate_many(num_obstacles, world)
    for obstacle in obstacles:
        world.add_entity(obstacle)

    rocks = Rock.generate_many(num_rocks, world)
    for rock in rocks:
        world.add_entity(rock)

    return world


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--obstacles', default=10, dest='obstacles', type=int)
    parser.add_argument('--rocks', default=100, dest='rocks', type=int)
    parser.add_argument('--explorers', default=10, dest='explorers', type=int)

    args = parser.parse_args()

    world = init_entities(args.obstacles,
                          args.rocks,
                          args.explorers)

    gui = GUI(world)
    gui.start()


if __name__ == '__main__':
    main()
