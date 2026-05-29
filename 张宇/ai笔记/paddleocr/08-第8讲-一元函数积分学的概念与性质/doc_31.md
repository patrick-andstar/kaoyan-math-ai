## 解答

8.1 (C) 解 当  $ x \in \left(0, \frac{\pi}{2}\right) $ 时，  $ \sin x < x $ ，故  $ \frac{x}{\sin x} > 1 > \frac{\sin x}{x} $ ，则

 $$ I_{2}=\int_{0}^{\frac{\pi}{2}}\frac{x}{\sin x}\mathrm{d}x>\int_{0}^{\frac{\pi}{2}}\frac{\sin x}{x}\mathrm{d}x=I_{1}, $$ 

排除选项(A)和(B).

由第2讲“6. 注(2)⑧”可知，当 $ 0<x<\frac{\pi}{2} $时， $ \frac{\sin x}{x}>\frac{2}{\pi} $，则有

 $$ I_{1}=\int_{0}^{\frac{\pi}{2}}\frac{\sin x}{x}\mathrm{d}x>\int_{0}^{\frac{\pi}{2}}\frac{2}{\pi}\mathrm{d}x=1\quad. $$ 

故 $ (\mathrm{C}) $正确.

8.2 (B) 解 x=0 是  $ f(x) $ 的跳跃间断点，于是①错误；

 $ f(x) $ 在  $ [-1,1] $ 上有界且只有一个间断点，于是②正确；

在 $ f(x) $的跳跃间断点x=0处， $ F(x) $连续但不可导，于是③错误，④正确.

注 进一步，本题的 $ f(x)=\begin{cases}x,&x<0,\\\frac{1}{2},&x=0,\\1,&x>0\end{cases} $，可由 $ \lim_{t\to0^{+}}\frac{x+\mathrm{e}^{\frac{x}{t}}}{1+\mathrm{e}^{\frac{x}{t}}} $获得，即 $ f(x)=\lim_{t\to0^{+}}\frac{x+\mathrm{e}^{\frac{x}{t}}}{1+\mathrm{e}^{\frac{x}{t}}} $

8.3 (C) 解 此积分为有一个瑕点 x=0 的无穷区间上的反常积分，可写为

 $$ \int_{0}^{+\infty}\frac{\ln x}{(1+x)x^{1-p}}\mathrm{d}x=\int_{0}^{1}\frac{\ln x}{(1+x)x^{1-p}}\mathrm{d}x+\int_{1}^{+\infty}\frac{\ln x}{(1+x)x^{1-p}}\mathrm{d}x\quad. $$ 

对任意  $ \varepsilon > 0 $ ，有

 $$ \lim_{x\to0^{+}}\frac{\frac{\ln x}{(1+x)x^{1-p}}}{\frac{1}{x^{1-p+\varepsilon}}}=\lim_{x\to0^{+}}x^{\varepsilon}\ln x=0, $$ 

若 $ \int_{0}^{1}\frac{1}{x^{1-p+\varepsilon}}dx $收敛，即1-p<1,p>0，则 $ \int_{0}^{1}\frac{\ln x}{(1+x)x^{1-p}}dx $也收敛.

对任意  $ \varepsilon > 0 $ ，有

 $$ \lim_{x\to+\infty}\frac{\frac{\ln x}{(1+x)x^{1-p}}}{\frac{1}{x^{2-p-\varepsilon}}}=\lim_{x\to+\infty}\frac{\ln x}{x^{\varepsilon}}=0, $$ 