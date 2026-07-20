import random

from core.ambient.world import World
from core.ambient.sky import Sky
from core.ambient.tile import WATER, FOOD
from core.being.organism import Organism
from core.simulation.renderer import Renderer
from core.simulation.gtime import Gtime
from core.simulation.simulation import Simulation

def build_scenario(config): #monta um cenario completo a partir da scenarioconfig
    random.seed(config.seed)

    world = World(config.world_width, config.world_height)

    water_x = config.world_width - 5
    food_x = config.world_width -2
    mid_y = config.world_height // 2
    world.set_tile(water_x, mid_y, WATER)
    world.set_tile(food_x, mid_y, FOOD)

    for i in range(config.num_organism):
        x = random.radint(0, config.world_width -1)
        y = random.randint(0, config.world_height -1)
        organism = Organism(f"gaiano_{i}", "@", x, y)
        world.add_entity(organism)

    sky = Sky()
    renderer = Renderer()
    gtime = Gtime(mtksptk=config.mtksptk)

    simulation = Simulation(
        world=World
        sky=Sky
        renderer=renderer
        gtime=gtime
        simulation_duration=config.simulation_duration,
        frame_delay=config.frame_delay,
        )

    return Simulation
