## 3 斜渐近线

若  $ \lim_{x\to+\infty}\frac{f(x)}{x}=a_{1}(a_{1}\neq0) $， $ \lim_{x\to+\infty}\left[f(x)-a_{1}x\right]=b_{1} $，则  $ y=a_{1}x+b_{1} $ 是曲线  $ y=f(x) $ 的一条斜渐近线；

若  $ \lim_{x\to-\infty}\frac{f(x)}{x}=a_{2}(a_{2}\neq0) $， $ \lim_{x\to-\infty}\left[f(x)-a_{2}x\right]=b_{2} $，则  $ y=a_{2}x+b_{2} $ 是曲线  $ y=f(x) $ 的一条斜渐近线；

若  $ \lim_{x\to+\infty}\frac{f(x)}{x}=\lim_{x\to-\infty}\frac{f(x)}{x}=a(a\neq0) $， $ \lim_{x\to+\infty}\left[f(x)-ax\right]=\lim_{x\to-\infty}\left[f(x)-ax\right]=b $，则  $ y=ax+b $ 是曲线  $ y=f(x) $ 的一条斜渐近线.

注1  $ f(x) $ 向直线  $ y = ax + b $ 趋近，表明二者在无穷远处无限接近。即对任意  $ \varepsilon > 0 $ 都有  $ |f(x) - (ax + b)| < \varepsilon $，也即

 $$ \lim_{x\to\infty}[f(x)-(ax+b)]=0, $$ 

从而

 $$ \lim_{x\to\infty}\frac{f(x)-(ax+b)}{x}=0\ ,\  即 \lim_{x\to\infty}\frac{f(x)}{x}=a(a\neq0) $$ 

将②结果代入①，可知

 $$ \lim_{x\to\infty}[f(x)-ax]=b, $$ 

由②，③，可以得出a与b，即可得到斜渐近线.

注2  $ x \rightarrow +\infty $ 与  $ x \rightarrow -\infty $ 时的斜渐近线可能相同，也可能不同。有时需分左右两侧分别去求。

注3 寻找渐近线的顺序：铅直渐近线、水平渐近线、斜渐近线。

若求曲线  $ y = f(x) $ 的渐近线，要先找函数的无定义点，定义区间的端点或分段函数的分段点，具体说来，若  $ \lim_{x \to x_0^-} f(x) = \infty $（或  $ \lim_{x \to x_0^-} f(x) = \infty $），则  $ x = x_0 $ 为一条铅直渐近线；然后判别  $ \lim_{x \to \infty} f(x) $ 是否为常数，若是常数，则存在水平渐近线；若是  $ \infty $，则最后判别  $ \lim_{x \to \infty} \frac{f(x)}{x} $ 是否为非零常数  $ a $，若是，则求出常数  $ a $，再求  $ b = \lim_{x \to \infty} [f(x) - ax] $，当  $ a, b $ 都存在时，则存在斜渐近线，否则就没有斜渐近线。可总结成如下程序。