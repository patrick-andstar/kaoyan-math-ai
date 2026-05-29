又  $ S''(1) > 0 $ ，故当 t = 1 时，S 取最小值，此时 l 的方程为  $ y = \frac{x}{2} + \frac{1}{2} $

10.7 解 (1) 由题意得

 $$ V_{1}=\pi\int_{a}^{2}(2x^{2})^{2}\mathrm{d}x=\frac{4}{5}\pi(32-a^{5}), $$ 

 $$ V_{2}=\pi a^{2}\bullet2a^{2}-\pi\int_{0}^{2a^{2}}\frac{y}{2}\mathrm{d}y=\pi a^{4}. $$ 

(2) 由(1)得

 $$ V=V_{1}+V_{2}=\frac{4}{5}\pi(32-a^{5})+\pi a^{4}. $$ 

令

 $$ V^{\prime}=4\pi a^{3}(1-a)=0, $$ 

得区间 $ (0,2) $内唯一的驻点 $ a=1 $，且 $ V''(1)=-4\pi<0 $，因此 $ a=1 $是极大值点，即最大值点，此时

 $$ V_{\mathrm{m a x}}=\frac{129}{5}\pi. $$ 

10.8 解 作平面图形，如图 10-17 所示.

方法一 平面图形绕y轴旋转一周所得旋转体体积为

<div style="text-align: center;"><img src="imgs/img_in_image_box_729_637_951_756.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">图 10-17</div>


 $$ \begin{aligned}V_{_{y}}&=\pi\left[\int_{0}^{2a}x_{2}^{2}(y)\mathrm{d}y-\int_{0}^{2a}x_{1}^{2}(y)\mathrm{d}y\right]^{-1}&\\&=\pi\left[\int_{2\pi}^{\pi}a^{2}\left(t-\sin t\right)^{2}a\sin t\mathrm{d}t-\int_{0}^{\pi}a^{2}\left(t-\sin t\right)^{2}a\sin t\mathrm{d}t\right.\\ &\\&=\pi a^{3}\left[-\int_{\pi}^{2\pi}\left(t-\sin t\right)^{2}\sin t\mathrm{d}t-\int_{0}^{\pi}\left(t-\sin t\right)^{2}\sin t\mathrm{d}t\right]\\ &\\&=-\pi a^{3}\int_{0}^{2\pi}\left(t-\sin t\right)^{2}\sin t\mathrm{d}t,\\ \end{aligned} $$ 

其中

 $$ \int_{0}^{2\pi}(t-\sin t)^{2}\sin t\mathrm{d}t=\int_{0}^{2\pi}(t^{2}\sin t+\sin^{3}t-2t\sin^{2}t)\mathrm{d}t=\int_{0}^{2\pi}t^{2}\sin t\mathrm{d}t-\int_{0}^{2\pi}2t\sin^{2}t\mathrm{d}t. $$ 

因为

 $$ \begin{aligned}\int_{0}^{2\pi}t^{2}\sin t\mathrm{d}t&=-t^{2}\cos t\Big|_{0}^{2\pi}+\int_{0}^{2\pi}2t\cos t\mathrm{d}t\\&=-4\pi^{2}+2t\sin t\Big|_{0}^{2\pi}-\int_{0}^{2\pi}2\sin t\mathrm{d}t=-4\pi^{2},\end{aligned} $$ 

 $$ \begin{aligned}\int_{0}^{2\pi}2t\sin^{2}t\mathrm{d}t&=\int_{0}^{2\pi}2t\frac{1-\cos2t}{2}\mathrm{d}t=\int_{0}^{2\pi}(t-t\cos2t)\mathrm{d}t\\&=\left(\frac{1}{2}t^{2}-\frac{t\sin2t}{2}\right)\Bigg|_{0}^{2\pi}+\int_{0}^{2\pi}\frac{\sin2t}{2}\mathrm{d}t\\&=2\pi^{2}-\frac{\cos2t}{4}\Bigg|_{0}^{2\pi}=2\pi^{2},\end{aligned} $$ 