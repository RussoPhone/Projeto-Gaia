import os
import time
from core.organism import Organism
from core.tile import WATER, FOOD, GRASS

class Simulation: #È aqui que fica os parametros da simulação.
    def __init__(self, world, sky, renderer, gtime, simulation_duration=120, frame_delay=0.05):
        self.world = world
        self.sky = sky
        self.renderer = renderer
        self.gtime = gtime
        self.simulation_duration = simulation_duration
        self.frame_delay = frame_delay

    def clear_screen(self): #Limpa a tela
        os.system("cls" if os.name == "nt" else "clear")

    #metodo pra atualizar entidades na simulação
    def update_entities(self):
        directions = [
            (1, 0), #direita
            (-1, 0), #esquerda
            (0, 1), #baixo
            (0, -1), #cima
            ]
        for entity in self.world.entities:

            if isinstance(entity, Organism):
                entity.update(self.world)

                if entity.needs_action():
                    moved = False

                    for dx, dy in directions:
                        moved = self.world.move_entity(entity, dx, dy)

                        if moved:
                            entity.record_action(f"moved ({dx}, {dy})")
                            break

                    if not moved:
                        entity.record_action("tried to move")

                self.apply_environment_effects(entity)

    def apply_environment_effects(self, entity): #Aplica efeitos no ambiente
        current_tile = self. world.get_tile(entity.x, entity.y)

        if current_tile == WATER:
            entity.drink()

        if current_tile == FOOD:
            entity.eat()
            self.world.set_tile(entity.x, entity.y, GRASS)
    def process_entity(self, entity):
        if not isinstance(entity, Organism):
            return

        entity.update(self.world)

        perception = self.perceive(entity)

        if entity.needs_action():
            action = self.decide_action(entity, perception)

            applied = self.act(entity, action)

            entity.record_action(applied)
        self.apply_environment_effects(entity)

    def perceive(self, entity):

        return None

    def decide_action(self, entity, perception):
        return [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            ]

    def act(self, entity, directions):
        for dx, dy in directions:
            if self.world.move_entity(entity, dx, dy):
                return f"moved ({dx}, {dy})"
        return "tried to move"


    def step(self):
        for entity in self.world.entities:
            self.process_entity(entity)

        self.gtime.adv()

    def run(self):
        while self.gtime.mtk < self.simulation_duration:
            self.clear_screen()
            self.step()
            self.render()
            time.sleep(self.frame_delay)


    def render(self):
        print(self.gtime.debug_text())
        print()
        #calcula a luz atual a partir do tempo
        light = self.sky.get_light(self.gtime)
        #mostra o valor da luz
        print(f"Light: {light}")
        print()
        for entity in self.world.entities:
            print(entity.debug_text())
            if entity.needs_action():
                print(f"{entity.name} needs action")
            print()
        #desenha o mundo + luz atual
        print(self.renderer.render_lit(self.world, light))
