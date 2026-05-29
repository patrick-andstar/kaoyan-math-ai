 $ u_{n}=(-1)^{n-1} $; 对于命题④, 令  $ u_{n}=(-1)^{n-1} $,  $ v_{n}=(-1)^{n} $.

由级数去掉前面有限项，不改变级数收敛性的性质，可知命题②正确。

若级数满足  $ \lim_{n\to\infty}\frac{u_{n+1}}{u_n} $ 存在且大于 1，则级数发散，可知命题③正确.

综上可知，应选(B).

16.2 (B) 解 因为级数  $ \sum_{n=1}^{\infty}a_{n}^{2} $， $ \sum_{n=1}^{\infty}b_{n}^{2} $ 都为正项级数且收敛，又  $ \left|a_{n}b_{n}\right|=\sqrt{a_{n}^{2}\cdot b_{n}^{2}}\leqslant\frac{a_{n}^{2}+b_{n}^{2}}{2} $，故由比较判别法知， $ \sum_{n=1}^{\infty}\left|a_{n}b_{n}\right| $ 收敛，即  $ \sum_{n=1}^{\infty}a_{n}b_{n} $ 绝对收敛。选 (B).

16.3 (A) 解 由题设知  $ \sum_{n=1}^{\infty}a_{n} $ 为正项级数且收敛，故级数  $ \sum_{n=1}^{\infty}a_{2n} $ 收敛.

记 $ u_{n}=\left|n\sin\frac{\lambda}{n}\right|a_{2n},\quad v_{n}=a_{2n} $，由于

 $$ \lim_{n\to\infty}\frac{u_{n}}{v_{n}}=\lim_{n\to\infty}\frac{\left|n\sin\frac{\lambda}{n}\right|a_{2n}}{a_{2n}}=\lim_{n\to\infty}\frac{\left|\sin\frac{\lambda}{n}\right|}{\frac{1}{n}}=\lim_{n\to\infty}\frac{\frac{\lambda}{n}}{\frac{1}{n}}=\lambda>0, $$ 

故由正项级数比较判别法的极限形式知  $ \sum_{n=1}^{\infty}u_{n} $ 与  $ \sum_{n=1}^{\infty}v_{n} $ 的敛散性相同。又  $ \sum_{n=1}^{\infty}v_{n}=\sum_{n=1}^{\infty}a_{2n} $ 收敛，故  $ \sum_{n=1}^{\infty}\left|n\sin\frac{\lambda}{n}\right|a_{2n} $ 收敛，从而  $ \sum_{n=1}^{\infty}(-1)^{n}\left(n\sin\frac{\lambda}{n}\right)a_{2n} $ 绝对收敛。故选 (A)。

16.4 (C) 解 利用泰勒展开式

 $$ \begin{aligned}\sin\frac{1}{n}-k\ln\left(1-\frac{1}{n}\right)&=\frac{1}{n}-\frac{1}{6n^{3}}+o\left(\frac{1}{n^{3}}\right)+\frac{k}{n}+\frac{k}{2n^{2}}+o\left(\frac{1}{n^{2}}\right)\\&=\frac{1+k}{n}+\frac{k}{2n^{2}}+o\left(\frac{1}{n^{2}}\right).\end{aligned} $$ 

若级数收敛，则  $ 1+k=0 $ ，即 k=-1 ，应选 (C).

16.5 -1 分析 一个自然的想法是求出  $ y(x) $ (这是可以的)，但借助微分方程  $ y' = x + y $ 及  $ y(0) = 1 $ 求出  $ y'(0) $ 和  $ y''(0) $，再利用泰勒公式确定  $ u_n = y\left(\frac{1}{n}\right) + k - \frac{1}{n} $ 关于  $ \frac{1}{n} $ 的阶数会更简单.

解 由  $ y' = x + y $,  $ y(0) = 1 $ 可得  $ y'(0) = 1 $，且由  $ y'' = 1 + y' $ 可得  $ y''(0) = 2 $，于是

 $$ y(x)=y(0)+y^{\prime}(0)x+\frac{1}{2}y^{\prime \prime}(0)x^{2}+o(x^{2})=1+x+x^{2}+o(x^{2}), $$ 

故 $ u_{n}=y\left(\frac{1}{n}\right)+k-\frac{1}{n}=\frac{1}{n^{2}}+1+k+o\left(\frac{1}{n^{2}}\right) $，当k=-1时， $ u_{n}=\frac{1}{n^{2}}+o\left(\frac{1}{n^{2}}\right) $，即 $ u_{n}=y\left(\frac{1}{n}\right)-1-\frac{1}{n}\sim\frac{1}{n^{2}} $（ $ n\to\infty $），故收敛.