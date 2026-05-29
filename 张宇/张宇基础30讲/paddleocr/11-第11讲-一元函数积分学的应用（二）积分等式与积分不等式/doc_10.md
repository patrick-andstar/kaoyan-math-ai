故原式得证.

11.3 分析 左端定积分的被积函数为变限积分，考虑分部积分法.

证明

 $$ \begin{aligned}\int_{0}^{1}\left[\int_{0}^{f(x)}\varphi(t)\mathrm{d}t\right]\mathrm{d}x&=x\int_{0}^{f(x)}\varphi(t)\mathrm{d}t\Big|_{0}^{1}-\int_{0}^{1}x\varphi[f(x)]\cdot f^{\prime}(x)\mathrm{d}x\\&=-\int_{0}^{1}x^{2}\cdot f^{\prime}(x)\mathrm{d}x=-\int_{0}^{1}x^{2}\mathrm{d}[f(x)]\\&=-x^{2}f(x)\Big|_{0}^{1}+2\int_{0}^{1}x f(x)\mathrm{d}x=2\int_{0}^{1}x f(x)\mathrm{d}x.\end{aligned} $$ 

11.4 分析  $ (a+b)\int_{a}^{b}f(x)\mathrm{d}x<2\int_{a}^{b}xf(x)\mathrm{d}x\Leftrightarrow(a+b)\int_{a}^{b}f(x)\mathrm{d}x-2\int_{a}^{b}xf(x)\mathrm{d}x<0 $，可构造辅助函数，用单调性证明.

证明 令  $  F(t) = (a + t) \int_{a}^{t} f(x) \, dx - 2 \int_{a}^{t} x f(x) \, dx  $,  $  t \in [a, b]  $，则

 $$ \begin{aligned}F^{\prime}(t)&=\int_{a}^{t}f(x)\mathrm{d}x+(a+t)f(t)-2tf(t)=\int_{a}^{t}f(x)\mathrm{d}x-(t-a)f(t)\\&=\int_{a}^{t}f(x)\mathrm{d}x-\int_{a}^{t}f(t)\mathrm{d}x=\int_{a}^{t}[f(x)-f(t)]\mathrm{d}x.\end{aligned} $$ 

因为 $ f(x) $在 $ [a,b] $上严格单调增加，所以 $ f(x)-f(t)<0 $，于是有

 $$ F^{\prime}(t)=\int_{a}^{t}\left[f(x)-f(t)\right]\mathrm{d}x<0, $$ 

即  $ F(t) $ 严格单调减少，又  $ F(a)=0 $ ，所以  $ F(b)<0 $ ，即

 $$ (a+b)\int_{a}^{b}f(x)\mathrm{d}x-2\int_{a}^{b}x f(x)\mathrm{d}x<0, $$ 

即

 $$ (a+b)\int_{a}^{b}f(x)\mathrm{d}x<2\int_{a}^{b}x f(x)\mathrm{d}x\ . $$ 

11.5 证明 方法一 任取  $ x \in (0, a] $，由微分中值定理有

 $$ f(x)-f(0)=f^{\prime}(\xi)x,\xi\in(0,x). $$ 

又因 $ f(0)=0 $，故 $ f(x)=f'(\xi)x $， $ x\in(0,a] $，于是

 $$ \left|\int_{0}^{a}f(x)\mathrm{d}x\right|=\left|\int_{0}^{a}f^{\prime}(\xi)x\mathrm{d}x\right|\leqslant\int_{0}^{a}\left|f^{\prime}(\xi)\right|x\mathrm{d}x\leqslant M\int_{0}^{a}x\mathrm{d}x=\frac{M}{2}a^{2}. $$ 

方法二 设  $ x \in [0, a] $，由  $ f(0) = 0 $ 知

 $$ \int_{0}^{x}f^{\prime}(t)\mathrm{d}t=f(x)-f(0)=f(x), $$ 

于是

 $$ \left|f(x)\right|=\left|\int_{0}^{x}f^{\prime}(t)\mathrm{d}t\right|\leqslant\int_{0}^{x}\left|f^{\prime}(t)\right|\mathrm{d}t\leqslant\int_{0}^{x}M\mathrm{d}t=Mx, $$ 

故

 $$ \left|\int_{0}^{a}f(x)\mathrm{d}x\right|\leqslant\int_{0}^{a}\left|f(x)\right|\mathrm{d}x\leqslant\int_{0}^{a}M x\mathrm{d}x=\frac{M a^{2}}{2}\quad. $$ 