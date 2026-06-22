from core.world import GW
from core.tile import STONE

world = GW(5, 3)
world.set_tile(2, 1, STONE)
print(world.render_text())
print(world.get_tile(2, 1))

print(world.is_inside(2, 1))
print(world.is_inside(5, 1))
print(world.is_inside(4, 2))