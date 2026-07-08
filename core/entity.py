class Entity:
    def __init__(self, name, symbol, x, y):
        self.name = name
        self.symbol = symbol
        self.x = x
        self.y = y
        self.hunger = 0
        self.thirst = 0
        self.alive = True
    #metodo de atualização de necessidades de uma entidade
    def update_needs(self):
        if not self.alive:
            return
        self.hunger += 1
        self.thirst += 2

        if self.hunger >= 100 or self.thirst >= 100:
            self.alive = False

    def needs_action(self):
        if not self.alive:
            return False

        return self.hunger >= 50 or self.thirst >= 50

    def debug_text(self):
        state = "vivo" if self.alive else "morto"
        return f"{self.name} | pos=({self.x}, {self.y}) | hunger={self.hunger} | thirst ={self.thirst} | {state}"
