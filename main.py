# Imports
import math


# Planet Class
class Planet:

    _STEP_SIZE: float = 1.0
    _GRAVITATION: float = 6.7
    _ZERO: tuple[float, float, float] = (0,0,0)

    # Constructer Method
    def init(self, mass, position, velocity, acceleration, neighbours) -> None:
        self.set_mass(mass)
        self.set_position(position)
        self.set_velocity(velocity)
        self.set_acceleration(_ZERO)
        self.set_force(_ZERO)
        self.set_neighbours(neighbours)

    # Methods
    def step() -> None:
        self.set_force(_ZERO)
        for neighbour_i in self.get_neighbours():
            _MAGNITUDE = _GRAVITATION * self.get_mass() * neighbour_i.get_mass()
            self.set_force(
                self.get_force()[0] + _MAGNITUDE / 
                (self.get_position()[0] - neighbour_i.get_position()[0]), 
                self.get_force()[1] + _MAGNITUDE / 
                (self.get_position()[1] - neighbour_i.get_position()[1]), 
                self.get_force()[2] + _MAGNITUDE / 
                (self.get_position()[2] - neighbour_i.get_position()[2]) 
            )
        self.set_acceleration(self.get_force / self.get_mass())
        self.set_velocity(self.get_velocity() + self.get_acceleration() * _STEP_SIZE)
        self.set_position(self.get_position() + self.get_velocity() * _STEP_SIZE)

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

    def get_neighbours() -> list[Planet]:
        return self._neighbours

    def set_neighbours(neighbours: list[Planet]):
        self._neighbours = neighbours

class System:
    def init(self) -> None:
        pass
