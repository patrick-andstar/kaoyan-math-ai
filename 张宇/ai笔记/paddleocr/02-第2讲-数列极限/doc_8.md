注 众所周知，虽然数列极限与函数极限是分别独立定义的，但是海涅定理是联系数列极限与函数极限的桥梁。它指出：在极限存在的条件下，函数极限和数列极限可以相互转化。有些考生可能没有听说过这个定理，但是在不知不觉中我们已经使用它了。

常考①当 $ x\to0 $时，取 $ x_{n}=\frac{1}{n} $，即若 $ \lim_{x\to0}f(x)=A $，则 $ \lim_{n\to\infty}f\left(\frac{1}{n}\right)=A $。例： $ \lim_{n\to\infty}\left(1-\frac{1}{n+1}\right)^{n}=e^{-1} $

②当 $ x\to+\infty $时，取 $ x_{n}=n $，即若 $ \lim_{x\to+\infty}f(x)=A $，则 $ \lim_{n\to\infty}f(n)=A $。 $ \lim_{x\to+\infty}\left(1-\frac{1}{x+1}\right)^{x}=e^{-1} $

③当 $ x_{n}\to a $，且 $ x_{n}\neq a $时，若 $ \lim_{x\to a}f(x)=A $，则 $ \lim_{n\to\infty}f(x_{n})=A $。

例 2.7 当  $ x \to 0 $ 时， $ \frac{1}{x} \sin \frac{1}{x} $ 是（）.

(A) 无穷大量

(B) 无界量，但不是无穷大量

(C) 有界量，但不是无穷小量

(D) 无穷小量

分析  $ \infty \cdot \sin \infty $ 型，使用归结原则.

## 解 应选(B)

设  $ f(x)=\frac{1}{x}\sin\frac{1}{x} $，若取  $ x_{n}=\frac{1}{n\pi}\rightarrow0,n\rightarrow\infty $，则  $ f(x_{n})=n\pi\cdot\sin(n\pi)=0 $，于是  $ \lim_{n\to\infty}f(x_{n})=0 $；若取  $ x_{n}^{\prime}=\frac{1}{\left(2n+\frac{1}{2}\right)\pi}\rightarrow0,n\rightarrow\infty $，则  $ f(x_{n}^{\prime})=\left(2n+\frac{1}{2}\right)\pi\rightarrow+\infty,n\rightarrow\infty $。根据归结原则，极限  $ \lim_{x\to0}\frac{1}{x}\sin\frac{1}{x} $ 不存在，且当  $ x\rightarrow0 $ 时， $ \frac{1}{x}\sin\frac{1}{x} $ 是无界量，但不是无穷大量。

注 令  $ f(x)=\begin{cases}x^{2}, & x \text{是有理数}, \\ 0, & x \text{是无理数},\end{cases} $ 事实上， $ f(x)=x^{2}D(x) $，其中  $ D(x)=\begin{cases}1, & x \text{是有理数}, \\ 0, & x \text{是无理数},\end{cases} $ 为狄利克雷函数，有如下结论：

(1)  $ f(x) $ 在 x=0 处连续.

无穷小量×有界量=无穷小量

证 方法一  $ \left|D(x)\right|\leq1 $，即  $ D(x) $ 为有界量，故  $ \lim_{x\to0}f(x)=\lim_{x\to0}x^{2}D(x)=0 $

因为 $ f(0)=0 $，所以 $ f(x) $在x=0处连续。

方法二  $ 0 \leqslant |f(x)| \leqslant |x^{2}| + |0| = x^{2} $

 $ \downarrow $

 $ 0 \rightarrow 0 \leftarrow  $

由夹逼准则得  $ \lim_{x\to0}f(x)=0 $，且  $ f(0)=0 $，故  $ f(x) $ 在 x=0 处连续。

(2) 当  $ x_{0} \neq 0 $ 时， $ f(x) $ 一定不连续.

证 使用归结原则：对于  $ \lim_{x\to x_{0}}f(x) $，当 x 分别取有理数列和无理数列时，极限不同，故极限不存在。