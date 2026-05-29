得

 $$ \begin{aligned}y&=\frac{1}{2}\int\ln(1+x^{2})\mathrm{d}(1+x^{2})=\frac{1}{2}\Biggl[\left(1+x^{2}\right)\ln(1+x^{2})-\int\frac{1+x^{2}}{1+x^{2}}\mathrm{d}(1+x^{2})\Biggr]\\ &=\frac{1}{2}(1+x^{2})[\ln(1+x^{2})-1]+C\xrightarrow{ 积分曲线（族 )}\end{aligned} $$ 

代入初始条件  $ y\big|_{x=0}=-\frac{1}{2} $ 得 C=0，故方程的特解为  $ y=\frac{1}{2}(1+x^{2})[\ln(1+x^{2})-1] $.

例 15.4 微分方程  $ \frac{ydy}{1+y^{2}} = \frac{dx}{x(1+x^{2})} $ 的解为 ___.

♡分析 已写成变量分离形式，也可写成  $ x(1+x^2)y dy = (1+y^2)dx $ 的形式考查。

解 应填 $ (1+x^{2})(1+y^{2})=Cx^{2} $，其中C为大于1的任意常数.

两边积分，得 $ \int\frac{ydy}{1+y^{2}}=\int\left(\frac{1}{x}-\frac{x}{1+x^{2}}\right)dx $，则

 $$ \frac{1}{2}\ln(1+y^{2})=\ln\left|x\right|-\frac{1}{2}\ln(1+x^{2})+\ln C_{1}, $$ 

即  $ \ln[(1+x^{2})(1+y^{2})]=\ln Cx^{2} $，故  $ (1+x^{2})(1+y^{2})=Cx^{2} $，其中 C 为大于 1 的任意常数。

注 (1) 为方便合并，不定积分后常加  $ \ln C $ 而非 C.

(2) 由本题的通解表达式可知，通解中的常数是指在一定范围内任意取值的常数，而未必是在实数范围内任意取值的常数.

(2) 换元后可分离.

形如  $ \frac{dy}{dx}=f(ax+by+c) $ 的方程，其中常数 a, b 全都不为零。其解法为令  $ u=ax+by+c $，则  $ \frac{du}{dx}=a+b\frac{dy}{dx} $，代入原方程得  $ \frac{du}{dx}=a+bf(u) $。

例 15.5 求微分方程  $ \mathrm{d}y = \sin(x + y + 100)\mathrm{d}x $ 的通解.

♡分析 无法分离变量，且含有x与y的线性组合，则作换元，即令 $ u=x+y+100 $

解 ①方程可写成  $ \frac{dy}{dx} = \sin(x + y + 100) $，令  $ u = x + y + 100 $，则  $ \frac{du}{dx} = 1 + \frac{dy}{dx} $，于是原方程化为  $ \frac{du}{dx} = 1 + \sin u $，就得到了可分离变量型微分方程。

②分离变量，得  $ \frac{du}{1+\sin u}=dx $，恒等变形，有  $ \frac{(1-\sin u)du}{1-\sin^2 u}=dx $，即  $ \left(\sec^2 u-\tan u\sec u\right)du=dx $。

两边积分，得  $ \tan u - \sec u = x + C $ 。将  $ u = x + y + 100 $ 代入，得原方程的通解为

 $$ \tan(x+y+100)-\sec(x+y+100)=x+C, $$ 

其中 C 为任意常数.