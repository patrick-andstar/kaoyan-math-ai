解 应填  $ 4\sqrt{2}\pi^{2} $

由古鲁金第二定理，有

 $$ \begin{aligned}V&=2\pi\bullet\underline{\underline{S}}\bullet\underline{\underline{r(\bar{x},\ \bar{y})}}\\&=2\pi\bullet4\bullet\frac{\pi}{\sqrt{2}}=4\sqrt{2}\pi^{2}.\end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_773_149_964_288.jpg" alt="Image" width="18%" /></div>


例 14.17 设  $ D $ 为  $ (x-1)^2 + y^2 = 1 $ 与  $ (x-2)^2 + y^2 = 2^2 $ 及  $ x $ 轴所围区域在第一象限的部分，则  $ D $ 的形心  $ (\bar{x}, \bar{y}) = $ ___。

解 应填 $ \left(\frac{7}{3},\frac{28}{9\pi}\right) $

<div style="text-align: center;"><img src="imgs/img_in_image_box_790_374_963_485.jpg" alt="Image" width="16%" /></div>


D 绕 y 轴旋转一周所成的旋转体的体积

 $$ V=2\pi\cdot\frac{\pi\cdot2^{2}}{2}\cdot2-2\pi\cdot\frac{\pi\cdot1^{2}}{2}\cdot1=7\pi^{2} $$ 

故 D 的形心到 y 轴的距离为  $ r(\overline{x}, \overline{y}) = \frac{V}{2\pi S} = \frac{7\pi^{2}}{2\pi(\pi \cdot 2^{2} - \pi \cdot 1^{2}) \cdot \frac{1}{2}} = \frac{7}{3} $.

显然，即  $ \bar{x} = \frac{7}{3} $ 。同理可求得  $ \bar{y} = \frac{28}{9\pi} $

注  $ \overline{y} $ 的求解较  $ \overline{x} $ 稍微复杂一些，要先求出半圆域  $ (x-1)^{2} + y^{2} \leqslant 1 (y \geqslant 0) $ 与半圆域  $ (x-2)^{2} + y^{2} \leqslant 2^{2} (y \geqslant 0) $ 的形心竖坐标  $ \overline{y}_{1}, \overline{y}_{2} $.

由  $ \overline{y}_{1}=\frac{\iint y\mathrm{d}\sigma}{\iint\mathrm{d}\sigma}=\frac{\int_{0}^{\frac{\pi}{2}}\mathrm{d}\theta\int_{0}^{2\cos\theta}r\sin\theta\cdot r\mathrm{d}r}{\pi\cdot1^{2}\cdot\frac{1}{2}}=\frac{4}{3\pi} $，得  $ \overline{y}_{1}=\frac{4}{3\pi} $，同理可得  $ \overline{y}_{2}=\frac{8}{3\pi} $，则 D 绕 x 轴旋转一周所成的旋转体的体积

 $$ V_{x}=2\pi\cdot\frac{\pi\cdot2^{2}}{2}\cdot\frac{8}{3\pi}-2\pi\cdot\frac{\pi\cdot1^{2}}{2}\cdot\frac{4}{3\pi}=\frac{28\pi}{3} $$ 

故 D 的形心到 x 轴的距离为

 $$ r(\overline{x},\overline{y})=\frac{V_{_{x}}}{2\pi S}=\frac{\frac{28\pi}{3}}{2\pi(\pi\cdot2^{2}-\pi\cdot1^{2})\cdot\frac{1}{2}}=\frac{28}{9\pi}, $$ 

即  $ \overline{y}=\frac{28}{9\pi} $