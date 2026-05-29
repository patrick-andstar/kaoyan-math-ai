 $$ m\leqslant f(x_{n})\leqslant M, $$ 

 $$ m\leqslant\frac{f(x_{1})+\cdots+f(x_{n})}{n}\leqslant M, $$ 

则存在  $ \xi \in [x_1, x_n] \subset [a, b] $ 使得  $ f(\xi) = \frac{f(x_1) + \cdots + f(x_n)}{n} $

定理 4(零点定理) 当  $ f(a) \cdot f(b) < 0 $ 时，存在  $ \xi \in (a, b) $，使得  $ f(\xi) = 0 $

a, b为无定义点，可直接用

<div style="text-align: center;"><img src="imgs/img_in_image_box_442_446_802_604.jpg" alt="Image" width="34%" /></div>


推广的零点定理：若  $ f(x) $ 在  $ (a, b) $ 内连续， $ \lim_{x \to a^+} f(x) = \alpha, \lim_{x \to b^+} f(x) = \beta $，且  $ \alpha \cdot \beta < 0 $，则  $ f(x) = 0 $ 在  $ (a, b) $ 内至少有一个根，这里  $ a, b, \alpha, \beta $ 可以是有限数，也可以是无穷大。

例 6.1 设函数  $ f(x) $ 在  $ [0,1] $ 上连续，且  $ f(1)=0 $， $ f\left(\frac{1}{2}\right)=1 $，证明：存在  $ \eta \in \left(\frac{1}{2}, 1\right) $，使得  $ f(\eta)=\eta $。

♡分析 涉及关系式，“做一至两步的逆运算”只需证“ $ f(\eta)-\eta=0 $”.

证 令  $ F(x)=f(x)-x $ ，则函数  $ F(x)=f(x)-x $ 在  $ \left[\frac{1}{2},1\right] $ 上连续，且有

 $ F\left(\frac{1}{2}\right)=f\left(\frac{1}{2}\right)-\frac{1}{2}=\frac{1}{2}>\underline{0},\quad F(1)=f(1)-1=-1<\underline{0}, $ 端点值异号

由于  $ F\left(\frac{1}{2}\right)\cdot F(1)<0 $，根据零点定理可知，存在  $ \eta\in\left(\frac{1}{2},1\right) $，使得  $ F(\eta)=0 $，即  $ f(\eta)=\eta $。

例 6.2 设函数  $ f(x) $ 在区间  $ [0,1] $ 上连续，且  $ f(1)>0 $， $ \lim_{x\to0^{+}}\frac{f(x)}{x}<0 $ 。证明：方程  $ f(x)=0 $ 在区间  $ (0,1) $ 内至少存在一个实根。一般作为解答题的第一问极限必须存在，才可和“0”比大小

证 由  $ \lim_{x\to0^{+}}\frac{f(x)}{x}<0 $ 与极限的保号性可知，存在  $ a\in(0,1) $，使得  $ \frac{f(a)}{a}<0 $，即  $ f(a)<0 $。

又 $ f(1)>0 $，所以存在 $ b\in(a,1)\subset(0,1) $，使得 $ f(b)=0 $，即方程 $ f(x)=0 $在区间 $ (0,1) $内至少存在一个实根。