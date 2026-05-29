 $$ \begin{aligned}&<\iint\limits_{D_{41}}f(x,\ y)\mathrm{d}x\mathrm{d}y+\iint\limits_{D_{42}}f(x,\ y)\mathrm{d}x\mathrm{d}y+\iint\limits_{D_{3}\cap D_{4}}f(x,\ y)\mathrm{d}x\mathrm{d}y\\ &=I_{4}.\\ \end{aligned} $$ 

所以  $ \max\{I_{1}, I_{2}, I_{3}, I_{4}\} = I_{4} $，即应选 (D).

注 事实上， $ D_{4} $ 是使得  $ \iint_{D}\left(1-x^{2}-\frac{1}{2}y^{2}\right)dxdy $ 取得最大值的区域，因为  $ D_{4} $ 包含了所有使  $ 1-x^{2}-\frac{1}{2}y^{2} $ 大于零的区域，而不包含任何使  $ 1-x^{2}-\frac{1}{2}y^{2} $ 小于零的区域，由二重积分的性质知  $ I_{4} $ 最大.

☑ 方法总结 寻找二重积分的最大值的区域，即是寻找被积函数大于等于零的区域。

例 14.2 设

 $$ D(t)=\left\{(x,y)\middle|2x^{2}+3y^{2}\leqslant6t\right\}(t\geqslant0), $$ 

 $$ f(x,y)=\left\{\begin{aligned}&\frac{\sqrt[3]{1-(x^{2}+y^{2})}-1}{e^{x^{2}+y^{2}}-1},&(x,y)\neq(0,0),\\ &a,&(x,y)=(0,0)\end{aligned}\right. $$ 

为连续函数，令  $ F(t)=\iint_{D(t)}f(x,y)\mathrm{d}x\mathrm{d}y $，则  $ F_{+}^{\prime}(0)= $ ___.

♡分析 本题积分区域为动态区域  $ D(t) $，当  $ t \to 0 $ 时， $ D(t) \to 0 $

本题研究的是在一点处的导数，所以用导数的定义，当  $ \iint_{D} f(x, y) \, \mathrm{d}\sigma $ 难计算时，可以利用二重积分的中值定理来处理.

解 应填  $ -\frac{\sqrt{6}\pi}{3} $.

由例 13.2 可知  $ a = -\frac{1}{3} $

由二重积分的中值定理知，存在  $ (\xi, \eta) \in D(t) $，使得

 $$ F(t)=\iint\limits_{D(t)}f(x,\ y)\mathrm{d}x\mathrm{d}y=\sqrt{6}\pi t f(\xi,\eta). $$ 

于是，

 $$ \begin{aligned}F_{+}^{\prime}(0)&=\lim_{t\rightarrow0^{+}}\frac{F(t)-F(0)}{t-0}=\lim_{t\rightarrow0^{+}}\frac{\sqrt{6}\pi t f(\xi,\eta)}{t}=\lim_{t\rightarrow0^{+}}\sqrt{6}\pi f(\xi,\eta)\\&=\sqrt{6}\pi f(0,0)=-\frac{\sqrt{6}\pi}{3}.\end{aligned} $$ 