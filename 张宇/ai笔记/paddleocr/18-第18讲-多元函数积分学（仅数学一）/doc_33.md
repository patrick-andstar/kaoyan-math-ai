<div style="text-align: center;"><img src="imgs/img_in_image_box_368_135_616_254.jpg" alt="Image" width="24%" /></div>


这里的  $ \alpha $， $ \beta $ 谁大谁小无关紧要，关键是分别与起点和终点对应。

如果 L 由方程  $ y = y(x) $ ( $ x: a \to b $) 给出，可以看作参数方程  $ \left\{\begin{aligned} x &= x, \\ y &= y(x), \end{aligned}\right. $ 于是有

 $$ \begin{aligned}&\int_{L}P(x,\ y)\mathrm{d}x+Q(x,\ y)\mathrm{d}y\\=&\iint_{\boxed{a}}^{b}\{P[x,\ y(x)]+Q[x,\ y(x)]\ y^{\prime}(x)\\}\mathrm{d}x\ .\quad\\ &\rightarrow 不管大小 , 只管对应 \end{aligned} $$ 

注 如果你理解了上面的注释，则也可这样处理：

 $$ \begin{aligned}&\int_{L}P(x,\ y)\mathrm{d}x\\ &\xrightarrow{ 一报 } 二代 \\ =&\int_{\min\{a,\ b\}}^{\max\{a,\ b\}}P[x,\ y(x)](\pm\mathrm{d}x),\\ &\quad\mathrm{d}x>0\\ \end{aligned} $$ 

其中，当a<b时，取+dx；当a>b时，取-dx。

★ 例 18.15 设 $D$ 是由曲线 $L$：$\begin{cases} x = \cos^3 t, (0 \leqslant t \leqslant 2\pi) \\ y = \sin^3 t \end{cases}$ 与 $x$ 轴所围平面有界闭区域在第一、二象限的部分，$\partial D$ 为其边界，取逆时针方向，计算 $\oint_{\partial D} |x| \, dy + |y| \, dx$。

♡分析 从物理背景出发，在边界线上做功，分为3段进行处理，其中力  $ F = |y|i + |x|j $

解 如图 18-15 所示，对于曲线  $ L_1 $， $ L_2 $，在水平方向上，由于点  $ (x, y) $ 和点  $ (-x, y) $ 处的功的微元均为  $ |y|(-\mathrm{d}x) $，则  $ y(-\mathrm{d}x) + y(-\mathrm{d}x) = -2y\mathrm{d}x $，在铅直方向上，功的微元分别为  $ |x|\mathrm{d}y $ 与  $ |x|(-\mathrm{d}y) $，则  $ |x|\mathrm{d}y + |x|(-\mathrm{d}y) = 0 $。对于曲线  $ L_3 $： $ y = 0 $， $ x $ 从  $ -1 \to 1 $，于是  $ \int_{L_3} |x|\mathrm{d}y + |y|\mathrm{d}x = 0 $。故

<div style="text-align: center;"><img src="imgs/img_in_image_box_673_958_963_1152.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;">图 18-15</div>


 $$ \begin{aligned}\oint_{\partial D}\left|x\right|\mathrm{d}y+\left|y\right|\mathrm{d}x=&\oint_{L_{1}+L_{2}+L_{3}}\left|x\right|\mathrm{d}y+\left|y\right|\mathrm{d}x=\int_{L_{1}+L_{2}}\frac{\left|x\right|\mathrm{d}y+\left|y\right|\mathrm{d}x}{\downarrow}\\=&\int_{L_{1}+L_{2}}\left|y\right|\mathrm{d}x=-\int_{0}^{1}2y\mathrm{d}x=-\int_{\frac{\pi}{2}}^{0}2\sin^{3}t\mathrm{d}(\cos^{3}t)& 在 L_{1} 上 ,\left|x\right|j\cdot\mathrm{d}y=\left|x\right|\mathrm{d}y\cdot1,\\=&-\int_{L_{1}+L_{2}}\mathrm{y}\mathrm{d}x\\=&-2\int_{0}^{1}\mathrm{y}\mathrm{d}x&=2\int_{0}^{\frac{\pi}{2}}\sin^{3}t\cdot3\cos^{2}t(-\sin t)\mathrm{d}t\end{aligned} $$ 