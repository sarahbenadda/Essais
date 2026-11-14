from constants import GameState
from model.car import Car
from model.jussieu_data import (
    create_jussieu, JUSSIEU_STARTS, JUSSIEU_FINISH,
    JUSSIEU_CHECKPOINTS, JUSSIEU_BOOSTS, JUSSIEU_LAPS
)
from model.orly_data import (
    create_orly, ORLY_STARTS, ORLY_FINISH,
    ORLY_CHECKPOINTS, ORLY_BOOSTS, ORLY_LAPS
)
from model.tokyo_data import (
    create_tokyo, TOKYO_STARTS, TOKYO_FINISH,
    TOKYO_CHECKPOINTS, TOKYO_BOOSTS, TOKYO_LAPS
)


class GameModel:
    """Gère les données du jeu et le circuit choisi."""

    def __init__(self):
        """Prépare le menu et les trois circuits."""
        self.state = GameState.MENU
        self.circuit = None
        self.car = None
        self.circuit_names = ["Jussieu (facile)", "Orly (moyen)", "Japon (difficile)"]
        self.selected_circuit = 0
        self.starts = []
        self.finish = None
        self.checkpoints = []
        self.boosts = []
        self.laps = 0

    def change_circuit(self, direction: int) -> None:
        """Passe au circuit suivant ou précédent."""
        self.selected_circuit = (self.selected_circuit + direction) % len(self.circuit_names)

    def load_circuit(self) -> None:
        """Charge le circuit sélectionné et place la voiture au départ."""
        if self.selected_circuit == 0:
            self.circuit = create_jussieu()
            self.starts = JUSSIEU_STARTS
            self.finish = JUSSIEU_FINISH
            self.checkpoints = JUSSIEU_CHECKPOINTS
            self.boosts = JUSSIEU_BOOSTS
            self.laps = JUSSIEU_LAPS
        elif self.selected_circuit == 1:
            self.circuit = create_orly()
            self.starts = ORLY_STARTS
            self.finish = ORLY_FINISH
            self.checkpoints = ORLY_CHECKPOINTS
            self.boosts = ORLY_BOOSTS
            self.laps = ORLY_LAPS
        else:
            self.circuit = create_tokyo()
            self.starts = TOKYO_STARTS
            self.finish = TOKYO_FINISH
            self.checkpoints = TOKYO_CHECKPOINTS
            self.boosts = TOKYO_BOOSTS
            self.laps = TOKYO_LAPS

        self.car = Car(*self.starts[0])
        self.car.angle = -90 if self.selected_circuit != 2 else 0

    def update(self) -> None:
        """Met à jour la position de la voiture pendant la course."""
        if self.state == GameState.RACING and self.car is not None:
            self.car.update_position()
