# Imports
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
                    self._GRAVITATIONAL_CONSTANT * planet_i.get_mass() * planet_j.get_mass() / distance ** 2
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
    EARTH_MASS: float = 5.972e24
    EARTH_DISTANCE: float = 1.495978707e11
    EARTH_VELOCITY: float = 2.978e4

    MARS_MASS: float = 6.417e23
    MARS_DISTANCE: float = 2.279e11
    MARS_VELOCITY: float = 2.4007e4
    MARS_VERTICAL_DISTANCE: float = 7.4e9

    SUN_MASS: float = 1.9885e30

    earth = Planet(mass=EARTH_MASS, position=(EARTH_DISTANCE, 0, 0), velocity=(0, EARTH_VELOCITY, 0))
    mars = Planet(mass=MARS_MASS, position=(MARS_DISTANCE, MARS_VERTICAL_DISTANCE, 0), velocity=(0, MARS_VELOCITY, 0))
    sun = Planet(mass=SUN_MASS, position=(0, 0, 0), velocity=(0, 0, 0))

    planets = [sun, earth, mars]


    system = System(planets=planets)

    delta_time = 3600
    steps_per_frame = 12

    colours = ["gold", "royalblue", "firebrick"]

    fig = plt.figure(figsize=(8, 8))

    ax = fig.add_subplot(111, projection="3d")

    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.set_zlabel("Z (m)")

    limit = 2.6e11

    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.set_zlim(-limit, limit)
 
    initial_positions_x = [planet.get_position()[0] for planet in system.get_planets()]
    initial_positions_y = [planet.get_position()[1] for planet in system.get_planets()]
    initial_positions_z = [planet.get_position()[2] for planet in system.get_planets()]

    scatter = ax.scatter(initial_positions_x, initial_positions_y, initial_positions_z, s=50, c=colours)
 
    trails = [ax.plot([], [], [], color=colour)[0] for colour in colours]
    trail_history = [([], [], []) for _ in planets]
    trail_length = 200
 
    def update(frame):
        for _ in range(steps_per_frame):
           system.step(delta_time)

        positions_x = []
        positions_y = []
        positions_z = []

        for planet in system.get_planets():
            position_x, position_y, position_z = planet.get_position()

            positions_x.append(position_x)
            positions_y.append(position_y)
            positions_z.append(position_z)

        scatter._offsets3d = (positions_x, positions_y, positions_z)
 
        for i, (x, y, z) in enumerate(zip(positions_x, positions_y, positions_z)):
            history_x, history_y, history_z = trail_history[i]

            history_x.append(x)
            history_y.append(y)
            history_z.append(z)

            del history_x[:-trail_length]
            del history_y[:-trail_length]
            del history_z[:-trail_length]

            trails[i].set_data_3d(history_x, history_y, history_z)
 
        return scatter,
 
    animation = FuncAnimation(
        fig,
        update,
        interval=20,
        blit=False,
    )

    plt.show()

if __name__ == "__main__":
    main()
