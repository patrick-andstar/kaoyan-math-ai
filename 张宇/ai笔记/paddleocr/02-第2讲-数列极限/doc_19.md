对于任意给定的  $ k \in \mathbb{N}_+ $， $ \frac{1}{2^k} $ 可为任意小的正数，记  $ \frac{1}{2^k} = \varepsilon > 0 $，则该题干说法是  $ \{x_n\} $ 收敛于  $ a $ 的充分必要条件。

例 2.17 “存在正整数 N，当  $ n \geq N $ 时，恒有  $ |x_n - a| \leq \frac{1}{n} $” 是数列  $ \{x_n\} $ 收敛于  $ a $ 的（）.

(A) 充分不必要条件

(B) 必要不充分条件

(C) 充分必要条件

(D) 既不充分也不必要条件

## 解 应选(A)

如果存在正整数  $ N $，当  $ n \geq N $ 时，恒有  $ |x_n - a| \leq \frac{1}{n} $，那么任意的  $ \varepsilon > 0 $，取  $ n = \max\left\{N, \left[\frac{1}{\varepsilon}\right] + 1\right\} $，则  $ |x_n - a| \leq \frac{1}{n} < \varepsilon $，所以数列  $ \{x_n\} $ 收敛于  $ a $。

反之，取  $ x_{n}=a+\frac{1}{\sqrt{n}} $ ，则数列  $ \{x_{n}\} $ 收敛于 a ，但 “存在正整数 N ，当  $ n\geqslant N $ 时，恒有  $ \left|x_{n}-a\right|\leqslant\frac{1}{n} $ 并不成立 .

综上，“存在正整数N，当 $ n \geqslant N $时，恒有 $ \left|x_{n}-a\right| \leqslant \frac{1}{n} $”是数列 $ \left\{x_{n}\right\} $收敛于a的充分不必要条件.

注 对比本题与上一题，数列极限定义中的  $ \varepsilon $ 可以被替换为不依赖于  $ n $ 的任意小的正数，即不能与  $ n $ 有关，否则相当于对收敛速度提出了要求。比如此题中，若  $ x_n = a + \frac{1}{\sqrt{n}} $，其收敛于  $ a $ 的速度是慢于  $ y_n = a + \frac{1}{n} $ 的，于是存在正整数  $ N $，当  $ n \geq N $ 时， $ |x_n - a| > \frac{1}{n} $，但不影响  $ \lim_{n \to \infty} x_n = a $。总之，可作为  $ \lim_{n \to \infty} x_n = a $ 的充分必要条件的命题中，不能对收敛速度提要求，因为数列极限定义中只体现收敛目标，不体现收敛速度。

例 2.18 设  $ \lim_{n\to\infty}a_n=a $，且  $ a\neq0 $，则当  $ n $ 充分大时，有（ ）。

(A)  $ |a_n|>\frac{|a|}{2} $

(B)  $ |a_n|<\frac{|a|}{2} $

(C)  $ a_n>a-\frac{1}{n} $

(D)  $ a_n<a+\frac{1}{n} $

## 解 应选(A)

对于选项(A)，(B)，由极限保号性，当  $ n \to \infty $ 时，显然有  $ \left|a_{n}\right| $ 与  $ \left|a\right| $ 无限靠近，故  $ \left|a_{n}\right| > \frac{\left|a\right|}{2} $，因此选项(A)正确，(B)不正确。

对于选项(C)，(D)，无论是 $ b_{n}=a-\frac{1}{n} $，还是 $ c_{n}=a+\frac{1}{n} $，当 $ n\to\infty $时， $ b_{n} $， $ c_{n} $均收敛于a，但它们都提出了收敛的速度，而 $ \lim_{n\to\infty}a_{n}=a $并不知其收敛速度，所以 $ a_{n} $与 $ b_{n} $， $ c_{n} $的大小关系显然都不能确定，