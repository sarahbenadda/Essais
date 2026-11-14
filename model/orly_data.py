from model.circuit import Circuit
from model.road_tile import RoadTile


# R = route, . = herbe ou decor de l'aeroport
ORLY_MAP = [
    "................",
    "................",
    ".RRRRRRRRRRRRRR.",
    ".R............R.",
    ".R............R.",
    ".R...........RR.",
    ".R..........RR..",
    ".R..........RR..",
    ".RR.........RR..",
    "..R..........R..",
    "..RRRRRRRRRRRR..",
    "................",
]

# Coordonnees sous la forme (colonne, ligne)
ORLY_STARTS = [(6, 10), (7, 10)]
ORLY_FINISH = (7, 10)
ORLY_CHECKPOINTS = [(12, 10), (13, 5), (10, 2), (1, 5)]
ORLY_BOOSTS = [(9, 2), (12, 7)]
ORLY_LAPS = 3


def create_orly():
    """Cree le circuit d'Orly avec les cases de route et d'herbe."""
    grid = []
    for row, line in enumerate(ORLY_MAP):
        tiles = []
        for col, symbol in enumerate(line):
            tile = RoadTile(col, row)
            tile.terrain = "route" if symbol == "R" else "herbe"
            tiles.append(tile)
        grid.append(tiles)
    return Circuit(grid)
