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

    _GRAVITATION: float = 6.7

    # Constructor Method
    def __init__(self, planets: list["Planet"]) -> None:
        self._planets = planets

    # Methods
    def step():
        # Calculate Forces
        forces: list[float] = []
        for i, planet_i in enumerate(self.get_planets()):
            for j, planet_j in enumerate(self.get_planets()):
                if i == j:
                    continue
                forces[i] += (
                    _GRAVITATION * planet_i.get_mass() * planet_j * get_mass() / 
                    math.sqrt(
                        (planet_j.get_position()[0] + planet_i.get_position()[0])**2 +
                        (planet_j.get_position()[1] + planet_i.get_position()[1])**2 +
                        (planet_j.get_position()[2] + planet_i.get_position()[2])**2
                    )
                )

        ## Calculate Direction


        ## Calculate Distance

        ## Calculate Magnitude

        ## Calculate Unit Direction 

        ## Calculate Force

        # Calculate Accelerations

        # Calculate Velocities

        # Calculate Positions

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
