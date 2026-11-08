---
title: Home
permalink: /
---

# The Standard Model

Conventions: 
- metric diag$(+{-}{-}{-})$
- $g_3, g_2, g_1$ are the $SU(3), SU(2), U(1)_Y$ couplings

## Fields

<details markdown="1">
<summary>Definitions</summary>

Gauge group $SU(3)\times SU(2)\times U(1)_Y$. 
Representations written $(\mathbf{n}_3,\mathbf{n}_2)_Y$.

</details>

| field | name | rep |
|---|---|---|
| $G^{(i)}_\mu$ ($i=1..8$) | gluon | $(\mathbf 8,\mathbf 1)_0$ |
| $W^{(i)}_\mu$ ($i=1..3$) | weak boson | $(\mathbf 1,\mathbf 3)_0$ |
| $B_\mu$ | hypercharge boson | $(\mathbf 1,\mathbf 1)_0$ |
| $L_m=(\nu_L,e_L)_m$ | lepton doublet | $(\mathbf 1,\mathbf 2)_{-1/2}$ |
| $e_{Rm}$ | charged lepton | $(\mathbf 1,\mathbf 1)_{-1}$ |
| $Q_m=(u_L,d_L)_m$ | quark doublet | $(\mathbf 3,\mathbf 2)_{1/6}$ |
| $u_{Rm}$ | up quark | $(\mathbf 3,\mathbf 1)_{2/3}$ |
| $d_{Rm}$ | down quark | $(\mathbf 3,\mathbf 1)_{-1/3}$ |
| $\phi=(\phi^+,\phi^0)$ | Higgs | $(\mathbf 1,\mathbf 2)_{1/2}$ |

## Lagrangian

$$\mathcal L_{SM}=\mathcal L_{\rm gauge}+\mathcal L_{\rm spinor}+\mathcal L_{\rm Higgs}+\mathcal L_{\rm Yukawa}+\mathcal L_\Theta$$

$$\begin{aligned}
G^a_{\mu\nu}&=\partial_\mu G^a_\nu-\partial_\nu G^a_\mu+g_3 f^{abc}G^b_\mu G^c_\nu\\
W^i_{\mu\nu}&=\partial_\mu W^i_\nu-\partial_\nu W^i_\mu+g_2\epsilon^{ijk}W^j_\mu W^k_\nu\\
B_{\mu\nu}&=\partial_\mu B_\nu-\partial_\nu B_\mu
\end{aligned}$$

**Covariant derivative.** $$D_\mu=\partial_\mu-ig_3 G^a_\mu\tfrac{\lambda^a}{2}-ig_2 W^i_\mu\tfrac{\sigma^i}{2}-ig_1 Y B_\mu$$

$$\begin{aligned}
\mathcal L_{\rm gauge}&=-\tfrac14 G^a_{\mu\nu}G^{a\mu\nu}-\tfrac14 W^i_{\mu\nu}W^{i\mu\nu}-\tfrac14 B_{\mu\nu}B^{\mu\nu}\\[4pt]
\mathcal L_{\rm spinor}&=-i\left(\bar L\gamma^\mu D_\mu L+\bar e_R\gamma^\mu D_\mu e_R+\bar Q\gamma^\mu D_\mu Q\right.\\
&\qquad\left.+\bar u_R\gamma^\mu D_\mu u_R+\bar d_R\gamma^\mu D_\mu d_R\right)\\[4pt]
\mathcal L_{\rm Higgs}&=-D_\mu\phi^\dagger D^\mu\phi-\lambda\left(\phi^\dagger\phi-\tfrac{\mu^2}{2\lambda}\right)^2\\[4pt]
\mathcal L_{\rm Yukawa}&=-\left(f_{mn}\bar L_m e_{Rn}\phi+h_{mn}\bar Q_m d_{Rn}\phi\right.\\
&\qquad\left.+k_{mn}\bar Q_m u_{Rn}\tilde\phi\right)+\text{h.c.},\quad\tilde\phi=\begin{pmatrix}\phi^{0*}\\-\phi^{+*}\end{pmatrix}\\[4pt]
\mathcal L_\Theta&=-\sum_{k=1}^3\frac{g_k^2\Theta_k}{32\pi^2}F^{(k)}_{\mu\nu}\tilde F^{(k)\mu\nu},\quad \tilde F_{\mu\nu}=\tfrac12\epsilon_{\mu\nu\alpha\beta}F^{\alpha\beta}
\end{aligned}$$

