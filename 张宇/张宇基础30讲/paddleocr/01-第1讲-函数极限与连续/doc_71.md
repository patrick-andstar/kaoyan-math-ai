注 若想到了例 1.22 的 “当  $ x \to 0 $ 时， $ 1 - \cos^a x \sim \frac{a}{2} x^2 $， $ a \neq 0 $”，则解题就更简单了。

1.8  $ e^{3} $ 解  $ \lim_{x\to\infty}\left(\frac{x+2}{x-1}\right)^{x}=\lim_{x\to\infty}\left(\frac{1+\frac{2}{x}}{1-\frac{1}{x}}\right)^{x}=\frac{\lim\limits_{x\to\infty}\left(1+\frac{2}{x}\right)^{x}}{\lim\limits_{x\to\infty}\left(1-\frac{1}{x}\right)^{x}}=\frac{e^{2}}{e^{-1}}=e^{3} $

注  $ \lim_{x\to\infty}\left(1+\frac{a}{x}\right)^{bx+d}=e^{ab} $ 是常用的公式.

相仿，

 $$ \lim_{x\to\infty}\left(\frac{x+a}{x-a}\right)^{x}=\lim_{x\to\infty}\left(\frac{1+\frac{a}{x}}{1-\frac{a}{x}}\right)^{x}=\frac{\lim\limits_{x\to\infty}\left(1+\frac{a}{x}\right)^{x}}{\lim\limits_{x\to\infty}\left(1-\frac{a}{x}\right)^{x}}=\mathrm{e}^{2a} $$ 

上述两种表达式变形是求极限运算的常见技巧，为固定模式的求解方法，应熟记。

1.9  $ \ln\frac{a}{b} $ 解 利用变量代换．令 $ \frac{1}{x}=t $，则

 $$ \lim_{x\to+\infty}x\left(a^{\frac{1}{x}}-b^{\frac{1}{x}}\right)=\lim_{t\to0^{+}}\frac{a^{t}-b^{t}}{t}=\lim_{t\to0^{+}}(a^{t}\ln a-b^{t}\ln b)=\ln\frac{a}{b}(a>0,b>0) $$ 

1.10 -2 解 因为  $ f(x) $ 在 x=0 处连续，所以  $ \lim_{x\to0^{+}}f(x)=\lim_{x\to0^{-}}f(x)=f(0) $. 又

 $$ \begin{aligned}\lim_{x\rightarrow0^{+}}f(x)&=\lim_{x\rightarrow0^{+}}\frac{1-\mathrm{e}^{\tan x}}{\arcsin\frac{x}{2}}=\lim_{x\rightarrow0^{+}}\frac{-\tan x}{\frac{x}{2}}=-2,\\\lim_{x\rightarrow0^{-}}f(x)&=\lim_{x\rightarrow0^{-}}a\mathrm{e}^{2x}=a,\end{aligned} $$ 

所以a=-2.

1.11 解  $ f(x+2\pi)=\arcsin[\sin(x+2\pi)]=\arcsin(\sin x)=f(x) $，故  $ f(x) $ 以  $ 2\pi $ 为周期。

当 $ x\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right) $时，有 $ \arcsin(\sin x)=x $;

当 $ x\in\left[\frac{\pi}{2},\pi\right) $时，有 $ \pi-x\in\left(0,\frac{\pi}{2}\right] $，则

 $$ \arcsin(\sin x)=\arcsin[\sin(\pi-x)]=\pi-x; $$ 

当 $ x\in\left[\pi,\frac{3}{2}\pi\right) $时，有 $ x-\pi\in\left[0,\frac{\pi}{2}\right) $，则

 $$ \arcsin(\sin x)=\arcsin[-\sin(x-\pi)]=\pi-x. $$ 