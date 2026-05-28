---
type: 公式
title: "[[Wallis公式]]"
tags:
  - 高数
  - 一元函数积分学及其应用
aliases:
  - Wallis公式
---
[Wallis公式及其应用-CSDN博客](https://blog.csdn.net/ACdreamers/article/details/41451591)

$\lim\limits_{n\to\infty}\frac{1}{2n+1}\left[\frac{(2n)!!}{(2n-1)!!}\right]^2=\frac{\pi}{2}$

$$\int_0^{\frac\pi2}\sin^nxdx=\begin{cases}\frac{(n-1)!!}{(n)!!}\cdot\frac\pi2,&\text{n为正偶数}\\\\\frac{(n-1)!!}{(n)!!},&\text{n为正奇数}\end{cases}$$ ^4sl2p5

$故\frac{(2k)!!}{(2k+1)!!}<\frac{(2k-1)!!}{(2k)!!}\frac{\pi}{2}<\frac{(2k-2)!!}{(2k-1)!!} \Rightarrow 1<\frac{\frac{\pi}{2}}{\left(\frac{(2k)!!}{(2k-1)!!}\right)^2\frac{1}{2k+1}}<\frac{2k+1}{2k}$

$由夹逼准则，\lim\limits_{k\to\infty}\frac{1}{2k+1}\left[\frac{(2k)!!}{(2k-1)!!}\right]^2=\frac{\pi}{2}$

$\begin{aligned}\int\frac{x+\sin x}{1+\cos x}\mathrm{d}x& =\int\frac{x}{1+\cos x}\mathrm{d}x+\int\frac{\sin x}{1+\cos x}\mathrm{d}x \\&=\int\frac12x\cdot\sec^2\frac x2\mathrm{d}x-\int\frac1{1+\mathrm{cos}x}\mathrm{d}(1+\mathrm{cos}x) \\&=\int x\mathrm{d}\tan\frac x2-\ln\mid1+\mathrm{cos}x\mid \\&=x\tan\frac x2+2\mathrm{ln}\bigg|\cos\frac x2\bigg|-\ln\mid1+\mathrm{cos}x\mid+C_1. \\&=x\tan\frac x2+C.\end{aligned}$
