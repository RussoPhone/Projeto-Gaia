import os
import time

class Simulation:
    def __init__(self, world, sky, renderer, gtime, simulation_duration=120, frame_delay=0.05):
        self.world = world
        self.sky = sky
        self.renderer = renderer
        self.gtime = gtime
        self.simulation_duration = simulation_duration
        self.frame_delay = frame_delay

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def run(self):
        while self.gtime.mtk < self.simulation_duration:
            self.clear_screen()

            self.render()

            self.gtime.adv()
            time.sleep(self.frame_delay)

    def render(self):
        print(self.gtime.debug_text)
        print()

        light = self.sky.get_light(self.gtime)

        print(f"Light: {light}")
        print()

        print(self.renderer.render_lit(self.world, light))
