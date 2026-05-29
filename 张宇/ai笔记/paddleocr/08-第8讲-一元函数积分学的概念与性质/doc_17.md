由连续函数的局部保号性知，存在  $ \delta > 0 $ 与  $ \eta > 0 $，使得当  $ x \in [x_0 - \delta, x_0 + \delta] \subset [a, b] $ 时，恒有  $ f(x) \geq \eta > 0 $。

根据定积分的不等式性质，有 $ \int_{a}^{b}f(x)\mathrm{d}x\geqslant\int_{x_{0}-\delta}^{x_{0}+\delta}f(x)\mathrm{d}x\geqslant\eta\int_{x_{0}-\delta}^{x_{0}+\delta}\mathrm{d}x=2\eta\delta>0 $

该命题的推论：若连续函数 $ f(x) $， $ g(x) $满足 $ \underline{f(x)\geq g(x)} $，且 $ f(x) $不恒等于 $ g(x) $，又 $ a<b $，则必有严格不等式 $ \int_{a}^{b}f(x)dx>\int_{a}^{b}g(x)dx $。

 $$ \begin{array}{c}f(x)-g(x)\geqslant0\\ \downarrow\end{array} $$ 

 $$ \int_{a}^{b}\left[f(x)-g(x)\right]\mathrm{d}x\geqslant0 $$ 

 $$ \int_{a}^{b}f(x)\mathrm{d}x\geqslant\int_{a}^{b}g(x)\mathrm{d}x $$ 

若 $ f(x) $， $ g(x) $连续、不恒等，则满足严格不等式.

例 8.8 设  $ f(x) $ 在  $ [a, b] $ 上连续，证明存在  $ \xi \in [a, b] $，使得

 $$ \int_{a}^{b}f(x)\mathrm{d}x=f(\xi)(b-a). $$ 

证 因为  $ f(x) $ 在  $ [a, b] $ 上连续，所以  $ f(x) $ 在  $ [a, b] $ 上存在最大值 M 与最小值 m，使得

 $$ m(b-a)\leqslant\int_{a}^{b}f(x)\mathrm{d}x\leqslant M(b-a), $$ 

故

 $$ m\leqslant\frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x\leqslant M. $$ 

由介值定理可知，存在  $ \xi \in [a, b] $，使得  $ f(\xi) = \frac{1}{b - a} \int_{a}^{b} f(x) \, dx $，得证。

## 注 如何证明  $ \xi \in (a, b) $ 时，结论仍成立？

设 $ f(x) $在 $ [a,b] $上连续，证明存在 $ \xi\in(a,b) $，使得 $ \int_{a}^{b}f(x)\mathrm{d}x=f(\xi)(b-a) $

证 方法一 令  $ F(x)=\int_{a}^{x}f(t)dt $，在  $ [a,b] $ 上用拉格朗日中值定理，则  $ F(b)-F(a)=F'(\xi)(b-a) $，即

 $$ \int_{a}^{b}f(x)\mathrm{d}x-0=f(\xi)(b-a),\xi\in(a,b), $$ 

得证.

见到 $ \int_{a}^{b}f(x)dx $

①用积分中值定理： $ \int_{a}^{b}f(x)dx=f(\xi)(b-a) $



②改成 $ \int_{a}^{x}f(t)dt $，辅助法.