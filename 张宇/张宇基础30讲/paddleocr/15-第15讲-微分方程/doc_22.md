## 第15讲 微分方程

的坐标为 $ (x,y) $，P点坐标为 $ (0,Y) $，由 $ \left|PQ\right|=1 $，得

 $ x^{2}+(y-Y)^{2}=1 $，即 $ y-Y=\sqrt{1-x^{2}} $。 $ Y>y $。故取负值

由题意知，QP的方向就是曲线 $ y=y(x) $在 $ (x,y) $点的切线方向，故

 $$ \frac{\mathrm{d}y}{\mathrm{d}x}=\frac{y-Y}{x}=-\frac{\sqrt{1-x^{2}}}{x} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_810_130_963_346.jpg" alt="Image" width="14%" /></div>


两边积分得

<div style="text-align: center;">图 15-4</div>


 $ y = -\int \frac{\sqrt{1 - x^2}}{x} \, dx \xrightarrow{\quad} $ 此处注意到  $ x $ 与  $ \sqrt{1 - x^2} $ 的平方关系，也可令  $ m = x $， $ n = \sqrt{1 - x^2} $，利用合分比定理来计算，可省去三角换元以及还原

令 $ x=\sin t $，则

 $$ \begin{aligned}y&=-\int\frac{\sqrt{1-x^{2}}}{x}\mathrm{d}x=-\int\frac{\cos^{2}t}{\sin t}\mathrm{d}t\\ &=-\int\frac{1-\sin^{2}t}{\sin t}\mathrm{d}t\\ &=-\int\csc t\mathrm{d}t+\int\sin t\mathrm{d}t\\ &=-\ln\left|\csc t-\cot t\right|-\cos t+C\\ &=-\ln\left|\frac{1}{x}-\frac{\sqrt{1-x^{2}}}{x}\right|-\sqrt{1-x^{2}}+C\\ &=\ln\left|\frac{1}{x}+\frac{\sqrt{1-x^{2}}}{x}\right|-\sqrt{1-x^{2}}+C\\ &=\ln\frac{1+\sqrt{1-x^{2}}}{x}-\sqrt{1-x^{2}}+C.\\ \end{aligned} $$ 

由 x=1, y=0 ，可得 C=0 。故 Q 点的轨迹方程为

 $$ y=\ln\frac{1+\sqrt{1-x^{2}}}{x}-\sqrt{1-x^{2}}\quad. $$ 

注 追及点到被追及点的连线始终为该点的切线方向.

## 五 微分方程的物理应用（仅数学一、数学二）

<div style="text-align: center;"><img src="imgs/img_in_image_box_856_1191_960_1295.jpg" alt="Image" width="10%" /></div>


例 15.22 飞机在机场降落时，为了减少滑行距离，在触地的瞬间，飞机尾部张开减速伞，以增大阻力，使飞机迅速减速并停下.