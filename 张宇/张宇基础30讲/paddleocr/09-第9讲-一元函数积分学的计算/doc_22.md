例9.23 证明连续的奇函数的一切原函数都是偶函数；连续的偶函数的原函数中仅有一个原函数是奇函数.

证 设 $ f(x) $是连续函数，则其一个原函数可以表示为 $ F(x)=\int_{a}^{x}f(t)dt $

若 $ f(x) $是连续的奇函数，即有 $ f(x)=-f(-x) $，且 $ \int_{-a}^{a}f(t)dt=0 $，则

 $$ F(-x)=\int_{a}^{-x}f(t)\mathrm{d}t\xlongequal{t=-u}-\int_{-a}^{x}f(-u)\mathrm{d}u=\int_{-a}^{a}f(u)\mathrm{d}u+\int_{a}^{x}f(u)\mathrm{d}u=0+F(x)=F(x), $$ 

所以连续的奇函数的一切原函数都是偶函数。

若 $ f(x) $是连续的偶函数，即有 $ f(-x)=f(x) $，且 $ \int_{-a}^{a}f(t)dt=2\int_{0}^{a}f(t)dt $，则

 $$ F(-x)=\int_{a}^{-x}f(t)\mathrm{d}t=\int_{-a}^{x}f(-u)\mathrm{d}u=-\int_{-a}^{x}f(u)\mathrm{d}u-\int_{a}^{x}f(u)\mathrm{d}u=-2\int_{0}^{a}f(u)\mathrm{d}u-F(x), $$ 

只有当 $ \int_{0}^{a}f(u)du=0 $时， $ F(-x)=-F(x) $，即连续的偶函数的原函数中仅有一个原函数为奇函数。

★★★ ☐ 例9.24 设奇函数 $ f(x) $在 $ (-\infty, +\infty) $上具有连续导数，则（）.

(A)  $ \int_{0}^{x}[\cos f(t)+f'(t)]\,dt $ 是奇函数 (B)  $ \int_{0}^{x}[\cos f(t)+f'(t)]\,dt $ 是偶函数

(C)  $ \int_{0}^{x}[\cos f'(t) + f(t)]\,dt $ 是奇函数 (D)  $ \int_{0}^{x}[\cos f'(t) + f(t)]\,dt $ 是偶函数

分析 内偶则偶，内奇同外.

 $ \cos f(t) \Rightarrow $ 偶， $ \cos f'(t) \Rightarrow $ 偶；

 $ \cos f(t) + f'(t) \Rightarrow $ 偶， $ \cos f'(t) + f(t) \Rightarrow $ 非奇非偶。

解 应选(A).

由题设可知  $ \cos f(x) $ 和  $ f'(x) $ 均为偶函数，则由上述重要结论 (2) 知， $ \int_{0}^{x}[\cos f(t) + f'(t)]\,dt $ 为奇函数。

一题一练 判别函数  $ f(x) = \int_{0}^{\sin x} \cos t^{2} \, dt $ 的奇偶性。

分析令  $ h(x)=\int_{0}^{x}\cos t^{2}dt $，则  $ f(x)=h(\sin x)=h[g(x)] $，又有内奇同外，且  $ h(x) $ 为奇函数，故  $ f(x) $ 为奇函数。

例9.25 设  $ f(x) $ 连续且以  $ T $ 为周期， $ F(x)=\int_{a}^{x}f(t)dt $。

证明：(1) 当且仅当  $ \int_{0}^{T} f(x) dx = 0 $ 时， $ F(x) $ 以 T 为周期；

(2) $ F(x)-\frac{\int_{0}^{T}f(x)dx}{T}x $ 以 T 为周期.

证 $ ^{(1)} $

 $$ F(x+T)=\int_{a}^{x+T}f(t)\mathrm{d}t=\int_{a}^{x}f(t)\mathrm{d}t+\int_{x}^{x+T}f(t)\mathrm{d}t, $$ 

因为  $ f(x) $ 以 T 为周期，于是  $ \int_{x}^{x+T} f(t) dt = \int_{0}^{T} f(t) dt $，即  $ F(x+T) - F(x) = \int_{0}^{T} f(t) dt $，所以当且仅当