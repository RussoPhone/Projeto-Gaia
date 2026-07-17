

class Entity:
    def __init__(self, name, symbol, x, y):
        self.name = name
        self.symbol = symbol
        self.x = x
        self.y = y
        self.hunger = 0
        self.thirst = 0
        self.alive = True
        self.last_action = "born"


    def update_needs(self):
        if not self.alive:
            return
        self.hunger += 1
        self.thirst += 2
        self.last_action = "needs increased"

        if self.hunger >= 100 or self.thirst >= 100:
            self.alive = False
            self.last_action = "morto"

    #metodo de atualização de necessidades de uma entidade
    def update(self, world):
        if not self.alive:
            self.record_action("dead")
            return

        self.update_needs()

        if not self.alive:
            return

        current_tile = world.get_tile(self.x, self.y)

        if self.thirst >= 50:
            if current_tile.tile_type == "water":
                self.drink()
            else:
                self.record_action("needs water")
            return

        if self.hunger >= 50:
            if current_tile.tile_type == "food":
                self.eat()
            else:
                self.record_action("needs food")
            return

        self.record_action("idle")

    def needs_action(self): #função que desperta ação
        if not self.alive:
            return False

        return self.hunger >= 50 or self.thirst >= 50

    def record_action(self, action):
        self.last_action = action

    def drink(self): #função de consumir liquido.
        if not self.alive:
            return
        self.thirst -= 30
        self.last_action = "drank"

        if self.thirst < 0:
            self.thirst = 0

    def eat(self):
        if not self.alive:
            return
        self.hunger -=30
        self.last_action = "ate"

        if self.hunger < 0:
            self.hunger = 0

    def debug_text(self):
        state = "vivo" if self.alive else "morto"
        return f"action ={self.last_action}| name={self.name} | pos=({self.x}, {self.y}) | hunger={self.hunger} | thirst ={self.thirst} | {state} "
