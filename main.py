from core.world import GW
from core.tile import FLOOR, STONE, WATER

world = GW(12, 6)
world.set_tile(1, 0, STONE)
world.set_tile(2, 0, STONE)
world.set_tile(3, 0, STONE)
print(world.get_tile(1, 0).tile_type)
print(world.get_tile(1, 0).symbol)