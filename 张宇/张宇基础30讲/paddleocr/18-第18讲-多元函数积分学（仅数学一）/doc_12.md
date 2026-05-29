 $$ \begin{aligned}\iint\limits_{D_{\alpha}}\mathrm{d}\sigma\int_{0}^{1-x-y}\overbrace{z\mathrm{d}z}^{}\underbrace{\iiint\limits_{D}\mathrm{d}v=\iint\limits_{D_{\alpha}}\left(\int_{0}^{1-x-y}z\mathrm{d}z\right)}_{\alpha}\mathrm{d}x\mathrm{d}y&=\iint\limits_{D_{\alpha}}\frac{1}{2}(1-x-y)^{2}\mathrm{d}x\mathrm{d}y\\&=\frac{1}{2}\int_{0}^{1}\mathrm{d}x\int_{0}^{1-x}(1-x-y)^{2}\mathrm{d}y\\&=\frac{1}{2}\int_{0}^{1}\left[-\frac{1}{3}(1-x-y)^{3}\bigg|_{y=0}^{y=1-x}\right]\mathrm{d}x\\&=\frac{1}{6}\int_{0}^{1}(1-x)^{3}\mathrm{d}x=\frac{1}{24},\end{aligned} $$ 

因此 $ I=6\times\frac{1}{24}=\frac{1}{4} $

(2)柱面坐标系 = 极坐标系下二重积分与定积分.

在直角坐标系的计算中，如若  $ \iint_{D_{xy}} d\sigma $ 适用于极坐标系，则令  $ \begin{cases} x = r \cos \theta, \\ y = r \sin \theta, \end{cases} $ 便有

 $$ \iiint\limits_{\Omega}f(x,y,z)\mathrm{d}x\mathrm{d}y\mathrm{d}z=\iiint\limits_{\Omega}f(r\cos\theta,r\sin\theta,z)r\mathrm{d}r\mathrm{d}\theta\mathrm{d}z, $$ 

此种计算方法称为柱面坐标系下三重积分的计算.

例 18.2 设  $ \Omega $ 是由圆柱面  $ x^{2} + (y - 1)^{2} = 1 $，旋转抛物面  $ 8z = x^{2} + y^{2} $ 以及平面 z = 0 所围成的区

域，则 $ I=\iiint_{\Omega}\sqrt{x^{2}+y^{2}}\,\mathrm{d}v= $

解 应填 $ \frac{64}{75} $

如图 18-7 所示，用先一后二法（投影穿线法），即

<div style="text-align: center;"><img src="imgs/img_in_image_box_630_818_923_993.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;">图 18-7</div>


 $$ I=\iint\limits_{D_{xy}}\mathrm{d}\sigma\int_{0}^{\frac{x^{2}+y^{2}}{8}}\sqrt{x^{2}+y^{2}}\mathrm{d}z $$ 

 $$ \begin{aligned} 柱面坐标法 \quad&\begin{aligned}=\int_{0}^{\pi}\mathrm{d}\theta\int_{0}^{2\sin\theta}r\mathrm{d}r\int_{0}^{\frac{\pi}{8}}r\mathrm{d}z=\frac{1}{8}\int_{0}^{\pi}\mathrm{d}\theta\int_{0}^{2\sin\theta}r^{4}\mathrm{d}r\end{aligned}\Rightarrow\frac{1}{8}\iint_{D_{0}}\sqrt{x^{2}+y^{2}}\cdot(x^{2}+y^{2})\mathrm{d}\sigma\\&=\frac{4}{5}\int_{0}^{\pi}\sin^{5}\theta\mathrm{d}\theta=\frac{4}{5}\left(2\times\frac{4}{5}\times\frac{2}{3}\right)=\frac{64}{75}\cdot\\&\begin{aligned}&=\frac{1}{40}\cdot2^{5}\int_{0}^{\pi}\sin^{5}\theta\mathrm{d}\theta=\frac{64}{75}.\end{aligned}\end{aligned} $$ 

(3) 球面坐标系.

①适用场合.

<div style="text-align: center;"><img src="imgs/img_in_image_box_639_1191_860_1270.jpg" alt="Image" width="21%" /></div>


a. 被积函数中含  $ \begin{cases} f(x^{2} + y^{2} + z^{2}), \\ f(x^{2} + y^{2}). \end{cases} $