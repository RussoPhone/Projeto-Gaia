from core.world import world
from core.tile import GRASS, STONE, WATER

world = world(20, 10, GRASS)

world.fill(GRASS)
world.fill_rect(13, 1, 6, 4, STONE)
world.border_tile(STONE)

print(world.render_debug())
