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
   \frac{\ddot{a}}{a} + 2 \left(\frac{\dot{a}}{a}\right)^2+2\frac{K}{a^2}
\right)g_{ij}.
$$


## Dynamics

### Friedmann equations

$$\left(\frac{\dot a}{a}\right)^2=\frac{8\pi G}{3}\rho-\frac{K}{a^2}$$

$$\frac{\ddot a}{a}=-\frac{4\pi G}{3}(\rho+3P)$$

$$\dot\rho+3\frac{\dot a}{a}(\rho+P)=0,\qquad \rho=\sum_i\rho_i$$

### Dilution Laws

$$
w_i \equiv P_i/\rho_i \Rightarrow
\rho_i(a) = \rho_{i,0}a^{-3(1+w_i)}
$$

| Component | $w$ | Density | Why
|---|---|---|---|
| baryon | 0 | $a^{-3}$ | Particle number is conserved while volume expands |
| radiation | $1/3$ | $a^{-4}$ | Number dilutes as $a^{-3}$ but also redshift $a^{-1}$ for energy |
| cosmological constant | $-1$ | constant | Vacuum energy density is constant |

<figure>
<img src="{{ '/source/images/cmb.webp' | relative_url }}" alt="All-sky map of the cosmic microwave background temperature from Planck: small blue and red blotches on a nearly uniform background">
<figcaption>CMB temperature map (Planck)</figcaption>
</figure>
