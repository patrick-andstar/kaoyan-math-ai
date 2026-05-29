于是 $ F'(t)=(t-1)f(t) $.

14.7  $ -\pi $ 解 所给积分区域如图 14-15 所示.

记 $ A\left(-\frac{\pi}{2},-1\right) $， $ B\left(-\frac{\pi}{2},1\right) $， $ C\left(\frac{\pi}{2},1\right) $。作辅助线 $ y=-\sin x $，则曲线BO将区域D划分为 $ D_{1} $， $ D_{2} $两个子区域，区域 $ D_{1} $关于x轴对称，区域 $ D_{2} $关于y轴对称。而 $ xy^{5} $既为x的奇函数，也为y的奇函数，从而 $ \iint_{D_{1}}xy^{5}dxdy=0 $， $ \iint_{D_{2}}xy^{5}dxdy=0 $，因此

<div style="text-align: center;"><img src="imgs/img_in_image_box_655_130_931_368.jpg" alt="Image" width="26%" /></div>


<div style="text-align: center;">图 14-15</div>


 $$ \begin{aligned} 原式 &=-\iint\limits_{D}\mathrm{d}x\mathrm{d}y=-\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\mathrm{d}x\int_{\sin x}^{1}\mathrm{d}y\\&=-\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}(1-\sin x)\mathrm{d}x=-2\int_{0}^{\frac{\pi}{2}}\mathrm{d}x=-\pi\end{aligned} $$ 

14.8 解 因为  $ I_{1}=\iint_{D}\frac{1}{1+x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\mathrm{d}\theta\int_{0}^{1}\frac{1}{1+r^{2}}r\mathrm{d}r=\frac{\pi}{2}\ln(1+r^{2})\bigg|_{0}^{1}=\frac{\pi}{2}\ln2 $

 $$ I_{2}=\iint\frac{xy}{1+x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\mathrm{d}\theta\int_{0}^{1}\frac{r^{3}\cos\theta\sin\theta}{1+r^{2}}\mathrm{d}r=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\cos\theta\sin\theta\mathrm{d}\theta\int_{0}^{1}\frac{r^{3}}{1+r^{2}}\mathrm{d}r=0, $$ 

所以

 $$ I=I_{1}+I_{2}=\frac{\pi}{2}\ln2\quad. $$ 

14.9 解 设  $ D_{1}=\left\{(x,y)|0\leqslant x\leqslant1,0\leqslant y\leqslant x\right\} $， $ D_{2}=\left\{(x,y)|0\leqslant x\leqslant1,x\leqslant y\leqslant1\right\} $，则

 $$ \begin{aligned}\iint\limits_{D}\mathbf{e}^{\max\{x^{2},y^{2}\}}\mathrm{d}x\mathrm{d}y&=\iint\limits_{D_{1}}\mathbf{e}^{\max\{x^{2},y^{2}\}}\mathrm{d}x\mathrm{d}y+\iint\limits_{D_{2}}\mathbf{e}^{\max\{x^{2},y^{2}\}}\mathrm{d}x\mathrm{d}y=\iint\limits_{D_{1}}\mathbf{e}^{x^{2}}\mathrm{d}x\mathrm{d}y+\iint\limits_{D_{2}}\mathbf{e}^{y^{2}}\mathrm{d}x\mathrm{d}y\\&=\int_{0}^{1}\mathrm{d}x\int_{0}^{x}\mathbf{e}^{x^{2}}\mathrm{d}y+\int_{0}^{1}\mathrm{d}y\int_{0}^{y}\mathbf{e}^{y^{2}}\mathrm{d}x=\int_{0}^{1}x\mathbf{e}^{x^{2}}\mathrm{d}x+\int_{0}^{1}y\mathbf{e}^{y^{2}}\mathrm{d}y=\mathbf{e}-1\quad.\end{aligned} $$ 

14.10 解 先画出积分区域 D（见图 14-16），然后将积分化为直角坐标系下的二重积分，再去计算，即

 $$ \begin{aligned}I=&\iint_{D}r^{2}\sin\theta\sqrt{1-r^{2}}\cos^{2}\theta+r^{2}\sin^{2}\theta\mathrm{d}r\mathrm{d}\theta=\iint_{D}y\sqrt{1-x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y\\=&\frac{1}{2}\int_{0}^{1}\mathrm{d}x\int_{0}^{x}\sqrt{1-x^{2}+y^{2}}\mathrm{d}(1-x^{2}+y^{2})=\frac{1}{3}\int_{0}^{1}(1-x^{2}+y^{2})^{\frac{3}{2}}\bigg|_{0}^{x}\mathrm{d}x\\=&\frac{1}{3}\int_{0}^{1}\left[1-(1-x^{2})^{\frac{3}{2}}\right]\mathrm{d}x.&r=\sec\theta, 即 r=\frac{1}{\cos\theta},\\& 也即 r\cos\theta=1, 得 x=1\end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_763_1115_940_1248.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">图 14-16</div>


设  $ x = \sin t $，则  $ I = \frac{1}{3} - \frac{1}{3} \int_{0}^{\frac{\pi}{2}} \cos^{4} t \, dt = \frac{1}{3} - \frac{1}{3} \times \frac{3}{4} \times \frac{1}{2} \times \frac{\pi}{2} = \frac{1}{3} - \frac{\pi}{16} $.