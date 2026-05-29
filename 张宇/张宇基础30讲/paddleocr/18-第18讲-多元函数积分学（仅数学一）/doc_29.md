## 5 应用

三重积分：形心最重要。

第一型曲面积分：曲面面积最重要

(1) 对于光滑曲面薄片  $ \Sigma $，若  $ \Sigma $ 由单值函数  $ z = z(x, y) $ 给出， $ D_{xy} $ 为曲面  $ \Sigma $ 在 xOy 面上的投影区域，则其面积

 $$ A=\iint\limits_{D_{xy}}\sqrt{1+\left(z_{x}^{\prime}\right)^{2}+\left(z_{y}^{\prime}\right)^{2}}\mathrm{d}x\mathrm{d}y. $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_825_198_946_342.jpg" alt="Image" width="11%" /></div>


注 同理，在同样保证单值函数的情况下，可向另外两个坐标面投影，得

 $$ A=\iint\limits_{D_{y z}}\sqrt{1+\left(x_{y}^{\prime}\right)^{2}+\left(x_{z}^{\prime}\right)^{2}}\mathrm{d}y\mathrm{d}z, $$ 

其中  $ \Sigma: x = x(y, z) $， $ D_{yz} $ 是曲面在 yOz 面上的投影区域；

 $$ A=\iint\limits_{D_{x}}\sqrt{1+\left(y_{z}^{\prime}\right)^{2}+\left(y_{x}^{\prime}\right)^{2}}\mathrm{d}z\mathrm{d}x, $$ 

其中  $ \Sigma: y = y(x, z) $， $ D_{zx} $ 是曲面在 zOx 面上的投影区域。

事实上，曲面面积就是当第一型曲面积分的被积函数是1时，用投影法所得出的积分，请大家注意这个联系。

(2)对于光滑曲面薄片Σ，若面密度为 $ \rho(x,y,z) $，则计算重心 $ (\overline{x},\overline{y},\overline{z}) $的公式为

 $$ \overline{x}=\frac{\iint\limits_{\Sigma}x\rho(x,y,z)\mathrm{d}S}{\iint\limits_{\Sigma}\rho(x,y,z)\mathrm{d}S},\overline{y}=\frac{\iint\limits_{\Sigma}y\rho(x,y,z)\mathrm{d}S}{\iint\limits_{\Sigma}\rho(x,y,z)\mathrm{d}S},\overline{z}=\frac{\iint\limits_{\Sigma}z\rho(x,y,z)\mathrm{d}S}{\iint\limits_{\Sigma}\rho(x,y,z)\mathrm{d}S}. $$ 

注 $ ^{(1)} $在考研的范畴内，重心就是质心。

(2) 当密度  $ \rho(x, y) $ 或者  $ \rho(x, y, z) $ 为常数时，重心就成了形心.

(3) 形心公式的逆用.

由  $ \overline{x} = \frac{\iint\limits_{\Sigma} x \, \mathrm{d}S}{\iint\limits_{\Sigma} 1 \, \mathrm{d}S} $，得  $ \iint\limits_{\Sigma} x \, \mathrm{d}S = \overline{x} \cdot A $，其中  $ A = \iint\limits_{\Sigma} 1 \, \mathrm{d}S $ 为曲面  $ \Sigma $ 的面积；

由  $ \overline{y}=\frac{\iint\limits_{\Sigma}y\mathrm{d}S}{\iint\limits_{\Sigma}1\mathrm{d}S} $，得  $ \iint\limits_{\Sigma}y\mathrm{d}S=\overline{y}\cdot A $，其中  $ A=\iint\limits_{\Sigma}1\mathrm{d}S $ 为曲面  $ \Sigma $ 的面积；

由  $ \overline{z} = \frac{\iint\limits_{\Sigma} z \, dS}{\iint\limits_{\Sigma} 1 \, dS} $，得  $ \iint\limits_{\Sigma} z \, dS = \overline{z} \cdot A $，其中  $ A = \iint\limits_{\Sigma} 1 \, dS $ 为曲面  $ \Sigma $ 的面积。