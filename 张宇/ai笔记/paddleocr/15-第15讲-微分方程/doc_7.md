(2) 求曲线  $ y(x) $ 与 x 轴在  $ [0, +\infty) $ 上所围图形的面积.

解 (1) 根据一阶非齐次线性微分方程的通解公式，得

 $$ \begin{aligned}y(x)&=\mathrm{e}^{-\int\mathrm{d}x}\left(\int\mathrm{e}^{-x}\cos x\bullet\mathrm{e}^{\int\mathrm{d}x}\mathrm{d}x+C\right)\\&=\mathrm{e}^{-x}\left(\int\cos x\mathrm{d}x+C\right)\\&=\mathrm{e}^{-x}(\sin x+C)\enspace.\\ \end{aligned} $$ 

由 $ y(0)=0 $，得C=0，所以 $ y=e^{-x}\sin x $。

(2)由例10.4，可知所求面积为 $ \frac{e^{-\pi}+1}{2(1-e^{-\pi})} $

例 15.8 微分方程  $ y \mathrm{d}x + (x - 3y^{2}) \mathrm{d}y = 0 $ 满足条件  $ y|_{x=1} = 1 $ 的解为  $ y = $ ___。

(2) 分析 无法直接计算  $ \frac{dy}{dx} = \frac{y}{3y^{2} - x} $，此题可以取倒数，拆分，交换 x 与 y 的 “角色”.

解 应填 $ \sqrt{x} $

将微分方程变形为  $ \frac{dx}{dy} + \frac{x}{y} = 3y $，这是 x 关于 y 的一阶线性微分方程，其通解为

 $ x=\mathrm{e}^{-\int\frac{1}{y}\mathrm{d}y}\left(\int3y\mathrm{e}^{\int\frac{1}{y}\mathrm{d}y}\mathrm{d}y+C\right)=\frac{1}{y}\left(\int3y^{2}\mathrm{d}y+C\right)=y^{2}+\frac{C}{y} $.  $ \ln|y| $，理由见“二、3.”的注(2).

将  $ y\big|_{x=1}=1 $ 代入上式，得 C=0，于是  $ x=y^{2} $，即  $ y=\pm\sqrt{x} $。注意到  $ y\big|_{x=1}=1 $，故将  $ y=-\sqrt{x} $ 舍去，得  $ y=\sqrt{x} $。

注 此题中的初始条件不仅可以求独立常数 C，还可以确定解的符号。

★★★例15.9 设函数  $ y = \varphi(x) $ 是微分方程  $ y' + ey = \left(1 - \frac{1}{x}\right)^x $ 的一个解，则  $ \lim_{x \to +\infty} \varphi(x) = (\quad) $.

(A) e 

(B)  $ e^{2} $

(C) $ \frac{1}{e} $ (D) $ \frac{1}{e^{2}} $

解 应选(D).

 $ y' + ey = \left(1 - \frac{1}{x}\right)^x $ 为一阶线性微分方程，其通解为

 $$ y=\mathrm{e}^{-\int\mathrm{e}\mathrm{d}x}\left[\int\left(1-\frac{1}{x}\right)^{x}\bullet\mathrm{e}^{\int\mathrm{e}\mathrm{d}x}\mathrm{d}x+C\right]=\mathrm{e}^{-\mathrm{e}x}\left[\int\left(1-\frac{1}{x}\right)^{x}\bullet\mathrm{e}^{\mathrm{e}x}\mathrm{d}x+C\right] $$ 