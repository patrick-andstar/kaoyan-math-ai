## 微分不等式

## 用函数性态（包括单调性、凹凸性和最值等）证明不等式

一般地，使用如下依据。

(1)若有 $ f'(x)\geq0 $, $ a<x<b $，则有 $ f(a)\leq f(x)\leq f(b) $.

★(2)若有 $ f''(x)\geq0 $, $ a<x<b $，则有 $ f'(a)\leq f'(x)\leq f'(b) $.

①当 $ f'(a)>0 $时， $ f'(x)>0 $，则 $ f(x) $单调增加；

②当 $ f'(b)<0 $时， $ f'(x)<0 $，则 $ f(x) $单调减少.

★(3)设 $ f(x) $在I内连续，且有唯一的极值点 $ x_{0} $，则 $ \left\{\begin{aligned}& 当x_{0}为极大值点时，即为I内的最大值点，有 \\& f(x_{0})\geq f(x),\\& 当x_{0}为极小值点时，即为I内的最小值点，有 \\& f(x_{0})\leq f(x),\end{aligned}\right. $

其中 $ x\in I $

★(4)若有 $ f''(x)>0 $, $ a<x<b $, $ f(a)=f(b)=0 $,则有 $ f(x)<0 $.

例6.19 证明当  $ 0 < x < \frac{\pi}{2} $ 时，有  $ \sin x > \frac{2x}{\pi} \cdot \frac{2x}{\pi} < \sin x < x $

证 方法一 若证  $ \sin x > \frac{2x}{\pi} $，即需证  $ \frac{\sin x}{x} > \frac{2}{\pi} $，令  $ f(x) = \frac{\sin x}{x} $， $ x \in \left(0, \frac{\pi}{2}\right) $，则主流方法：单调性



<div style="text-align: center;"><img src="imgs/img_in_image_box_702_753_863_865.jpg" alt="Image" width="15%" /></div>


 $ f'(x)=\frac{x\cos x-\sin x}{x^{2}} $ 一定不出正负，继续求导

分母大于0，只需研究分子

令  $ \underline{g(x)=x\cos x-\sin x} $， $ x\in\left(0,\frac{\pi}{2}\right) $，得  $ g'(x)=-x\sin x<0 $，则  $ g(x) $ 单调递减， $ g(x)<g(0)=0 $，所以在  $ \left(0,\frac{\pi}{2}\right) $ 上  $ f'(x)<0 $， $ f(x) $ 单调递减， $ f(x)>f\left(\frac{\pi}{2}\right)=\frac{2}{\pi} $，即

 $$ \sin x>\frac{2x}{\pi},\;x\in\left(0,\;\frac{\pi}{2}\right). $$ 

方法二 设  $ f(x)=\sin x-\frac{2x}{\pi} $， $ x\in\left(0,\frac{\pi}{2}\right) $，则

 $$ f^{\prime}(x)=\cos x-\frac{2}{\pi},f^{\prime \prime}(x)=-\sin x<0, $$ 