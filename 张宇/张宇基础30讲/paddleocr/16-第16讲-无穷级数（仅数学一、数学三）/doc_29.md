 $$ \lim_{n\to\infty}\sqrt[n]{a_{n}}=\lim_{n\to\infty}\sqrt[n]{1+\frac{1}{2}+\cdots+\frac{1}{n}} $$ 

由习题 2.6 知

 $$ \lim_{n\to\infty}\sqrt[n]{a_{n}}=1, $$ 

即级数  $ \sum_{n=1}^{\infty}a_{n}x^{n} $ 的收敛半径为 1.

例16.23 幂级数  $ \sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{2n-1}x^{2n} $ 的收敛域为 ___.

解 应填  $ [-1, 1] $.

记  $ u_{n}(x)=\frac{(-1)^{n-1}}{2n-1}x^{2n} $，由于  $ \lim_{n\to\infty}\left|\frac{u_{n+1}(x)}{u_{n}(x)}\right|=\lim_{n\to\infty}\frac{2n-1}{2n+1}x^{2}=x^{2} $，故

当 $ |x|<1 $时， $ \sum_{n=1}^{\infty}u_{n}(x) $收敛；

当 $ |x|>1 $时， $ \sum_{n=1}^{\infty}u_{n}(x) $发散；

当  $ x = \pm 1 $ 时， $ \sum_{n=1}^{\infty} u_{n} (\pm 1) = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{2n-1} $，根据莱布尼茨判别法知此级数收敛.

综上，幂级数  $ \sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{2n-1}x^{2n} $ 的收敛域为  $ [-1,1] $.

例 16.24 设  $ f(x)=\sum_{n=0}^{\infty}x^{n} $， $ g(x)=\int_{0}^{x}f(t)dt $，则  $ f(x) $ 与  $ g(x) $ 的收敛域分别为（）.

(A) $ (-1,1),(-1,1) $ (B) $ (-1,1),[-1,1) $ (C) $ [-1,1),(-1,1) $ (D) $ [-1,1),[-1,1) $

解 应选(B).

对于 $ f(x)=\sum_{n=0}^{\infty}x^{n} $，有

 $$ \lim_{n\to\infty}\left|\frac{a_{n+1}}{a_{n}}\right|=1=\rho, $$ 

所以收敛半径 R = 1，故收敛区间为  $ (-1, 1) $。又当  $ x = \pm 1 $ 时，级数  $ \sum_{n=0}^{\infty} (\pm 1)^{n} $ 发散，故收敛域为  $ (-1, 1) $。

对于  $ g(x) = \int_{0}^{x} f(t) \, dt $，因为

 $$ g(x)=\int_{0}^{x}\sum_{n=0}^{\infty}t^{n}\mathrm{d}t=\sum_{n=0}^{\infty}\int_{0}^{x}t^{n}\mathrm{d}t=\sum_{n=0}^{\infty}\frac{1}{n+1}x^{n+1}, $$ 

收敛时，可逐项积分