 $$ \begin{aligned}&\int_{0}^{1}\arcsin\sqrt{1-x^{2}}\mathrm{d}x\xlongequal{x=\cos t}\int_{-\frac{\pi}{2}}^{0}\arcsin(-\sin t)\bullet(-\sin t)\mathrm{d}t\\ &\\ =&\int_{-\frac{\pi}{2}}^{0}t\sin t\mathrm{d}t=-t\cos t\left|_{-\frac{\pi}{2}}^{0}+\sin t\right|_{-\frac{\pi}{2}}^{0}=1\quad.\\ \end{aligned} $$ 

 $$ \text{例 9.15}\quad\int_{0}^{1}x\arcsin\sqrt{4x-4x^{2}}\mathrm{d}x=\underline{\qquad}.\quad( 重要题源 ) $$ 

分析  $ \sqrt{4x-4x^{2}}=\sqrt{1^{2}-(1-2x)^{2}}\Rightarrow $ 三角函数代换，令  $ 1-2x=\cos t $（从头开始）

 $ \Rightarrow $ 令 1-2x=t（利用例 9.14 方法一的结论）.

解 应填 $ \frac{1}{2} $.

 $$ \int_{0}^{1}x\arcsin\sqrt{4x-4x^{2}}\mathrm{d}x=\int_{0}^{1}x\arcsin\sqrt{1-(1-2x)^{2}}\mathrm{d}x $$ 

 $$ \begin{aligned}&\frac{ 令 1-2x=t}{x=\frac{1}{2}(1-t)}\frac{1}{2}\int_{1}^{-1}(1-t)\arcsin\sqrt{1-t^{2}}\left(-\frac{1}{2}\mathrm{d}t\right)=\frac{1}{4}\int_{-1}^{1}(1-t)\arcsin\sqrt{1-t^{2}}\mathrm{d}t\\ &=\frac{1}{4}\int_{-1}^{1}\arcsin\sqrt{1-t^{2}}\mathrm{d}t-\frac{1}{4}\int_{-1}^{1}t\arcsin\sqrt{1-t^{2}}\mathrm{d}t\\ &=\frac{1}{2}\int_{0}^{1}\arcsin\sqrt{1-t^{2}}\mathrm{d}t,\\ \end{aligned} $$ 

由例 9.14 知， $ \int_{0}^{1}\arcsin\sqrt{1-t^{2}}dt=1 $，故原式  $ =\frac{1}{2} $.

例9.16 证明：若函数 $ f(x) $是以T为周期的连续函数，则对任意的实数a，都有

 $$ \int_{a}^{a+T}f(x)\mathrm{d}x=\int_{0}^{T}f(x)\mathrm{d}x\enspace. $$ 

证  $ \int_{a}^{a+T}f(x)\mathrm{d}x=\int_{a}^{0}f(x)\mathrm{d}x+\int_{0}^{T}f(x)\mathrm{d}x+\int_{T}^{a+T}f(x)\mathrm{d}x $

设 t = x - T，则

 $$ \int_{T}^{a+T}f(x)\mathrm{d}x=\int_{0}^{a}f(t+T)\mathrm{d}t=\int_{0}^{a}f(t)\mathrm{d}t=\int_{0}^{a}f(x)\mathrm{d}x, $$ 

所以

 $$ \int_{a}^{a+T}f(x)\mathrm{d}x=\int_{a}^{0}f(x)\mathrm{d}x+\int_{0}^{T}f(x)\mathrm{d}x+\int_{0}^{a}f(x)\mathrm{d}x=\int_{0}^{T}f(x)\mathrm{d}x\ . $$ 

注 若函数 $ f(x) $是连续且以T为周期的奇函数，则 $ \int_{0}^{T}f(x)dx=0 $

例9.17 设 $ f(x) $为连续函数，证明 $ \int_{a}^{b}f(x)dx=\int_{a}^{b}f(a+b-x)dx $

证 作变量代换，令  $ x = a + b - t $，则

 $$ \int_{a}^{b}f(x)\mathrm{d}x=\int_{b}^{a}f(a+b-t)(-\mathrm{d}t) $$ 