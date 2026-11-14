from model.circuit import Circuit
from model.road_tile import RoadTile


# R = route, . = decor (herbe, bâtiments ou jardin)
TOKYO_MAP = [
    '................',
    '..RRR......RRRR.',
    '.RRRRR....RRRRR.',
    '.RR.RRRRRRRR.RR.',
    '.RR..RRRRRR...R.',
    '.RRRRR........R.',
    '..RRRRR......RRR',
    '....RRR......RR.',
    '.RRRRR.....RRRR.',
    '.RRR.....RRRRRR.',
    '.RRRRRRRRRR.....',
    '................',
]

# Chaque position correspond à (colonne, ligne).
TOKYO_STARTS = [(13, 3), (14, 3)]
TOKYO_FINISH = (14, 3)
TOKYO_CHECKPOINTS = [(12, 1), (2, 3), (5, 7), (12, 9)]
TOKYO_BOOSTS = [(8, 3), (2, 9)]
TOKYO_LAPS = 3


def create_tokyo():
    """Prépare la grille du circuit japonais avec ses cases de route et de décor."""
    grid = []
    for row, line in enumerate(TOKYO_MAP):
        tiles = []
        for col, symbol in enumerate(line):
            tile = RoadTile(col, row)
            tile.terrain = "route" if symbol == "R" else "herbe"
            tiles.append(tile)
        grid.append(tiles)
    return Circuit(grid)
