(5) 如果级数  $ \sum_{n=1}^{\infty}|u_n| $ 发散，我们不能断定级数  $ \sum_{n=1}^{\infty}u_n $ 也发散。但是，如果我们是用比值判别法或根值判别法根据  $ \lim_{n\to\infty}\left|\frac{u_{n+1}}{u_n}\right|=\rho>1 $ 或  $ \lim_{n\to\infty}\sqrt[n]{|u_n|}=\rho>1 $ 而判定级数  $ \sum_{n=1}^{\infty}|u_n| $ 发散的，那么我们可以断定级数  $ \sum_{n=1}^{\infty}u_n $ 也必定发散。这是因为从  $ \rho>1 $ 可推知  $ \lim_{n\to\infty}|u_n|\neq0 $，从而  $ \lim_{n\to\infty}u_n\neq0 $，因此级数  $ \sum_{n=1}^{\infty}u_n $ 是发散的。

 $$ \begin{aligned}\left|u_{_{n+1}}\right|>k*\left|u_{_{n}}\right|>\left|u_{_{n}}\right|&\Longrightarrow\left|u_{_{n+1}}\right|>\left|u_{_{n}}\right|\\&\Longrightarrow\lim_{_{n\rightarrow\infty}}\left|u_{_{n}}\right|\neq0\quad( 绝对值只和正负号有关 )\\&\Longrightarrow\lim_{_{n\rightarrow\infty}}u_{_{n}}\neq0,\end{aligned} $$ 

故  $ \sum_{n=1}^{\infty}u_{n} $ 发散

例如，级数  $ \sum_{n=1}^{\infty}(-1)^{n}\frac{1}{2^{n}}\left(1+\frac{1}{n}\right)^{n^{2}} $，若记  $ u_{n}=\frac{1}{2^{n}}\left(1+\frac{1}{n}\right)^{n^{2}} $，有  $ \lim_{n\to\infty}\sqrt[n]{u_{n}}=\lim_{n\to\infty}\frac{1}{2}\left(1+\frac{1}{n}\right)^{n}=\frac{\mathrm{e}}{2}>1 $，则原级数  $ \sum_{n=1}^{\infty}(-1)^{n}\frac{1}{2^{n}}\left(1+\frac{1}{n}\right)^{n^{2}} $ 发散。 $ \rightarrow $ 如绝对值后变成  $ \sum_{n=1}^{\infty}\frac{1}{n^{p}} $

(6) 交错 p 级数  $ \sum_{n=1}^{\infty}(-1)^{n-1}\frac{1}{n^{p}}\left\{\begin{array}{l} 绝对收敛, p>1, \\  条件收敛, 0<p\leq1\end{array}\right. $

例16.17 已知级数  $ \sum_{n=1}^{\infty}(-1)^{n-1}u_{n} $ 条件收敛， $ u_{n}>0 $，则级数  $ \sum_{n=1}^{\infty}(u_{2n}-2u_{2n-1}) $（）.

(A) 发散 (B) 绝对收敛 (C) 条件收敛 (D) 敛散性无法判断

☐ 分析 交错级数条件收敛，故其全体正项构成的级数和全体负项构成的级数均发散。

## 解 应选(A)

由  $ \sum_{n=1}^{\infty}(-1)^{n-1}u_{n} $ 条件收敛，可知  $ \sum_{n=1}^{\infty}u_{2n-1} $ 发散，且由 “二、2. 注 (3)” 知，  $ \sum_{n=1}^{\infty}(-1)^{n-1}u_{n}=\sum_{n=1}^{\infty}(u_{2n-1}-u_{2n}) $ 收敛，故  $ \sum_{n=1}^{\infty}(u_{2n}-2u_{2n-1})=\sum_{n=1}^{\infty}[(u_{2n}-u_{2n-1})-u_{2n-1}] $ 发散。选 (A).

偶数项减2倍的奇数项 拆开处理（学会这种方法）

例 16.18 级数  $ \sum_{n=1}^{\infty}\left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right)\sin(n+k) $ (k 为常数)（）.

(A) 绝对收敛  

无穷大量 + 有界量还是无穷大量  

(B) 条件收敛  

(C) 发散  

(D) 敛散性与 k 有关

分析 当  $ n \to \infty $ 时， $ |\sin(n+k)| \leq 1 $，而