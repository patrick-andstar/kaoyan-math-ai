公式  $ \left(\frac{\sin\theta}{\cos\theta+\sin\theta}\right)'=\frac{1}{(\cos\theta+\sin\theta)^2} $

<div style="text-align: center;"><img src="imgs/img_in_image_box_93_286_127_322.jpg" alt="Image" width="3%" /></div>


## 古鲁金第二定理

<div style="text-align: center;"><img src="imgs/img_in_image_box_835_244_938_350.jpg" alt="Image" width="9%" /></div>


如图 14-12 所示，将平面有界闭区域 $D$ 任意分成 $n$ 个小闭区域，$\Delta\sigma_i(i=1,2,\cdots,n)$ 为面积，在 $\Delta\sigma_i$ 中任取一点 $(\xi_i,\eta_i)$，记 $\lambda=\max\{\Delta\sigma_i\}$，则

 $$ \Delta V_{i}=2\pi r_{i}\Delta\sigma_{i}=2\pi\frac{\left|a\xi_{i}+b\eta_{i}+c\right|}{\sqrt{a^{2}+b^{2}}}\Delta\sigma_{i}, $$ 

故

 $$ \begin{aligned}V=&\lim_{\lambda\rightarrow0}\sum_{i=1}^{n}\Delta V_{i}=\lim_{\lambda\rightarrow0}\sum_{i=1}^{n}2\pi\frac{\left|a\xi_{i}+b\eta_{i}+c\right|}{\sqrt{a^{2}+b^{2}}}\Delta\sigma_{i}\\=&\iint\limits_{D}2\pi\frac{\left|ax+by+c\right|}{\sqrt{a^{2}+b^{2}}}\mathrm{d}\sigma\\=&\frac{2\pi}{\sqrt{a^{2}+b^{2}}}\iint\limits_{D}\left|ax+by+c\right|\mathrm{d}\sigma\;.\end{aligned} $$ 

与第 12 讲的公式 (12-5) 比较，得

 $$ r(\overline{x},\overline{y})=\frac{M_{L_{0}}}{M}=\frac{2\pi M_{L_{0}}}{2\pi M}=\frac{V}{2\pi\bullet S}, $$ 

即

 $ V = 2\pi \cdot S \cdot r(\overline{x}, \overline{y}) $

旋转体 平面区域 形心  $ (\overline{x}, \overline{y}) $ 到

的体积 D的面积 旋转轴的距离

<div style="text-align: center;"><img src="imgs/img_in_image_box_407_984_628_1222.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">图 14-12</div>


例 14.16 曲线  $ y = \sin x (0 \leq x \leq 2\pi) $ 与 x 轴所围区域 D 绕直线 y = -x 旋转一周所成的旋转体的体积为 ___.