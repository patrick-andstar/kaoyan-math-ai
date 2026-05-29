注 $ ^{(1)} $推导通解公式.

在方程两边同时乘以  $ e^{\int p(x)dx} $，得

 $$ \mathrm{e}^{\int p(x)\mathrm{d}x}\bullet y^{\prime}+\mathrm{e}^{\int p(x)\mathrm{d}x}p(x)\bullet y=\mathrm{e}^{\int p(x)\mathrm{d}x}\bullet q(x), $$ 

于是

 $$ \left[\mathrm{e}^{\int p(x)\mathrm{d}x}\cdot y\right]^{\prime}=\mathrm{e}^{\int p(x)\mathrm{d}x}\cdot q(x), $$ 

两边积分，得

 $$ \mathbf{e}^{\int p(x)\mathrm{d}x}\bullet y=\int\mathbf{e}^{\int p(x)\mathrm{d}x}\bullet q(x)\mathrm{d}x+C, $$ 

则

 $$ y=\mathrm{e}^{-\int p(x)\mathrm{d}x}\left[\int\mathrm{e}^{\int p(x)\mathrm{d}x}\cdot q(x)\mathrm{d}x+C\right] $$ 

(2) 在一阶线性微分方程的通解公式  $ y = e^{-\int p(x)dx} \left[ \int e^{\int p(x)dx} \cdot q(x)dx + C \right] $ 中，若

 $$ \int p(x)\mathrm{d}x=\ln\left|\varphi(x)\right|, $$ 

则

 $$ \mathrm{e}^{\int p(x)\mathrm{d}x}=\left|\varphi(x)\right|=\pm\varphi(x),\mathrm{e}^{-\int p(x)\mathrm{d}x}=\pm\frac{1}{\varphi(x)}, $$ 

代入上述通解公式，有

 $$ \begin{aligned}y=&\pm\frac{1}{\varphi(x)}\Big[\int\pm\varphi(x)\bullet q(x)\mathrm{d}x+C\Big]\\=&\frac{1}{\varphi(x)}\Big[\int\varphi(x)\bullet q(x)\mathrm{d}x\pm C\Big]\end{aligned} $$ 

 $$ \xlongequal{ 令 \pm C=D}\frac{1}{\varphi(x)}\Big[\int\varphi(x)\cdot q(x)\mathrm{d}x+D\Big], $$ 

其中 $D$ 依然为任意常数，故 $\mathrm{e}^{\int p(x)\mathrm{d}x} = |\varphi(x)|$ 可不加绝对值。

在其他计算过程中，若出现  $ \ln u $，且  $ u $ 不知正负，一律加绝对值。

★ (3) 由于  $ \int p(x)dx $ 与  $ \int q(x)e^{\int p(x)dx}dx $ 均应理解为某一不含任意常数的原函数，故公式法亦可写成  $ y = e^{-\int x_0^2 p(t)dt} \left[ \int x_0^2 q(t)e^{\int x_0^2 p(s)ds} dt + C \right] $，这里的  $ x_0 $ 在题设未提出定值要求时，可按方便解题的原则来取。此写法在研究解的性质时颇为有用，最近几年高频较高。研究解的周期性、有界性、求极限等需用定值处理的问题时，常用定积分的表达式表示通解。

例 15.7 设  $ y = y(x) $ 是微分方程  $ y' + y = e^{-x} \cos x $ 满足  $ y(0) = 0 $ 的特解.

(1) 求  $ y(x) $;