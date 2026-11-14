import pygame

MAPPING = {
    pygame.K_UP: "accelerate",
    pygame.K_DOWN: "brake",
    pygame.K_LEFT: "turn_left",
    pygame.K_RIGHT: "turn_right",
    pygame.K_z: "accelerate",
    pygame.K_s: "brake",
    pygame.K_q: "turn_left",
    pygame.K_d: "turn_right",
}


class InputHandler:
    """Gère les touches pour conduire la voiture."""

    def __init__(self):
        """Associe les touches du clavier aux actions de conduite."""
        self.mapping = MAPPING

    def get_inputs(self) -> dict:
        """Vérifie les touches maintenues et renvoie les actions correspondantes."""
        keys = pygame.key.get_pressed()
        p = {action: False for action in self.mapping.values()}

        for key, action in self.mapping.items():
            if keys[key]:
                p[action] = True

        return p
