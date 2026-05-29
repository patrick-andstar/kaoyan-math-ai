5.8 （仅数学一、数学二）曲线  $ y = x^{2} + x (x < 0) $ 上曲率为  $ \frac{\sqrt{2}}{2} $ 的点的坐标是 ___.

5.9 设函数  $ y = y(x) $ 由方程

 $$ 2y^{3}-2y^{2}+2xy-x^{2}=1 $$ 

所确定，试求  $ y = y(x) $ 的驻点，并判别它是否为极值点.

## 解答

5.1 (B) 解 由于  $ g(x_{0}) $ 是  $ g(x) $ 的极值，故由题设知  $ g'(x_{0})=0 $ 。记  $ y=f[g(x)] $ ，则  $ \left.\frac{dy}{dx}\right|_{x=x_{0}}=f'(a)g'(x_{0})=0 $ ，从而  $ x=x_{0} $ 是函数  $ y=f[g(x)] $ 的驻点。由于

 $$ \frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}=\left\{f^{\prime}\left[g(x)\right]g^{\prime}(x)\right\}^{\prime}=f^{\prime \prime}\left[g(x)\right]\left[g^{\prime}(x)\right]^{2}+f^{\prime}\left[g(x)\right]g^{\prime \prime}(x), $$ 

则

 $$ \left.\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}\right|_{x=x_{0}}=f^{\prime}(a)g^{\prime \prime}(x_{0}). $$ 

由题设知  $ g''(x_0) < 0 $，所以，若  $ f'(a) > 0 $，则可得到  $ \left.\frac{\mathrm{d}^2y}{\mathrm{d}x^2}\right|_{x=x_0} < 0 $，这正是函数  $ y = f[g(x)] $ 在驻点  $ x = x_0 $ 处取得极大值的充分条件，从而可知选项 (B) 正确。

若 $ f'(a)<0 $，则可推出函数 $ f[g(x)] $在 $ x_{0} $处取得极小值，故选项(A)不正确。

 $ f[g(x)] $ 在  $ x_0 $ 处取得极大值，与  $ f''(a) $ 的取值无关，即当  $ f''(a) > 0 $ 和  $ f''(a) < 0 $ 时都可能使  $ f[g(x)] $ 在  $ x_0 $ 处取得极大值。

例如，取  $ g(x) = -x^2 $， $ f(x) = \mathrm{e}^x $， $ x_0 = 0 $，则  $ g'(x) = -2x $， $ g''(x) = -2 < 0 $， $ g(0) = 0 $ 是  $ g(x) $ 的极大值， $ f[g(x)] = \mathrm{e}^{-x^2} $ 在  $ x = 0 $ 处取极大值，但  $ f''(0) = \mathrm{e}^0 = 1 > 0 $，故选项 (C) 不是充分条件。

又例如，取  $ g(x) = -x^2 $， $ f(x) = \ln(1 + x) $， $ x_0 = 0 $，则  $ f[g(x)] = \ln(1 - x^2) $ 在  $ x = 0 $ 处显然取得极大值，但此时  $ f''(0) = -\frac{1}{(1 + x)^2} \bigg|_{x=x_0} = -1 < 0 $，故选项 (D) 不是充分条件。

5.2 (D) 解 因为  $ f(a) $ 是最小值，所以  $ f(x) \geq f(a) $， $ x \in (a, b] $，又  $ f_{+}^{\prime}(a) $ 存在，故

 $$ f_{+}^{\prime}(a)=\lim_{x\to a^{+}}\frac{f(x)-f(a)}{x-a}\geqslant0\quad. $$ 

因为 $ f(b) $是最大值，所以 $ f(x) \leqslant f(b) $， $ x \in [a, b) $，又 $ f_{-}^{\prime}(b) $存在，故

 $$ f_{-}^{\prime}(b)=\lim_{x\to b^{-}}\frac{f(x)-f(b)}{x-b}\geq0. $$ 