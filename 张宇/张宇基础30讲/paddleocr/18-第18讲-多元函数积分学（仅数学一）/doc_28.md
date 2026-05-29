②球面  $ x^{2} + y^{2} + z^{2} = a^{2} $ 的 dS =  $ \frac{a}{\sqrt{a^{2} - x^{2} - y^{2}}} $ dxdy

③锥面  $ z=\sqrt{x^{2}+y^{2}} $ 的  $ \mathrm{d}S=\sqrt{2}\mathrm{d}x\mathrm{d}y $

例 18.13 设  $ \Sigma $ 为椭球面  $ \frac{x^2}{2} + \frac{y^2}{2} + z^2 = 1 $ 的上半部分，点  $ P(x, y, z) \in \Sigma $， $ \pi $ 为  $ \Sigma $ 在点  $ P $ 处的切平面， $ \rho(x, y, z) $ 为点  $ O(0, 0, 0) $ 到平面  $ \pi $ 的距离，求  $ \iint_{\Omega(x, y, z)} \mathrm{d}S $。

分析 ①求  $ \rho(x,y,z) $; ②代入  $ \iint_{\Sigma}\frac{z}{\rho}dS $

由第17讲的“四、2.(1)”，令 $ F(x,y,z)=\frac{x^{2}}{2}+\frac{y^{2}}{2}+z^{2}-1 $，则 $ F_{x}^{\prime}=x $， $ F_{y}^{\prime}=y $， $ F_{z}^{\prime}=2z $，故 $ \pi $的法向量为 $ (x,y,2z) $。 $ \pi $的方程为 $ x(X-x)+y(Y-y)+2z(Z-z)=0 $。又因为 $ P(x,y,z)\in\Sigma $，所以 $ \frac{x^{2}}{2}+\frac{y^{2}}{2}+z^{2}=1 $。代入 $ \pi $的方程化简可得 $ \frac{xX}{2}+\frac{yY}{2}+zZ=1 $。

解 设  $ (X, Y, Z) $ 为  $ \pi $ 上任意一点，则  $ \pi $ 的方程为

 $$ \frac{xX}{2}+\frac{yY}{2}+zZ=1 $$ 

从而知

 $$ \begin{aligned}\rho(x,\ y,\ z)=&\frac{\left|0+0+0-1\right|}{\sqrt{\left(\frac{x}{2}\right)^{2}+\left(\frac{y}{2}\right)^{2}+z^{2}}}=\left(\frac{x^{2}}{4}+\frac{y^{2}}{4}+z^{2}\right)^{\frac{1}{2}}.\\&z=\sqrt{1-\left(\frac{x^{2}}{2}+\frac{y^{2}}{2}\right)},\\\end{aligned} $$ 

由

二代，把z换了，得  $ \rho=\left(1-\frac{x^{2}}{4}-\frac{y^{2}}{4}\right)^{\frac{1}{2}} $

有

 $$ \frac{\partial z}{\partial x}=\frac{-x}{2\sqrt{1-\left(\frac{x^{2}}{2}+\frac{y^{2}}{2}\right)}},\frac{\partial z}{\partial y}=\frac{-y}{2\sqrt{1-\left(\frac{x^{2}}{2}+\frac{y^{2}}{2}\right)}}, $$ 

于是

 $$ \begin{aligned}&\mathrm{d}S=\sqrt{1+\left(\frac{\partial z}{\partial x}\right)^{2}+\left(\frac{\partial z}{\partial y}\right)^{2}}\mathrm{d}\sigma=\sqrt{1+\frac{x^{2}}{4\left(1-\frac{x^{2}}{2}-\frac{y^{2}}{2}\right)}+\frac{y^{2}}{4\left(1-\frac{x^{2}}{2}-\frac{y^{2}}{2}\right)}}\mathrm{d}\sigma\\ &\\&=\sqrt{\frac{4-2x^{2}-2y^{2}+x^{2}+y^{2}}{4\left(1-\frac{x^{2}}{2}-\frac{y^{2}}{2}\right)}}\mathrm{d}\sigma=\frac{\sqrt{4-x^{2}-y^{2}}}{2\sqrt{1-\left(\frac{x^{2}}{2}+\frac{y^{2}}{2}\right)}}\mathrm{d}\sigma,\xrightarrow{}\mathrm{d}S 有时可与被积函数钩掉 \\ \end{aligned} $$ 

所以

 $$ \iint_{\Sigma}\frac{z\mathrm{d}S}{\rho(x,y,z)}=\frac{1}{4}\iint_{D_{xy}}(4-x^{2}-y^{2})\mathrm{d}\sigma=\frac{1}{4}\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{\sqrt{2}}(4-r^{2})r\mathrm{d}r=\frac{3}{2}\pi, $$ 

其中 $ D_{xy}=\left\{(x,y)\mid x^{2}+y^{2}\leqslant2\right\} $