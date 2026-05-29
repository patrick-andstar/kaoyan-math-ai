♡分析 缺x与y，属于(3)中的情形，则令 $ y' = p $， $ y'' = p' $

解 令  $ y' = p $，则  $ y'' = p' $，代入题干微分方程得

 $$ p^{\prime}=p(1+p^{2}), $$ 

分离变量得

 $$ \frac{\mathrm{d}p}{p(1+p^{2})}=\mathrm{d}x\ , $$ 

两边积分得

 $$ \ln\frac{p^{2}}{1+p^{2}}=2x+\ln C_{1}(C_{1}>0). $$ 

由题意有  $ y'(0)=1 $ ，即当 x=0 时 p=1 ，代入上式得  $ C_{1}=\frac{1}{2} $ ，于是有

 $$ y^{\prime}=p=\frac{\frac{\mathrm{e}^{x}}{\sqrt{2}}}{\sqrt{1-\frac{1}{2}\mathrm{e}^{2x}}}, $$ 

两边积分得

 $$ y=\int\frac{\frac{\mathbf{e}^{x}}{\sqrt{2}}}{\sqrt{1-\left(\frac{\mathbf{e}^{x}}{\sqrt{2}}\right)^{2}}}\mathrm{d}x=\arcsin\frac{\mathbf{e}^{x}}{\sqrt{2}}+C_{2}. $$ 

由题意有  $ y(0)=0 $ ，代入上式得  $ C_{2}=-\frac{\pi}{4} $ ，所以  $ y=\arcsin\frac{e^{x}}{\sqrt{2}}-\frac{\pi}{4} $

例 15.13 求微分方程  $ yy'' - \frac{2}{3}(y')^2 = 0 $ 满足  $ y(0) = 0 $ 的解.

分析缺x，属于(2)中的情形，则令 $ y^{\prime}=p $， $ y^{\prime\prime}=p\frac{dp}{dy} $

解 令  $ y' = p $，则  $ y'' = \frac{dp}{dy} \cdot p $，于是  $ y \cdot \frac{dp}{dy} \cdot p - \frac{2}{3}p^2 = 0 $，分离变量，得  $ \frac{dp}{p} = \frac{2}{3} \frac{dy}{y} (p \neq 0) $，两边积分得

 $$ \ln\left|p\right|=\frac{2}{3}\ln\left|y\right|+\ln C_{0} $$ 

即

 $$ |p|=C_{0}\left|y\right|^{\frac{2}{3}}, $$ 

 $$ p=\pm C_{0}y^{\frac{2}{3}}=C_{1}y^{\frac{2}{3}}, $$ 

即  $ \frac{dy}{y^{\frac{2}{3}}}=C_{1}dx $，两边积分，得  $ 3y^{\frac{1}{3}}=C_{1}x+C_{2} $