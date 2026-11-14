from model.circuit import Circuit
from model.road_tile import RoadTile


# R = route, . = herbe (ou decor du campus)
# La grille a 16 colonnes et 12 lignes, comme la fenetre du jeu.
JUSSIEU_MAP = [
    "................",
    "................",
    "......RRRRRRR...",
    "..RRRRR.....R...",
    "..R.........R...",
    "..R.........R...",
    "..R.........R...",
    "..R.........R...",
    "..R.........R...",
    "..R.........R...",
    "..RRRRRRRRRRR...",
    "................",
]

# Coordonnees : (colonne, ligne)
JUSSIEU_STARTS = [(6, 10), (7, 10)]
JUSSIEU_FINISH = (7, 10)
JUSSIEU_CHECKPOINTS = [(12, 6), (11, 2), (2, 3), (2, 9)]
JUSSIEU_BOOSTS = [(9, 10), (12, 5)]
JUSSIEU_LAPS = 3


def create_jussieu():
    """Cree la grille du circuit de Jussieu avec la route et l'herbe."""
    grid = []
    for row, line in enumerate(JUSSIEU_MAP):
        tiles = []
        for col, symbol in enumerate(line):
            tile = RoadTile(col, row)
            tile.terrain = "route" if symbol == "R" else "herbe"
            tiles.append(tile)
        grid.append(tiles)
    return Circuit(grid)
