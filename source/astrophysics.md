---
title: Astrophysics
permalink: /astrophysics/
nav: Astrophysics
nav_order: 8
---

# Astrophysics: scales and magnitudes

## Scales

### Distance

{% include table.html data=site.data.astro_distance cols="name" %}

### Mass

{% include table.html data=site.data.astro_mass cols="name" %}

### Luminosity

{% include table.html data=site.data.astro_luminosity cols="name" %}

### Angles

$$1^\circ=60'=3600'',\qquad 1\ \mathrm{rad}=\frac{648000}{\pi}''\approx206265''$$

$$\theta=\frac{s}{d}\quad(\theta\ \text{in rad, small angle})$$

### Parallax

$$d\ [\mathrm{pc}]=\frac{1}{p\ [\mathrm{arcsec}]}$$

## Flux and magnitudes

### Flux

$$f=\frac{L}{4\pi d^2}$$

$$f\ [\mathrm{W}\ \mathrm{m}^{-2}],\quad L\ [\mathrm{W}],\quad d\ [\mathrm{m}]$$

### Magnitudes

$$\begin{aligned}
m&\equiv\text{apparent magnitude}\\
M&\equiv\text{absolute magnitude}=m\ (d=10\ \mathrm{pc})
\end{aligned}$$

$$m_1-m_2=-2.5\log_{10}\frac{f_1}{f_2}$$

$$M_1-M_2=-2.5\log_{10}\frac{L_1}{L_2}$$

### Distance modulus

$$m-M=5\log_{10}\frac{d}{10\ \mathrm{pc}}=5\log_{10}d-5\quad(d\ \text{in pc})$$

$$d=10^{(m-M+5)/5}\ \mathrm{pc}$$

## Redshift

$$z=\frac{\lambda_{\rm obs}-\lambda_{\rm emit}}{\lambda_{\rm emit}}$$

<details markdown="1">
<summary>References</summary>

- PDG Review 2, Astrophysical Constants and Parameters (2025), Table 2.1: au, pc (1 au / 1 arcsec), ly, solar mass, nominal solar radius and luminosity

</details>
