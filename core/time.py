mtk = 0 
"""microticks"""
mtksptk = 24
"""microticks por tick, tk são ticks"""
tkrun = 3 
"""quantos ticks devem rodar"""
sim_duration = mtksptk * tkrun 
"""duração da simulação"""

while mtk < sim_duration:
    tick = mtk // mtksptk
    pos = mtk % mtksptk
    progress = pos / mtksptk
    progress_percent = f"{progress:.0%}"

    print(
        "Microtick", mtk,
        "Tick:", tick,
        "Position:", pos,
        "Progress:", progress_percent
    )
    mtk = mtk + 1