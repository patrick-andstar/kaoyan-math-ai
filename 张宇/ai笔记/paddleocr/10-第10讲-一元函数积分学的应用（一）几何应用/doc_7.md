<div style="text-align: center;"><img src="imgs/img_in_image_box_410_129_588_264.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">图 10-7</div>


注 掌握住此结论，会套公式即可.

∅公式  $ \left|B^{3}\right| \equiv B\left|B^{2}\right| = B^{2}\left|B\right| $

例 10.7 过坐标原点作曲线  $ y = e^x $ 的切线，该切线与曲线  $ y = e^x $ 以及  $ x $ 轴围成的向  $ x $ 轴负向无限伸展的平面图形记为  $ D $。求：

(1) D 的面积 A;

(2) D 绕直线 x=1 旋转一周所成的旋转体的体积 V .

(♂) 先求切点与切线方程，进而套面积公式和旋转体体积公式.

解 设切点坐标为  $ P(x_{0}, y_{0}) $，于是曲线  $ y = e^{x} $ 在点 P 的切线斜率为

 $$ y^{\prime}(x_{0})=\mathrm{e}^{x_{0}}, $$ 

切线方程为

 $$ y-y_{0}=\mathbf{e}^{x_{0}}(x-x_{0}) $$ 

因为该切线经过点 $ (0,0) $，所以 $ -y_{0}=-x_{0}e^{x_{0}} $。又因为 $ y_{0}=e^{x_{0}} $，代入求得 $ x_{0}=1 $，从而 $ y_{0}=e^{x_{0}}=e $，切线方程为 $ y=ex $，如图10-8所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_696_747_915_899.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">图 10-8</div>


(1) 取水平条面积微元，则 D 的面积

若取竖直条面积微元：

 $$ \Delta S_{1}=\mathrm{e}^{x}\mathrm{d}x,\Delta S_{2}=(\mathrm{e}^{x}-\mathrm{e}x)\mathrm{d}x. $$ 

再积分： $  S = \int_{-\infty}^{0} e^{x} dx + \int_{0}^{1} (e^{x} - ex) dx  $

则较为麻烦，故不建议

 $$ \begin{aligned}&A=\int_{0}^{e}\left(\frac{y}{e}-\ln y\right)\mathrm{d}y\xrightarrow{}\left\{\begin{aligned}&\int\ln y\mathrm{d}y=y\ln y-\int y\cdot\frac{1}{y}\mathrm{d}y=y\ln y-y+C\\& 收敛的  反常积分 \end{aligned}\right.\\ &=\frac{1}{\mathrm{e}}\cdot\left.\frac{y^{2}}{2}\right|_{0}^{e}-(y\ln y-\left.\frac{y}{y}\right|_{0}^{e}\\ &=\frac{\mathrm{e}}{2}+\lim_{\underline{y\rightarrow0^{+}}}y\ln y=\frac{\mathrm{e}}{2}\quad.\\ \end{aligned} $$ 

(2) D 绕直线 x=1 旋转一周所成的旋转体的体积微元为

先取微元：用“大体积” - “小体积”  $ \mathrm{d}V = \left[\pi(1 - \ln y)^2 - \pi\left(1 - \frac{y}{\mathrm{e}}\right)^2\right]\mathrm{d}y $，

从而

<div style="text-align: center;"><img src="imgs/img_in_image_box_643_1261_923_1415.jpg" alt="Image" width="27%" /></div>
