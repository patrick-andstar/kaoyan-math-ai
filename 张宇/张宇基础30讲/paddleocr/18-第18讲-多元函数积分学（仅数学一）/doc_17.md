 $$ \begin{aligned}I&=\iiint\limits_{x^{2}+4y^{2}+z^{2}\leq1}(1-x^{2}-4y^{2}-z^{2})\mathrm{d}x\mathrm{d}y\mathrm{d}z\\&=\iiint\limits_{x_{1}^{2}+y_{1}^{2}+z_{1}^{2}\leq1}(1-x_{1}^{2}-y_{1}^{2}-z_{1}^{2})\frac{1}{2}\mathrm{d}x_{1}\mathrm{d}y_{1}\mathrm{d}z_{1}\\&=\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{\pi}\mathrm{d}\varphi\int_{0}^{1}(1-r^{2})\frac{1}{2}r^{2}\sin\varphi\mathrm{d}r=\frac{4\pi}{15}\quad.\\ \end{aligned}\rightarrow\begin{aligned}x_{1}&=r\sin\varphi\cos\theta\\y_{1}&=r\sin\varphi\sin\theta.\end{aligned} $$ 

## 5 应用

(1) 若  $ \Omega $ 是物体所占的空间区域，则其体积为  $ V = \iiint_{\Omega} dv $

★(2)对于空间物体，若体密度为  $ \rho(x, y, z) $， $ \Omega $ 是物体所占的空间区域，则计算重心  $ (\bar{x}, \bar{y}, \bar{z}) $ 的公式为

 $$ \overline{x}=\frac{\iiint\limits_{\Omega}x\rho(x,y,z)\mathrm{d}v}{\iiint\limits_{\Omega}\rho(x,y,z)\mathrm{d}v},\quad\overline{y}=\frac{\iiint\limits_{\Omega}y\rho(x,y,z)\mathrm{d}v}{\iiint\limits_{\Omega}\rho(x,y,z)\mathrm{d}v},\quad\overline{z}=\frac{\iiint\limits_{\Omega}z\rho(x,y,z)\mathrm{d}v}{\iiint\limits_{\Omega}\rho(x,y,z)\mathrm{d}v}. $$ 

注 $ ^{(1)} $在考研的范畴内，重心就是质心。

(2) 当密度  $ \rho(x, y) $ 或者  $ \rho(x, y, z) $ 为常数时，重心就成了形心。

(3) 形心公式的逆用.

因子、分母、被积函数都有这个常数，故可约掉

由  $ \overline{x} = \frac{\iiint\limits_{\Omega} x \, \mathrm{d}v}{\iiint\limits_{\Omega} \, \mathrm{d}v} $，得  $ \iiint\limits_{\Omega} x \, \mathrm{d}v = \overline{x} \cdot V $，其中  $ V $ 为  $ \Omega $ 的体积。若  $ \overline{x} $ 与  $ V $ 均易于求出，则可快速计算出  $ \iiint\limits_{\Omega} x \, \mathrm{d}v $，以下同理。

由  $ \overline{y} = \frac{\iiint\limits_{\Omega} y \, \mathrm{d}v}{\iiint\limits_{\Omega} \, \mathrm{d}v} $，得  $ \iiint\limits_{\Omega} y \, \mathrm{d}v = \overline{y} \cdot V $，其中  $ V $ 为  $ \Omega $ 的体积。

由  $ \overline{z} = \frac{\iiint\limits_{\Omega} z \, \mathrm{d}v}{\iiint\limits_{\Omega} \mathrm{d}v} $，得  $ \iiint\limits_{\Omega} z \, \mathrm{d}v = \overline{z} \cdot V $，其中  $ V $ 为  $ \Omega $ 的体积。

(3)对于空间物体，若体密度为  $ \rho(x,y,z) $， $ \Omega $ 是物体所占的空间区域，则计算该物体对 x 轴、y 轴、z 轴和原点 O 的转动惯量  $ I_{x}, I_{y}, I_{z} $ 和  $ I_{0} $ 公式分别为

 $$ I_{x}=\iiint\limits_{\Omega}(y^{2}+z^{2})\rho(x,y,z)\mathrm{d}v,I_{y}=\iiint\limits_{\Omega}(z^{2}+x^{2})\rho(x,y,z)\mathrm{d}v, $$ 