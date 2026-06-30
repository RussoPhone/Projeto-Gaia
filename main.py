from core.world import world
from core.tile import FLOOR, STONE, WATER

world = world(10, 5)

print("Mundo inicial:")
print(world.render_text())

world.set_tile(2, 1, STONE)
world.set_tile(3, 1, STONE)
world.set_tile(4, 1, STONE)
#world.set_tile(99, 99, STONE)

print()
print("Mundo com pedras:")
print(world.render_text())

tile = world.get_tile(2, 1)

print()
print("Tile em x=2, y=1:")
print(tile.tile_type, tile.symbol)
