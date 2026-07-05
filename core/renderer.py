class Renderer: #aqui é onde se configura os paraetros da renderização.
    def render_lit(self, world, light): #função de renderizção de iluminação nas tiles
        lines = []

        for row in world.tiles:
            symbols = []

            for tile in row:
                if light < 0.25: #aqui é a função de renderização da luz.
                    symbols.append(" ")
                elif light <0.50:
                    symbols.append(".")
                else:
                    symbols.append(tile.symbol)

            line = " ".join(symbols)
            lines.append(line) #junta tudo

        return "\n".join(lines)
