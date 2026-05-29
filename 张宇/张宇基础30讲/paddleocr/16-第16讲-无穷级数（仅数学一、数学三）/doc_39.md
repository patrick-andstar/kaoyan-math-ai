 $$ \lim_{n\to\infty}\frac{\left|a_{n+1}\right|}{\left|a_{n}\right|}=\lim_{n\to\infty}\frac{n+\frac{1}{2}}{n+1}=1, $$ 

所以幂级数  $ \sum_{n=1}^{\infty}a_{n}x^{n} $ 的收敛半径为 1，从而当  $ |x|<1 $ 时，幂级数  $ \sum_{n=1}^{\infty}a_{n}x^{n} $ 收敛.

当 $ |x|<1 $时，设 $ S(x)=\sum_{n=1}^{\infty}a_{n}x^{n} $，逐项求导得

 $$ \begin{aligned}S^{\prime}(x)&=\sum_{n=1}^{\infty}na_{n}x^{n-1}\\&=1+\sum_{n=1}^{\infty}(n+1)a_{n+1}x^{n}\\&=1+\sum_{n=1}^{\infty}na_{n}x^{n}+\frac{1}{2}\sum_{n=1}^{\infty}a_{n}x^{n}\\&=1+xS^{\prime}(x)+\frac{1}{2}S(x),\end{aligned} $$ 

所以

 $$ S^{\prime}(x)-\frac{1}{2(1-x)}S(x)=\frac{1}{1-x}. $$ 

根据一阶线性微分方程的通解公式得

 $$ S(x)=\mathrm{e}^{\int\frac{\mathrm{d}x}{2(1-x)}\left[\int\mathrm{e}^{-\int\frac{\mathrm{d}x}{2(1-x)}}\cdot\frac{1}{1-x}\mathrm{d}x+C\right]}=\frac{C}{\sqrt{1-x}}-2 $$ 

由题设知  $ S(0)=0 $ ，得 C=2 ，所以  $ S(x)=2\left(\frac{1}{\sqrt{1-x}}-1\right) $， $ |x|<1 $

☑ 方法总结 当幂函数是抽象形式，但给出了递推公式时，可以考虑求导，建立微分方程，该方法也称和函数的微分方程解法。

公式  $ \int\frac{1}{2(1-x)}\mathrm{d}x=-\frac{1}{2}\ln|1-x|+C $

例 16.34 设  $ a_n = \int_0^1 x^n \sqrt{1 - x^2} \, dx $,  $ b_n = \int_0^{\frac{\pi}{2}} \sin^n t \, dt $,  $ n = 1, 2, \cdots $, 计算  $ \sum_{n=1}^{\infty} (-1)^n \frac{a_n}{b_n} $

(分析) 应先考虑对  $ a_{n} $ 这部分求解。因为被积函数中有  $ \sqrt{1-x^{2}} $，考虑三角换元  $ x=\sin t $。此时  $ a_{n}=b_{n}-b_{n+2} $ （将  $ a_{n} $ 与  $ b_{n} $ 联系起来）， $ \frac{a_{n}}{b_{n}}=\frac{b_{n}-b_{n+2}}{b_{n}}=1-\frac{b_{n+2}}{b_{n}} $，根据华里士公式可知  $ \frac{b_{n+2}}{b_{n}}=\frac{n+1}{n+2} $，即  $ \frac{a_{n}}{b_{n}}=\frac{1}{n+2} $，相当于计算  $ \sum_{n=1}^{\infty}(-1)^{n}\cdot\frac{1}{n+2} $，结合  $ \frac{1}{n+2} $ 特点将其转化为  $ \sum_{n=1}^{\infty}(-1)^{n}\frac{x^{n+2}}{n+2}\bigg|_{x=1} $。

 $$ a_{n}\xlongequal{x=\sin t}\int_{0}^{\frac{\pi}{2}}\sin^{n}t\cos^{2}t\mathrm{d}t=\int_{0}^{\frac{\pi}{2}}\sin^{n}t(1-\sin^{2}t)\mathrm{d}t=b_{n}-b_{n+2} $$ 