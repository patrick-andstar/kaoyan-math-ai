所以  $ \iint_{S}|y|dS=\frac{4}{3}\sqrt{3} $，从而原式  $ =\frac{4}{3}\sqrt{3} $

18.7  $ \frac{12}{5}\pi a^{3} $ 解 记  $ \Omega $ 是  $ \Sigma $ 所围的空间区域.

 $$ \begin{aligned}\oint_{\Sigma}\frac{x^{3}\mathrm{d}y\mathrm{d}z+y^{3}\mathrm{d}z\mathrm{d}x+z^{3}\mathrm{d}x\mathrm{d}y}{x^{2}+y^{2}+z^{2}}&=\frac{1}{a^{2}}\oint_{\Sigma}x^{3}\mathrm{d}y\mathrm{d}z+y^{3}\mathrm{d}z\mathrm{d}x+z^{3}\mathrm{d}x\mathrm{d}y=\frac{3}{a^{2}}\iiint_{\Omega}\left(x^{2}+y^{2}+z^{2}\right)\mathrm{d}x\mathrm{d}y\mathrm{d}z\\ &=\frac{3}{a^{2}}\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{\pi}\mathrm{d}\varphi\int_{0}^{a}r^{4}\sin\varphi\mathrm{d}r=\frac{12}{5}\pi a^{3}\end{aligned} $$ 

18.8  $ \frac{2}{3}\pi $ 解 如图 18-28 所示，积分区域  $ \Omega $ 在 xOy 面上的投影是一个圆心在原点的单位圆，所以

 $$ \Omega=\left\{(r,\theta,z)\middle|0\leqslant r\leqslant1,0\leqslant\theta\leqslant2\pi,4r^{2}\leqslant z\leqslant4\right\}\quad. $$ 

于是

 $$ \begin{aligned}\iiint\limits_{\Omega}(x^{2}+y^{2})\mathrm{d}v=&\iiint\limits_{\Omega}r^{2}\bullet r\mathrm{d}r\mathrm{d}\theta\mathrm{d}z=\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{1}r^{2}\bullet r\mathrm{d}r\int_{4r^{2}}^{4}\mathrm{d}z\\=&\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{1}(4r^{3}-4r^{5})\mathrm{d}r=\frac{2}{3}\pi.\end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_750_434_924_618.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">图 18-28</div>


18.9 解 补线，用格林公式.

 $$ \begin{aligned}&I=\oint_{L+\overline{AO}}-\int_{\overline{AO}}=-\iint_{D}\left(-\frac{1}{2}\right)\mathrm{d}x\mathrm{d}y-\int_{\pi}^{0}(\mathrm{e}^{x}+2x)\mathrm{d}x\\ &\\&=\frac{1}{2}\int_{0}^{\pi}\mathrm{d}x\int_{0}^{\sin x}\mathrm{d}y-(\mathrm{e}^{x}+x^{2})\Big|_{\pi}^{0}\\ &\\&=\frac{1}{2}\times2-\left[1-(\mathrm{e}^{\pi}+\pi^{2})\right]=\mathrm{e}^{\pi}+\pi^{2}.\\ \end{aligned} $$ 

18.10 解 以  $ \Sigma_{1} $ 表示法向量指向 z 轴负向的有向平面  $ z = 1(x^{2} + y^{2} \leqslant 1) $，D 为  $ \Sigma_{1} $ 在 xOy 平面上的投影区域，则

 $$ \iint_{\Sigma_{1}}(2x+z)\mathrm{d}y\mathrm{d}z+z\mathrm{d}x\mathrm{d}y=-\iint\limits_{D}\mathrm{d}x\mathrm{d}y=-\pi. $$ 

设  $ \Omega $ 表示由  $ \Sigma $ 和  $ \Sigma_{1} $ 所围成的空间区域，则由高斯公式知

 $$ \begin{aligned}\oint_{\Sigma+\Sigma_{1}}(2x+z)\mathrm{d}y\mathrm{d}z+z\mathrm{d}x\mathrm{d}y&=-\iiint_{\Omega}(2+1)\mathrm{d}v=-3\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{1}r\mathrm{d}r\int_{r^{2}}^{1}\mathrm{d}z\\&=-6\pi\int_{0}^{1}(r-r^{3})\mathrm{d}r=-6\pi\left(\frac{1}{2}-\frac{1}{4}\right)=-\frac{3}{2}\pi.\end{aligned} $$ 

因此， $ \iint_{\Sigma}(2x+z)\mathrm{d}y\mathrm{d}z+z\mathrm{d}x\mathrm{d}y=-\frac{3}{2}\pi-(-\pi)=-\frac{1}{2}\pi $

18.11 (1) 证明 根据高斯公式， $ I = \iiint(1 - x^2 - 4y^2 - z^2) \, dx \, dy \, dz $，其中  $ \Omega $ 为  $ \Sigma $ 所围的空间区域。为