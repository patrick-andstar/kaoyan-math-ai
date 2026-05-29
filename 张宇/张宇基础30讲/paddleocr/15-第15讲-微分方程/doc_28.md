积分得

 $$ \ln\left|\ln y\right|=\ln\left|\sin x\right|+C_{1}, $$ 

故通解为  $ \ln y = C \sin x $ 或  $ y = e^{C \sin x} $，其中 C 为任意常数。

15.4  $ C\sqrt{x^{2}+y^{2}}=\mathrm{e}^{\frac{2}{x}\arctan\frac{y}{x}} $，其中 C 为任意正常数 解 所求微分方程为齐次型微分方程，只要作代换  $ u=\frac{y}{x} $ 解之即可.

将方程变形为 $ \frac{dy}{dx}=\frac{1}{\arctan\frac{y}{x}}+\frac{y}{x} $，令 $ u=\frac{y}{x} $，则有 $ \arctan udu=\frac{dx}{x} $，两边积分，得

 $$ u\arctan u-\int\frac{u}{1+u^{2}}\mathrm{d}u=\int\frac{\mathrm{d}x}{x}, $$ 

所以有  $ u \arctan u - \frac{1}{2} \ln(1 + u^{2}) = \ln |x| + \ln C $，即  $ u \arctan u = \ln(C \cdot |x| \sqrt{1 + u^{2}}) $。

回代  $ u=\frac{y}{x} $，得  $ \frac{y}{x}\arctan\frac{y}{x}=\ln(C\sqrt{x^{2}+y^{2}}) $，即得原方程的通解  $ C\sqrt{x^{2}+y^{2}}=\mathrm{e}^{\frac{y}{x}\arctan\frac{y}{x}} $，其中 C 为任意正常数.

注 变量代换是求解微分方程问题的重要方法。

15.5  $  \mathrm{e}^{y} = \mathrm{e}^{-x} \left[ \frac{1}{2} \mathrm{e}^{x} (\sin x - \cos x) + C \right]  $，其中 C 为任意常数 解 将方程  $  y' + 1 = \mathrm{e}^{-y} \sin x  $ 变形为  $  (\mathrm{e}^{y})' + \mathrm{e}^{y} = \sin x  $，这是关于  $  \mathrm{e}^{y}  $ 的一阶线性微分方程。利用一阶非齐次线性微分方程的通解公式，得

 $$ \begin{aligned}\mathrm{e}^{y}&=\mathrm{e}^{-\int\mathrm{d}x}\left(\int\sin x\cdot\mathrm{e}^{\int\mathrm{d}x}\mathrm{d}x+C\right)=\mathrm{e}^{-x}\left(\int\mathrm{e}^{x}\sin x\mathrm{d}x+C\right)\\&=\mathrm{e}^{-x}\left[\frac{1}{2}\mathrm{e}^{x}(\sin x-\cos x)+C\right], 其中 C 为任意常数 .\end{aligned} $$ 

15.6  $ y = C_{1} + \frac{C_{2}}{x^{2}} $ （ $ C_{1} $， $ C_{2} $ 为任意常数） 解 这是  $ y'' = f(x, y') $ 型的可降阶微分方程．令  $ p = y' $，则

 $$ p^{\prime}+\frac{3}{x}p=0,\ p=C x^{-3}, $$ 

因此

 $$ y=\int C x^{-3}\mathrm{d}x=C_{1}-\frac{C}{2}x^{-2}=C_{1}+\frac{C_{2}}{x^{2}}\left(C_{1},C_{2} 为任意常数 \right). $$ 

15.7  $ y = C_{1} e^{-2x} + C_{2} e^{2x} + \frac{1}{4} x e^{2x} $，其中  $ C_{1}, C_{2} $ 为任意常数 解 对应的齐次方程为  $ y'' - 4y = 0 $，

特征方程

 $$ r^{2}-4=0, $$ 