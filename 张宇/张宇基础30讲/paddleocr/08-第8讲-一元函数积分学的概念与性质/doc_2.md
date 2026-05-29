(A)  $ F(x)=\begin{cases}\ln\left(\sqrt{1+x^2}-x\right), & x\leq0,\ $ x+1)\cos x-\sin x, & x>0\end{cases} $

(B)  $ F(x)=\begin{cases}\ln\left(\sqrt{1+x^2}-x\right)+1, & x\leq0,\ $ x+1)\cos x-\sin x, & x>0\end{cases} $

(C)  $ F(x)=\begin{cases}\ln\left(\sqrt{1+x^2}+x\right), & x\leq0,\ $ x+1)\sin x+\cos x, & x>0\end{cases} $

(D)  $ F(x)=\begin{cases}\ln\left(\sqrt{1+x^2}+x\right)+1, & x\leq0,\ $ x+1)\sin x+\cos x, & x>0\end{cases} $

♡分析  $ F'(x) = f(x) $. 由  $ f(x) $ 处处有定义得  $ F(x) $ 处处可导，推出  $ F(x) $ 处处连续.

解 应选(D).

对于选项(A):  $ \lim_{x\to0^-}F(x)=0 $， $ \lim_{x\to0^+}F(x)=1 $，由于 $ F(x) $在x=0处左右极限不同，故 $ F(x) $不连续。

对于选项(C):  $ \lim_{x\to0^-}F(x)=0 $， $ \lim_{x\to0^+}F(x)=1 $，由于 $ F(x) $在x=0处左右极限不同，故 $ F(x) $不连续。

由  $ F'(x) = f(x) $ 知， $ F(x) $ 必连续，故可排除(A)，(C).

对于选项(B): 当 x > 0 时,  $ F'(x) = \cos x - (x + 1) \sin x - \cos x = -(x + 1) \sin x \neq (x + 1) \cos x $, 故可排除(B)

因此选(D).

## 2 原函数（不定积分）存在定理

(1) 连续函数  $  f(x)  $ 必有原函数  $  F(x)  $ 。不作要求，但最好在草稿本上写一遍，大致思路要懂

注 证明：如果函数 $ f(x) $在 $ [a,b] $上连续，则函数 $ F(x)=\int_{a}^{x}f(t)dt $在 $ [a,b] $上可导，且 $ \frac{F'(x)=f(x)}{x} $。证 若 $ x\in(a,b) $，取 $ \Delta x $使 $ x+\Delta x\in(a,b) $，则 说明 $ \int f(x)dx=\int_{a}^{x}f(t)dt+C $

 $$ \begin{aligned}\Delta F&=F(x+\Delta x)-F(x)=\int_{a}^{x+\Delta x}f(t)\mathrm{d}t-\int_{a}^{x}f(t)\mathrm{d}t\\&=\int_{a}^{x}f(t)\mathrm{d}t+\int_{x}^{x+\Delta x}f(t)\mathrm{d}t-\int_{a}^{x}f(t)\mathrm{d}t=\int_{x}^{x+\Delta x}f(t)\mathrm{d}t,\end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_794_869_937_974.jpg" alt="Image" width="13%" /></div>


使用积分中值定理，有 $ \int_{x}^{x+\Delta x} f(t) dt = f(\xi) \Delta x $，其中 $ \xi $介于 $ x $与 $ x+\Delta x $之间，当 $ \Delta x \to 0 $时， $ \xi \to x $，于是

 $$ F^{\prime}(x)=\lim_{\Delta x\to0}\frac{\Delta F}{\Delta x}=\lim_{\Delta x\to0}f(\xi)=\lim_{\xi\to x}f(\xi)=f(x) $$ 

若 x = a，取  $ \Delta x > 0 $，则同理可证  $ F_{+}^{\prime}(a) = f(a) $；若 x = b，取  $ \Delta x < 0 $，则同理可证  $ F_{-}^{\prime}(b) = f(b) $。

注意：当四则运算中出现不同形式的表达式时，需要化为统一的形式，本题借助了积分中值定理。

①  $ \int f(x)dx $ 称为不定积分，表示全体原函数。