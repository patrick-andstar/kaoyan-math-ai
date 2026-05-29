注 (1) 这里有一点需要特别强调，将Σ投影到哪个平面上由你自己决定，但是Σ上的任何两点的投影点不能重合，换言之，假如要将Σ投向xOy面，则 $ z=z(x,y) $必须是单值函数。忘记了这一点，就可能算错结果。

如果将  $ \Sigma $ 投向某一平面，但是曲面投影后有重合点，且对称性不能使用时，则

①要么将Σ转投向另一个平面，使得曲面投影后无重合点；

②要么将Σ分成若干曲面Σ₁，Σ₂，…，使得这些曲面各自投影后无重合点。

(2) 曲面拆分方法（即求拆分曲线的方法）：若将Σ投向xOy面时有重合点，取曲面拆分曲线上一点 $ P(x,y,z) $，记该点的切平面的法向量为n，则法向量n与z轴垂直，即法向量n与 $ (0,0,1) $垂直，即可得到拆分曲线的轨迹方程。

<div style="text-align: center;"><img src="imgs/img_in_image_box_698_385_941_529.jpg" alt="Image" width="23%" /></div>


例 18.12 求  $ \iint_{\Sigma} zdS $，其中  $ \Sigma $ 为柱面  $ x^2 + y^2 = R^2 (R > 0) $ 被  $ x = 0, y = 0, z = 0 $ 及  $ z = 1 $ 所截得的第一卦限部分，如图 18-12 所示。

♂分析 投影点不可重合，故可向xOz面投（向左投）.

<div style="text-align: center;"><img src="imgs/img_in_image_box_575_644_668_743.jpg" alt="Image" width="9%" /></div>


解 选择向 xOz 面投影，由曲面方程得

 $ y=\sqrt{R^{2}-x^{2}} $ 写成  $ y=y(x,z) $ 的形成

 $$ \mathrm{d}S=\sqrt{1+\left(y_{x}^{\prime}\right)^{2}+\left(y_{z}^{\prime}\right)^{2}}\mathrm{d}x\mathrm{d}z $$ 

 $$ \begin{aligned}\sqrt{1+\frac{x^{2}}{R^{2}-x^{2}}}&=\sqrt{\frac{R^{2}}{R^{2}-x^{2}}}&=\sqrt{1+\left(\frac{-2x}{2\sqrt{R^{2}-x^{2}}}\right)^{2}+0^{2}}\mathrm{d}x\mathrm{d}z\\ &=\frac{R}{\sqrt{R^{2}-x^{2}}}\mathrm{d}x\mathrm{d}z,\\ \end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_675_759_952_961.jpg" alt="Image" width="26%" /></div>


<div style="text-align: center;">图 18-12</div>


故 $ \iint_{\Sigma}z\mathrm{d}S=\iint_{D_{x}}\frac{Rz}{\sqrt{R^{2}-x^{2}}}\mathrm{d}x\mathrm{d}z $，其中 $ D_{xx}=\left\{(x,z)\mid0\leqslant x\leqslant R,0\leqslant z\leqslant1\right\} $，即

 $$ \iint_{\Sigma}z\mathrm{d}S=R\int_{0}^{R}\mathrm{d}x\int_{0}^{1}\frac{z}{\sqrt{R^{2}-x^{2}}}\mathrm{d}z=\frac{\pi}{4}R\quad.\quad\int_{0}^{R}\frac{1}{\sqrt{R^{2}-x^{2}}}\mathrm{d}x\int_{0}^{1}z\mathrm{d}z=\arcsin\frac{x}{R}\bigg|_{0}^{R}\cdot\frac{1}{2}z^{2}\bigg|_{0}^{1}=\frac{\pi}{2}\cdot\frac{1}{2}=\frac{\pi}{4} $$ 

注 (1) 由于Σ在xOy面上的投影仅为一条曲线，若选择向xOy面投影，则投影区域的面积为0，于是 $ \iint_{\Sigma}z\mathrm{d}S=0 $。这是错误的，因为投影点不能重合。

(2) 以下常考：

①柱面  $ x^{2} + y^{2} = a^{2} $ 的  $ \mathrm{d}S = \frac{a}{\sqrt{a^{2} - x^{2}}} \mathrm{d}x \mathrm{d}z $ 。比如  $ x^{2} + y^{2} = 2 $ ，则  $ \mathrm{d}S = \frac{\sqrt{2}}{\sqrt{2 - x^{2}}} \mathrm{d}x \mathrm{d}z $