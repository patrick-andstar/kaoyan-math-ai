☐分析 本题是分段函数和复合函数的综合，不要盲目地先求出 $ f[f(x)] $的表达式，应先看看对应的求导表达式是什么.

解 应填 $ \frac{1}{e} $

因为

 $$ \left.\frac{\mathrm{d}y}{\mathrm{d}x}\right|_{x=\mathrm{e}}=f^{\prime}[f(x)]f^{\prime}(x)\big|_{x=\mathrm{e}}=f^{\prime}[f(\mathrm{e})]f^{\prime}(\mathrm{e}), $$ 

其中

 $$ f(\mathrm{e})=\ln\sqrt{x}\bigg|_{x=\mathrm{e}}=\frac{1}{2},\left.f^{\prime}[f(\mathrm{e})]=f^{\prime}\left(\frac{1}{2}\right)=\left(2x-1\right)^{\prime}\right|_{x=\frac{1}{2}}=2,\left.f^{\prime}(\mathrm{e})=(\ln\sqrt{x})^{\prime}\right|_{x=\mathrm{e}}=\frac{1}{2\mathrm{e}}, $$ 

所以

 $$ \left.\frac{\mathrm{d}y}{\mathrm{d}x}\right|_{x=\mathrm{e}}=2\bullet\frac{1}{2\mathrm{e}}=\frac{1}{\mathrm{e}}. $$ 

☑ 方法总结 本题求的是某一点的导数值，不是求导函数，所以无须先求  $ f[f(x)] $ 的表达式.

∅公式  $ \left\{f[f(x)]\right\}' = f'[f(x)] \cdot f'(x) $

例 4.4 设  $ y = e^{\sin(\ln x)} $，求 dy 及  $ \frac{dy}{dx} $.

☑分析 本题是函数求导的题目，可以直接用复合函数的链式求导法则，先求导数，后求微分.也可以用微分形式不变性先求微分，再求导.

方法一：链式求导法则；

方法二：微分形式的不变性.

 $$ \mathrm{d}\big\{f\big[g(x)\big]\big\}=f^{\prime}\big[g(x)\big]g^{\prime}(x)\mathrm{d}x=f^{\prime}\big[g(x)\big]\mathrm{d}\big[g(x)\big]\;. $$ 

解 由一阶微分形式的不变性，得

 $ \begin{cases}

d[f(u)] = f'(u) du, & \text{令 } u = g(x) \text{ 为中间变量，形式不变} \\

\end{cases} $

 $ \rightarrow $ 若  $ u $ 就是  $ x $，则  $ d[f(x)] = f'(x) dx $，这就是一阶微分形式不变性！

 $$ \begin{aligned}\mathrm{d}[\mathrm{e}^{\sin(\ln x)}]&=\mathrm{e}^{\sin(\ln x)}\mathrm{d}[\sin(\ln x)]&\rightarrow\mathrm{d}(\mathrm{e}^{u})=(\mathrm{e}^{u})^{\prime}\mathrm{d}u=\mathrm{e}^{u}\mathrm{d}u\\ &=\mathrm{e}^{\sin(\ln x)}\cos(\ln x)\mathrm{d}(\ln x)\\ &=\mathrm{e}^{\sin(\ln x)}\cos(\ln x)\frac{1}{x}\mathrm{d}x,\\ \end{aligned} $$ 

所以

 $$ \mathrm{d}y=\mathrm{e}^{\sin(\ln x)}\cos(\ln x)\frac{1}{x}\mathrm{d}x,\frac{\mathrm{d}y}{\mathrm{d}x}=\mathrm{e}^{\sin(\ln x)}\cos(\ln x)\frac{1}{x}. $$ 

☑ 方法总结 求微分的题目可以选择用链式求导法则，也可以选择用一阶微分形式不变性处理.

公式  $ (e^{x})^{\prime}=e^{x} $， $ (\sin x)^{\prime}=\cos x $， $ (\ln x)^{\prime}=\frac{1}{x} $