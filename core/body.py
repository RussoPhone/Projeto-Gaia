class Body:
    def __init__(self):
        self.hunger = 0
        self.thirst = 0
        self.alive = True

    def update_needs(self):
        if not self.alive:
            return

        self.hunger += 1
        self.thirst += 2

        if self.hunger >= 100 or self.thirst >= 100:
            self.alive = False

    def drink(self): #função de consumir liquido.
        if not self.alive:
            return
        self.thirst -= 30

        if self.thirst < 0:
            self.thirst = 0

    def eat(self):
        if not self.alive:
            return
        self.hunger -=30

        if self.hunger < 0:
            self.hunger = 0
