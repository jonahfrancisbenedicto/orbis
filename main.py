# Newton's Law of Gravitation
# F_n = G*m_1*m_2/r**2

# Newton's Second Law
# F_net = m*a
# a = F_net/m

# Position, Velocity and Acceleration

# Euler Method
# a = dv/dt
# v = dx/dt
# v_new = v_old + a_new * dt
# x_new = x_old + v_new * dt

# Imports
import math

class Planet:

    # Constructer Method
    def init(self, mass, position, velocity, acceleration) -> None:
        self._mass: float = mass
        self._position: tuple[float, float, float] = position
        self._velocity: tuple[float, float, float] = velocity
        self._acceleration: tuple[float, float, float] = acceleration

    # Methods
    def get_speed() -> float:
        return math.sqrt(velocity[0]**2+velocity[1]**2+velocity[2]**2)

    def get_kinetic_energy() -> float:
        return 0.5 * self._mass * self.get_speed() ** 2

    def get_momentum() -> float:
        return self._mass * self.get_speed()

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


class System:
    def init(self) -> None:
        pass
