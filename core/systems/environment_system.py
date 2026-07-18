from core.being.body import Body
from core.ambient.tile import FOOD, GRASS, WATER

class EnvironmentSystem:
    def __init__(self):
        pass

    #Classe pra sistema de efeitos no ambiente
    def apply(self, simulation, entity):
        self.body = Body()
        current_tile = simulation.world.get_tile(
            entity.x,
            entity.y
        )

        if current_tile == WATER:
            self.body.drink()

        if current_tile == FOOD:
            self.body.eat()
            simulation.world.set_tile(entity.x, entity.y, GRASS)
