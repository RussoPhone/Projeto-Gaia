from core.world import world
from core.tile import GRASS, STONE, WATER

world = world(20, 10, GRASS)

world.fill_rect(4, 0, 3, 9, WATER)
world.fill_rect(11, 1, 2, 7, STONE)

print(world.render_debug())
