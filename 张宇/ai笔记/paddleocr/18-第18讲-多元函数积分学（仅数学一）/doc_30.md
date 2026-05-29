(3)对于光滑曲面薄片Σ，若面密度为ρ(x, y, z)，则计算该薄片对x轴、y轴、z轴和原点O的转动惯量 $ I_{x} $， $ I_{y} $， $ I_{z} $和 $ I_{O} $的公式分别为

 $$ I_{x}=\iint\limits_{x}(y^{2}+z^{2})\rho(x,y,z)\mathrm{d}S,\ I_{y}=\iint\limits_{x}(z^{2}+x^{2})\rho(x,y,z)\mathrm{d}S, $$ 

 $$ I_{z}=\iint\limits_{\Sigma}(x^{2}+y^{2})\rho(x,y,z)\mathrm{d}S,\;I_{O}=\iint\limits_{\Sigma}(x^{2}+y^{2}+z^{2})\rho(x,y,z)\mathrm{d}S. $$ 

例 18.14 设薄片形物体  $ \Sigma $ 是圆锥面  $ z = \sqrt{x^2 + y^2} $ 被柱面  $ z^2 = 2x $ 截下的有限部分，其上任一点的密度为  $ \mu(x, y, z) = 9\sqrt{x^2 + y^2 + z^2} $。记圆锥面与柱面的交线为 C。

(1) 求 C 在 xOy 平面上的投影曲线的方程；

(2) 求  $ \Sigma $ 的质量 M .

(1) 联立锥面与柱面，得到交线 C，将其投影到 xOy 面，也就是消去交线中的 z，且让其与 xOy 面（即平面 z=0）联立。

(2)  $ \Sigma $ 的质量  $ M = \iint_{\Sigma} dm = \iint_{\Sigma} \mu dS $. 面密度

解 (1) 如图 18-13 所示，圆锥面与柱面的交线 C 的方程为  $ \begin{cases} z=\sqrt{x^{2}+y^{2}}, \\ z^{2}=2x, \end{cases} $ 消去 z，得 C 在 xOy 平面

的投影柱面为 $ x^{2}+y^{2}=2x $，故所求投影曲线的方程为 $ \left\{\begin{aligned}x^{2}+y^{2}&=2x,\\ z&=0.\end{aligned}\right. $

(2) 因为  $ \Sigma $ 的点密度为  $ \mu(x, y, z) = 9\sqrt{x^{2} + y^{2} + z^{2}} $，所以  $ \Sigma $ 的

<div style="text-align: center;"><img src="imgs/img_in_image_box_751_773_948_929.jpg" alt="Image" width="19%" /></div>


“代”曲面方程 $ z=\sqrt{x^{2}+y^{2}} $  $ M=\iint_{\Sigma}9\sqrt{x^{2}+y^{2}+z^{2}}dS. $  $ \rightarrow $  $ \sqrt{2}dxdy. $ 见例18.12 中注（2）③

<div style="text-align: center;">图 18-13</div>


又Σ在xOy面上的投影区域为 $ D_{xy}=\left\{(x,y)\mid x^{2}+y^{2}\leqslant2x\right\} $，所以

 $$ \begin{aligned}M&=9\iint\limits_{D_{xy}}\sqrt{2(x^{2}+y^{2})}\sqrt{1+\left(\frac{x}{\sqrt{x^{2}+y^{2}}}\right)^{2}+\left(\frac{y}{\sqrt{x^{2}+y^{2}}}\right)^{2}}\mathrm{d}x\mathrm{d}y&\\ &=18\iint\limits_{D_{xy}}\sqrt{x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y=18\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\mathrm{d}\theta\int_{0}^{2\cos\theta}r\bullet r\mathrm{d}r\\ &=48\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\cos^{3}\theta\mathrm{d}\theta=96\int_{0}^{\frac{\pi}{2}}\cos^{3}\theta\mathrm{d}\theta=64.\\ \end{aligned} $$ 