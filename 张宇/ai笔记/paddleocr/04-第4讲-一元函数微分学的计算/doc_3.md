③复合函数的导数与微分形式不变性 微分不变性是微分学中最重要的计算方法，要认识规则，严守规则

设 $ u=g(x) $在点 $ x $（没有下标是泛指的点，下同）处可导， $ y=f(u) $在点 $ u=g(x) $处可导，则

 $$ \left\{f[g(x)]\right\}^{\prime}=f^{\prime}[g(x)]g^{\prime}(x), $$ 

 $$ \left\lfloor f\left[g(x)\right]\right\rfloor^{\prime}=\frac{\mathrm{d}\left\lfloor f\left[g(x)\right]\right\rfloor}{\mathrm{d}x}=\frac{\mathrm{d}\left\lfloor f\left[g(x)\right]\right\rfloor}{\mathrm{d}\left\lfloor g(x)\right\rfloor}\cdot\frac{\mathrm{d}\left\lfloor g(x)\right\rfloor}{\mathrm{d}x}=f^{\prime}\left[g(x)\right]\cdot g^{\prime}(x). $$ 

 $ \left[\frac{f[g(x)]}{dx}\right]^{\prime}=\frac{d[f[g(x)]]}{dx} $，而 $ \frac{f^{\prime}[g(x)]}{dx}=\frac{d[f[g(x)]]}{dx} $，要看清楚求导符号的位置，不要弄错了。

一元复合函数求导规则图（链式求导法则）：

 $$ f \to u \to x $$ 

 $$ \left[f\left[g(x)\right]\right]^{\prime}=f^{\prime}(u)\bullet u^{\prime}=f^{\prime}\left[g(x)\right]\bullet g^{\prime}(x). $$ 

 $$  再来一层： $$ 

 $$ f \to u \to v \to x $$ 

 $$ f_{x}^{\prime}\{u[v(x)]\}=f_{u}^{\prime}\bullet u_{v}^{\prime}\bullet v_{x}^{\prime}=\frac{\mathrm{d}f}{\mathrm{d}u}\bullet\frac{\mathrm{d}u}{\mathrm{d}v}\bullet\frac{\mathrm{d}v}{\mathrm{d}x}. $$ 

正如歌词：如果你愿意一层一层一层地剥开“它”的心，你会发现，你会讶异……

考试最多3层，对于多元函数的链式求导法则后面会讲！

 $$ \mathbf{d}\big\{f\big[g(x)\big]\big\}=f^{\prime}\big[g(x)\big]g^{\prime}(x)\mathbf{d}x=f^{\prime}\big[g(x)\big]\mathbf{d}\big[g(x)\big]\;. $$ 

上式就是微分形式的不变性——无论 u 是中间变量还是自变量， $ dy = f'(u)du $ 都成立。

例 4.2 设  $ y = \ln(x + \sqrt{x^2 + a^2}) (a \neq 0) $，求  $ y'\big|_{x=0} $.

分析 当 a=1 时，就是反双曲正弦函数。本题是复合函数，外层  $ y=\ln u $，内层  $ u=x+\sqrt{x^{2}+a^{2}} $。所求的导数等于外层导数乘以内层导数。

解 因为

 $$ \begin{aligned}y^{\prime}&=\frac{1}{x+\sqrt{x^{2}+a^{2}}}\bullet(x+\sqrt{x^{2}+a^{2}})^{\prime}\\&=\frac{1}{x+\sqrt{x^{2}+a^{2}}}\left[1+\frac{1}{2\sqrt{x^{2}+a^{2}}}\bullet(x^{2}+a^{2})^{\prime}\right]\\&=\frac{1}{x+\sqrt{x^{2}+a^{2}}}\left(1+\frac{x}{\sqrt{x^{2}+a^{2}}}\right)=\frac{1}{\sqrt{x^{2}+a^{2}}},\\ \end{aligned} $$ 

所以

 $$ y^{\prime}\Big|_{x=0}=\frac{1}{\sqrt{x^{2}+a^{2}}}\Bigg|_{x=0}=\frac{1}{|a|}(a\neq0)\ . $$ 

☑ 方法总结 对于复合函数的求导，直接使用链式求导法则.

公式  $ \left(\ln x\right)'=\frac{1}{x},\quad\left(\sqrt{x^{2}+a^{2}}\right)'=\frac{1}{2}\frac{1}{\sqrt{x^{2}+a^{2}}}\cdot2x $

例 4.3 设函数  $ f(x)=\begin{cases}\ln\sqrt{x}, & x\geq1, \\ 2x-1, & x<1,\end{cases} $ 且  $ y=f[f(x)] $，则  $ \left.\frac{dy}{dx}\right|_{x=e} $