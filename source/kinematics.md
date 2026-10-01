---
title: Kinematics
permalink: /kinematics/
nav: Kinematics
nav_order: 2
---

# Kinematics and conventions

## Collider coordinates

$$p_T=\sqrt{p_x^2+p_y^2},\qquad \phi=\arctan\frac{p_y}{p_x}$$

$$y=\tfrac12\ln\frac{E+p_z}{E-p_z},\qquad \eta=-\ln\tan\frac\theta2$$

$$p_z=p_T\sinh\eta,\qquad |\vec p|=p_T\cosh\eta$$

$$m_T=\sqrt{m^2+p_T^2}$$

$$E=m_T\cosh y,\qquad p_z=m_T\sinh y$$

$$y=\eta\ \ (m=0),\qquad \Delta R=\sqrt{(\Delta y)^2+(\Delta\phi)^2}$$

$$y\to y+y_{\rm boost}\ \text{under a boost along } z$$

## Masses

$$m^2=\Big(\sum_i p_i\Big)^2$$

$$m^2=2p_{T1}p_{T2}\left(\cosh\Delta\eta-\cos\Delta\phi\right)\quad(\text{two massless})$$

$$\vec E_T^{\rm miss}=-\sum_i\vec p_{T,i},\qquad H_T=\sum_i p_{T,i}$$

$$m_T^2=2p_T^\ell E_T^{\rm miss}\left(1-\cos\Delta\phi\right)$$

## Partons

$$\hat s=x_1x_2s,\qquad \hat y=\tfrac12\ln\frac{x_1}{x_2}$$

$$x_{1,2}=\frac{m}{\sqrt s}e^{\pm\hat y}\quad(2\to1,\ \hat s=m^2)$$

## Decays

$$p^*=\frac{\sqrt{\left[M^2-(m_1+m_2)^2\right]\left[M^2-(m_1-m_2)^2\right]}}{2M}$$

$$\tau=\frac{\hbar}{\Gamma},\qquad L=\beta\gammac\tau=\frac{p}{m}c\tau$$

$$\sigma\propto\frac{1}{(\hat s-M^2)^2+M^2\Gamma^2}$$

## Rates

$$N=\sigma\mathcal B(A\epsilon)\mathcal L_{\rm int},\qquad \mathcal L_{\rm int}=\int\mathcal Ldt$$

$$\langle\mu\rangle=\frac{\mathcal L_{\rm inst}\sigma_{\rm inel}}{f_{\rm rev}n_b}$$

$$\begin{aligned}
1\ \mathrm{pb}&=10^3\ \mathrm{fb}\\
1\ \mathrm{fb}&=10^{-39}\ \mathrm{cm}^2\\
1\ \mathrm{fb}^{-1}&=10^{39}\ \mathrm{cm}^{-2}
\end{aligned}$$

## Natural units

$$c=\hbar=1$$

{% include table.html data=site.data.units %}
