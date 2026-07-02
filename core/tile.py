class Tile:
    def __init__(self, tile_type, symbol):
        self.tile_type = tile_type
        self.symbol = symbol

GRASS = Tile("grass", ".")
STONE = Tile("stone", "^")
WATER = Tile("water", "~")
