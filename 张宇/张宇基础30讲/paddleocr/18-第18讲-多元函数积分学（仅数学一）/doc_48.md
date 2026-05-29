☑ 方法总结 计算三重积分时，利用好概念、对称性.

②非封闭曲面，且  $ \mathrm{div}F=\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}\neq0 $ ，补面使其封闭（加面减面）.

例 18.27 计算  $ \iint_{\Sigma} \frac{x \, dy \, dz + (z + 1)^2 \, dx \, dy}{(x^2 + y^2 + z^2)^{\frac{1}{2}}} $，其中  $ \Sigma $ 为下半球面  $ z = -\sqrt{1 - x^2 - y^2} $ 的上侧。

分析 利用第二型曲面积分的替代法，然后补面用高斯公式。



解 先将  $ (x^{2}+y^{2}+z^{2})^{\frac{1}{2}}=1 $ 代入被积函数.

<div style="text-align: center;"><img src="imgs/img_in_image_box_797_363_940_478.jpg" alt="Image" width="13%" /></div>


 $$ I=\iint_{\Sigma}\frac{x\mathrm{d}y\mathrm{d}z+(z+1)^{2}\mathrm{d}x\mathrm{d}y}{\left(x^{2}+y^{2}+z^{2}\right)^{\frac{1}{2}}}=\iint_{\Sigma}x\mathrm{d}y\mathrm{d}z+(z+1)^{2}\mathrm{d}x\mathrm{d}y $$ 

补充一块有向平面  $ \Sigma_{1}:\left\{\begin{aligned}&x^{2}+y^{2}\leqslant1,\\&z=0,\end{aligned}\right. $ 其法向量与 z 轴正向相反，从而得到

 $$ \begin{aligned}I=&\iint\limits_{\Sigma+\Sigma_{1}}x\mathrm{d}y\mathrm{d}z+(z+1)^{2}\mathrm{d}x\mathrm{d}y-\iint\limits_{\Sigma_{1}}x\mathrm{d}y\mathrm{d}z+(z+1)^{2}\mathrm{d}x\mathrm{d}y\\=&-\iiint\limits_{\Omega}(3+2z)\mathrm{d}v+\iint\limits_{D}1\mathrm{d}x\mathrm{d}y,\end{aligned} $$ 

其中  $ \Omega $ 为  $ \Sigma + \Sigma_{1} $ 围成的空间区域，D 为 z = 0 上的平面区域  $ x^{2} + y^{2} \leqslant 1 $，于是

 $$ I=-2\pi-2\iiint\limits_{\Omega}z\mathrm{d}v+\pi=-\pi-2\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{1}r\mathrm{d}r\int_{-\sqrt{1-r^{2}}}^{0}z\mathrm{d}z=-\frac{\pi}{2} $$ 

★③封闭曲面，有奇点在其内部，且除奇点外 div F = 0，可换个面积分 .(边界无须与原曲面重合)

注 为什么可以换个面积分？div F = 0 是指所给场无“源”，于是通过任何封闭曲面（且无奇点在其内部）的通量为 0。如图 18-24 所示，由于  $ \iint\limits_{D} = 0 $，于是  $ \iint\limits_{\Sigma} = -\iint\limits_{\Sigma_1} = \iint\limits_{\Sigma_1} (\Sigma \text{与 } \Sigma_1 \text{ 同向}) $。

<div style="text-align: center;"><img src="imgs/img_in_image_box_783_963_937_1114.jpg" alt="Image" width="14%" /></div>


<div style="text-align: center;">图 18-24</div>


有时虽然所给的曲面是一张封闭曲面，法向量指的也是外侧，但“在Σ所包围的有界闭区域Ω的内部有奇点，但除奇点外P, Q, R具有连续的一阶偏导数，且满足 $ \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} \equiv 0 $”。此时，可以作一封闭曲面 $ \Sigma_1 \subset \Omega $，将上述使偏导数不连续的点都包含在 $ \Sigma_1 $的内部， $ \Sigma_1 $的法向量指向它所包围的有界区域的外侧，则有公式