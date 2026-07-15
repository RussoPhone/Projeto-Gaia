from core.entity import Entity
from core.body import Body


class Organism(Entity):
    def __init__(self, name, symbol, x, y):
        super().__init__(name, symbol, x, y)

        self.body = Body() #Necessidades, vida e morte
        self.sensors = [] #capacidade de percepção, incremento futuro
        self.memory = None #padrões aprendido, inc futuro
        self.decision_system = None #escolha de ação, incf
        self.orientation = (0, -1) #vetor de direção onde um organismo esta olhando

    def update(self, world):
        if not self.body.alive:
            self.record_action("dead")
            return

        self.body.update_needs()

        if not self.body.alive:
            self.record_action("morto")
            return

        current_tile = world.get_tile(self.x, self.y)

    def needs_action(self):
        return self.body.needs_action()


    def debug_text(self):
        state = "vivo" if self.body.alive else "morto"
        return f" name={self.name} | pos=({self.x}, {self.y}) | hunger={self.body.hunger} | thirst ={self.body.thirst} | {state} "
