---
title: QFT
permalink: /qft/
nav: QFT
nav_order: 1
---

# QFT

Conventions: 
- metric diag$(+{-}{-}{-})$
- $[...]$ for length dimension of $...$. For example $[\phi] = \tfrac{1}{L^{d/2-1}}$.
- $S = \int d^dx \mathcal{L}$, $[S] = [\hbar]$.

## Representations

$$
R(g_1)\cdot R(g_2) = e^{i\theta(g_1,g_2)}\cdot R(g_1 \cdot g_2)
$$

$$
\begin{aligned}
\text{Unitarity}
&\Leftrightarrow
\bra{p}\ket{p'}=
\bra{p} R^\dagger(\Lambda)
R(\Lambda)\ket{p'}\\
&\Rightarrow \text{want unitary irreps of sym grp}.
\end{aligned}
$$

- passive: $\Phi'_a(\Lambda x) = D(\Lambda)_a{}^{b}\Phi_b(x)$
- active: $\Phi'_a(x) = D(\Lambda)_a{}^{b}\Phi_b(\Lambda^{-1}x)$

### Lorentz Group reps

Vector

$$
v^\mu \to v^{\prime \mu}
=\Lambda^\mu{}_{\nu} v^\nu,
$$

$$
\Lambda^\mu{}_{\nu} =
\left(
    e^{-i\tfrac{w_{\alpha\beta}}{2}M^{\alpha\beta}}
\right)^\mu{}_{\nu},\quad
\left(M^{\alpha\beta}\right)^\mu{}_{\nu}
=i\left(
    \eta^{\alpha\mu}\delta^\beta_\nu-
    \eta^{\beta\mu}\delta^\alpha_\nu
\right).
$$

Spinor

$$
\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}\mathbf{1}_{4\times4}
$$

$$
S^{\mu\nu} \equiv \frac{i}{4}[\gamma^\mu,\gamma^\nu],\quad
[\gamma^\mu,S^{\alpha\beta}]
= (M^{\alpha\beta})^\mu{}_{\nu}\gamma^\nu
$$

$$
[S^{\alpha\beta},S^{\rho\sigma}]
=(M^{\rho\sigma})^\alpha{}_{\mu}S^{\mu\beta}
-(M^{\rho\sigma})^\beta{}_{\mu}S^{\mu\alpha}.
$$

$$
\psi \to \psi' = \Lambda_{1/2} \psi,\quad
\Lambda_{1/2} = e^{-\tfrac{i}{2}w_{\alpha\beta}S^{\alpha\beta}},\quad
\Lambda^{-1}_{1/2}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_{\nu}\gamma^\nu.
$$

$$
\overline{\psi}\equiv \psi^\dagger \gamma^0
$$

## Harmonic Oscillators

$$
\hat{a}^\dagger \ket{n}= \sqrt{n+1}\ket{n},\quad
\hat{a} \ket{n}= \sqrt{n}\ket{n-1},\quad
\hat{a}^\dagger\hat{a} \ket{n} = n\ket{n}
$$

$$
[\hat{q},\hat{p}] = i\hbar,\quad
[\hat{a},\hat{a}^\dagger] = 1.
$$

## Canonical Quantization

$$
\begin{aligned}
\phi(x) 
&= \int \frac{d^3 \vec{k}}{(2\pi)^3}\frac{1}{\sqrt{2\omega_{\vec{k}}}}\left(
    \hat{a}_{\vec{k}}e^{-ipx}+
    \hat{a}_{\vec{k}}^\dagger e^{ipx}
\right),\\
\pi(x) 
&= \frac{\delta \mathcal{L}[\phi,\partial_\mu\phi]}{\delta \dot{\phi}(x)} = \dot\phi(x).
\end{aligned}
$$

$$
[a_{\vec{p}},a_{\vec{q}}^\dagger]=(2\pi)^3 \delta^{(3)}(\vec{p} - \vec{q}).
$$

$$
\left[\phi(t,\vec{x}),\pi(t,\vec{y})\right]
=i\hbar\delta^{(3)}(\vec{x}-\vec{y}).
$$

Fermionic Fields

$$
\overline{\psi}(x)
=
\sum_r \int \frac{d^3\vec{k}}{(2\pi)^3}
\frac{1}{\sqrt{2\omega_{\vec{k}}}}
\left[
    b_{\vec{k},r}u_{\vec{k},r}e^{-ikx}
    + c^\dagger_{\vec{k},r}v_{\vec{k},r}e^{ikx}
\right]
$$

$$
\left\{
    b_{\vec{k},r},b^\dagger_{\vec{q},s}
\right\} = (2\pi)^3 \delta_{rs}\delta^{(3)}(\vec{k}-\vec{q}),\quad
\left\{
    c_{\vec{k},r},c^\dagger_{\vec{q},s}
\right\} = (2\pi)^3 \delta_{rs}\delta^{(3)}(\vec{k}-\vec{q}).
$$

<details markdown="1">
<summary>References</summary>

- Goldberg, D. (2017). The standard model in a nutshell. Princeton University Press.
- Schwartz, M. (2013). Quantum field theory and the Standard Model. CUP.



</details>