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

## Harmonic Oscillators

$$
\hat{a}^\dagger \ket{n}= \sqrt{n+1}\ket{n},\quad
\hat{a} \ket{n}= \sqrt{n}\ket{n-1},\quad
\hat{a}^\dagger\hat{a} \ket{n} = n\ket{n}
$$

$$
[\hat{q},\hat{p}] = i\\hbar,\quad
[\hat{a},\hat{a}^\dagger] = 1.
$$

## Canonical Quantization

$$
\phi(x) = \int \frac{d^3 \vec{k}}{(2\pi)^3}\frac{1}{\sqrt{2\omega_{\vec{k}}}}\left(
    \hat{a}_{\vec{k}}e^{-ipx}+
    \hat{a}_{\vec{k}}^\dagger e^{ipx}
\right),\quad
\pi(x) = \frac{\delta \mathcal{L}[\phi,\partial_\mu\phi]}{\delta \dot{\phi}(x)} = \dot\phi(x).
$$

$$
[a_{\vec{p}},a_{\vec{q}}^\dagger]=(2\pi)^3 \delta^{(3)}(\vec{p} - \vec{q}).
$$

$$
\left[\phi(t,\vec{x}),\pi(t,\vec{y})\right]
=i\hbar\delta^{(3)}(\vec{x}-\vec{y}).
$$


<details markdown="1">
<summary>References</summary>

- Goldberg, D. (2017). The standard model in a nutshell. Princeton University Press.
- Schwartz, M. (2013). Quantum field theory and the Standard Model. CUP.

</details>