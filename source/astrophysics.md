---
title: Astrophysics
permalink: /astrophysics/
nav: Astrophysics
nav_order: 8
---

# Astrophysics: scales and magnitudes

## Scales

### Distance

|  | name | value |
|---|---|---|
| $$R_\odot$$ | solar radius | 6.957 $$\mathrm{\times10^{8}\ m}$$ |
| $$\mathrm{au}$$ | astronomical unit | 1.496 $$\mathrm{\times10^{11}\ m}$$ |
| $$\mathrm{ly}$$ | light year | 9.461 $$\mathrm{\times10^{15}\ m}$$ |
| $$\mathrm{pc}$$ | parsec | 3.086 $$\mathrm{\times10^{16}\ m}$$ |

Source: [PDG 2025, Review 2](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-astrophysical-constants.pdf), Table 2.1. $$R_\odot$$, au and pc are exact.

### Mass

|  | name | value |
|---|---|---|
| $$M_\odot$$ | solar mass | 1.988 $$\mathrm{\times10^{30}\ kg}$$ |

Source: [PDG 2025, Review 2](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-astrophysical-constants.pdf), Table 2.1.

### Luminosity

|  | name | value |
|---|---|---|
| $$L_\odot$$ | solar luminosity | 3.828 $$\mathrm{\times10^{26}\ W\ (J/s)}$$ |

Source: [PDG 2025, Review 2](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-astrophysical-constants.pdf), Table 2.1. Exact.

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

|  | name | value |
|---|---|---|
| $$M_{\rm peak}$$ | Type Ia supernova (B band) | −19.3 $$\mathrm{mag}$$ |

Source: [Riess et al. (SH0ES), ApJ Lett. 934 (2022) L7](https://arxiv.org/abs/2112.04510), Table 5 baseline, rounded from $$-19.253$$.

### Distance modulus

$$m-M=5\log_{10}\frac{d}{10\ \mathrm{pc}}=5\log_{10}d-5\quad(d\ \text{in pc})$$

$$d=10^{(m-M+5)/5}\ \mathrm{pc}$$

## Redshift

$$z=\frac{\lambda_{\rm obs}-\lambda_{\rm emit}}{\lambda_{\rm emit}}$$

<details markdown="1">
<summary>References</summary>

- PDG Review 2, Astrophysical Constants and Parameters (2025), Table 2.1: au, pc (1 au / 1 arcsec), ly, solar mass, nominal solar radius and luminosity
- Riess et al. 2022 (SH0ES), ApJ 934, L7, Table 5: baseline $$M_B^0=-19.253$$ for Type Ia supernovae (B band, Cepheid-calibrated), rounded to $$-19.3$$

</details>
