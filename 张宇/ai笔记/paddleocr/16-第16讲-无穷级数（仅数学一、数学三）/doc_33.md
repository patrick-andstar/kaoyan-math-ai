## 3 恒等变形方式

(1) 通项、下标一起变.

 $$ \sum_{n=k}^{\infty}a_{n}x^{n}=\sum_{n=k+l}^{\infty}a_{n-l}x^{n-l}, $$ 

其中 l 为整数，可正、可负、可为 0.

例如，

 $$ \sum_{n=0}^{\infty}a_{n}x^{n}=\sum_{n=1}^{\infty}a_{n-1}x^{n-1},\quad\sum_{n=1}^{\infty}a_{n}x^{n}=\sum_{n=0}^{\infty}a_{n+1}x^{n+1}. $$ 

(2) 只变下标，不变通项.

 $$ \sum_{n=k}^{\infty}a_{n}x^{n}=a_{k}x^{k}+a_{k+1}x^{k+1}+\cdots+a_{k+l-1}x^{k+l-1}+\sum_{n=k+l}^{\infty}a_{n}x^{n} $$ 

例如，

 $$ \sum_{n=0}^{\infty}a_{n}x^{n}=a_{0}x^{0}+a_{1}x^{1}+\sum_{n=2}^{\infty}a_{n}x^{n}. $$ 

(3) 只变通项，不变下标.

 $$ \sum_{n=k}^{\infty}a_{n}x^{n}=x^{l}\sum_{n=k}^{\infty}a_{n}x^{n-l}\xrightarrow{} $$ 

例如，

 $$ \begin{aligned}\sum_{n=0}^{\infty}a_{n}x^{2n}+\sum_{n=0}^{\infty}b_{n+1}x^{2n+2}&=a_{0}x^{0}+\sum_{n=1}^{\infty}a_{n}x^{2n}+\sum_{n=1}^{\infty}b_{n}x^{2n}=a_{0}+\sum_{n=1}^{\infty}\underline{\left(a_{n}+b_{n}\right)x^{2n}}.\\  注意下标和通项 \sum_{n=0}^{\infty}&\underline{\text{只}} 下标和 x 的次数都相同才能合并 \end{aligned} $$ 

## 4 性质

(1) 幂级数  $ \sum_{n=0}^{\infty}a_{n}x^{n} $ 的和函数  $ S(x) $ 在其收敛域 I 上连续.

幂级数的和函数必连续，其他级数的和函数不一定

注 如果幂级数在收敛区间的端点  $ x = R $（或  $ x = -R $）处收敛，则和函数  $ S(x) $ 在  $ (-R, R] $（或  $ [-R, R) $）上连续，即  $ \lim_{x \to R} S(x) = S(R) $（或  $ \lim_{x \to -R^+} S(x) = S(-R) $）。端点处单侧连续

(2) 幂级数  $ \sum_{n=0}^{\infty}a_{n}x^{n} $ 的和函数  $ S(x) $ 在其收敛域 I 上可积，且有逐项积分公式

 $$ \int_{0}^{x}S(t)\mathrm{d}t=\int_{0}^{x}\left(\sum_{n=0}^{\infty}a_{n}t^{n}\right)\mathrm{d}t=\sum_{n=0}^{\infty}a_{n}\int_{0}^{x}t^{n}\mathrm{d}t=\sum_{n=0}^{\infty}\frac{a_{n}}{n+1}x^{n+1}(x\in I), $$ 

逐项积分后所得到的幂级数与原级数有相同的收敛半径，但收敛域可能扩大。

(3) 幂级数  $ \sum_{n=0}^{\infty} a_n x^n $ 的和函数  $ S(x) $ 在其收敛区间  $ (-R, R) $ 内可导，且有逐项求导公式