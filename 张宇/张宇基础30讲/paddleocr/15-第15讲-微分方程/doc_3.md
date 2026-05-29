本题涉及微分方程的概念，难度不大。

例 15.2 设  $ y = y(x) $ 是二阶常系数线性微分方程  $ y'' + py' + qy = e^{3x} $ 满足初始条件  $ y(0) = y'(0) = 0 $ 的特解，则  $ \lim_{x \to 0} \frac{\ln(1 + x^2)}{y(x)} = $ ___.

☐ 分析 由  $ y(0) $,  $ y'(0) $，分析出  $ y''(0) $，然后借助洛必达法则求解.

解 应填 2.

不用求解微分方程，而是利用方程所反映出来的函数与各阶导数之间的关系来解题。由  $ y'' + py' + qy = e^{3x} $ 得  $ y''(x) $ 连续，且  $ y''(0) = -py'(0) - qy(0) + e^0 = 1 $，故

 $$ \lim_{x\to0}\frac{\ln(1+x^{2})}{y(x)}=\lim_{x\to0}\frac{x^{2}}{y(x)}=\lim_{x\to0}\frac{2x}{y^{\prime}(x)}=\lim_{x\to0}\frac{2}{y^{\prime \prime}(x)}=\frac{2}{y^{\prime \prime}(0)}=2 $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_105_564_139_600.jpg" alt="Image" width="3%" /></div>


## 一 阶微分方程的求解

<div style="text-align: center;"><img src="imgs/img_in_image_box_847_546_951_654.jpg" alt="Image" width="10%" /></div>


## 1 可分离变量型微分方程

(1) 直接可分离.

能写成 $ y' = f(x)g(y) $形式的方程称为可分离变量型微分方程，其解法为

 $$ \frac{\mathrm{d}y}{\mathrm{d}x}=f(x)g(y)\Rightarrow\int\frac{\mathrm{d}y}{g(y)}=\int f(x)\mathrm{d}x\text{．"物以类聚，人以群分"} $$ 

例 15.3 已知曲线  $ y = f(x) $ 过点  $ \left(0, -\frac{1}{2}\right) $，且其上任一点  $ (x, y) $ 处的切线斜率为  $ x \ln(1 + x^2) $，则  $ f(x) = $ ___.

☑分析 本题考查根据实际问题建立微分方程的能力，关键是要知道导数的几何意义即为曲线在这一点处的切线的斜率。本讲中将经常出现由几何、物理问题建立微分方程并求解的题目。

解 应填  $ \frac{1}{2}(1+x^{2})[\ln(1+x^{2})-1] $.

由实际问题建立微分方程为

学会将几何表达翻译成数学表达式.

 $ \left\{\begin{aligned}\frac{\mathrm{d}y}{\mathrm{d}x}&=x\ln(1+x^{2}),\\ y|_{x=0}&=-\frac{1}{2},\end{aligned}\right. $

这是一个可分离变量型微分方程求特解的问题，用分离变量法求解。由

 $$ \int\mathrm{d}y=\int x\ln(1+x^{2})\mathrm{d}x, $$ 