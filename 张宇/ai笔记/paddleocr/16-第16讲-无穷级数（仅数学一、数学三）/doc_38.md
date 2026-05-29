 $$ \begin{aligned}&\sum_{n=0}^{\infty}(an^{3}+bn^{2}+cn+d)\overrightarrow{x^{n}}\overrightarrow{an^{3}+bn^{2}+cn+d}=\Box\overrightarrow{n(n-1)(n-2)}+\Box\overrightarrow{n(n-1)}+\Box\overrightarrow{n+\frac{d}{n-1}}\\ &\\ =a\sum_{n=3}^{\infty}n(n-1)(n-2)x^{n}+(3a+b)\sum_{n=2}^{\infty}n(n-1)x^{n}+(a+b+c)\sum_{n=1}^{\infty}nx^{n}+d\sum_{n=0}^{\infty}x^{n}\\ &\\ =\frac{6ax^{3}}{(1-x)^{4}}+\frac{2(3a+b)x^{2}}{(1-x)^{3}}+\frac{(a+b+c)x}{(1-x)^{2}}+\frac{d}{1-x}\left(-1<x<1\right).\\ &\xrightarrow{a=1,b=c=0,d=-1} \end{aligned} $$ 

例如  $ \sum_{n=0}^{\infty}(n^{3}-1)x^{2n}=\sum_{n=0}^{\infty}(n^{3}-1)(x^{2})^{n}=\frac{6x^{6}}{(1-x^{2})^{4}}+\frac{6x^{4}}{(1-x^{2})^{3}}+\frac{x^{2}}{(1-x^{2})^{2}}-\frac{1}{1-x^{2}}(-1<x<1) $

例16.32 求幂级数  $ \sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{2n-1}x^{2n} $ 的和函数.

(2)分析)2n-1为分母，应先求导、后积分，注意求导前，应先提一个x，变为 $ x\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{2n-1}x^{2n-1} $，求导 $ \sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{2n-1}x^{2n-1} $这部分，然后对其和函数进行积分.

解 由例 16.23 知该级数的收敛域为  $ [-1,1] $.

设  $ S(x)=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{2n-1}x^{2n-1}(-1\leqslant x\leqslant1) $，由于  $ S'(x)=\sum_{n=1}^{\infty}(-1)^{n-1}x^{2n-2}=\frac{1}{1+x^{2}} $，且  $ S(0)=0 $，因此  $ S(x)=\int_{0}^{x}\frac{dt}{1+t^{2}}+S(0)=\arctan x $，从而

 $$ \sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{2n-1}x^{2n}=xS(x)=x\arctan x(-1\leqslant x\leqslant1)\ . $$ 

方法总结 求和函数，先求收敛域，结合 $ \frac{(-1)^{n-1}}{2n-1} $的特点，应先求导化为简单的幂级数，然后再积分。

公式  $ \left[\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{2n-1}x^{2n-1}\right]^{\prime}=\frac{1}{1+x^{2}},-1\leqslant x\leqslant1 $

例 16.33 设数列 $\{a_n\}$ 满足 $a_1 = 1$, $(n+1)a_{n+1} = \left(n + \frac{1}{2}\right)a_n$, 证明：当 $|x| < 1$ 时, 幂级数 $\sum_{n=1}^{\infty} a_n x^n$ 收敛, 并求其和函数.

♣分析 本题给出的是幂级数系数的递推关系式，因为不缺项，故利用 $ \lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right| $研究收敛区间（域），又 $ S(x)=\sum_{n=1}^{\infty}a_n x^n $是抽象形式下的和函数，所以采用定义法，结合已知的递推公式对 $ S(x) $求导，然后再求解微分方程即可。

解 由条件可知， $ a_{n} \neq 0 $，且