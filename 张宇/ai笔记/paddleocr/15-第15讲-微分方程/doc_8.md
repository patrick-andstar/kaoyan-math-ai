 $$ \mathrm{e}^{-\mathrm{e x}}\left[\int_{x_{0}}^{x}\left(1-\frac{1}{t}\right)^{t}\cdot\mathrm{e}^{\mathrm{e t}}\mathrm{d}t+C\right]=\frac{\int_{x_{0}}^{x}\left(1-\frac{1}{t}\right)^{t}\cdot\mathrm{e}^{\mathrm{e t}}\mathrm{d}t+C}{\mathrm{e}^{\mathrm{e x}}}, $$ 

其中  $ x_{0} $ 为任意正实数，则  $ \lim_{x\to+\infty}y=\lim_{x\to+\infty}\frac{\int_{x_{0}}^{x}\left(1-\frac{1}{t}\right)^{t}\cdot\mathrm{e}^{\mathrm{e}t}\mathrm{d}t+C}{\mathrm{e}^{\mathrm{e}x}}=\lim_{x\to+\infty}\frac{\left(1-\frac{1}{x}\right)^{x}\cdot\mathrm{e}^{\mathrm{e}x}}{\mathrm{e}\cdot\mathrm{e}^{\mathrm{e}x}}=\frac{\mathrm{e}^{-1}}{\mathrm{e}}=\frac{1}{\mathrm{e}^{2}} $

故  $ \lim_{x\to+\infty}\varphi(x)=\frac{1}{e^{2}} $，选(D).

例 15.10 设  $ a > 0 $，函数  $ f(x) $ 在  $ [0, +\infty) $ 内连续有界。证明：微分方程  $ y' + ay = f(x) $ 的解在  $ [0, +\infty) $ 内有界。

☐ 分析 证明有界性，需先求出用定积分表示的积分曲线方程.

证

 $$ y=\mathrm{e}^{-\int a\mathrm{d}x}\left[\int f(x)\bullet\mathrm{e}^{\int a\mathrm{d}x}\mathrm{d}x+C\right]=\mathrm{e}^{-a x}\left[\int f(x)\bullet\mathrm{e}^{a x}\mathrm{d}x+C\right]=\mathrm{e}^{-a x}\left[\int_{0}^{x}f(t)\mathrm{e}^{a t}\mathrm{d}t+C\right], $$ 

由例 8.14 知  $ y(x) $ 在  $ [0, +\infty) $ 内有界.

## 4 伯努利方程（仅数学一）（数学二、数学三考纲不作要求，但应会用换元法）

形如

 $$ \frac{\mathrm{d}y}{\mathrm{d}x}+p(x)y=q(x)y^{n}(n\neq0,\;1) $$ 

的方程叫作伯努利方程，其中 $ p(x) $， $ q(x) $为已知的连续函数。其解法为

①先变形为  $ y^{-n} \cdot \frac{dy}{dx} + p(x)y^{1-n} = q(x) $;

②令  $ z = y^{1-n} $，得  $ \frac{dz}{dx} = (1-n)y^{-n} \frac{dy}{dx} $，则  $ \frac{1}{1-n} \frac{dz}{dx} + p(x)z = q(x) $;

③解此一阶线性微分方程即可.

例 15.11 求  $ y\mathrm{d}x=(1+x\ln y)x\mathrm{d}y(y>0) $ 的通解.

(2)分析)与例15.8类似，无法直接计算 $ \frac{dy}{dx}=\frac{y}{(1+x\ln y)x} $，应对调x与y的“角色”，才能拆分成常见形式.

解 方程变形为  $ \frac{dx}{dy} - \frac{1}{y}x = \frac{\ln y}{y}x^{2} $，这是以 y 为自变量，x 为未知函数的伯努利方程（如果以 x 为自变量，y 为未知函数来解方程，是极其困难的，所以当我们遇到困难时，要学会 “换位思考”——x 与 y 谁作为自变量，谁作为未知函数是可以互换的）.