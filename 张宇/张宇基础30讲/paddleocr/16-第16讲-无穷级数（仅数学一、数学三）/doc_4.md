若  $ q < -1, \lim_{n \to \infty} q^n $ 不存在，则  $ \lim_{n \to \infty} S_n $ 不存在.

综上所述，当 $ |q|\geq1 $时， $ \lim_{n\to\infty}S_n $均不存在，则 $ \sum_{n=1}^{\infty}aq^{n-1} $发散。于是有

 $ \sum_{n=1}^{\infty}aq^{n-1}\left\{\begin{aligned}& 发散,&\left|q\right|\geqslant1,\\ & 收敛,& 其和为 \frac{a}{1-q},\left|q\right|<1,\end{aligned}\right. $ 其中  $ a\neq0 $

注 显然，在引例中提出的芝诺的问题是几何级数的特例， $ T=\sum_{n=1}^{\infty}\frac{1}{2^{n}}=\sum_{n=1}^{\infty}\frac{1}{2}\cdot\left(\frac{1}{2}\right)^{n-1} $，其首项 $ a=\frac{1}{2} $，公比 $ q=\frac{1}{2} $，是 $ |q|<1 $的情况，则 $ \lim_{n\to\infty}S_n=\frac{a}{1-q}=\frac{\frac{1}{2}}{1-\frac{1}{2}}=1 $。事实上，此人将恰好用一个小时从A点走到B点。上述过程告诉我们，不能用有限项相加去理解和处理无限项相加。

## 3 性质

性质 1 若级数  $ \sum_{n=1}^{\infty}u_{n} $， $ \sum_{n=1}^{\infty}v_{n} $ 均收敛，则任给常数 a, b，有  $ \sum_{n=1}^{\infty}(a u_{n} \pm b v_{n}) $ 也收敛，且

 $$ \sum_{n=1}^{\infty}(a u_{n}\pm b v_{n})=a\sum_{n=1}^{\infty}u_{n}\pm b\sum_{n=1}^{\infty}v_{n}\left( 分配律 \right) $$ 

记忆口诀：若  $ \sum_{n=1}^{\infty}u_{n} $， $ \sum_{n=1}^{\infty}v_{n} $ 均收敛，则其线性组合也收敛。

注 (1) 收敛 ± 发散 = 发散；(2) 发散 ± 发散 = 不一定.

★性质 2 改变级数任意有限项，不会改变该级数的敛散性. 级数的敛散性取决于  $ n \rightarrow \infty $ 时的情况.

★性质 3 收敛级数的项任意加括号后所得的新级数仍收敛，且其和不变.

如若  $ \sum_{n=1}^{\infty}u_{n} $ 收敛，则  $ \sum_{n=1}^{\infty}(u_{2n-1}+u_{2n})=(u_{1}+u_{2})+(u_{3}+u_{4})+\cdots $ 也收敛.

注 根据性质 3，有如下两个结论需要注意.

(1) 若加括号后得到的新级数发散，则原级数必然发散（逆否命题）.

(2) 若加括号后得到的新级数收敛，不能断言原级数一定收敛。如级数  $ \sum_{n=1}^{\infty}(-1)^{n-1}a $，其中常数  $ a \neq 0 $，若从第一项起，两项两项地加括号，可得  $ (a-a)+(a-a)+\cdots=0 $ 收敛，但原级数是发散的。