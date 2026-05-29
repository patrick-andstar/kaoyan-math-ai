即

 $$ f(1)=3\xi^{2}f(\xi)+\xi^{3}f^{\prime}(\xi). $$ 

6.6 证明 (1) 令  $ F(x) = f(x) - 1 + x $，可得  $ \begin{cases} F(0) = f(0) - 1 + 0 = -1 < 0, \\ F(1) = f(1) - 1 + 1 = 1 > 0, \end{cases} $ 由零点定理可知，存在  $ \xi \in (0, 1) $，使得  $ F(\xi) = 0 $，即  $ f(\xi) = 1 - \xi $。

(2) 用  $ \xi $ 将  $ [0,1] $ 划分为  $ [0,\xi], [\xi,1] $，再用拉格朗日中值定理有

 $$ f(\xi)-f(0)=f^{\prime}(\eta)(\xi-0),\eta\in(0,\xi), $$ 

 $$ f(1)-f(\xi)=f^{\prime}(\tau)(1-\xi),\tau\in(\xi,1), $$ 

则

 $$ f^{\prime}(\eta)=\frac{f(\xi)-f(0)}{\xi}=\frac{1-\xi}{\xi},f^{\prime}(\tau)=\frac{f(1)-f(\xi)}{1-\xi}=\frac{\xi}{1-\xi}. $$ 

故 $ f'(\eta)f'(\tau)=1 $

6.7 证明 对  $ f(x) $ 在  $ [a, b] $ 上应用拉格朗日中值定理，则

 $$ f(b)-f(a)=f^{\prime}(\eta)(b-a),\eta\in(a,b), $$ 

对 $ f(x) $， $ x^{2} $在 $ [a,b] $上应用柯西中值定理，则

 $$ \frac{f(b)-f(a)}{b^{2}-a^{2}}=\frac{f^{\prime}(\xi)}{2\xi},\xi\in(a,b), $$ 

所以 $ f(b)-f(a)=\frac{f'(\xi)}{2\xi}(b^{2}-a^{2}) $，则

 $$ f^{\prime}(\eta)(b-a)=\frac{f^{\prime}(\xi)}{2\xi}(b^{2}-a^{2}), $$ 

即  $ \frac{f'(\xi)}{2\xi} = \frac{f'(\eta)}{b + a} $

6.8 (1) 解  $ f(x)=f(c)+f'(c)(x-c)+\frac{f''(\xi)}{2!}(x-c)^2 $，其中  $ \xi=c+\theta(x-c), 0<\theta<1 $

(2) 证明 在以上一阶泰勒公式中，分别令 x=0 和 x=1，则有

 $$ f(0)=f(c)-f^{\prime}(c)c+\frac{f^{\prime \prime}(\xi_{1})}{2!}c^{2},0<\xi_{1}<c<1, $$ 

 $$ f(1)=f(c)+f^{\prime}(c)(1-c)+\frac{f^{\prime \prime}(\xi_{2})}{2!}(1-c)^{2},0<c<\xi_{2}<1, $$ 

两式相减得

 $$ f(1)-f(0)=f^{\prime}(c)+\frac{1}{2!}\left[f^{\prime \prime}(\xi_{2})(1-c)^{2}-f^{\prime \prime}(\xi_{1})c^{2}\right], $$ 

于是  $ \left|f'(c)\right|\leqslant\left|f(1)\right|+\left|f(0)\right|+\frac{1}{2}\left|f''(\xi_{2})\right|(1-c)^{2}+\frac{1}{2}\left|f''(\xi_{1})\right|c^{2}\leqslant a+a+\frac{b}{2}\left[(1-c)^{2}+c^{2}\right], $

又因  $ c \in (0, 1) $， $ (1 - c)^{2} + c^{2} \leqslant 1 $，故  $ \left|f'(c)\right| \leqslant 2a + \frac{b}{2} $.