from core.world import World
from core.entity import Entity
from core.sky import Sky
from core.renderer import Renderer
from core.gtime import Gtime
from core.simulation import Simulation
from core.tile import WATER, FOOD

world = World(20, 10)
world.set_tile(15, 5, WATER)
world.set_tile(18, 5, FOOD)
entity = Entity("maria", "@", 10, 5)
world.add_entity(entity)
sky = Sky()

renderer = Renderer()

gtime = Gtime(mtksptk=24)

simulation = Simulation(
    world=world,
    sky=sky,
    renderer=renderer,
    gtime=gtime,
    simulation_duration=120,
    frame_delay=0.08
)
simulation.run()

