由  $ 1+x^{3}=(1+x)(1-x+x^{2}) $，故当  $ x \neq -1 $ 时，有  $ \frac{1+x^{3}}{1+x}=1-x+x^{2} $

解 应填  $ \sum_{n=1}^{\infty}(-1)^{n-1}\frac{x^{3n}-x^{n}}{n}(-1<x\leqslant1) $.

由于当 $ x\neq-1 $时， $ \ln(1-x+x^{2})=\ln\frac{1+x^{3}}{1+x}=\ln\left|1+x^{3}\right|-\ln\left|1+x\right| $，且

利用对数公式： $ \ln\left|1+x^{3}\right|=\sum_{n=1}^{\infty}(-1)^{n-1}\frac{(x^{3})^{n}}{n}(-1<x^{3}\leq1 $，即 $ -1<x\leq1 $， $ \ln\frac{b}{a}=\ln b-\ln a; $

 $$ \ln a b=\ln a+\ln b $$ 

 $$ \ln\left|1+x\right|=\sum_{n=1}^{\infty}(-1)^{n-1}\frac{x^{n}}{n}(-1<x\leqslant1), $$ 

于是

 $$ \ln(1-x+x^{2})=\sum_{n=1}^{\infty}(-1)^{n-1}\frac{\left(x^{3}\right)^{n}}{n}-\sum_{n=1}^{\infty}(-1)^{n-1}\frac{x^{n}}{n}=\sum_{n=1}^{\infty}(-1)^{n-1}\frac{x^{3n}-x^{n}}{n}(-1<x\leqslant1). $$ 

有的考生可能会把  $ \ln(1-x+x^{2}) $ 中的  $ -x+x^{2} $ 看成一个整体进行展开，这样是不对的，题干的是关于 x 的展开式.

例 16.37 将函数  $ f(x)=\arctan\frac{1+x}{1-x} $ 展开为 x 的幂级数.

☐分析 因为所给函数和我们已知的幂级数相差甚远，无法通过简单恒等变形得到，所以需要想到先积后导或先导后积公式.

 $$ f^{\prime}(x)=\left(\arctan\frac{1+x}{1-x}\right)^{\prime}=\frac{1}{1+\left(\frac{1+x}{1-x}\right)^{2}}\cdot\frac{(1-x)+(1+x)}{(1-x)^{2}}=\frac{(1-x)^{2}}{2(1+x^{2})}\cdot\frac{2}{(1-x)^{2}} $$ 

这个是复合函数求导 x=1 是跳跃间断点

需要记住，它与  $ \arctan x $

的导函数一样

 $$ =\frac{1}{1+x^{2}}=\frac{1}{1-\left(-x^{2}\right)}=\sum_{n=0}^{\infty}\left(-1\right)^{n}x^{2n},\;-1<x<1\quad. $$ 

对 $ f'(x) $逐项积分，下限取在 $ x_{0}=0 $处的变上限积分，得

 $$ \begin{aligned}\int_{0}^{x}f^{\prime}(t)\mathrm{d}t=&\int_{0}^{x}\left[\sum_{n=0}^{\infty}(-1)^{n}t^{2n}\right]\mathrm{d}t=\sum_{n=0}^{\infty}(-1)^{n}\int_{0}^{x}t^{2n}\mathrm{d}t\\=&\sum_{n=0}^{\infty}\frac{(-1)^{n}}{2n+1}x^{2n+1},\ -1<x<1,\end{aligned} $$ 

 $$ f(x)=f(0)+\sum_{n=0}^{\infty}\frac{(-1)^{n}}{2n+1}x^{2n+1}=\frac{\pi}{4}+\sum_{n=0}^{\infty}\frac{(-1)^{n}}{2n+1}x^{2n+1},-1<x<1 $$ 