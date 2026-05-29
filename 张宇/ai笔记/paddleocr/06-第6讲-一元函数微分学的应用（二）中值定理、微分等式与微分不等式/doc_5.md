见到  $ f'(x)x - f(x) $,  $ x \neq 0 $，令  $ F(x) = \frac{f(x)}{x} $.

b.  $ \left[\frac{f'(x)}{f(x)}\right]^{\prime} = \frac{f''(x)f(x) - [f'(x)]^2}{f^2(x)} $.

见到  $ f''(x)f'(x) - [f'(x)]^2 $,  $ f(x) \neq 0 $，令  $ F(x) = \frac{f'(x)}{f(x)} $.

c.  $ [\ln f(x)]' = \frac{f'(x)}{f(x)} $，故  $ [\ln f(x)]'' = \left[\frac{f'(x)}{f(x)}\right]' $ =  $ \frac{f''(x)f(x) - [f'(x)]^2}{f^2(x)} $.

见到  $ f''(x)f(x) - [f'(x)]^2 $,  $ f(x) > 0 $，亦可考虑令  $ F(x) = \ln f(x) $.

事实上，这些辅助函数的构造不仅仅限于罗尔定理的使用.

例 6.4 设  $ f(x) $ 在  $ [0, 3] $ 上连续，在  $ (0, 3) $ 内可导，且  $ f(0) + f(1) + f(2) = 3 $， $ f(3) = 1 $。证明：必存在  $ \xi \in (0, 3) $，使得  $ f'(\xi) = 0 $。

证 因为  $ f(x) $ 在  $ [0, 3] $ 上连续，所以  $ f(x) $ 在  $ [0, 2] $ 上连续，且在  $ [0, 2] $ 上必有最大值 M 和最小值 m，于是

 $$ m\leq f(0)\leq M,m\leq f(1)\leq M,m\leq f(2)\leq M, $$ 

故

 $$ m\leqslant\frac{f(0)+f(1)+f(2)}{3}\xrightarrow{ 平均值定理 }=1\leqslant M\text{．} $$ 

由介值定理可知，至少存在一点  $ c \in [0, 2] $，使得  $ f(c) = \frac{f(0) + f(1) + f(2)}{3} = 1 $。

所以函数 $ f(x) $在 $ [c, 3] $上满足罗尔定理的条件，于是存在 $ \xi \in (c, 3) \subset (0, 3) $，使得 $ f'(\xi) = 0 $

例 6.5 设  $ f(x) $ 在  $ [a, b] $ 上连续，在  $ (a, b) $ 内可导， $ f(a) = 0, a > 0 $，证明：存在  $ \xi \in (a, b) $，使得  $ f(\xi) = \frac{b - \xi}{a} f'(\xi) $。

♀分析 先将结论改写为 $ f'(\xi)-\frac{a}{b-\xi}f(\xi)=0 $（对照 $ f'(x)+f(x)\varphi'(x) $，所以构造辅助函数 $ F(x)=f(x)\mathrm{e}^{\int\left(\frac{a}{b-x}\right)\mathrm{d}x}=f(x)(b-x)^a $，再利用罗尔定理即可．

证 令  $  F(x) = f(x)(b - x)^a  $，显然  $  F(a) = F(b) = 0  $，由罗尔定理知，存在  $  \xi \in (a, b)  $，使得  $  F'(\xi) = 0  $，即  $  f'(\xi)(b - \xi)^a - af(\xi)(b - \xi)^{a-1} = 0  $，已知 a > 0，故  $  f(\xi) = \frac{b - \xi}{a} f'(\xi)  $。

注 上面是证明一阶导数为 0，也就是使用一次罗尔定理的问题，但有些题目涉及二阶导数为 0，即要多次使用罗尔定理，这种问题的难点是要找到函数值相等的三个不同点，即  $ f(a) = f(b) = f(c) $（不