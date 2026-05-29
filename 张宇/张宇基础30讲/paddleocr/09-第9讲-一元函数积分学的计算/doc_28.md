9.8 解 因为不满足凑微分法的条件，所以要用分部积分法.

方法一

 $$ \begin{aligned}\int\frac{\arctan\mathrm{e}^{x}}{\mathrm{e}^{x}}\mathrm{d}x&=-\int\arctan\mathrm{e}^{x}\mathrm{d}(\mathrm{e}^{-x})=-\mathrm{e}^{-x}\arctan\mathrm{e}^{x}+\int\frac{\mathrm{d}x}{1+\mathrm{e}^{2x}}\\ &=-\mathrm{e}^{-x}\arctan\mathrm{e}^{x}+\int\left(1-\frac{\mathrm{e}^{2x}}{1+\mathrm{e}^{2x}}\right)\mathrm{d}x\\ &=-\mathrm{e}^{-x}\arctan\mathrm{e}^{x}+x-\frac{1}{2}\ln(1+\mathrm{e}^{2x})+C.\\ \end{aligned} $$ 

方法二 令  $ e^{x}=t $ ，则

 $$ \begin{aligned}\int\frac{\arctan\mathrm{e}^{x}}{\mathrm{e}^{x}}\mathrm{d}x&=\int\frac{\arctan t}{t^{2}}\mathrm{d}t=-\int\arctan t\mathrm{d}\left(\frac{1}{t}\right)=-\frac{1}{t}\arctan t+\int\frac{\mathrm{d}t}{t(1+t^{2})}\\&=-\frac{1}{t}\arctan t+\int\frac{\mathrm{d}t}{t}-\int\frac{t\mathrm{d}t}{1+t^{2}}=-\frac{1}{t}\arctan t+\ln t-\frac{1}{2}\ln(1+t^{2})+C\\&=-\frac{1}{\mathrm{e}^{x}}\arctan\mathrm{e}^{x}+x-\frac{1}{2}\ln(1+\mathrm{e}^{2x})+C.\end{aligned} $$ 

9.9 解 设  $ f(x)=\max\{1,|x|\} $，则

 $$ f(x)=\begin{cases}-x,&x<-1,\\1,&-1\leq x\leq1,\\x,&x>1.\end{cases} $$ 

由于 $ f(x) $在 $ (-∞,+∞) $上连续，因此必存在原函数 $ F(x) $，即

 $$ F(x)=\begin{cases}-\frac{x^{2}}{2}+C_{1},&x<-1,\\x+C_{2},&-1\leq x\leq1,\\\frac{x^{2}}{2}+C_{3},&x>1,\end{cases} $$ 

又  $ F(x) $ 在  $ (-∞, +∞) $ 上处处连续，可得  $ \left\{\begin{aligned}-\frac{1}{2}+C_{1}&=-1+C_{2},\\1+C_{2}&=\frac{1}{2}+C_{3},\end{aligned}\right. $ 令  $ C_{1}=C $，则可得  $ C_{2}=\frac{1}{2}+C $， $ C_{3}=1+C $．故

原式= $ \begin{cases}-\dfrac{x^{2}}{2}+C,&x<-1,\\x+\dfrac{1}{2}+C,&-1\leqslant x\leqslant1,\\\dfrac{x^{2}}{2}+1+C,&x>1.\end{cases} $

注 事实上，本题是一个分段函数的不定积分，这类问题的关键是分段求出每段上的原函数后，适当调整每一段上的常数使其原函数在分段函数的分段点处连续.