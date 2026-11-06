---
title: Cosmology
permalink: /cosmology/
nav: Cosmology
nav_order: 7
---

# Cosmology: FLRW and ΛCDM

## Conventions

$$
G=c=1,\qquad \text{metric }(-+++),\qquad w=\frac{P}{\rho}
$$

$$
\hom\equiv\text{``homogeneous"},\qquad
\iso\equiv\text{``isotropic"}
$$

$$
H\equiv\frac{\dot a}{a},\qquad 
1+z
=\frac{a_0}{a}
=\frac{\lambda_{\text{obs}}}{\lambda_{\text{orig}}}
$$

## FLRW Geometry

$$ds^2=-dt^2+a^2(t)d\Sigma^2,\quad
d\Sigma^2 = \gamma_{ij}dx^idx^j$$

$$\hom\ \&\ \iso\Rightarrow{}^{(3)}R_{ikjl}=K(\gamma_{ij}\gamma_{kl}-\gamma_{il}\gamma_{kj})$$

$$
{}^{(3)}R=6K,\quad
K = \text{+1 (closed)},\;
\text{0 (flat)},\;
\text{-1 (open)}.
$$

### Ricci tensor

$$
R_{00} = -3 \frac{\ddot{a}}{a} = -3 (\dot{H} - H^2),\quad H \equiv \frac{\dot{a}}{a},
$$

$$
R_{ij} = 
\left(
    \frac{\ddot{a}}{a} + 2 \left(\frac{\dot{a}}{a}\right)^2+2\frac{k}{a^2}
\right)
=
\left(
    \dot{H} + 3 H^2 + \frac{2k}{a^2}
\right)g_{ij}.
$$

### Einstein Equations (Friedmann)

$$
T_{00} = \rho(t),\quad
T_{ij} = p(t) g_{ij}(t).
$$

$$
\begin{aligned}
\left(
    \frac{\dot{a}}{a}
\right)^2 + \frac{k}{a^2} 
&= 8\pi G \sum_i \rho_i\\
\frac{\ddot{a}}{a}&=-\frac{4\pi G}{3} \sum_i (\rho_i + 3p_i)
\end{aligned}
$$

## Quintessence

$$
w = \frac{\tfrac12 \dot \phi^2 - V}{\tfrac12 \dot \phi^2 + V},\quad
\ddot \phi + 3 H \dot \phi + V_{,\phi} = 0
$$

### Dynamics

$$
p_i = \omega_i \rho_i
$$


<figure>
<img src="{{ '/source/images/cmb.webp' | relative_url }}" alt="All-sky map of the cosmic microwave background temperature from Planck: small blue and red blotches on a nearly uniform background">
<figcaption>CMB temperature map (Planck)</figcaption>
</figure>
