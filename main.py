import os
import time as pytime
from core.gtime import Gtime
from core.world import World
from core.sky import Sky
from core.renderer import Renderer

simulation_duration = 120
frame_delay = 0.5

time=Gtime(24)
sky=Sky(cycle_length=24)
mundo=World(20, 10)
renderer = Renderer()

for i in range(48):
    os.system("clear")

    light = sky.get_light(time)

    print(time.debug_text())
    print(sky.debug_text(time))
    print()
    print(renderer.render_lit(mundo, light))

    pytime.sleep(frame_delay)
    time.adv()

