# Orbis
Simulates how planets move and interact using Newton's law of gravity.

## Math

### Newton's Law of Universal Gravitation
```math
F_{1 \to 2} = \frac{Gm_1m_2}{r_{1 \to 2}^2}
```
where:
- F is force
- G is universal gravitational constant
- m is mass
- r is distance

**Calculate net force:**
```math
F_{\text{net}_k} = \sum_i^{n | n \neq k}{\frac{Gm_km_i}{r_{k \to i}^2}}
```

### Newton's Second Law of Motion
**Calculate acceleration:**
```math
\begin{aligned}
    F_{\text{net}} &= ma \\
    \frac{F_{\text{net}}}{m} &= a \\
    a &= \frac{F_{\text{net}}}{m}
\end{aligned}
```
where:
- $F$ is net force
- $m$ is mass
- $a$ is acceleration

### Acceleration
**Calculate velocity:**
```math
\begin{aligned}
    a &= \frac{dv}{dt} \\
    adt &= dv \\
    dv &= adt \\
    v_f - v_i &= adt \\
    v_f &= adt + v_i \\
\end{aligned}
```
where:
- $a$ is acceleration
- $v_f$ is final velocity
- $v_i$ is initial velocity
- $dt$ is change in time


### Velocity
**Calculate position:**
```math
\begin{aligned}
    v &= \frac{dx}{dt} \\
    vdt &= dx \\
    dx &= vdt \\
    x_f - x_i &= vdt \\
    x_f &= vdt + x_i
\end{aligned}
```
where:
- $v$ is velocity
- $x_f$ is final position
- $x_i$ is initial position
- $dt$ is change in time

### Direction
```math
\vec{AB} = (x_B - x_A, y_B - y_A, z_B - z_A)
```

Distance
```math

```

## Contributions
This repository is maintained by @jonahfrancisbenedicto
1. **Fork** the Project
2. **Create** your Feature Branch (`git checkout -b feature/custom-feature`)
3. **Commit** your Changes (`git commit -m 'Add custom feature'`)
4. **Push** to the Branch (`git push origin feature/custom-feature`)
5. **Open** a Pull Request

## License
This repository is licensed under the [MIT License](./LICENSE).
