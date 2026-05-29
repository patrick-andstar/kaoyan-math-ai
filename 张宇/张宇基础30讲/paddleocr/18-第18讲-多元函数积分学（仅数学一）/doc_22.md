例 18.8 已知曲线  $ L: y = x^2 (0 \leq x \leq \sqrt{2}) $，则  $ \int_L x \, ds = $ ___.

分析 利用“一投二代三计算”的口诀计算直角坐标系下的第一型曲线积分.

解 应填 $ \frac{13}{6} $

凑微分

 $$ \begin{aligned}\int_{L}x\mathrm{d}s=&\int_{0}^{\sqrt{2}}x\sqrt{1+(2x)^{2}}\mathrm{d}x=\frac{1}{8}\int_{0}^{\sqrt{2}}\sqrt{1+4x^{2}}\mathrm{d}(1+4x^{2})\\=&\frac{1}{12}(1+4x^{2})^{\frac{3}{2}}\bigg|_{0}^{\sqrt{2}}=\frac{13}{6}.\end{aligned} $$ 

例 18.9 设  $ L: x^2 + y^2 = -2y $，则  $ I = \oint_L \sqrt{x^2 + y^2} \, ds = $ ___.

 $ \phi \rightarrow $ 封闭曲线的专用符号

♡分析 根据曲线 L 及被积函数的表达式，不难发现都含有平方和，所以本题不宜用直角坐标计算，故采用极坐标解题.

解 应填 8.

 $$  由 x^{2}+y^{2}=-2y\Rightarrow r^{2}=-2r\sin\theta\Rightarrow r=-2\sin\theta $$ 

将曲线方程用极坐标表示： $ r = -2\sin\theta(-\pi \leq \theta \leq 0) $，则

故

 $$ \begin{aligned}x=r\cos\theta,\ y=r\sin\theta,\ \frac{\mathrm{d}s=\sqrt{[r(\theta)]^{2}+[r^{\prime}(\theta)]^{2}}\mathrm{d}\theta=\sqrt{4\sin^{2}\theta+}\\ \rightarrow 一投 ,\ I=\int_{-\pi}^{0}r\cdot2\mathrm{d}\theta\\ 二代 \quad I=\int_{-\pi}^{0}\frac{(-2\sin\theta)}{} \cdot2\mathrm{d}\theta=-4\int_{-\pi}^{0}\sin\theta\mathrm{d}\theta=8\end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_679_739_799_827.jpg" alt="Image" width="11%" /></div>


例 18.10 设  $ \Gamma $ 是空间曲线  $ \begin{cases} x^2 + y^2 + z^2 = 1, \\ x + y + z = 0, \end{cases} $ 则  $ \oint_{\Gamma} (x^2 + y^2) ds = $ ___.

分析 空间曲线是过原点的平面切球心在原点的单位球面所切出的一个大圆，且 x, y, z 地位相等，故可以考虑用轮换对称性. 后续所有积分，首先考虑用性质进行化简.

解 应填 $ \frac{4}{3}\pi $.

由轮换对称性知  $ \oint_{r} x^{2} ds = \oint_{r} y^{2} ds = \oint_{r} z^{2} ds $，于是

 $$ \begin{aligned}&\oint_{r}(x^{2}+y^{2})\mathrm{d}s=\oint_{r}x^{2}\mathrm{d}s+\oint_{r}y^{2}\mathrm{d}s\\ &\\ =2\oint_{r}x^{2}\mathrm{d}s=\frac{2}{3}\Big(\oint_{r}x^{2}\mathrm{d}s+\oint_{r}y^{2}\mathrm{d}s+\oint_{r}z^{2}\mathrm{d}s\Big)\\ &\\ =\frac{2}{3}\oint_{r}(x^{2}+y^{2}+z^{2})\mathrm{d}s\xlongequal{(*)}\frac{2}{3}\oint_{r}1\mathrm{d}s=\frac{2}{3}\times2\pi\times1=\frac{4}{3}\pi.\\ \end{aligned} $$ 

注 (1)  $ \Omega: x^2 + y^2 + z^2 \leq 1 $，不止包括曲面  $ x^2 + y^2 + z^2 = 1 $，还包括曲面内部，即三重积分的积分区域  $ \Omega: x^2 + y^2 + z^2 \leq 1 $ 为实心球体。

<div style="text-align: center;"><img src="imgs/img_in_image_box_828_1309_910_1401.jpg" alt="Image" width="7%" /></div>
