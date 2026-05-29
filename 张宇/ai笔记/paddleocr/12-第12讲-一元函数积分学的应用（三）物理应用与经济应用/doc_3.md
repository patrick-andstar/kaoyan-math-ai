→默认不流动水给的压力为静水压力

## 3 静水压力（水压力）

垂直浸没在水中的平板 ABCD (见图 12-4) 的一侧受到的水压力为

 $$ P=\rho g\int_{a}^{b}x[f(x)-h(x)]\mathrm{d}x, $$ 

其中  $ \rho $ 为水的密度，g 为重力加速度。

压力微元  $ \mathrm{d}P = \rho g x [f(x) - h(x)] \mathrm{d}x $，即图中矩形条所受到的压力 x 表示水深， $ f(x) - h(x) $ 是矩形条的宽度，dx 是矩形条的高度。

<div style="text-align: center;"><img src="imgs/img_in_image_box_658_139_956_410.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;">图 12-4</div>


注 水压力问题的特点：压强随水的深度的改变而改变，求解这类问题的关键是确定水深x处的平板的宽度 $ f(x)-h(x) $。

例 12.3 斜边长为 2a 的等腰直角三角形平板铅直地沉没在水中，且斜边与水面相齐。记重力加速度为 g，水的密度为  $ \rho $，则该平板一侧所受的水压力为 ___.

♡分析 建系、取微元、再积分即可.

解 应填 $ \frac{1}{3}a^{3}\rho g $

如图 12-5 所示，该平板一侧所受的水压力为

 $$ P=\int_{0}^{a}2\rho g(a-y)y\mathrm{d}y=2\rho g\int_{0}^{a}(a y-y^{2})\mathrm{d}y=2\rho g\left(\frac{a^{3}}{2}-\frac{a^{3}}{3}\right)=\frac{1}{3}a^{3}\rho g. $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_360_899_694_1097.jpg" alt="Image" width="32%" /></div>


<div style="text-align: center;">图 12-5</div>


## 4 引力

设有一长度为 l、线密度为常数  $ \mu $ 的细棒，在与细棒右端的距离为 a 处有一质量为 m 的质点 M（见图 12-6），已知引力常量为 G，则质点 M 与细棒之间的引力的大小为  $ \int_{-l}^{0} \frac{G m \mu}{(a - x)^2} \, dx $。

<div style="text-align: center;"><img src="imgs/img_in_image_box_391_1298_666_1350.jpg" alt="Image" width="26%" /></div>


<div style="text-align: center;">图 12-6</div>
