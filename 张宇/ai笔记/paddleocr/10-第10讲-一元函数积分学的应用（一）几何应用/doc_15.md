 $ y=2x^{2} $ 和直线 y=0, x=a 所围成的平面区域，其中 0<a<2

(1) 求  $ D_{1} $ 绕 x 轴旋转一周而成的旋转体体积  $ V_{1} $， $ D_{2} $ 绕 y 轴旋转一周而成的旋转体体积  $ V_{2} $

(2) 问当 a 为何值时， $ V_{1} + V_{2} $ 取得最大值？并求此最大值.

10.8 计算由摆线  $ \left\{\begin{aligned} x &= a(t - \sin t), \\ y &= a(1 - \cos t) \end{aligned}\right. $  $ (a > 0, 0 \leqslant t \leqslant 2\pi) $ 与 x 轴所围平面图形绕 y 轴旋转一周所得旋转体的体积.

10.9 求曲线  $ y = 3 - |x^{2} - 1| $ 与 x 轴围成的封闭图形绕直线 y = 3 旋转一周所得旋转体的体积.

## 解答

10.1  $ \frac{\pi^{2}}{2} $ 解 所求体积为

 $$ \int_{0}^{+\infty}\pi\left(\frac{1}{\sqrt{1+x^{2}}}\right)^{2}\mathrm{d}x=\lim_{b\rightarrow+\infty}\pi\int_{0}^{b}\frac{1}{1+x^{2}}\mathrm{d}x=\left.\pi\lim_{b\rightarrow+\infty}\arctan x\right|_{0}^{b}=\frac{\pi^{2}}{2}. $$ 

10.2  $ 2\pi^2k^2b $ 解 如图 10-15 所示，上半圆周为  $ y_2 = b + \sqrt{k^2 - x^2} $，下半圆周为  $ y_1 = b - \sqrt{k^2 - x^2} $。其体积微元为

 $$ \begin{aligned}\mathrm{d}V&=(\pi y_{2}^{2}-\pi y_{1}^{2})\mathrm{d}x\\&=\pi[(b+\sqrt{k^{2}-x^{2}})^{2}-(b-\sqrt{k^{2}-x^{2}})^{2}]\mathrm{d}x\\&=4\pi b\sqrt{k^{2}-x^{2}}\mathrm{d}x,\end{aligned} $$ 

则所求旋转体的体积为

 $$ \begin{aligned}V=&4\pi b\int_{-k}^{k}\sqrt{k^{2}-x^{2}}\mathrm{d}x=8\pi b\int_{0}^{k}\sqrt{k^{2}-x^{2}}\mathrm{d}x\\=&8\pi b\bullet\frac{\pi k^{2}}{4}=2\pi^{2}k^{2}b.\end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_411_1098_603_1329.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;">图 10-15</div>
