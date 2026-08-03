# Imports
import math

# Planet Class
class Planet:
    # Constructor Method
    def __init__(
        self,
        mass: float,
        position: tuple[float, float, float],
        velocity: tuple[float, float, float],
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

    _GRAVITATIONAL_CONSTANT: float = 6.674e-11

    # Constructor Method
    def __init__(self, planets: list["Planet"]) -> None:
        self._planets = planets

    # Methods
    def step(self, delta_time: float) -> None:

        # Calculate Forces
        planet_count = len(self._planets)
        net_forces = [(0.0, 0.0, 0.0) for _ in self._planets]

        for i, planet_i in enumerate(self._planets):
            position_x_i, position_y_i, position_z_i = planet_i.get_position()
            for j, planet_j in enumerate(self._planets):
                if i == j:
                    continue
                position_x_j, position_y_j, position_z_j = planet_j.get_position()

                # Displacement
                displacement_x = position_x_j - position_x_i
                displacement_y = position_y_j - position_y_i
                displacement_z = position_z_j - position_z_i

                # Distance
                distance = math.sqrt(
                    displacement_x ** 2 + displacement_y ** 2 + displacement_z ** 2
                )
                if distance == 0:
                    continue

                # Newton's law of gravitation
                force_magnitude = (
                    self._GRAVITATIONAL_CONSTANT
                    * planet_i.get_mass()
                    * planet_j.get_mass()
                    / distance ** 2
                )

                # Unit direction
                unit_direction_x = displacement_x / distance
                unit_direction_y = displacement_y / distance
                unit_direction_z = displacement_z / distance

                # Force
                force_x = force_magnitude * unit_direction_x
                force_y = force_magnitude * unit_direction_y
                force_z = force_magnitude * unit_direction_z

                # Net force
                net_force_x, net_force_y, net_force_z = net_forces[i]
                net_forces[i] = (
                    net_force_x + force_x,
                    net_force_y + force_y,
                    net_force_z + force_z,
                )

        for i in range(planet_count):
            planet = self._planets[i]
            net_force_x, net_force_y, net_force_z = net_forces[i]
            mass = planet.get_mass()

            # Calculate Accelerations
            acceleration_x = net_force_x / mass
            acceleration_y = net_force_y / mass
            acceleration_z = net_force_z / mass

            # Calculate Velocities 
            velocity_x, velocity_y, velocity_z = planet.get_velocity()
            velocity_x += acceleration_x * delta_time
            velocity_y += acceleration_y * delta_time
            velocity_z += acceleration_z * delta_time
            planet.set_velocity((velocity_x, velocity_y, velocity_z))

            # Calculate Positions
            position_x, position_y, position_z = planet.get_position()
            position_x += velocity_x * delta_time
            position_y += velocity_y * delta_time
            position_z += velocity_z * delta_time
            planet.set_position((position_x, position_y, position_z))

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
