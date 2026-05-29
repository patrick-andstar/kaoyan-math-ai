注 事实上，在本题解析过程中的②处，分离变量得  $ \frac{du}{1+\sin u}=dx $ 时，默认了一件事情，那就是  $ \sin u\neq-1 $，回避了  $ 1+\sin u=0 $ 的情况，从而丢掉了全部解中的部分解（可称为“奇解”）。当  $ \sin u=-1 $ 时，得  $ x+y+100=2k\pi-\frac{\pi}{2} $，其中  $ k=0,\pm1,\pm2,\cdots $ 在《全国硕士研究生招生考试数学考试大纲》中，只要求求解，并不要求求出全部解。→非线性方程，全部解=通解+奇解。线性方程：全部解=通解。

## 2 齐次型微分方程

形如  $ \frac{dy}{dx} = \varphi\left(\frac{y}{x}\right) $ 的方程叫作齐次型微分方程。其解法为令  $ u = \frac{y}{x} $，则  $ y = u x \Rightarrow \frac{dy}{dx} = u + x \frac{du}{dx} $，于是原方程变为  $ x \frac{du}{dx} + u = \varphi(u) $，即  $ \frac{du}{\varphi(u) - u} = \frac{dx}{x} $。

例 15.6 设 $L$ 是一条平面曲线，其上任意一点 $P(x, y) (x > 0)$ 到坐标原点的距离恒等于该点处的切线在 $y$ 轴上的截距，且 $L$ 经过点 $\left(\frac{1}{2}, 0\right)$。求曲线 $L$ 的方程。

由于 $(x, y)$ 为泛指的点，故用 $X$，$Y$ 表示坐标系

解 设曲线  $ L $ 过点  $ P(x, y) $ 的切线方程为  $ Y - y = y'(X - x) $。令  $ X = 0 $，得该切线在  $ y $ 轴上的截距为  $ y - xy' $。与  $ y $ 轴交点的纵坐标

由题设知  $ \sqrt{x^{2}+y^{2}}=y-xy' $，又 x>0，故  $ \sqrt{1+\left(\frac{y}{x}\right)^{2}}=\frac{y}{x}-y' $，令  $ u=\frac{y}{x} $，则此方程可化为  $ \frac{du}{\sqrt{1+u^{2}}}=-\frac{dx}{x} $，解得

 $$ y+\sqrt{x^{2}+y^{2}}=C\ . $$ 

由 L 经过点  $ \left(\frac{1}{2}, 0\right) $，知  $ C = \frac{1}{2} $。于是 L 的方程为  $ y + \sqrt{x^{2} + y^{2}} = \frac{1}{2} $，即  $ y = \frac{1}{4} - x^{2} (x > 0) $。

## 3 一阶线性微分方程

形如  $ y' + p(x)y = q(x) $ 的方程叫作一阶线性微分方程，其中  $ p(x) $， $ q(x) $ 为已知的连续函数，其通解公式为

 $$ y=\mathrm{e}^{-\int p(x)\mathrm{d}x}\left[\int\mathrm{e}^{\int p(x)\mathrm{d}x}\bullet q(x)\mathrm{d}x+C\right]. $$ 

请大家一定要掌握该公式的推导过程，这是一个很好的锻炼机会，不要错过。