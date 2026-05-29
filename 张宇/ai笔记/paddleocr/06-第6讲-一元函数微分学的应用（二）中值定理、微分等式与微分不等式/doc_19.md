6.9 证明  $ 0 < x < \frac{\pi}{4} $ 时，有  $ \tan x < \frac{4}{\pi}x $

6.10 设 p, q 是大于 1 的常数，并且  $ \frac{1}{p} + \frac{1}{q} = 1 $ 。证明：对于任意的 x > 0 ，有  $ \frac{1}{p} x^{p} + \frac{1}{q} \geq x $

## 解答

6.1 (B) 解 易知  $ f'(x) = \frac{1}{x} - \frac{1}{e} $. 当 x > e 时， $ f'(x) < 0 $；当 0 < x < e 时， $ f'(x) > 0 $，故在  $ (0, e) $ 和  $ (e, +\infty) $ 内  $ f(x) $ 分别至多有一个零点，又  $ f(e) = k > 0 $， $ \lim_{x \to 0^+} f(x) = -\infty $， $ \lim_{x \to +\infty} f(x) = -\infty $，所以  $ f(x) $ 在  $ (0, +\infty) $ 内有两个零点. 故答案选 (B).

6.2 (B) 解 令  $ g(x)=xe^{-x}-a $，则函数  $ f(x)=\frac{1}{xe^{-x}-a} $ 在  $ (-\infty,+\infty) $ 内处处连续等价于函数  $ g(x) $ 在  $ (-\infty,+\infty) $ 内没有零点.

 $$ g^{\prime}(x)=\mathrm{e}^{-x}(1-x), $$ 

令  $ g'(x)=0 $，得  $ x=1 $。因为当  $ x<1 $ 时， $ g'(x)>0 $， $ g(x) $ 单调增加，当  $ x>1 $ 时， $ g'(x)<0 $， $ g(x) $ 单调减少，所以  $ \max\{g(x)\}=g(1)=\mathrm{e}^{-1}-a $。又  $ \lim_{x\to-\infty}g(x)=\lim_{x\to-\infty}(xe^{-x}-a)=-\infty $， $ \lim_{x\to+\infty}g(x)=\lim_{x\to+\infty}(xe^{-x}-a)=-a $，故当  $ \max\{g(x)\}=e^{-1}-a<0 $ 时，即当  $ a>e^{-1} $ 时，函数  $ g(x) $ 没有零点。此时，函数  $ f(x) $ 在  $ (-\infty,+\infty) $ 内处处连续。

6.3 证明 令  $  F(x) = a_{0}x + \frac{a_{1}}{2}x^{2} + \frac{a_{2}}{3}x^{3} + \cdots + \frac{a_{n}}{n+1}x^{n+1}  $， $ 0 \leqslant x \leqslant 1 $，显然  $  F(0) = 0  $，且

 $$ F(1)=a_{0}+\frac{a_{1}}{2}+\frac{a_{2}}{3}+\cdots+\frac{a_{n}}{n+1}=0, $$ 

故由罗尔定理知，存在  $ \xi \in (0, 1) $，使  $ F'(\xi) = 0 $，即  $ a_0 + a_1 \xi + a_2 \xi^2 + \cdots + a_n \xi^n = 0 $，故所证方程在  $ (0, 1) $ 内至少有一个根。

6.4 证明 (1) 设  $ \varphi(x) = xf(x) $，则  $ \varphi(x) $ 在  $ [a, b] $ 上连续，在  $ (a, b) $ 内可导，且  $ \varphi(a) = \varphi(b) = 0 $，由罗尔定理得，存在  $ \xi \in (a, b) $，使  $ \varphi'(\xi) = 0 $，即  $ f(\xi) + \xi f'(\xi) = 0 $。

(2) 设  $  F(x) = e^{\frac{x^2}{2}} f(x)  $，则  $  F(x)  $ 在  $ [a, b] $ 上连续，在  $ (a, b) $ 内可导，且  $  F(a) = F(b) = 0  $，由罗尔定理得，存在  $  \eta \in (a, b)  $，使  $  F'(\eta) = e^{\frac{\eta^2}{2}} f'(\eta) + e^{\frac{\eta^2}{2}} \cdot \eta \cdot f(\eta) = 0  $，由于  $  e^{\frac{\eta^2}{2}} \neq 0  $，则有  $  \eta f(\eta) + f'(\eta) = 0  $。

6.5 证明 注意到  $ 3x^{2}f(x)+x^{3}f'(x) $ 是  $ x^{3}f(x) $ 的导函数，故令  $ F(x)=x^{3}f(x) $，易知  $ F(x) $ 在  $ [0,1] $ 上连续，在  $ (0,1) $ 内可导，即  $ F(x) $ 在  $ [0,1] $ 上满足拉格朗日中值定理的条件，于是得

 $$ F(1)-F(0)=F^{\prime}(\xi),\xi\in(0,1), $$ 