 $$ \lim_{x\to0}f(x)=\lim_{x\to0}\frac{1}{\mathrm{e}^{\frac{x}{x-1}}-1}=\infty, $$ 

 $$ \lim_{x\to1^{+}}f(x)=\lim_{x\to1^{+}}\frac{1}{\mathrm{e}^{\frac{x}{x-1}}-1}=0,\lim_{x\to1^{-}}f(x)=\lim_{x\to1^{-}}\frac{1}{\mathrm{e}^{\frac{x}{x-1}}-1}=-1, $$ 

故 x=0 是  $ f(x) $ 的第二类间断点，x=1 是  $ f(x) $ 的第一类间断点．故选 (D).

1.4 (B) 解 这是 “1” 型未定式，于是

 $$ f(x)=\lim_{t\to0}\left(1+\frac{\sin t}{x}\right)^{\frac{x}{t}}=\mathrm{e}^{\lim_{t\to0}\frac{x^{2}}{t}\cdot\left(1+\frac{\sin t}{x}-1\right)}=\mathrm{e}^{\lim_{t\to0}\frac{\sin t}{t}}=\mathrm{e}^{x},\quad x\neq0 $$ 

又 $ f(x) $在x=0处无定义，且 $ \lim_{x\to0}f(x)=\lim_{x\to0}e^x=1 $，故x=0是 $ f(x) $的可去间断点。选(B)。

1.5 (B) 分析 函数  $ f(x)=\lim_{n\to\infty}\frac{1+x}{1+x^{2n}} $ 是以 x 为自变量的函数，但是当  $ n\to\infty $ 求极限时，x 则被看成一个常数（参数），根据 x 的不同取值求出极限，求完极限后 x 又恢复变量的本来身份。

因为分式中有 $ x^{2n} $，所以应先把x=-1和x=1作为分段点将函数写成分段函数，然后讨论函数的间断点.

解 当 $ \left|x\right|<1 $时， $ \lim_{n\to\infty}x^{2n}=0 $，所以 $ f(x)=1+x $；当 $ \left|x\right|>1 $时， $ f(x)=\lim_{n\to\infty}\frac{1+x}{1+x^{2n}}=0 $．

又 $ f(1)=1,\ f(-1)=0 $，所以

 $$ f(x)=\lim_{n\to\infty}\frac{1+x}{1+x^{2n}}=\begin{cases}0,&x\leq-1,\\1+x,&-1<x<1,\\1,&x=1,\\0,&x>1.\end{cases} $$ 

由此可知x=1为间断点.故选(B).

 $$ 1.6\quad\frac{x}{1+nx}(n=1,2,3,\cdots)\quad 解 \quad f_{2}(x)=f[f_{1}(x)]=\frac{f_{1}(x)}{1+f_{1}(x)}=\frac{\frac{x}{1+x}}{1+\frac{x}{1+x}}=\frac{x}{1+2x}. $$ 

 $$ f_{3}(x)=f\left[f_{2}(x)\right]=\frac{f_{2}(x)}{1+f_{2}(x)}=\frac{\frac{x}{1+2x}}{1+\frac{x}{1+2x}}=\frac{x}{1+3x}, $$ 

由数学归纳法得 $ f_{n}(x)=\frac{x}{1+nx}(n=1,2,3,\cdots) $

1.7  $ \frac{1}{2} $ 解 原式  $ =\lim_{x\to0^{+}}\frac{1-\cos x}{x(1-\cos\sqrt{x})(1+\sqrt{\cos x})}=\lim_{x\to0^{+}}\frac{\frac{1}{2}x^{2}}{x\cdot\frac{1}{2}x\cdot(1+\sqrt{\cos x})}=\frac{1}{2} $