from core.tile import GRASS

class world:
    def __init__(self, width, height, default_tile=GRASS):
        self.width = width
        self.height = height
        self.tiles = [
            [default_tile for x in range(width)]
            for y in range(height)
            ]



    def render_text(self):
        lines = []
                
        for row in self.tiles:

            symbols = []

            for tile in row:
                symbols.append(tile.symbol)

            line = "".join(symbols)
            lines.append(line)

        return "\n".join(lines)
    
    def render_debug(self):
        y_label_width = len(str(self.height - 1))

        header = " " * (y_label_width + 1)
        header += " ".join(str(x % 10) for x in range(self.width))

        lines = [header]

        for y, row in enumerate(self.tiles):
            line = " ".join(tile.symbol for tile in row)
            lines.append(f"{y:>{y_label_width}} {line}")

        return "\n".join(lines)

    def set_tile(self, x, y, tile): # x = coluna, y = linha
        if not self.is_inside(x, y):
            raise ValueError(f"posição fora do mundo: x={x}, y={y}")

        self.tiles[y][x] = tile

    def fill_rect(self, x, y, width, height, tile):
        for current_y in range(y, y + height):
            for current_x in range(x, x + width):
                self.set_tile(current_x, current_y, tile)
    def fill(self, tile):
            for y in range(self.height):
                for x in range(self.width):
                        self.set_tile(x, y, tile)

    def border_tile(self, tile):
            for x in range(self.width):
                    self.set_tile(x, 0, tile)
                    self.set_tile(x, self.height - 1, tile)

            for y in range(self.height):
                self.set_tile(0, y, tile)
                self.set_tile(self.width - 1, y, tile)

    def get_tile(self, x, y):
        if not self.is_inside(x, y):
            raise ValueError(f"posição fora do mundo: x={x}, y={y}")

        return self.tiles[y][x]
    
    def is_inside(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height
