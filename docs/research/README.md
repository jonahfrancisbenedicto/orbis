# Research

## Physics

### Newton's Law of Gravitation
**Newton's law of gravitation** $F=G\frac{m_1m_2}{r^2}$:
- $F$ is the force of gravity acting on the object
- $G$ is the Newton's constant of gravitation $G=(6.67430 \pm 0.00015) \times 10^{-11} \text{m}^3 \text{kg}^{-1} \text{s}^{-2}$ [Source](https://physics.nist.gov/cuu/Constants/index.html)
- $m$ is the mass of the object
- $r$ is the distance between the objects

In a system with multiple objects in 3-dimensions: $F_i=\sum_{j \neq i}{G\frac{m_im_j}{r^2_{ij}}\hat{r}_{ij}}$

### Newton's Second Law of Motion
**Newton's second law of motion** $F_{\text{net}}=ma$:
- $F_{\text{net}}$ is the net force acting on the object in $\text{kg} \text{m} \text{s}^-2$
- $m$ is the mass of the object in $\text{kg}$
- $a$ is the acceleration of the object in $\text{m} \text{s}^{-1}$

Newton's second law of motion can be used to determine the **acceleration** of the object: $a=\frac{F_{\text{net}}{m}$
```math
\begin{aligned}
    F_{\text{net}}&=ma \\
    \frac{F_{\text{net}}}{m}&=a \\
    \therefore \ a&=\frac{F_{\text{net}}}{m}
\end{aligned}
```

In a system with multiple objects in 3-dimensions: $a_i=\sum_{j \neq i}{G\frac{m_j}{r^2_{ij}}\hat{r}_{ij}}$

### Kinematic Equations
Acceleration is the change in velocity over time $a=\frac{dv}{dt}$:
- $a$ is the acceleration of the object in $\text{m} \text{s}^{-2}$
- $v$ is the velocity of the object in $\text{m} \text{s}^{-1}$
- $t$ is the time in $\text{s}$

Acceleration can be used to determine the **first kinematic equation**: $v=u+at$.

Suppose the initial velocity is $u$ and final velocity is $v$.

Suppose the initial time is $0$ and final time is $t$.

```math
\begin{aligned}
    a&=\frac{dv}{dt} \\
    adt&=dv \\
    \int^v_u{dv}&=\int^t_0{adt} \\
    [v]^v_u=a[t]^t_0 \\
    v-u=at \\
    \therefore \ v=u+at
\end{aligned}
```
- $v$ is the final velocity of the object in $\text{m} \text{s}^{-1}$
- $u$ is the inital velocity of the object in $\text{m} \text{s}^{-1}$
- $a$ is the acceleration of the object in $\text{m} \text{s}^{-2}$
- $t$ is the change in time in $\text{s}$

Velocity is the change in displacement over time $v=\frac{ds}{dt}$:
- $v$ is the velocity of the object in $\text{m} \text{s}^{-1}$
- $s$ is the displacement of the object in $\text{m}$
- $t$ is the time in $\text{s}$

Velocity can be used to determine the **second kinematic equation**: $s=ut+\frac{1}{2}at^2$.

Suppose the initial displacement is $0$ and final displacement is $s$.

Suppose the initial time is $0$ and final time is $t$.

```math
\begin{aligned}
    v&=\frac{ds}{dt} \\
    vdt&=ds \\
    (u+at)dt&=ds \\
    \int^t_0{u+at}dt&=\int^s_0{ds} \\
    \int^t_0{udt}+\int^t_0{atdt}&=s \\
    u[t]^t_0+a[\frac{1}{2}t^2]^t_0&=s \\
    ut+\frac{1}{2}at^2&=s \\
    \therefore \ s&=ut+\frac{1}{2}at^2
\end{aligned}
```
- $u$ is the inital velocity of the object in $\text{m} \text{s}^{-1}$
- $a$ is the acceleration of the object in $\text{m} \text{s}^{-2}$
- $t$ is the change in time in $\text{s}$
- $s$ is the displacement of the object in $\text{m}$

Acceleration can be rewritten using chainrule in terms of displacement to determine the **third kinematic equation**: $v^2=u^2+2as$

Suppose the initial displacement is $0$ and final displacement is $s$.

Suppose the initial velocity is $u$ and final velocity is $v$.

```math
\begin{aligned}
    a&=\frac{dv}{dt} \\
    a&=\frac{dv}{ds}\frac{ds}{dt} \\
    a&=v\frac{dv}{ds} \\
    ads&=vdv \\
    \int^s_0{ads}&=\int^v_u{vdv} \\
    a[s]^s_0&=[\frac{1}{2}v^2]^v_u \\
    as&=\frac{1}{2}v^2-\frac{1}{2}u^2 \\
    2as&=v^2-u^2 \\
    u^2+2as&=v^2 \\
    \therefore \ v^2=u^2+2as
\end{aligned}
```
- $v$ is the final velocity of the object in $\text{m} \text{s}^{-1}$
- $u$ is the inital velocity of the object in $\text{m} \text{s}^{-1}$
- $a$ is the acceleration of the object in $\text{m} \text{s}^{-2}$
- $s$ is the displacement of the object in $\text{m}$

The **fourth kinematic equation**: $s=\frac{1}{2}(u+v)t$
- $v$ is the final velocity of the object in $\text{m} \text{s}^{-1}$
- $u$ is the inital velocity of the object in $\text{m} \text{s}^{-1}$
- $t$ is the change in time in $\text{s}$
- $s$ is the displacement of the object in $\text{m}$

Kinematics assumes acceleration is constant. 

Acceleration is not constant according to Newton's law of gravitation and Newton's second law of motion because as the objects move the distance between the object changes and thus the gravitational force changes and thus the acceleration changes.

However, the kinematic equations can be used at discrete time intervals to account for the change in acceleration over time using numerical integration to approximate the changes in position and velocity over time.

### Numerical Integration

