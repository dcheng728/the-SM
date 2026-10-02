---
title: Statistics
permalink: /statistics/
nav: Statistics
nav_order: 6
---

# Statistics: maximum likelihood

## Likelihood

$$L(\theta)=\prod_{i=1}^np(x_i\mid\theta),\qquad \ell(\theta)=\ln L(\theta)$$

## Estimator

$$\hat\theta=\arg\max_\theta L(\theta),\qquad \left.\frac{\partial\ell}{\partial\theta}\right|_{\hat\theta}=0$$

## Fisher information

$$I(\theta)=-\mathbb E\!\left[\frac{\partial^2\ell}{\partial\theta^2}\right]=\mathbb E\!\left[\left(\frac{\partial\ell}{\partial\theta}\right)^2\right]$$

$$\mathrm{Var}(\hat\theta)\ge\frac1{I(\theta)}\quad\text{(Cram\'er–Rao)}$$

$$\hat\theta\ \xrightarrow{n\to\infty}\ \mathcal N\!\left(\theta,\ I^{-1}\right)$$

$$\hat V^{-1}_{jk}=-\left.\frac{\partial^2\ell}{\partial\theta_j\partial\theta_k}\right|_{\hat\theta}$$

## Intervals

$$\ell(\hat\theta\pm k\sigma)=\ell(\hat\theta)-\tfrac12k^2$$

## Examples

| model | $$\hat\theta$$ | $$\mathrm{Var}(\hat\theta)$$ |
|---|---|---|
| Gaussian, mean | $$\bar x$$ | $$\sigma^2/n$$ |
| Gaussian, variance | $$\tfrac1n\sum_i(x_i-\bar x)^2$$ | biased: $$\mathbb E\hat\sigma^2=\tfrac{n-1}{n}\sigma^2$$ |
| Poisson, one count | $$n$$ | $$\lambda$$ |
| Binomial | $$k/n$$ | $$p(1-p)/n$$ |
| Exponential, lifetime | $$\bar t$$ | $$\tau^2/n$$ |

## Likelihood ratio

$$\Lambda=\frac{L(H_1)}{L(H_0)}\quad\text{(Neyman–Pearson: most powerful)}$$

$$t_\theta=-2\ln\frac{L(\theta)}{L(\hat\theta)}\ \to\ \chi^2_1\quad\text{(Wilks)}$$

## Signal strength

$$\mu=\frac{\sigma}{\sigma_{\rm SM}},\qquad \langle n\rangle=\mu s+b$$

$$s,b$$: expected SM signal and background counts.

## Profile likelihood (nuisance parameters $$\nu$$)

$$\lambda(\mu)=\frac{L\!\left(\mu,\hat{\hat\nu}(\mu)\right)}{L(\hat\mu,\hat\nu)}$$

## Discovery

$$q_0=\begin{cases}-2\ln\lambda(0)&\hat\mu\ge0\\0&\hat\mu<0\end{cases}\qquad Z=\sqrt{q_0}$$

$$p=\tfrac12\ \mathrm{erfc}\!\left(Z/\sqrt2\right)$$

| $$Z$$ | one-sided $$p$$ |
|---|---|
| 1 | 0.15866 |
| 2 | 0.02275 |
| 3 (evidence) | 0.0013499 |
| 4 | $$3.1671\times10^{-5}$$ |
| 5 (discovery) | $$2.8665\times10^{-7}$$ |

### Expected significance (Asimov)

$$Z_A=\sqrt{2\left[(s+b)\ln\!\left(1+\frac sb\right)-s\right]}$$

## Exclusion

$$q_\mu=\begin{cases}-2\ln\lambda(\mu)&\hat\mu\le\mu\\0&\hat\mu>\mu\end{cases}$$

$$\mathrm{CL}_s=\frac{p_{s+b}}{1-p_b},\qquad \mathrm{CL}_s<0.05\Rightarrow\text{excluded at }95\%$$

## Look-elsewhere

$$p_{\rm global}\approx N_{\rm trials}p_{\rm local}$$

<details markdown="1">
<summary>References</summary>

- Neyman, Pearson, Phil. Trans. R. Soc. A 231 (1933) 289
- Read, J. Phys. G 28 (2002) 2693 ($$\mathrm{CL}_s$$)
- Gross, Vitells, EPJC 70 (2010) 525, arXiv:1005.1891 (look-elsewhere)
- Cowan, Cranmer, Gross, Vitells, EPJC 71 (2011) 1554, arXiv:1007.1727 (asymptotic formulae)
- ATLAS, Phys. Lett. B 716 (2012) 1, arXiv:1207.7214 (Higgs discovery)
- CMS, Phys. Lett. B 716 (2012) 30, arXiv:1207.7235 (Higgs discovery)

</details>

“It does not make any difference how beautiful your guess is. It does not make any difference how smart you are, who made the guess, or what his name is – if it disagrees with experiment it is wrong.” — Richard P. Feynman, *The Character of Physical Law* (1965), ch. 7
