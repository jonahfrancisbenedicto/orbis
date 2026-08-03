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
    MERCURY_MASS: float = 3.3011e23
    MERCURY_DISTANCE: float = 5.79e10
    MERCURY_VELOCITY: float = 4.74e4
    MERCURY_VERTICAL_DISTANCE: float = 7.1e9

    VENUS_MASS: float = 4.8675e24
    VENUS_DISTANCE: float = 1.082e11
    VENUS_VELOCITY: float = 3.502e4
    VENUS_VERTICAL_DISTANCE: float = 6.4e9

    EARTH_MASS: float = 5.972e24
    EARTH_DISTANCE: float = 1.495978707e11
    EARTH_VELOCITY: float = 2.978e4

    MARS_MASS: float = 6.417e23
    MARS_DISTANCE: float = 2.279e11
    MARS_VELOCITY: float = 2.4007e4
    MARS_VERTICAL_DISTANCE: float = 7.4e9

    JUPITER_MASS: float = 1.898e27
    JUPITER_DISTANCE: float = 7.785e11
    JUPITER_VELOCITY: float = 1.307e4
    JUPITER_VERTICAL_DISTANCE: float = 1.8e10

    SATURN_MASS: float = 5.683e26
    SATURN_DISTANCE: float = 1.4335e12
    SATURN_VELOCITY: float = 9.69e3
    SATURN_VERTICAL_DISTANCE: float = 6.2e10

    URANUS_MASS: float = 8.681e25
    URANUS_DISTANCE: float = 2.8725e12
    URANUS_VELOCITY: float = 6.81e3
    URANUS_VERTICAL_DISTANCE: float = 3.9e10

    NEPTUNE_MASS: float = 1.024e26
    NEPTUNE_DISTANCE: float = 4.4951e12
    NEPTUNE_VELOCITY: float = 5.43e3
    NEPTUNE_VERTICAL_DISTANCE: float = 1.4e11

    SUN_MASS: float = 1.9885e30

    mercury = Planet(mass=MERCURY_MASS, position=(MERCURY_DISTANCE, MERCURY_VERTICAL_DISTANCE, 0), velocity=(0, MERCURY_VELOCITY, 0))
    venus = Planet(mass=VENUS_MASS, position=(VENUS_DISTANCE, VENUS_VERTICAL_DISTANCE, 0), velocity=(0, VENUS_VELOCITY, 0))
    earth = Planet(mass=EARTH_MASS, position=(EARTH_DISTANCE, 0, 0), velocity=(0, EARTH_VELOCITY, 0))
    mars = Planet(mass=MARS_MASS, position=(MARS_DISTANCE, MARS_VERTICAL_DISTANCE, 0), velocity=(0, MARS_VELOCITY, 0))
    jupiter = Planet(mass=JUPITER_MASS, position=(JUPITER_DISTANCE, JUPITER_VERTICAL_DISTANCE, 0), velocity=(0, JUPITER_VELOCITY, 0))
    saturn = Planet(mass=SATURN_MASS, position=(SATURN_DISTANCE, SATURN_VERTICAL_DISTANCE, 0), velocity=(0, SATURN_VELOCITY, 0))
    uranus = Planet(mass=URANUS_MASS, position=(URANUS_DISTANCE, URANUS_VERTICAL_DISTANCE, 0), velocity=(0, URANUS_VELOCITY, 0))
    neptune = Planet(mass=NEPTUNE_MASS, position=(NEPTUNE_DISTANCE, NEPTUNE_VERTICAL_DISTANCE, 0), velocity=(0, NEPTUNE_VELOCITY, 0))
    sun = Planet(mass=SUN_MASS, position=(0, 0, 0), velocity=(0, 0, 0))

    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    colours = [
        "gold",
        "gray",
        "orange",
        "royalblue",
        "firebrick",
        "peru",
        "khaki",
        "lightblue",
        "darkblue",
    ]

    system = System(planets=planets)

    delta_time = 3600*10
    steps_per_frame = 12

    fig = plt.figure(figsize=(8, 8))

    ax = fig.add_subplot(111, projection="3d")

    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.set_zlabel("Z (m)")

    limit = 5e12 #3e11

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
        frames=200,
        interval=20,
        blit=False,
    )

    animation.save("orbit.gif", writer="pillow", fps=30)
    plt.show()

if __name__ == "__main__":
    main()
