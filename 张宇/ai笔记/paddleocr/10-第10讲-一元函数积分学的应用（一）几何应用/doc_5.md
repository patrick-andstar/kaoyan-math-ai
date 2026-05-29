 $$ V=\int_{0}^{\pi}\pi y^{2}(x)\mathrm{d}x=\int_{0}^{\pi}\pi\mathrm{e}^{-x}\sin x\mathrm{d}x\xlongequal{ 见注 }\frac{1}{2}\pi(1+\mathrm{e}^{-\pi}). $$ 

 $$ \int_{0}^{\pi}\pi\mathrm{e}^{-x}\sin x\mathrm{d}x=\frac{\pi}{2}\left|\begin{matrix}(\mathrm{e}^{-x})^{\prime}&(\sin x)^{\prime}\\ \mathrm{e}^{-x}&\sin x\end{matrix}\right|_{0}^{\pi}=-\frac{\pi}{2}(\cos x+\sin x)\mathrm{e}^{-x}\bigg|_{0}^{\pi}=\frac{\pi}{2}(\mathrm{e}^{-\pi}+1) $$ 

(2) 曲线  $ y = y(x) $ 与 x = a,  $ x = b (0 \leq a < b) $ 及 x 轴围成的曲边梯形绕 y 轴旋转一周所得到的旋转体的体积为

 $$ V_{y}=2\pi\int_{a}^{b}x\left|y(x)\right|\mathrm{d}x\quad. $$ 

注 公式 (*) 有时用起来很方便，现简单推导如下（微元法）：

取  $ [x, x + \Delta x](\Delta x > 0) $，得到一个小竖条，如图10-5的阴影区域所示，此小竖条绕着y轴旋转一周，成为一个“圆柱壳”，将其沿任何一条竖线“切开”，可展开为一个“长方体”，其体积为

 $$ \mathrm{d}V_{y}=2\pi x\mid y(x)\mid\mathrm{d}x\;, $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_520_540_784_734.jpg" alt="Image" width="25%" /></div>


 $ V_y = 2\pi \int_a^b x |y(x)| \, dx. $

柱壳法



<div style="text-align: center;"><img src="imgs/img_in_image_box_790_557_912_711.jpg" alt="Image" width="11%" /></div>


<div style="text-align: center;">图 10-5</div>


总结  $ V_{x}=\pi\int_{a}^{b}\Box^{2}dx, $

 $ V_{y}=2\pi\int_{a}^{b}x\left|\Box\right|dx $

<div style="text-align: center;"><img src="imgs/img_in_image_box_188_812_490_907.jpg" alt="Image" width="29%" /></div>


“前世今生”，见例1.2.

例 10.6 设函数  $  f(x)  $ 的定义域为  $  (0, +\infty)  $，且满足  $  2f(x) + x^2f\left(\frac{1}{x}\right) = \frac{x^2 + 2x}{\sqrt{1 + x^2}}  $. 求  $  f(x)  $，并求曲线  $  y = f(x)  $，直线  $  y = \frac{1}{2}  $， $  y = \frac{\sqrt{3}}{2}  $ 及  $  y  $ 轴所围图形绕  $  x  $ 轴旋转一周所成旋转体的体积.

♡分析 ①x与y地位交换，求出 $ y=f(x)\Rightarrow x=\varphi(y) $.

<div style="text-align: center;"><img src="imgs/img_in_image_box_275_1108_486_1259.jpg" alt="Image" width="20%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_525_1108_709_1258.jpg" alt="Image" width="17%" /></div>


②套  $ V_{y} $ 体积公式，y 作自变量，x 作因变量，有  $ V_{y}=\int_{\frac{1}{2}}^{\frac{\sqrt{3}}{2}}2\pi y\cdot\varphi(y)dy $

由例 1.2 知