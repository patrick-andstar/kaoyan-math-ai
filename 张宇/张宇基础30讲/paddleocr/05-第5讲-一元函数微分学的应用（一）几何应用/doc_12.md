 $$ \begin{aligned}f^{\prime}(x)&=2(x-1)(x-3)^{3}+3(x-1)^{2}(x-3)^{2}\\&=(x-1)(x-3)^{2}(5x-9),\end{aligned} $$ 

易知 $ f''(x) $中必含一次因式 $ x-3 $。另由 $ f'(1)=f'\left(\frac{9}{5}\right)=f'(3)=0 $，知必存在 $ x_1\in\left(1,\frac{9}{5}\right) $， $ x_2\in\left(\frac{9}{5},3\right) $，使得 $ f''(x_1)=f''(x_2)=0 $，故可令

 $$ f^{\prime \prime}(x)=k(x-x_{1})(x-x_{2})(x-3), $$ 

其中 k 是不为 0 的常数. 由于  $ f''(x) $ 在  $ x = x_{1}, x = x_{2}, x = 3 $ 两侧都异号，因此该曲线共有 3 个拐点.

(2) 曲线  $ y=(x-1)^{2}(x-3)^{2} $ 的极值点个数与拐点个数分别为（）.

(A) 3, 2          (B) 2, 3          (C) 3, 4          (D) 4, 3

## 解 应选(A)

由 “五、③” 可知， $ k_{1}=0, k_{2}=2, k_{3}=0 $，于是极值点个数为  $ 0+2\times2+0-1=3 $，拐点个数为  $ 0+2\times2+3\times0-2=2 $。可直接得出答案。

当曲线上的点远离原点时，曲线与某直线充分靠近，则称该直线为曲线的渐近线。

<div style="text-align: center;"><img src="imgs/img_in_image_box_847_707_952_815.jpg" alt="Image" width="10%" /></div>


## 铅直渐近线

若  $ \lim_{x\to x_0^+}f(x)=\infty $ （或  $ \lim_{x\to x_0^-}f(x)=\infty $），则  $ x=x_0 $ 为一条铅直渐近线.

注 此处的 $ x_{0} $或是函数的无定义点，或是函数定义区间的端点，或是分段函数的分段点。

例： $ y=\tan x $ 在  $ x=\frac{\pi}{2} $ 处 ② ② ③ 1,  $ x\geq0 $, ② 1,  $ x\geq0 $, ③ 1,  $ x<0 $ 在 x=0 处 1,  $ x<0 $

## 2 水平渐近线

<div style="text-align: center;"><img src="imgs/img_in_image_box_725_1097_897_1155.jpg" alt="Image" width="16%" /></div>


若  $ \lim_{x\to+\infty}f(x)=y_1 $，则  $ y=y_1 $ 为一条水平渐近线；若  $ \lim_{x\to-\infty}f(x)=y_2 $，则  $ y=y_2 $ 为一条水平渐近线；若  $ \lim_{x\to+\infty}f(x)=\lim_{x\to-\infty}f(x)=y_0 $，则  $ y=y_0 $ 为一条水平渐近线。

注  $ x \to +\infty $ 与  $ x \to -\infty $ 时的水平渐近线可能相同，如  $ y = e^{-|x|} $；也可能不同，如  $ y = \arctan x $