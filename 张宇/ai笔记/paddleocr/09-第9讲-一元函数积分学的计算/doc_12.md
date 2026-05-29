 $$ x\equiv A(x^{2}+1)+(Bx+C)(x-1), $$ 

在 $ (*) $式中，令x=1，得 $ 1=2A $， $ A=\frac{1}{2} $；令x=0，得 $ 0=A-C $， $ C=\frac{1}{2} $。

比较 $ ^{*} $式两端 $ x^{2} $的系数，有 $ 0=A+B $，已求得 $ A=\frac{1}{2} $，故有 $ B=-\frac{1}{2} $。于是可得

 $$ \begin{aligned}\int\frac{x}{x^{3}-x^{2}+x-1}\mathrm{d}x&=\frac{1}{2}\int\frac{\mathrm{d}x}{x-1}-\frac{1}{2}\int\frac{x-1}{x^{2}+1}\mathrm{d}x\\&=\frac{1}{2}\ln|x-1|-\frac{1}{4}\ln(x^{2}+1)+\frac{1}{2}\arctan x+C_{1}\\&=\frac{1}{4}\ln\frac{(x-1)^{2}}{x^{2}+1}+\frac{1}{2}\arctan x+C_{1}.\end{aligned} $$ 

注 ①形如  $ R(\sin x, \cos x) $ 的有理式称为三角函数有理式 →有理函数

a. 令  $ t = \tan \frac{x}{2} $， $ \sin x = \frac{2t}{1 + t^{2}} $， $ \cos x = \frac{1 - t^{2}}{1 + t^{2}} $（万能公式），则有

 $$ \int R(\sin x,\cos x)\mathrm{d}x=\int R\left(\frac{2t}{1+t^{2}},\frac{1-t^{2}}{1+t^{2}}\right)\frac{2}{1+t^{2}}\mathrm{d}t=\int\frac{P_{n}(t)}{Q_{m}(t)}\mathrm{d}t $$ 

b. 若  $ R(\sin x, \cos x) = -R(-\sin x, \cos x) $，令  $ \cos x = t $ 凑微分。

 $ R(\sin x, \cos x) = -R(\sin x, -\cos x) $，令  $ \sin x = t $ 凑微分。

若  $ R(\sin x, \cos x) = R(-\sin x, -\cos x) $，令  $ \tan x = t $ 凑微分。

② $ \int f(\sqrt{a^{2}+x^{2}})\,\mathrm{d}x\xrightarrow{x=\tan t} $有理函数.

 $ \int f\left(\sqrt{\frac{ax+b}{cx+d}}\right)dx \xrightarrow{t=\sqrt{\frac{ax+b}{cx+d}}} $ 有理函数.

例9.10  $ \int\frac{2x+3}{x^{2}-x+1}dx= $ ___.

解 应填  $ \ln(x^{2}-x+1)+\frac{8\sqrt{3}}{3}\arctan\frac{2x-1}{\sqrt{3}}+C $

 $ \rightarrow $ 已是最简有理分式，请注意看接下来的积分方法

 $$ \begin{aligned}\int\frac{2x+3}{x^{2}-x+1}\mathrm{d}x=&\int\frac{2x-1+4}{x^{2}-x+1}\mathrm{d}x\xrightarrow{ 分子凑为 k( 分母 )}\int\frac{u^{\prime}}{u}\mathrm{d}x=\int\frac{\mathrm{d}u}{u}=\ln|u|+C\\=&\int\frac{1}{x^{2}-x+1}\mathrm{d}(x^{2}-x+1)+\int\frac{4}{x^{2}-x+1}\mathrm{d}x\\=&\ln(x^{2}-x+1)+4\int\frac{1}{x^{2}-x+1}\mathrm{d}x\end{aligned} $$ 