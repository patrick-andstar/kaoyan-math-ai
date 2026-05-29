9.16 解 当  $ x \neq 0 $ 时，令 tx = u，则原式  $ = \frac{1}{x} \int_{0}^{x} f(u) \, du = f(x) + x \sin x $，即

 $$ \int_{0}^{x}f(u)\mathrm{d}u=x f(x)+x^{2}\sin x, $$ 

两边对x求导，得

 $$ f(x)=f(x)+xf^{\prime}(x)+2x\sin x+x^{2}\cos x, $$ 

即

 $$ f^{\prime}(x)=-2\sin x-x\cos x, $$ 

积分，得

 $$ \begin{aligned}f(x)&=2\cos x-\int x\mathrm{d}(\sin x)=2\cos x-x\sin x-\cos x+C\\&=\cos x-x\sin x+C\end{aligned} $$ 

当x=0时，上式 $ f(0) $仍满足题干.

注 不要把  $ \int_{0}^{1} f(tx) dt $ 误认为定积分.

9.17 解 当  $ x \leq 0 $ 时，

 $$ f(x)=\int_{0}^{1}t(t-x)\mathrm{d}t=\frac{1}{3}-\frac{x}{2} $$ 

当 $ 0<x\leq1 $时，

 $$ \begin{aligned}f(x)&=\int_{0}^{x}t(x-t)\mathrm{d}t+\int_{x}^{1}t(t-x)\mathrm{d}t\\&=\frac{1}{3}-\frac{x}{2}+\frac{x^{3}}{3}\;;\end{aligned} $$ 

当x>1时，

 $$ f(x)=\int_{0}^{1}t(x-t)\mathrm{d}t=\frac{x}{2}-\frac{1}{3}, $$ 

则

 $$ f^{\prime}(x)=\begin{cases}-\frac{1}{2},&x<0,\\x^{2}-\frac{1}{2},&0<x<1,\\\frac{1}{2},&x>1.\end{cases} $$ 

又

 $$ f_{-}^{\prime}(0)=\lim_{x\to0^{-}}\frac{\frac{1}{3}-\frac{x}{2}-\frac{1}{3}}{x-0}=-\frac{1}{2},f_{+}^{\prime}(0)=\lim_{x\to0^{+}}\frac{\frac{1}{3}-\frac{x}{2}+\frac{x^{3}}{3}-\frac{1}{3}}{x-0}=-\frac{1}{2}, $$ 

可知 $ f_{-}^{\prime}(0)=f_{+}^{\prime}(0) $，故 $ f^{\prime}(0)=-\frac{1}{2} $