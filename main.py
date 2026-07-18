from core.ambient.world import World
from core.being.entity import Entity
from core.being.organism import Organism
from core.being.body import Body
from core.ambient.sky import Sky
from core.simulation.renderer import Renderer
from core.simulation.gtime import Gtime
from core.simulation.simulation import Simulation
from core.ambient.tile import WATER, FOOD

world = World(20, 10)
world.set_tile(15, 5, WATER)
world.set_tile(18, 5, FOOD)
organism = Organism("maria", "@", 10, 5)
world.add_entity(organism)
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


