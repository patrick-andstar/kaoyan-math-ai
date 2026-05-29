 $$ \lim_{x\to1^{-}}\frac{\mathrm{e}^{\frac{1}{x-1}}\ln\left|1+x\right|}{(\mathrm{e}^{x}-1)(x-2)}=0, $$ 

 $$ \lim_{x\to1^{+}}\frac{\mathrm{e}^{\frac{1}{x-1}}\ln\left|1+x\right|}{(\mathrm{e}^{x}-1)(x-2)}=-\infty, $$ 

可知当 $ x\to1 $时，函数 $ \frac{\mathrm{e}^{\frac{1}{x-1}}\ln\left|1+x\right|}{(\mathrm{e}^{x}-1)(x-2)} $的极限不存在且不为 $ \infty $，故选(D).

☑ 方法总结 遇到  $ e^{\infty} $，需讨论  $ e^{+\infty} $ 和  $ e^{-\infty} $

公式  $ \lim_{u\to+\infty}e^{u}=+\infty,\lim_{u\to-\infty}e^{u}=0 $

注 对于上述  $ \lim_{x\to1}e^{\frac{1}{x-1}} $ 的情形，由于  $ \lim_{x\to1^{+}}\frac{1}{x-1} $ 与  $ \lim_{x\to1^{-}}\frac{1}{x-1} $ 不相等，因此不能忽视左极限与右极限，否则会导致错误，这是这类问题经常出现错误的原因。

例1.16 设 $ g(x)=\begin{cases}2-x,&x\leq0,\\2+x,&x>0,\end{cases} $  $ f(x)=\begin{cases}x^{2},&x<0,\\-x-1,&x\geq0,\end{cases} $ 则 $ \lim_{x\to0}g[f(x)] $ ___.

(A) 为 3          (B) 为 2          (C) 为 1          (D) 不存在

这个题已见过，例1.5，分段函数的复合方法，有前世今生，越往后学越轻松，这个题还有连续剧，后面再说解应选(D).

由例 1.5 可知，

 $$ g\left[f(x)\right]=\begin{cases}3+x,&x\geqslant0,\\2+x^{2},&x<0.\end{cases} $$ 

又  $ \lim_{x\to0^{+}}g[f(x)]=\lim_{x\to0^{+}}\frac{(3+x)}{1}= $  $ 3\neq\lim_{x\to0^{-}}g[f(x)]=\lim_{x\to0^{-}}\frac{(2+x^{2})}{1}=2 $ ，故  $ \lim_{x\to0}g[f(x)] $ 不存在 .

这是超实数这个超实数的极限结果是2

☑ 方法总结 分段函数在分段点处的极限要考虑左、右极限.

公式 若  $ \lim_{x\to x_0}f(x)\neq\lim_{x\to x_0}f(x) $，则  $ \lim_{x\to x_0}f(x) $ 不存在.

两件事：①抽象证明，方法（技巧）重要。②具体例子理解。

(2) 局部有界性.

如果  $ \lim_{x\to x_0}f(x)=A $，则存在常数 M 和  $ \delta $，使得当  $ 0<|x-x_0|<\delta $ 时，有  $ |f(x)|\leq M $。

注 (1) 证  $ \lim_{x \to x_0} f(x) = A \Leftrightarrow \forall \varepsilon > 0, \exists \delta > 0 $，当  $ 0 < |x - x_0| < \delta $ 时， $ |f(x) - A| < \varepsilon $。

则  $ |f(x)| = |f(x) - A + A| \leqslant |f(x) - A| + |A| $ 。取  $ \varepsilon = 1 $， $ |f(x)| \leqslant 1 + |A| = M $ 。

(2) 这个 $M$ 必须是个确定的数, 比如 2023 年考研试题中出现 $|b_n| \equiv |b_n - a_n + a_n| \leqslant |b_n - a_n| + |a_n|$（是整个过程中的最关键环节）, 下面 4 条都有可能在考场出现.