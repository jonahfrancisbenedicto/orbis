# Imports
import math

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


# System Class
class System:

    # Constructor Method
    def __init__(self, planets: list["Planet"]) -> None:
        self._planets = planets

    # Methods
    def step():
        # Calculate Forces

        ## Calculate Direction

        ## Calculate Distance

        ## Calculate Magnitude

        ## Calculate Unit Direction 

        ## Calculate Force

        # Calculate Accelerations

        # Update Velocities

        # Update Positions

        pass

    # Getter and Setter Methods
    def get_planets(self) -> list["Planet"]:
        return self._planets

    def set_planets(self, planets: list["Planet"]) -> None:
        self._planets = planets

# Main Program
def main() -> None:
    pass

if __name__ == "__main__":
    main()
