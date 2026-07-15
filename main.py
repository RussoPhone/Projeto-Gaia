#from core.world import World
#from core.entity import Entity
#from core.organism import Organism
#from core.body import Body
#from core.sky import Sky
#from core.renderer import Renderer
#from core.gtime import Gtime
#from core.simulation import Simulation
#from core.tile import WATER, FOOD

#world = World(20, 10)
#world.set_tile(15, 5, WATER)
#world.set_tile(18, 5, FOOD)
#organism = Organism("maria", "@", 10, 5)
#world.add_entity(organism)
#sky = Sky()

#renderer = Renderer()

#gtime = Gtime(mtksptk=24)

#simulation = Simulation(
#    world=world,
#    sky=sky,
#    renderer=renderer,
#    gtime=gtime,
#    simulation_duration=120,
#    frame_delay=0.08
#)
#simulation.run()

from core.spatial import Spatial
from core.sensor import Sensor

orientation = (0, -1)
sensor = Sensor(range_=5)

na_frente = Spatial(5, 5, 5, 2)
atras = Spatial(5, 5, 5, 8)
de_lado = Spatial(5, 5, 8, 5)
fora_do_alcance = Spatial(5, 5, 5, -2)

print(sensor.can_perceive(na_frente, orientation))
print(sensor.can_perceive(atras, orientation))
print(sensor.can_perceive(de_lado, orientation))
print(sensor.can_perceive(fora_do_alcance, orientation))
print(sensor.can_perceive(na_frente, orientation, light=0.1))
