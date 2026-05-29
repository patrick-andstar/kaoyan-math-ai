注 第 (2) 问利用公式  $ ab \leqslant \frac{a^{2} + b^{2}}{2} $，同理还有  $ ab = 2a\frac{b}{2} $， $ ab = \frac{a}{b}b^{2} $ 等。

例 16.7 设有方程  $ x^n + nx - 1 = 0 $，其中  $ n $ 为正整数。证明此方程存在唯一的正实根  $ x_n $，并证明当  $ a > 1 $ 时，级数  $ \sum_{n=1}^{\infty} x_n^a $ 收敛。

证 由例 6.18 知，此方程存在唯一的正实根  $ x_{n} $，且  $ 0 < x_{n} < 1 $

因为 $ x_{n}^{n}+nx_{n}-1=0 $，且 $ 0<x_{n}<1 $，所以

 $$ 0<x_{_{n}}=\frac{1-x_{_{n}}^{^{n}}}{n}<\frac{1}{n}。 $$ 

当a>1时，有

 $$ 0<x_{n}^{a}<\left(\frac{1}{n}\right)^{a}. $$ 

又当a>1时，正项级数 $ \sum_{n=1}^{\infty}\frac{1}{n^{a}} $收敛，所以级数 $ \sum_{n=1}^{\infty}x_{n}^{a} $收敛.

注 记  $ f_{n}(x)=x^{n}+nx-1 $，若是观察到  $ f_{n}\left(\frac{1}{n}\right)=\left(\frac{1}{n}\right)^{n}>0 $，则此时  $ 0<x_{n}<\frac{1}{n} $，进而有  $ 0<x_{n}^{a}<\frac{1}{n^{a}} $，这样更简单。

(3) 比较判别法的极限形式（无穷小比阶）.

给出两个正项级数  $ \sum_{n=1}^{\infty}u_{n} $ 和  $ \sum_{n=1}^{\infty}v_{n}, v_{n} \neq 0 (n=1, 2, \cdots) $，且  $ \lim_{n \to \infty} \frac{u_{n}}{v_{n}} = A. \longrightarrow \frac{0}{0} $ 时才有“意义”

①若A=0，则当 $ \sum_{n=1}^{\infty}v_{n} $收敛时， $ \sum_{n=1}^{\infty}u_{n} $也收敛；

②若 $ A=+\infty $，则当 $ \sum_{n=1}^{\infty}v_{n} $发散时， $ \sum_{n=1}^{\infty}u_{n} $也发散；

★③若  $ 0 < A < +\infty $，则  $ \sum_{n=1}^{\infty} u_{n} $ 与  $ \sum_{n=1}^{\infty} v_{n} $ 有相同的敛散性.

例 16.8 设  $ \alpha > 0 $，级数  $ \sum_{n=2}^{\infty} \sin(n^{-\alpha} \ln n) $ 收敛，则（）.

(A)  $ \alpha \leqslant 1 $ (B)  $ \alpha < 1 $ (C)  $ \alpha \geqslant 1 $ (D)  $ \alpha > 1 $

解 应选(D).

对任意给定的  $ \alpha > 0 $， $ \lim_{n \to \infty} \frac{\ln n}{n^{\alpha}} = 0 $，所以当  $ n $ 足够大时，有  $ 0 < n^{-\alpha} \ln n < \frac{\pi}{2} $，故  $ \sin(n^{-\alpha} \ln n) > 0 $，则目标级数为正项级数。