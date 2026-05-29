 $$ \begin{aligned}&=\frac{1}{2}x(x-1)f^{\prime}(x)\bigg|_{0}^{1}-\frac{1}{2}\int_{0}^{1}f^{\prime}(x)\widehat{2x-1}\mathrm{d}x\\&=-\frac{1}{2}\int_{0}^{1}(2x-1)\mathrm{d}\left[f(x)\right]\\&=-\frac{1}{2}(2x-1)f(x)\bigg|_{0}^{1}+\int_{0}^{1}f(x)\mathrm{d}x\ ,\end{aligned} $$ 

由条件 $ f(0)=f(1)=0 $，知结论成立.

(2) 记  $ M = \max_{0 \leq x \leq 1} \left\{ \left| f''(x) \right| \right\} $，则由 (1) 有

 $$ \left|\int_{0}^{1}f(x)\mathrm{d}x\right|=\frac{1}{2}\left|\int_{0}^{1}x(x-1)f^{\prime \prime}(x)\mathrm{d}x\right|\leqslant\frac{1}{2}\int_{0}^{1}\left|x(x-1)\right|\left|f^{\prime \prime}(x)\right|\mathrm{d}x\leqslant\frac{M}{2}\int_{0}^{1}x(1-x)\mathrm{d}x=\frac{M}{2}\left(\frac{1}{2}-\frac{1}{3}\right)=\frac{M}{12} $$ 

得证.

<div style="text-align: center;"><img src="imgs/img_in_image_box_93_620_126_655.jpg" alt="Image" width="3%" /></div>


## 积分不等式

<div style="text-align: center;"><img src="imgs/img_in_image_box_843_591_948_698.jpg" alt="Image" width="10%" /></div>


## 用函数的单调性

通常的做法：首先将某一积分限（通常取上限）变量化，然后移项构造辅助函数，由辅助函数的单调性来证明不等式，此方法多用于所给条件为“ $ f(x) $在 $ [a,b] $上连续”的情形．

★★★例 11.7 设函数 $ f(x) $， $ g(x) $在区间 $ [a, b] $上连续，且 $ f(x) $单调增加， $ 0 \leq g(x) \leq 1 $。证明：

(1)  $ 0 \leqslant \int_{a}^{x} g(t) \, dt \leqslant x - a $,  $ x \in [a, b] $;

(2)  $ \int_{a}^{a+\int_{a}^{b}g(t)\mathrm{d}t} f(x)\mathrm{d}x \leqslant \int_{a}^{b} f(x)g(x)\mathrm{d}x $.

(1) 中，因为  $ a \leqslant x $，所以  $ \int_{a}^{x} g(t) dt $ 是正向的积分，可直接用积分的保号性；

(2) 中，该题是考研以来上限较复杂的定积分，做题时要注意形式的复杂性。

证 (1) 因为  $ 0 \leqslant g(x) \leqslant 1 $，所以当  $ x \in [a, b] $ 时，有  $ \int_{a}^{x} 0 \, dt \leqslant \int_{a}^{x} g(t) \, dt \leqslant \int_{a}^{x} 1 \, dt $，即

 $$ 0\leqslant\int_{a}^{x}g(t)\mathrm{d}t\leqslant x-a\enspace. $$ 

(2) 令  $  F(x) = \int_{a}^{a + \int_{a}^{x} g(u) \, du} f(t) \, dt - \int_{a}^{x} f(t) g(t) \, dt  $,  $  x \in [a, b]  $.

三个变量要区分开

因为 $ f(x) $， $ g(x) $在区间 $ [a,b] $上连续，所以 $ F(x) $在区间 $ [a,b] $上可导，且

 $$ F^{\prime}(x)=f\Biggl[a+\int_{a}^{x}g(u)\mathrm{d}u\Biggr]g(x)-f(x)g(x)=\Biggl\{f\Biggl[a+\int_{a}^{x}g(u)\mathrm{d}u\Biggr]-f(x)\Biggr\}g(x). $$ 