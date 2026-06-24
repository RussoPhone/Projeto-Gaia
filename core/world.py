from core.tile import FLOOR

class GW:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = []

        for y in range(height):
            row = [FLOOR for x in range(width)]
            self.tiles.append(row)

    def render_text(self):
                lines = []
                
                for row in self.tiles:

                    symbols = []

                    for tile in row:
                         symbols.append(tile.symbol)
                    line = "".join(symbols)
                    lines.append(line)
                return "\n".join(lines)
    
    def set_tile(self, x, y, tile): # x = coluna, y = linha
        self.tiles[y][x] = tile

    def get_tile(self, x, y):
        return self.tiles[y][x]
    
    def is_inside(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height