 $$ \begin{aligned} 再积分 \leftarrow&V=\pi\int_{0}^{\mathrm{e}}\left(\ln^{2}y-2\ln y+\frac{2y}{\mathrm{e}}-\frac{y^{2}}{\mathrm{e}^{2}}\right)\mathrm{d}y\\=&\pi\left(y\ln^{2}y-4y\ln y+4y+\frac{y^{2}}{\mathrm{e}}-\frac{y^{3}}{3\mathrm{e}^{2}}\right)\Bigg|_{0}^{\mathrm{e}}=\frac{5}{3}\pi\mathrm{e}.\end{aligned} $$ 

注 第(2)问也可以直接套公式（10-1），可得方法二。

 $ L_0: x = 1 \Rightarrow Ax + By + C = 0 $ 中， $ A = 1 $， $ B = 0 $， $ C = -1 $。

 $ L: y_{\text{大}} = e^x $， $ y_{\text{小}} = ex $。

由

 $$ V=\frac{\pi}{\left(A^{2}+B^{2}\right)^{\frac{3}{2}}}\int_{a}^{b}\left[Ax+Bf(x)+C\right]^{2}\left|Af^{\prime}(x)-B\right|\mathrm{d}x, $$ 

得

则

 $$ V_{ 大 }=\pi\int_{-\infty}^{1}(x-1)^{2}\mathrm{e}^{x}\mathrm{d}x,\ V_{ 小 }=\pi\int_{0}^{1}(x-1)^{2}\mathrm{e}\mathrm{d}x\ , $$ 

 $$ \begin{aligned}V&=V_{ 大 }-V_{ 小 }&\\ &=\pi\int_{-∞}^{1}(x-1)^{2}\mathrm{e}^{x}\mathrm{d}x-\pi\int_{0}^{1}(x-1)^{2}\mathrm{e}\mathrm{d}x\\ &\\ &=\pi\int_{-∞}^{1}(x-1)^{2}\mathrm{d}(\mathrm{e}^{x})-\mathrm{e}\pi\int_{0}^{1}(x^{2}-2x+1)\mathrm{d}x\\ &\\ &=\pi\mathrm{e}^{x}(x-1)^{2}\Big|_{∞}^{1}-2\pi\int_{-∞}^{1}(x-1)\cdot\mathrm{e}^{x}\mathrm{d}x-\frac{\pi\mathrm{e}}{3}\\ &\\ &=-2\pi\int_{-∞}^{1}(x-1)\mathrm{d}(\mathrm{e}^{x})-\frac{\pi\mathrm{e}}{3}\\ &\\ &=-2\pi\mathrm{e}^{x}\cdot\left.(x-1)\right|_{∞}^{1}+2\pi\int_{-∞}^{1}\mathrm{e}^{x}\mathrm{d}x-\frac{\pi\mathrm{e}}{3}\\ &\\ &=2\pi\mathrm{e}^{x}\Big|_{∞}^{1}-\frac{\pi\mathrm{e}}{3}\\ &\\ &=\frac{5\pi\mathrm{e}}{3}.\\ \end{aligned} $$ 

## 3 用定积分表达和计算函数的平均值

设  $ x \in [a, b] $，函数  $ y(x) $ 在  $ [a, b] $ 上的平均值为  $ \bar{y} = \frac{1}{b - a} \int_a^b y(x) \, \mathrm{d}x \Rightarrow \bar{y} = y(\xi) $， $ \xi \in [a, b] $（由积分中值定理可得）。一般认为  $ y(x) $ 是连续函数

例 10.8 设  $ f(x) $ 连续，且  $ \frac{f(x+2)-f(x)=x}{x} $， $ \frac{\int_{0}^{2}f(x)dx=0}{x} $，则  $ f(x) $ 在  $ [1,3] $ 上的平均值为 ___.

♡分析 ①套公式： $ \overline{f}=\frac{1}{3-1}\int_{1}^{3}f(x)\mathrm{d}x=\frac{1}{2}\int_{1}^{3}f(x)\mathrm{d}x $ 观察可知区间长度均为2