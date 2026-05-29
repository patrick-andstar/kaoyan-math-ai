区间  $ (-R, R) $ 为幂级数  $ \sum_{n=0}^{\infty} a_n x^n $ 的收敛区间，单独考查幂级数在  $ x = \pm R $ 处的敛散性就可以确定其收敛域为  $ (-R, R) $ 或  $ [-R, R) $ 或  $ (-R, R] $ 或  $ [-R, R] $.

## 注 注例 1 求幂级数

 $$ 1+x+\frac{1}{2!}x^{2}+\cdots+\frac{1}{n!}x^{n}+\cdots $$ 

的收敛域.

解 因为

 $$ \rho=\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_{n}}\right|=\lim_{n\to\infty}\frac{\frac{1}{(n+1)!}}{\frac{1}{n!}}=\lim_{n\to\infty}\frac{1}{n+1}=0, $$ 

所以收敛半径 $ R=+\infty $，从而收敛域是 $ (-\infty,+\infty) $.

这种很好，处处收敛，非常有用

注例 2 求幂级数  $ \sum_{n=0}^{\infty} n! x^{n} $ 的收敛半径（规定 0!=1）

解 因为

这种很少碰到

 $$ \rho=\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_{n}}\right|=\lim_{n\to\infty}\frac{(n+1)!}{n!}=+\infty, $$ 

所以收敛半径 R = 0 ，即级数仅在点 x = 0 处收敛.

(2)对于缺项幂级数或一般函数项级数 $ \sum u_{n}(x) $

①加绝对值，即写成  $ \sum |u_n(x)| $。

一定是正项级数。

适用正项级数的判别法中，达朗贝尔判别法、柯西判别法最好用

（比值判别法）（根值判别法）

②用正项级数的比值（或根值）判别法.

令  $ \lim_{n\to\infty}\frac{\left|u_{n+1}(x)\right|}{\left|u_{n}(x)\right|} $ （或  $ \lim_{n\to\infty}\sqrt[n]{\left|u_{n}(x)\right|} $ ）<1 ，求出收敛区间  $ (a,b) $ 。

③单独讨论 x = a, x = b 时  $ \sum u_n(x) $ 的敛散性，从而确定收敛域。

注1  $ \sum a_{n}x^{n} $， $ \lim_{n\to\infty}\left|\frac{a_{n+1}x^{n+1}}{a_{n}x^{n}}\right|=\left|x\lim_{n\to\infty}\frac{\left|a_{n+1}\right|}{\left|a_{n}\right|}\right|<1 $，即 $ |x|\cdot\rho<1\Rightarrow|x|<\frac{1}{\rho} $.

实际上，有了(2)的方法之后，(1)的方法是可以不  $ \xrightarrow{R} $ 0  $ \xrightarrow{R} $

的.因为(1)的方法包含在(2)的方法里，无论哪种方法，都别忘了讨论两个端点处的敛散性.