$$G\tilde G=\partial_\mu k^\mu,\ k^\mu=2\epsilon^{\mu\alpha\beta\gamma}(G^a_\alpha\partial_\beta G^a_\gamma+\tfrac{g_3}{3}f^{abc}G^a_\alpha G^b_\beta G^c_\gamma)$$

## Electroweak symmetry breaking


## Fermion currents


## Measured values

### Quarks (mass)

|  | $$Q$$ | $$T_3$$ (L) | value |
|---|---|---|---|
| $$u$$ | $$+2/3$$ | $$+1/2$$ | 2.16 ± 0.07 $$\mathrm{MeV}$$ |
| $$d$$ | $$-1/3$$ | $$-1/2$$ | 4.70 ± 0.07 $$\mathrm{MeV}$$ |
| $$s$$ | $$-1/3$$ | $$-1/2$$ | 93.5 ± 0.8 $$\mathrm{MeV}$$ |
| $$c$$ | $$+2/3$$ | $$+1/2$$ | 1.2730 ± 0.0046 $$\mathrm{GeV}$$ |
| $$b$$ | $$-1/3$$ | $$-1/2$$ | 4.183 ± 0.007 $$\mathrm{GeV}$$ |
| $$t$$ | $$+2/3$$ | $$+1/2$$ | 172.56 ± 0.31 $$\mathrm{GeV}$$ |

Source: [PDG 2025](https://pdg.lbl.gov). $$\overline{\mathrm{MS}}$$ masses: $$m_{u,d,s}$$ at 2 GeV, $$m_c(m_c)$$, $$m_b(m_b)$$; $$m_t$$ from direct measurement.

### Leptons (mass)

|  | $$Q$$ | $$T_3$$ (L) | value |
|---|---|---|---|
| $$e$$ | $$-1$$ | $$-1/2$$ | 0.51099895 $$\mathrm{MeV}$$ |
| $$\mu$$ | $$-1$$ | $$-1/2$$ | 105.6583755 ± 0.0000023 $$\mathrm{MeV}$$ |
| $$\tau$$ | $$-1$$ | $$-1/2$$ | 1776.93 ± 0.09 $$\mathrm{MeV}$$ |
| $$m_\beta$$ | $$0$$ | $$+1/2$$ | < 0.8 $$\mathrm{eV}$$ |

Source: [PDG 2025](https://pdg.lbl.gov); $$m_\beta$$ from [PDG 2024](https://pdg.lbl.gov), 90% CL upper limit on the effective mass $$\sqrt{\sum_i |U_{ei}|^2 m_i^2}$$ (flavour states have no definite mass).

### Bosons (mass)

|  | spin | value |
|---|---|---|
| $$\gamma$$ | 1 | 0 |
| $$g$$ | 1 | 0 |
| $$W^\pm$$ | 1 | 80.3692 ± 0.0133 $$\mathrm{GeV}$$ |
| $$Z$$ | 1 | 91.1880 ± 0.0020 $$\mathrm{GeV}$$ |
| $$H$$ | 0 | 125.20 ± 0.11 $$\mathrm{GeV}$$ |

Source: [PDG 2025](https://pdg.lbl.gov).

### Constants

|  | value |
|---|---|
| $$\alpha^{-1}(0)$$ | 137.035999177 ± 0.000000021 |
| $$\alpha_s(M_Z)$$ | 0.1180 ± 0.0009 |
| $$\sin^2\theta_W$$ | 0.23129 ± 0.00004 |
| $$G_F$$ | 1.1663788 ± 0.0000006 $$\mathrm{\times10^{-5}\ GeV^{-2}}$$ |
| $$v$$ | 246.22 $$\mathrm{GeV}$$ |

Sources: $$\alpha^{-1}$$ from [CODATA 2022](https://physics.nist.gov/cuu/Constants/); the rest from [PDG 2024](https://pdg.lbl.gov). $$\sin^2\theta_W$$ is $$\overline{\mathrm{MS}}$$ at $$M_Z$$; $$v$$ is derived from $$G_F$$.
