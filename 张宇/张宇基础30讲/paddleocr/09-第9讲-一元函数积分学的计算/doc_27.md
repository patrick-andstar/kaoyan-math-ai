9.2  $ \frac{\pi}{3} $ 解 定积分  $ \int_{0}^{1}f(x)dx $ 是一个常数，所以等式两端同时在  $ [0,1] $ 上对 x 进行积分得

 $$ \int_{0}^{1}f(x)\mathrm{d}x=\int_{0}^{1}\frac{1}{1+x^{2}}\mathrm{d}x+\int_{0}^{1}\left[x^{3}\int_{0}^{1}f(x)\mathrm{d}x\right]\mathrm{d}x, $$ 

即

 $$ \begin{aligned}\int_{0}^{1}f(x)\mathrm{d}x&=\arctan x\Big|_{0}^{1}+\int_{0}^{1}f(x)\mathrm{d}x\int_{0}^{1}x^{3}\mathrm{d}x\\&=\frac{\pi}{4}+\frac{1}{4}\int_{0}^{1}f(x)\mathrm{d}x,\end{aligned} $$ 

解得  $ \int_{0}^{1}f(x)dx=\frac{\pi}{3} $

9.3  $ \frac{1}{e^{2}} $ 解 原式 =  $ \lim_{x \to +\infty} \frac{\left(1 - \frac{1}{x}\right)^x \cdot e^{ex}}{e \cdot e^{ex}} = \frac{e^{-1}}{e} = \frac{1}{e^2} $.

9.4  $ 2 \ln x - \ln^{2} x + C $ 解 被积函数中有  $ f'(x) $，用分部积分法.

 $$ \int x f^{\prime}(x)\mathrm{d}x=\int x\mathrm{d}[f(x)]=x f(x)-\int f(x)\mathrm{d}x=x f(x)-\ln^{2}x+C, $$ 

其中

 $$ f(x)=\left(\ln^{2}x\right)^{\prime}=\frac{2\ln x}{x}, $$ 

于是

 $$ \int x f^{\prime}(x)\mathrm{d}x=2\ln x-\ln^{2}x+C. $$ 

9.5  $ 2\sqrt{x}\arcsin\sqrt{x}+2\sqrt{1-x}+C $ 解 去掉根号将会使计算变得简单. 令  $ \sqrt{x}=t, x=t^{2} $，则

 $$ \begin{aligned}\int\frac{\arcsin\sqrt{x}}{\sqrt{x}}\mathrm{d}x&=2\int t\bullet\frac{\arcsin t}{t}\mathrm{d}t=2\int\arcsin t\mathrm{d}t=2(t\arcsin t+\sqrt{1-t^{2}})+C\\&=2\sqrt{x}\arcsin\sqrt{x}+2\sqrt{1-x}+C\ .\end{aligned} $$ 

9.6  $ \frac{\pi}{3} $ 解 令  $ t = \sqrt{x - 2} $，则  $ x = t^{2} + 2 $， $ dx = 2t dt $。当 x = 2 时，t = 0；当  $ x \to +\infty $ 时， $ t \to +\infty $。

 $$ \int_{0}^{+\infty}\frac{2t\mathrm{d}t}{(t^{2}+9)t}=\lim_{b\to+\infty}\left(\frac{2}{3}\arctan\frac{t}{3}\right|_{0}^{b}=\frac{\pi}{3} $$ 

9.7 解 令  $ \arcsin\sqrt{\frac{x}{a+x}}=t,\quad x=\frac{a\sin^{2}t}{1-\sin^{2}t}=a\tan^{2}t $ ，于是

 $$ \begin{aligned}\int\arcsin\sqrt{\frac{x}{a+x}}\mathrm{d}x&=\int t\mathrm{d}(a\tan^{2}t)=at\tan^{2}t-a\int\tan^{2}t\mathrm{d}t\\&=at\tan^{2}t+a\int(1-\sec^{2}t)\mathrm{d}t=at\tan^{2}t+at-a\tan t+C\\&=(a+x)\arcsin\sqrt{\frac{x}{a+x}}-\sqrt{ax}+C.\end{aligned} $$ 