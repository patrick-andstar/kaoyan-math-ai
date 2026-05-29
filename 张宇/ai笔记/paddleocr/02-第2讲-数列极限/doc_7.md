四则运算规则可以推广至有限个数列情形。

例 2.6 设  $ \lim_{n\to\infty}(a_n+b_n)=1 $， $ \lim_{n\to\infty}(a_n-b_n)=3 $，则（）.

(A)  $ \left\{a_{n}\right\} $ 极限存在， $ \left\{b_{n}\right\} $ 极限不存在

(B)  $ \left\{a_{n}\right\} $ 极限存在， $ \left\{b_{n}\right\} $ 极限存在

(C)  $ \left\{a_{n}\right\} $ 极限不存在， $ \left\{b_{n}\right\} $ 极限不存在

(D) $ \left\{a_{n}\right\} $ 极限不存在，

☐ 分析 对于数列极限的计算，可简记如下：

存在  $ \pm $ 存在 = 存在；

存在  $ \pm $ 不存在 = 不存在；

不存在 ± 不存在 = 不确定.

## 解 应选(B)

令  $ u_{n}=a_{n}+b_{n} $， $ v_{n}=a_{n}-b_{n} $，则  $ \lim_{n\to\infty}u_{n}=1 $， $ \lim_{n\to\infty}v_{n}=3 $ 。由极限四则运算规则 (1) 知， $ \left\{u_{n}+v_{n}\right\} $ 和  $ \left\{u_{n}-v_{n}\right\} $ 均存在极限，且有

 $$ \lim_{n\to\infty}(u_{n}+v_{n})=\lim_{n\to\infty}u_{n}+\lim_{n\to\infty}v_{n}=1+3=4, $$ 

 $$ \lim_{n\to\infty}(u_{n}-v_{n})=\lim_{n\to\infty}u_{n}-\lim_{n\to\infty}v_{n}=1-3=-2\quad. $$ 

又  $ a_{n}=\frac{1}{2}(u_{n}+v_{n}), b_{n}=\frac{1}{2}(u_{n}-v_{n}) $ ，所以  $ \left\{a_{n}\right\} $ 和  $ \left\{b_{n}\right\} $ 的极限均存在，且有

 $$ \lim_{n\to\infty}a_{n}=\frac{1}{2}\times4=2,\lim_{n\to\infty}b_{n}=\frac{1}{2}\times(-2)=-1 $$ 

注  $ \lim_{n\to\infty}(a_n+b_n) $ 存在，并不意味着  $ \lim_{n\to\infty}a_n $ 和  $ \lim_{n\to\infty}b_n $ 均存在。例如  $ \lim_{n\to\infty}[\sin n+(-\sin n)]=\lim_{n\to\infty}0=0 $，但  $ \lim_{n\to\infty}\sin n $ 与  $ \lim_{n\to\infty}(-\sin n) $ 均不存在。

## 5 海涅定理（归结原则）

在有的题目中，计算数列极限是极其困难的，这个时候我们就可以使用海涅定理，将原来的数列极限转化成函数极限，转换成函数极限后，有很多工具可以使用，比如洛必达法则、泰勒公式、等价无穷小代换等，计算出函数极限后，根据海涅定理，就可以得出数列极限的值，这是极限计算中一个非常重要的考点。比如

 $$ \lim_{x\to\infty}\frac{\ln n}{n}=\lim_{x\to\infty}\frac{\ln x}{x}=\lim_{x\to\infty}\frac{\frac{1}{x}}{1}=0. $$ 

这道题是一个非常典型的利用海涅定理将数列极限转化为函数极限的例子，之所以要这样操作，是因为题目中用到了洛必达法则，但是数列极限是不能用洛必达法则的，因为我们把数列理解成一个下标为整数的函数，所以它是一个一个离散的点，不能求导，但是通过海涅定理将它转化成函数极限之后，便可以求导，于是可以使用洛必达法则，进而由函数极限的值得到数列极限的值。

设 $ f(x) $在 $ U(x_{0},\delta) $内有定义，则 $ \lim_{x\to x_{0}}f(x)=A $存在 $ \Leftrightarrow $对任何 $ U(x_{0},\delta) $内以 $ x_{0} $为极限的数列 $ \left\{x_{n}\right\}(x_{n}\neq x_{0}) $，极限 $ \lim_{n\to\infty}f(x_{n})=A $存在.