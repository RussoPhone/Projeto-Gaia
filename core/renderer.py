class Renderer:
    def render_lit(self, world, light):
        lines = []

        for row in world.tiles:
            symbols = []

            for tile in row:
                if light < 0.25:
                    symbols.append(" ")
                elif light <0.50:
                    symbols.append(".")
                else:
                    symbols.append(tile.symbol)

            line = " ".join(symbols)
            lines.append(line)

        return "\n".join(lines)
