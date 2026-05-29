(A) 0          (B) dx          (C) 2dx         (D) 3dx

分析 概念题，转化成导数  $ \frac{dy}{dx} $ 代入数值即可.

解 应选(B).

由  $ \Delta y = \frac{y \Delta x}{x + \sqrt{x^2 + y^2}} + o(\Delta x) $，知  $ \frac{dy}{dx} = y' = \frac{y}{x + \sqrt{x^2 + y^2}} $，又  $ f(0) = 1 $，可得  $ y'(0) = 1 $，进而  $ \left. dy \right|_{x=0} = y'(0) dx = dx $，应选 (B).

例 3.11 设函数  $  f(u)  $ 可导，且  $  y = f(x^2)  $，当自变量  $ x $ 在  $ x = -1 $ 处取得增量  $ \Delta x = -0.1 $ 时，相应的函数增量  $ \Delta y $ 的线性主部为 0.1，则  $  f'(1) =  $（ ）。

(A)  $ -1 $

(B) 0.1

(C) 0.5

(D) 1

♡分析 概念题. 对复合函数  $ y = f[g(x)] $ 求导，有  $ y' = f'[g(x)] \cdot g'(x) $.

必背公式来源： $ \Delta y = A\Delta x + o(\Delta x) $，其中  $ dy = A\Delta x = y' $ dx 为线性主部。

解 应选(C).

本题依然是考查微分的定义。函数的微分是函数增量的线性主部，且  $ dy = y' \, dx = y' \Delta x $，而

 $$ \mathrm{d}y=f^{\prime}(x^{2})\mathrm{d}(x^{2})=2xf^{\prime}(x^{2})\mathrm{d}x=2xf^{\prime}(x^{2})\Delta x, $$ 

因此，由  $ 0.1 = -2f'(1) \cdot (-0.1) $，可得  $ f'(1) = 0.5 $，故选 (C).

题一练 设函数 $ f(x) $在 $ x=1 $处可导，且 $ \Delta f(1) $是 $ f(x) $在增量为 $ \Delta x $时的函数值增量，则 $ \lim_{\Delta x \to 0} \frac{\Delta f(1) - \Delta f}{|x - 1|} = $（ ）.

(A)  $ f'(1) $ (B) 1 (C)  $ \infty $ (D) 0

♡分析  $ \Delta y = dy + o(\Delta x) $，则  $ \Delta y - dy = o(\Delta x) $，故  $ \Delta f(x) - d[f(x)] = o(\Delta x) $。

由于  $ \Delta f(1)=f(1+\Delta x)-f(1) $，故  $ \lim_{\Delta x\to0}\frac{\Delta f(1)}{\Delta x}=\lim_{\Delta x\to0}\frac{f(1+\Delta x)-f(1)}{\Delta x}=f'(1) $，又

 $$ \lim_{\Delta x\to0}\frac{\left.\mathrm{d}f\right|_{x=1}}{\Delta x}=\lim_{\Delta x\to0}\frac{f^{\prime}(1)\mathrm{d}x}{\Delta x}=\lim_{\Delta x\to0}\frac{f^{\prime}(1)\Delta x}{\Delta x}=f^{\prime}(1) $$ 

于是，原式 $ =f'(1)-f'(1)=0 $

注 在微分概念中，由  $ \Delta y = A\Delta x + o(\Delta x) $，得  $ \frac{dy = A\Delta x}{dx} $，故由  $ \Delta x = 1 \cdot \Delta x + o(\Delta x) $，得  $ dx = 1 \cdot \Delta x $，也就有  $ dy = A\Delta x = A dx $。