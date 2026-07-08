import os
import time

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

    def run(self):
        while self.gtime.mtk < self.simulation_duration:
            self.clear_screen()
            #atualiza o estados de uma entidade
            for entity in self.world.entities:
                entity.update_needs()

                if entity.needs_action():
                    print(f"{entity.name} needs action")
            #mostra estado atual do mundo
            self.render()

            #avança em 1 mtk
            self.gtime.adv()
            #espera um teco pra prox animação
            time.sleep(self.frame_delay)
    #mostra as informações do tempo atual
    def render(self):
        print(self.gtime.debug_text)
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
