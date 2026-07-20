from dataclasses import dataclasses

@dataclass
class ScenarioConfig: #Config central de um cenario de simulação
    seed: int = 42
    world_width: int = 20
    world_height: int = 10
    num_organism: int = 10
    mtksptk: int = 24
    simulation_duration: int = 120
    frame_delay: float = 0.08
