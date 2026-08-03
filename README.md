# Orbis
Simulates how planets move and interact using Newton's law of gravity.

## Math

Newton's Law of Universal Gravitation
```math
F_{1->2} = \frac{Gm_1m_2}{r_{1->2}^2}
```

```math
F_{\text{1}} = \sum_i^{n-1}{\frac{Gm_1m_i}{r_{1->i}^2}
```

Newton's Second Law of Motion
```math
\begin{aligned}
    F_{\text{net}} &= ma \\
    \frac{F_{\text{net}}}{m} &= a \\
    a &= \frac{F_{\text{net}}}{m}
\end{aligned}
```

Acceleration
```math
\begin{aligned}
    a &= \frac{dv}{dt} \\
    adt &= dv \\
    dv &= adt \\
    v_f - v_i &= adt \\
    v_f &= adt + v_i
\end{aligned}
```

Velocity
```math
\begin{aligned}
    v &= \frac{dx}{dt} \\
    vdt &= dx \\
    dx &= vdt \\
    x_f - x_i &= vdt \\
    x_f &= vdt + x_i
\end{aligned}
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
