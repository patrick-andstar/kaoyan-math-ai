因为  $ \lim_{x\to+\infty}\frac{g(x)}{f(x)} = +\infty $， $ \lim_{x\to+\infty}\frac{h(x)}{g(x)} = +\infty $，所以当 x 充分大时，有  $ f(x) < g(x) < h(x) $。

故选项 (C) 正确。

注 ①当 $ x \to +\infty $时，有 $ \ln^{\alpha} x \ll x^{\beta} \ll a^{x} $，其中 $ \alpha, \beta > 0, a > 1 $，符号“ $ \ll $”叫远远小于；②当 $ n \to \infty $时，有 $ \ln^{\alpha} n \ll n^{\beta} \ll a^{n} \ll n! \ll n^{n} $，其中 $ \alpha, \beta > 0, a > 1 $。记住，考试时直接用

像上面这些公式必须要记住 . 在微积分中，有一个很要紧的问题，就是趋于零的函数，谁快谁慢，趋于无穷大的函数，谁快谁慢，这些问题解决好了，很多难题就迎刃而解 . 知识是有连续性的，它总是一环扣一环，其他方向如果欠缺，可能是因为这里的题目就掌握得不是太好 .

(3) 泰勒公式.

设 $ f(x) $在点x=0处n阶可导，则存在x=0的一个邻域，对于该邻域内的任一点x，有

<div style="text-align: center;"><img src="imgs/img_in_image_box_789_464_902_599.jpg" alt="Image" width="10%" /></div>


 $$ f(x)=f(0)+f^{\prime}(0)x+\frac{f^{\prime \prime}(0)}{2!}x^{2}+\cdots+\frac{f^{(n)}(0)}{n!}x^{n}+o(x^{n}). $$ 

泰勒（1685—1731）

牛顿学生（英国教育家）

泰勒公式背后的思想比拉格朗日中值定理的思想更精确。泰勒有一个非常直接的观点，就是可以用多项式（表达式最简单的）来表达任何一个函数（当然这个函数可导性要好）。

泰勒有一双火眼金睛，一眼看穿所有函数.

如  $ \sin x = \sin 0 + (\sin x)^{\prime}\big|_{x=0} \cdot x + \frac{(\sin x)^{\prime\prime}|_{x=0}}{2!} x^2 + \frac{(\sin x)^{\prime\prime\prime}|_{x=0}}{3!} x^3 + o(x^3) $，即  $ \sin x = \boxed{x - \frac{1}{6} x^3} + \boxed{o(x^3)} \cdot \boxed{x} $

再如  $ \sec x = \sec 0 + (\sec x)^{\prime}\big|_{x=0} \cdot x + \frac{(\sec x)^{\prime\prime}|_{x=0}}{2!} x^2 + \frac{(\sec x)^{\prime\prime\prime}|_{x=0}}{3!} x^3 + o(x^3) $，即  $ \sec x = 1 + \frac{x^2}{2} + o(x^3) $。

下面给同学们看个真题。

当  $ x \to 0 $ 时， $ \sec x $ 与 2 次泰勒多项式  $ g(x) $ 之差为  $ o(x^2) $，则  $ g(x) = 1 + \frac{1}{2} x^2 $。

另： $ \sec x $ 在  $ x = 0 $ 处的 2 次泰勒多项式为  $ \frac{1 + \frac{1}{2} x^2}{2} $。

同理可得如下重要函数的泰勒公式.

 $$ \sin x=x-\frac{x^{3}}{3!}+o(x^{3}), $$ 

 $$ \cos x=1-\frac{x^{2}}{2!}+\frac{x^{4}}{4!}+o(x^{4}), $$ 

 $$ \arcsin x=x+\frac{x^{3}}{3!}+o(x^{3}),\qquad\tan x=x+\frac{x^{3}}{3}+o(x^{3}), $$ 

 $$ \arctan x=x-\frac{x^{3}}{3}+o(x^{3}),\qquad\ln(1+x)=x-\frac{x^{2}}{2}+\frac{x^{3}}{3}+o(x^{3}), $$ 

8个都要“背”，泰勒公式熟记于心，都要“一站直达”

 $$ \mathrm{e}^{x}=1+x+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+o(x^{3}),\quad(1+x)^{\alpha}=1+\alpha x+\frac{\alpha(\alpha-1)}{2!}x^{2}+o(x^{2}). $$ 