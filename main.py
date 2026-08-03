# Imports
import math


# Constants
ZERO: tuple[float, float, float] = (0,0,0)

# Planet Class
class Planet:

    # Constructer Method
    def __init__(self, 
         mass: float, 
         position: tuple[float, float, float], 
         velocity: tuple[float, float, float]
    ) -> None:
        self.set_mass(mass)
        self.set_position(position)
        self.set_velocity(velocity)

    # Getter and Setter Methods
    def get_mass(self) -> float:
        return self._mass

    def set_mass(self, mass: float) -> None:
        self._mass = mass

    def get_position(self) -> tuple[float, float, float]:
        return self._position

    def set_position(self, position: tuple[float, float, float]) -> None:
        self._position = position

    def get_velocity(self) -> tuple[float, float, float]:
        return self._velocity

    def set_velocity(self, velocity: tuple[float, float, float]) -> None:
        self._velocity = velocity

class System:
    def __init__(self) -> None:
        pass
