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

### Proper-distance coordinate $$\chi$$

$$d\Sigma^2=d\chi^2+f^2(\chi)d\Omega^2,\qquad d\Omega^2=d\theta^2+\sin^2\theta d\phi^2$$

$$f(\chi)=\begin{cases}\sin\chi&K=+1\\\chi&K=0\\\sinh\chi&K=-1\end{cases}$$

## Einstein equations

$$G_{\mu\nu}=8\pi T_{\mu\nu}$$

$$\begin{aligned}
G_{00}&=3\left(\frac{\dot a}{a}\right)^2+\frac{3K}{a^2}=8\pi T_{00}\\
g^{ij}G_{ij}&=-6\frac{\ddot a}{a}-3\left(\frac{\dot a}{a}\right)^2-\frac{3K}{a^2}\\
&=8\pi g^{ij}T_{ij}
\end{aligned}$$


## Matter

### Perfect fluid

$$T_{\mu\nu}=(\rho+P)u_\mu u_\nu+Pg_{\mu\nu}$$

$$\hom\ \&\ \iso\Rightarrow u^\mu=(1,0,0,0)$$

$$T_{00}=\rho,\quad T_{0i}=0,\quad T_{ij}=Pg_{ij}$$

## Dynamics

### Friedmann equations

$$\left(\frac{\dot a}{a}\right)^2=\frac{8\pi}{3}\rho-\frac{K}{a^2}$$

$$\frac{\ddot a}{a}=-\frac{4\pi}{3}(\rho+3P)$$

$$\dot\rho+3\frac{\dot a}{a}(\rho+P)=0,\qquad \rho=\sum_i\rho_i$$

### Raychaudhuri (comoving observers)

$$\theta=3\frac{\dot a}{a},\qquad \sigma_{\mu\nu}=\omega_{\mu\nu}=0$$

$$\begin{aligned}
\dot\theta&=-\tfrac13\theta^2-R_{\mu\nu}u^\mu u^\nu\\
R_{\mu\nu}u^\mu u^\nu&=4\pi(\rho+3P)\ \Rightarrow\ \frac{\ddot a}{a}=-\frac{4\pi}{3}(\rho+3P)
\end{aligned}$$

### Static universe

$$\dot a=\ddot a=0\ \Rightarrow\ K=1,\quad \rho+3P=0$$

## Matter components

### Equations of state

$$\rho\propto a^{-3(1+w)}\quad(w\ \text{constant})$$

| component | $$w$$ | $$\rho\propto$$ |
|---|---|---|
| radiation | $$1/3$$ | $$a^{-4}$$ |
| matter (dust) | $$0$$ | $$a^{-3}$$ |
| $$\Lambda$$ | $$-1$$ | const |
| curvature (effective) | $$-1/3$$ | $$a^{-2}$$ |

$$T^\Lambda_{\mu\nu}=-\frac{\Lambda}{8\pi}g_{\mu\nu},\qquad \rho_\Lambda=\frac{\Lambda}{8\pi}=-P_\Lambda$$

$$\rho_K=-\frac{3K}{8\pi a^2}$$

### Scalar field $$\varphi(t)$$

$$\rho=\frac{\dot\varphi^2}{2}+V,\qquad P=\frac{\dot\varphi^2}{2}-V$$

$$V\gg\tfrac12\dot\varphi^2\ \Rightarrow\ w\approx-1\quad\text{(accelerated expansion)}$$

### Energy conditions

| condition | requires |
|---|---|
| weak | $$\rho\ge0$$ |
| dominant | $$-\rho\le P\le\rho$$ |
| strong | $$\rho\ge0,\quad \rho+3P\ge0$$ |

## Solutions

### Flat, $$K=0$$

$$a(t)=a_0\left(\frac{t}{t_0}\right)^{\frac{2}{3(1+w)}}$$

$$a\propto t^{1/2}\ \text{(radiation)},\qquad a\propto t^{2/3}\ \text{(matter)}$$

$$w=-1:\qquad a(t)=a_0\exp\!\left(\sqrt{\tfrac{\Lambda}{3}}t\right)$$

$$\rho_r\propto T^4\ \Rightarrow\ T\propto\frac1a\propto1+z$$

<figure>
<img src="{{ '/source/images/cmb.webp' | relative_url }}" alt="All-sky map of the cosmic microwave background temperature from Planck: small blue and red blotches on a nearly uniform background">
<figcaption>CMB temperature map (Planck)</figcaption>
</figure>
