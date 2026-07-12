from core.entity import Entity
from core.body import Body


class Organism(Entity):
    def __init__(self, name, symbol, x, y):
        super().__init__(name, symbol, x, y)
        self.body = Body()

    def update(self, world):
        if not self.body.alive:
            self.record_action("dead")
            return

        self.body.update_needs()

        if not self.body.alive:
            return

        current_tile = world.get_tile(self.x, self.y)

        if self.body.thirst >= 50:
            if current_tile.tile_type == "water":
                self.body.drink()
            else:
                self.record_action("needs water")
            return

        if self.body.hunger >= 50:
            if current_tile.tile_type == "food":
                self.body.eat()
            else:
                self.record_action("needs food")
            return

        self.record_action("idle")

    def record_action(self, action):
        self.last_action = action

    def debug_text(self):
        state = "vivo" if self.body.alive else "morto"
        return f" name={self.name} | pos=({self.x}, {self.y}) | hunger={self.body.hunger} | thirst ={self.body.thirst} | {state} "
