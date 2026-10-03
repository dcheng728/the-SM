---
title: Home
permalink: /
---

# The Standard Model

Conventions: $$g_3, g_2, g_1$$ are the $$SU(3), SU(2), U(1)_Y$$ couplings, $$Q = T_3 + Y$$, metric $$(-+++)$$.

## Fields

<details markdown="1">
<summary>Definitions</summary>

Gauge group $$SU(3)\times SU(2)\times U(1)$$. Representations written $$(\mathbf{n}_3,\mathbf{n}_2)_Y$$, generations $$m=1,2,3$$.

</details>

| field | name | rep |
|---|---|---|
| $$G^a_\mu$$ ($$a=1..8$$) | gluon | $$(\mathbf 8,\mathbf 1)_0$$ |
| $$W^i_\mu$$ ($$i=1..3$$) | weak boson | $$(\mathbf 1,\mathbf 3)_0$$ |
| $$B_\mu$$ | hypercharge boson | $$(\mathbf 1,\mathbf 1)_0$$ |
| $$L_m=(\nu_L,e_L)_m$$ | lepton doublet | $$(\mathbf 1,\mathbf 2)_{-1/2}$$ |
| $$e_{Rm}$$ | charged lepton | $$(\mathbf 1,\mathbf 1)_{-1}$$ |
| $$Q_m=(u_L,d_L)_m$$ | quark doublet | $$(\mathbf 3,\mathbf 2)_{1/6}$$ |
| $$u_{Rm}$$ | up quark | $$(\mathbf 3,\mathbf 1)_{2/3}$$ |
| $$d_{Rm}$$ | down quark | $$(\mathbf 3,\mathbf 1)_{-1/3}$$ |
| $$\phi=(\phi^+,\phi^0)$$ | Higgs | $$(\mathbf 1,\mathbf 2)_{1/2}$$ |

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

This section follows the PDG Higgs and electroweak reviews: metric $$(+---)$$, $$Y_\Phi=1$$, $$Q=T_{3L}+Y/2$$, and $$g\equiv g_2$$, $$g'\equiv g_1$$.

$$SU(2)_L\times U(1)_Y\to U(1)_Q$$

### Higgs Lagrangian

$$\mathcal L_{\rm Higgs}=(D_\mu\Phi)^\dagger(D^\mu\Phi)-V(\Phi)$$

$$D_\mu\Phi=\left(\partial_\mu+ig\tfrac{\sigma^a}{2}W^a_\mu+ig'\tfrac Y2B_\mu\right)\Phi$$

$$V(\Phi)=\mu^2\Phi^\dagger\Phi+\lambda(\Phi^\dagger\Phi)^2$$

### Vacuum

$$\mu^2<0,\qquad \langle\Phi^\dagger\Phi\rangle=\frac{v^2}2=-\frac{\mu^2}{2\lambda}$$

$$\langle\Phi\rangle=\frac1{\sqrt2}\begin{pmatrix}0\\v\end{pmatrix},\qquad v=\sqrt{-\mu^2/\lambda}$$

### Unitary gauge

$$\Phi=\frac1{\sqrt2}\begin{pmatrix}0\\H+v\end{pmatrix}$$

### Masses

$$M_W^2=\frac{g^2v^2}4,\qquad M_Z^2=\frac{(g'^2+g^2)v^2}4$$

$$m_H^2=2\lambda v^2=-2\mu^2,\qquad M_\gamma=0$$

### Mixing and charge

$$\theta_W=\tan^{-1}(g'/g),\qquad e=g\sin\theta_W=g'\cos\theta_W$$

$$A_\mu=B_\mu\cos\theta_W+W^3_\mu\sin\theta_W$$

$$Z_\mu=-B_\mu\sin\theta_W+W^3_\mu\cos\theta_W$$

$$W^\pm_\mu=\frac{W^1_\mu\mp iW^2_\mu}{\sqrt2},\qquad M_W=M_Z\cos\theta_W$$

### Fermion masses

$$\begin{aligned}
m^{(e)}_n&=\frac{v}{\sqrt2}f_n\\
m^{(d)}_n&=\frac{v}{\sqrt2}h_n\\
m^{(u)}_n&=\frac{v}{\sqrt2}k_n
\end{aligned}$$

### Higgs couplings

$$g_{Hf\bar f}=\frac{m_f}{v}$$

### Fermi constant

$$\frac{G_F}{\sqrt2}=\frac{g^2}{8M_W^2}=\frac1{2v^2}$$

$$v=\left(\sqrt2G_F\right)^{-1/2}$$

## Fermion currents

### Charged current

$$\begin{aligned}
\mathcal L_{cc}=-\frac{g_2}{\sqrt2}\Big[&W^+_\mu V_{mn}\bar u_{Lm}\gamma^\mu d_{Ln}\\
&+W^-_\mu V^*_{mn}\bar d_{Ln}\gamma^\mu u_{Lm}\Big]
\end{aligned}$$

$$\begin{aligned}
\mathcal L^{\ell}_{cc}=-\frac{g_2}{\sqrt2}\Big[&W^+_\mu\bar\nu_{Lm}\gamma^\mu e_{Lm}\\
&+W^-_\mu\bar e_{Lm}\gamma^\mu\nu_{Lm}\Big]
\end{aligned}$$

### Neutral current

$$\begin{aligned}
\mathcal L_{nc}=&-eA_\mu J^\mu_{\rm em}\\
&-\frac{g_2}{\cos\theta_W}Z_\mu\left(J^\mu_3-\sin^2\theta_WJ^\mu_{\rm em}\right)
\end{aligned}$$

$$\begin{aligned}
J^\mu_{\rm em}&=\sum_fQ_f\bar f\gamma^\mu f\\
J^\mu_3&=\sum_fT_{3f}\bar f_L\gamma^\mu f_L
\end{aligned}$$

### CKM matrix

$$V_{mn}=\left(U^{u_L}U^{d_L\dagger}\right)_{mn},\qquad V^\dagger V=1$$

$$9-5=4:\quad\theta_{12},\ \theta_{23},\ \theta_{13},\ \delta$$

## Measured values

### Quarks (mass)

{% include table.html data=site.data.quarks cols="Q" %}

### Leptons (mass)

{% include table.html data=site.data.leptons cols="Q" %}

### Bosons (mass)

{% include table.html data=site.data.bosons cols="spin" %}

### Constants

{% include table.html data=site.data.constants %}

### CKM magnitudes

{% include table.html data=site.data.ckm %}

CKMfitter global fit with three-generation unitarity (PDG 2025, Review 12).

$$\theta_W$$ runs with the momentum scale; $$\sin^2\theta_W$$ is quoted at $$M_Z$$.
