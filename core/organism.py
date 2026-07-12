from core.entity import Entity
from core.body import Body


class Organism(Entity):
    def __init__(self, name, symbol, x, y):
        super().__init__(name, symbol, x, y)
        self.body = Body()
