为___.

分析  $ r=\frac{\sqrt{x}-x}{\sqrt{2}} $

取微元： $  \mathrm{d}V = \pi \cdot \left( \frac{\sqrt{x} - x}{\sqrt{2}} \right)^2 \cdot \sqrt{2} \mathrm{d}x  $

解 应填 $ \frac{\sqrt{2}}{60}\pi $

 $ y=\sqrt{x} $ 与 y=x 交于点  $ (0,0) $， $ (1,1) $，如图 10-12 所示，曲线  $ y=\sqrt{x} $ 上的点到 y=x 的距离

为  $ r=\frac{\sqrt{x}-x}{\sqrt{2}} $，故垂直于 x 轴的平面截“该旋转体”所得的截面面积为  $ A(x)=\sqrt{2}\pi\left(\frac{\sqrt{x}-x}{\sqrt{2}}\right)^{2} $。因此，旋转体的体积为

 $$ V=\int_{0}^{1}\sqrt{2}\pi\left(\frac{\sqrt{x}-x}{\sqrt{2}}\right)^{2}\mathrm{d}x=\int_{0}^{1}\frac{\pi}{\sqrt{2}}(x-2x^{\frac{3}{2}}+x^{2})\mathrm{d}x=\frac{\sqrt{2}}{60}\pi. $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_748_461_934_621.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;">图 10-12</div>


注 ①事实上， $ V=\int_{a}^{b}A(x)dx $ 就是  $ V=\int_{a}^{b}\pi f^{2}(x)dx $ 的一般化。

②为什么 $ A(x)=\sqrt{2}\cdot\pi\left(\frac{\sqrt{x}-x}{\sqrt{2}}\right)^{2} $?

设  $ \alpha $ 为曲线  $ y = \sqrt{x} $ 任一点的切线与 x 轴正方向的夹角， $ \beta $ 为直线 y = x 与 x 轴正方向的夹角。

由于此题的对称性，现任一点处  $ \alpha = \beta $，误差抵消，为  $ 0.\left(*\right) $

<div style="text-align: center;"><img src="imgs/img_in_image_box_657_726_924_988.jpg" alt="Image" width="25%" /></div>


如图 10-13 所示，在曲线  $ y=\sqrt{x} $ 上的任一点  $ (x_{i},\sqrt{x_{i}}) $ 处均作平行于 y=x 的直线，则

<div style="text-align: center;">图 10-13</div>


 $$ \Delta u=\sqrt{2}\Delta x,\quad r(x_{i})=[f(x_{i})-x_{i}]\bullet\frac{1}{\sqrt{2}}=\frac{\sqrt{x_{i}}-x_{i}}{\sqrt{2}}, $$ 

 $$ V=\lim_{n\to\infty}\sum_{i=1}^{n}\pi\cdot r^{2}(x_{i})\cdot\Delta u=\lim_{n\to\infty}\sum_{i=1}^{n}\pi\cdot\left(\frac{\sqrt{x_{i}}-x_{i}}{\sqrt{2}}\right)^{2}\cdot\sqrt{2}\Delta x=\int_{0}^{1}\pi\left(\frac{\sqrt{x}-x}{\sqrt{2}}\right)^{2}\cdot\sqrt{2}\mathrm{d}x=\frac{\sqrt{2}}{60}\pi $$ 

事实上，这种处理作了等价变换。

 $ ^{*} $处的解释如图 10-14 所示：