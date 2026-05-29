abc = ___.

分析  $ \int_{a}^{b}f(x,t)\mathrm{d}t=F(x) $ 不是一个定积分，而是一个函数.

<div style="text-align: center;"><img src="imgs/img_in_image_box_432_228_611_329.jpg" alt="Image" width="17%" /></div>


解 应填 $ -\frac{\pi}{2} $

去掉绝对值 $ \Rightarrow $求 $ F(x)\Rightarrow $泰勒公式 $ \left\{\begin{array}{l} 直接展开 (定义法) \\ 利用已有展开式 (公式法) \end{array}\right. $

当 $ x\to0^{+} $时，

 $$ \begin{aligned}F(x)&=\int_{0}^{x}(\sin x-\sin t)\mathrm{d}t+\int_{x}^{\frac{\pi}{2}}(\sin t-\sin x)\mathrm{d}t\\&=x\sin x+(\cos x-1)+\cos x-\sin x\bullet\left(\frac{\pi}{2}-x\right)\\&=\left(2x-\frac{\pi}{2}\right)\sin x+2\cos x-1\end{aligned} $$ 

方法一 直接展开.

 $$ \sin x=x+o(x^{2}), $$ 

 $$ \cos x=1-\frac{1}{2}x^{2}+o(x^{2}), $$ 

 $$ \begin{aligned}F(x)=&\left(2x-\frac{\pi}{2}\right)[x+o(x^{2})]+2\left[1-\frac{1}{2}x^{2}+o(x^{2})\right]-1\\=&1-\frac{\pi}{2}x+x^{2}+o(x^{2}),\end{aligned} $$ 

因此  $ a=1,\quad b=-\frac{\pi}{2},\quad c=1 $ ，故  $ abc=-\frac{\pi}{2} $

方法二 由  $ F'(x)=2\sin x+\left(2x-\frac{\pi}{2}\right)\cos x-2\sin x=\left(2x-\frac{\pi}{2}\right)\cos x $

 $$ F^{\prime \prime}(x)=2\cos x-\left(2x-\frac{\pi}{2}\right)\sin x $$ 

故

 $$ F(0)=1,\;F_{+}^{\prime}(0)=-\frac{\pi}{2},\;F_{+}^{\prime \prime}(0)=2\;, $$ 

 $$ \begin{aligned}F(x)&=F(0)+F_{+}^{\prime}(0)x+\frac{F_{+}^{\prime \prime}(0)}{2!}x^{2}+\cdots\\&=1-\frac{\pi}{2}x+x^{2}+\cdots,\end{aligned} $$ 

即 a=1,  $ b=-\frac{\pi}{2} $, c=1 ，故  $ abc=-\frac{\pi}{2} $

例 9.22 设函数  $ f(x) $ 可导，且  $ f(x) < -2xf'(x) $，则曲线  $ F(x) = \int_0^x tf(x^2 - t^2) dt $（）.

(A) 在 x = 0 处取极大值

(B) 在 x=0 处取极小值