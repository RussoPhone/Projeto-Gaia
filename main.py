from core.world import World
from core.entity import Entity
from core.sky import Sky
from core.renderer import Renderer
from core.gtime import Gtime
from core.simulation import Simulation

world = World(20, 10)

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
    frame_delay=0.05
)
simulation.run()

