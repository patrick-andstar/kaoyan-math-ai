②分别投影到相应的坐标面上.

例如，对于 $ \iint_{\Sigma}R(x,y,z)\mathrm{d}x\mathrm{d}y $，将曲面 $ \Sigma $投影到xOy平面上去.

a. 若  $ \Sigma $ 在 xOy 平面上的投影为一条线，即  $ \Sigma $ 垂直于 xOy 平面，则此积分为零.

注 (1) 对于第一型曲面积分而言，投影时并不允许随便选择投影方向，要确保  $ z = z(x, y) $ 写得出来才行，如果写不出函数，说明此时的投影方向是错的。

(2) 在第二型曲面积分中， $ dydz $， $ dzdx $， $ dxdy $ 这三个不能想换什么换什么，一旦要转换投影，要先经过计算，确保能转化为  $ dxdy $，才能往  $ xOy $ 面投影。类似地，如果是转化为  $ dzdx $，只能往  $ xOz $ 面投影，如果是转化为  $ dydz $，就只能往  $ yOz $ 面投影。

对于图示的无限无顶铁圆柱桶，若求其质量，用到的是第一型曲面积分，注意，计算时不能往  $ xOy $ 面投影（因为x，y取定值时，对应无数多个z， $ z=z(x,y) $ 是多值函数），只能往  $ yOz $ 面（前，后）或  $ xOz $ 面（左，右）投影，在往  $ yOz $ 面或  $ xOz $ 面投影时，还要把柱面切成两部分（若不切，也是多值函数）分别去求第一型曲面积分，然后把两个积分相加。



<div style="text-align: center;"><img src="imgs/img_in_image_box_784_289_958_454.jpg" alt="Image" width="16%" /></div>


对于圆柱面  $ \Sigma $，有  $ \iint_{\Sigma} R(x, y, z) \, dx \, dy = \iint_{D_{xy}} R \, dx \, dy = 0 $。

b. 若不是 “a” 的情形，且  $ \Sigma $ 上存在两点，它们在 xOy 平面上的投影点重合，则应将  $ \Sigma $ 剖分成若干个曲面片，使对于每一曲面片上的点投影到 xOy 平面上的投影点不重合.

c. 假设已如 “b” 剖分好了，不妨将剖分之后的曲面片仍记为  $ \Sigma $ 。此时将  $ \Sigma $ 的方程写成  $ z = z(x, y) $ 的形式（只有投影到 xOy 平面上的投影点不重合时，  $ \Sigma $ 的方程才能写成  $ z = z(x, y) $ 的形式）。

③一投二代三计算.

a. 一投：确定出  $ \Sigma $ 在 xOy 平面上的投影域  $ D_{xy} $

b. 二代：将  $ z = z(x, y) $ 代入  $ R(x, y, z) $.

类比第二型曲线积分：

 $$ \int_{L:a\to b}P\mathrm{d}x $$ 

c. 三计算：将 dxdy 写成  $ \pm dxdy $ 。其中 “±” 号选取方式如下。

 $$ \begin{aligned}&a<b\Rightarrow+\mathrm{d}x\\&a>b\Rightarrow-\mathrm{d}x\\ \end{aligned} $$ 

当 $ \cos\gamma>0 $，即 $ \Sigma $的法向量与z轴交角为锐角，亦即当 $ \Sigma $的指定侧为上侧时，取“+”；

当  $ \cos\gamma<0 $，即  $ \Sigma $ 的法向量与 z 轴交角为钝角，亦即当  $ \Sigma $ 的指定侧为下侧时，取 “-”.

于是便得

<div style="text-align: center;"><img src="imgs/img_in_image_box_321_1175_884_1334.jpg" alt="Image" width="54%" /></div>
