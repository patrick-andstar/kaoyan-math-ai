注 采用对 y 积分，即取微元  $ [y, y + dy] $ 亦可算出 V.

10.3  $ \frac{1}{4}(e^{2}+1) $ 解 以 y 作为参数，则

 $$ \mathrm{d}s=\sqrt{\left(\frac{\mathrm{d}x}{\mathrm{d}y}\right)^{2}+1}\mathrm{d}y=\sqrt{\left(\frac{y}{2}-\frac{1}{2y}\right)^{2}+1}\mathrm{d}y=\frac{1}{2}\left(y+\frac{1}{y}\right)\mathrm{d}y $$ 

故弧长为

 $$ s=\int_{1}^{e}\frac{1}{2}\Bigg(y+\frac{1}{y}\Bigg)\mathrm{d}y=\frac{1}{4}\left(\mathrm{e}^{2}+1\right). $$ 

10.4 6 解 如图 10-16 所示，曲线具有对称性，我们只需计算在第一象限的弧段，即  $ t \in \left[0, \frac{\pi}{2}\right] $

对应部分的弧长.故

 $$ \begin{aligned}&s=4\int_{0}^{\frac{\pi}{2}}\sqrt{\left[x^{\prime}(t)\right]^{2}+\left[y^{\prime}(t)\right]^{2}}\mathrm{d}t\\ &\begin{aligned}\\ &=4\int_{0}^{\frac{\pi}{2}}\sqrt{(-3\cos^{2}t\sin t)^{2}+(3\sin^{2}t\cos t)^{2}}\mathrm{d}t\\&=4\int_{0}^{\frac{\pi}{2}}3|\sin t\cos t|\mathrm{d}t=12\int_{0}^{\frac{\pi}{2}}\sin t\cos t\mathrm{d}t=6.\\ &\end{aligned}\\ \end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_745_526_936_700.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;">图 10-16</div>


10.5  $ \frac{\sqrt{3}+1}{12}\pi $ 解 函数  $ y=f(x) $ 在区间  $ [a,b] $ 上的平均值是指  $ \frac{1}{b-a}\int_{a}^{b}f(x)dx $，故所求的平均值为

 $$ \frac{2}{\sqrt{3}-1}\int_{\frac{1}{2}}^{\frac{\sqrt{3}}{2}}\frac{x^{2}}{\sqrt{1-x^{2}}}\mathrm{d}x $$ 

令 $ x=\sin\theta $，则

 $$ \frac{2}{\sqrt{3}-1}\int_{\frac{\pi}{6}}^{\frac{\pi}{3}}\sin^{2}\theta d\theta=\left.\frac{2}{\sqrt{3}-1}\left(\frac{1}{2}\theta-\frac{1}{4}\sin2\theta\right)\right|_{\frac{\pi}{6}}^{\frac{\pi}{3}}=\frac{\sqrt{3}+1}{12}\pi $$ 

10.6 解 因为  $ y'=\frac{1}{2\sqrt{x}} $ ，所以  $ y=\sqrt{x} $ 在点  $ (t,\sqrt{t}) $ 处的切线 l 的方程为

 $$ y-\sqrt{t}=\frac{1}{2\sqrt{t}}(x-t), 即 y=\frac{1}{2\sqrt{t}}x+\frac{\sqrt{t}}{2}. $$ 

所围面积为

 $$ S(t)=\int_{0}^{2}\left[\left(\frac{1}{2\sqrt{t}}x+\frac{\sqrt{t}}{2}\right)-\sqrt{x}\right]\mathrm{d}x=\frac{1}{\sqrt{t}}+\sqrt{t}-\frac{4\sqrt{2}}{3}. $$ 

令  $ S'(t) = -\frac{1}{2}t^{-\frac{3}{2}} + \frac{1}{2}t^{-\frac{1}{2}} = 0 $，得 t = 1。