# Imports
import math


# Constants
ZERO: tuple[float, float, float] = (0,0,0)

# Planet Class
class Planet:


    # Constructer Method
    def __init__(self, mass, position, velocity, neighbours) -> None:
        self.set_mass(mass)
        self.set_position(position)
        self.set_velocity(velocity)
        self.set_acceleration(ZERO)
        self.set_force(ZERO)
        self.set_neighbours(neighbours)

    # Getter and Setter Methods
    def get_mass() -> float:
        return self._mass

    def set_mass(mass: float) -> None:
        self._mass = mass

    def get_position() -> tuple[float, float, float]:
        return self._position

    def set_position(position: tuple[float, float, float]) -> None:
        self._position = position

    def get_velocity() -> tuple[float, float, float]:
        return self._velocity

    def set_velocity(velocity: tuple[float, float, float]) -> None:
        self._velocity = velocity

    def get_acceleration() -> tuple[float, float, float]:
        return self._acceleration

    def set_acceleration(acceleration: tuple[float, float, float]) -> None:
        self._acceleration = acceleration

    def get_force() -> tuple[float, float, float]:
        return self._force
   
    def set_force(force: tuple[float, float, float]) -> None:
        self._force = force

    def get_neighbours() -> list["Planet"]:
        return self._neighbours

    def set_neighbours(neighbours: list["Planet"]):
        self._neighbours = neighbours

class System:
    def init(self) -> None:
        pass
