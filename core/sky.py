import math

class Sky:
    def __init__(self, cycle_length=24):
        self.cycle_length = cycle_length

    def get_phase(self, gtime):
        return (gtime.mtk % self.cycle_length) / self.cycle_length

    def get_light(self, gtime):
        phase = self.get_phase(gtime)

        light = (1 - math.cos(phase * 2 * math.pi)) / 2

        return light

    def get_darkness(self, gtime):
        return 1 - self.get_light(gtime)

    def get_state(self, gtime):
        phase = self.get_phase(gtime)

        if phase < 0.25:
            return "DAWN"
        elif phase < 0.50:
            return "DAY"
        elif phase < 0.75:
            return "DUSK"
        else:
            return "NIGHT"


    def debug_text(self, gtime):
        light = self.get_light(gtime)
        darkness = self.get_darkness(gtime)
        state = self.get_state(gtime)

        return f"SKY: {state}, LIGHT: {light:.0%}, DARKNESS: {darkness:.0%}"
