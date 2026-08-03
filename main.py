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
        forces = [(0.0, 0.0, 0.0) for _ in self._planets]

        for i, planet_i in enumerate(self._planets):
            xi, yi, zi = planet_i.get_position()

            for j, planet_j in enumerate(self._planets):
                if i == j:
                    continue

                xj, yj, zj = planet_j.get_position()
                
                displacement_x = xj - xi
                displacement_y = yj - yi
                displacement_z = zj - zi

                # Distance
                distance = math.sqrt(dx * dx + dy * dy + dz * dz)

                if distance == 0:
                    continue

                # Newton's law of gravitation
                force_magnitude = (
                    GRAVITATION * planet_i.get_mass() * planet_j.get_mass() / distance ** 2
                )

                # Unit direction
                unit_x_direction = dx / distance
                uy = dy / distance
                uz = dz / distance

                # Force 
                force_x = force_magnitude * ux
                force_y = force_magnitude * uy
                force_z = force_magnitude * uz

                # Accumulate net force
                current_force_x, current_force_y, current_force_z = forces[i]

                forces[i] = (
                    current_fx + fx,
                    current_fy + fy,
                    current_fz + fz,
                )

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
