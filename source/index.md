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
&\qquad\left.+k_{mn}\bar Q_m u_{Rn}\tilde\phi\right)+\text{h.c.}\\[4pt]
\mathcal L_\Theta&=-\sum_{k=1}^3\frac{g_k^2\Theta_k}{32\pi^2}F^{(k)}_{\mu\nu}\tilde F^{(k)\mu\nu},\quad \tilde F_{\mu\nu}=\tfrac12\epsilon_{\mu\nu\alpha\beta}F^{\alpha\beta}
\end{aligned}$$

$$\tilde\phi=\epsilon\phi^*=\begin{pmatrix}\phi^{0*}\\-\phi^{-}\end{pmatrix}$$

$$\mathcal L_\Theta$$ is a total divergence ($$F\tilde F=\partial_\mu k^\mu$$): no classical effect, parity-odd.

## Electroweak symmetry breaking

$$SU(2)_L\times U(1)_Y\to U(1)_{EM}$$

### Vacuum and unitary gauge

$$\begin{aligned}
\langle\phi\rangle&=\frac1{\sqrt2}\begin{pmatrix}0\\v\end{pmatrix},\quad v=\frac{\mu}{\sqrt\lambda}\\[4pt]
\phi_{\rm unitary}&=\frac1{\sqrt2}\begin{pmatrix}0\\v+H(x)\end{pmatrix}
\end{aligned}$$

### Masses

$$\begin{aligned}
m_H^2&=2\lambda v^2=2\mu^2,\qquad m_\gamma=0\\
m_W&=\tfrac12 g_2 v,\qquad M_Z=\tfrac12 v\sqrt{g_1^2+g_2^2}
\end{aligned}$$

$$W^\pm_\mu=\tfrac1{\sqrt2}\left(W^1_\mu\mp iW^2_\mu\right)$$

### Mixing

$$\cos\theta_W=\frac{g_2}{\sqrt{g_1^2+g_2^2}},\qquad \sin\theta_W=\frac{g_1}{\sqrt{g_1^2+g_2^2}}$$

$$m_W=M_Z\cos\theta_W$$

$$\begin{pmatrix}Z_\mu\\A_\mu\end{pmatrix}=\begin{pmatrix}\cos\theta_W&-\sin\theta_W\\\sin\theta_W&\cos\theta_W\end{pmatrix}\begin{pmatrix}W^3_\mu\\B_\mu\end{pmatrix}$$

### Electric charge

$$e=g_1\cos\theta_W=\frac{g_1g_2}{\sqrt{g_1^2+g_2^2}}$$

## Measured values

### Quarks (mass)

{% include table.html data=site.data.quarks cols="Q" %}

### Leptons (mass)

{% include table.html data=site.data.leptons cols="Q" %}

### Bosons (mass)

{% include table.html data=site.data.bosons cols="spin" %}

### Constants

{% include table.html data=site.data.constants %}

$$\theta_W$$ runs with the momentum scale; $$\sin^2\theta_W$$ is quoted at $$M_Z$$.
