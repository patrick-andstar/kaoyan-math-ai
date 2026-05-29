设  $ S(x)=\sum_{n=2}^{\infty}n(n-1)x^{n-2}=\left(\sum_{n=0}^{\infty}x^{n}\right)^{n}=\frac{2}{(1-x)^{3}},|x|<1 $ ，则

 $$ \sum_{n=2}^{\infty}n(n-1)x^{n}=\frac{2x^{2}}{(1-x)^{3}},\sum_{n=2}^{\infty}n(n-1)\left(-\frac{1}{2}\right)^{n}=\frac{4}{27}, $$ 

所以

 $$ \sum_{n=0}^{\infty}\frac{(-1)^{n}(n^{2}-n+1)}{2^{n}}=\frac{4}{27}+\frac{2}{3}=\frac{22}{27}. $$ 

16.15 解

 $$ f(x)=\frac{1}{x^{2}-3x+2}=\frac{1}{1-x}-\frac{1}{2-x}=\frac{1}{1-x}-\frac{1}{2}\cdot\frac{1}{1-\frac{x}{2}} $$ 

由麦克劳林展开式知

 $$ \frac{1}{1-x}=1+x+x^{2}+\cdots+x^{n}+\cdots=\sum_{n=1}^{\infty}x^{n-1},\;x\in(-1,\;1), $$ 

 $$ \frac{1}{1-\frac{x}{2}}=1+\frac{x}{2}+\left(\frac{x}{2}\right)^{2}+\cdots+\left(\frac{x}{2}\right)^{n}+\cdots=\sum_{n=1}^{\infty}\left(\frac{x}{2}\right)^{n-1},x\in(-2,2), $$ 

从而有

 $$ \begin{aligned}f(x)&=\frac{1}{x^{2}-3x+2}=\sum_{n=1}^{\infty}x^{n-1}-\frac{1}{2}\sum_{n=1}^{\infty}\left(\frac{x}{2}\right)^{n-1}\\&=\sum_{n=1}^{\infty}\left(1-\frac{1}{2^{n}}\right)x^{n-1},x\in(-1,1)\text{．}\\ \end{aligned} $$ 

16.16 解 (1) 特征方程为  $ r^{2}-r-2=0 $ ，得  $ r_{1}=-1, r_{2}=2 $ ，故通解为

 $$ f(x)=C_{1}\mathbf{e}^{-x}+C_{2}\mathbf{e}^{2x}. $$ 

由 $ f(0)=0,\ f'(0)=1 $，得

 $$ \begin{cases}C_{1}+C_{2}=0,\\-C_{1}+2C_{2}=1,\end{cases} $$ 

故  $ C_{1}=-\frac{1}{3} $， $ C_{2}=\frac{1}{3} $，所以

 $$ f(x)=-\frac{1}{3}\mathrm{e}^{-x}+\frac{1}{3}\mathrm{e}^{2x}. $$ 

(2)

 $$ \begin{aligned}f(x)&=\sum_{n=0}^{\infty}\frac{a_{n}}{n!}x^{n}=-\frac{1}{3}\mathrm{e}^{-x}+\frac{1}{3}\mathrm{e}^{2x}=-\frac{1}{3}\sum_{n=0}^{\infty}\frac{(-x)^{n}}{n!}+\frac{1}{3}\sum_{n=0}^{\infty}\frac{(2x)^{n}}{n!}\\&=-\frac{1}{3}\sum_{n=0}^{\infty}\frac{(-1)^{n}x^{n}}{n!}+\frac{1}{3}\sum_{n=0}^{\infty}\frac{2^{n}\cdot x^{n}}{n!}\end{aligned} $$ 