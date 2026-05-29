注 (1) 设 $ f(x, y) \geq 0 $，如图 14-1 所示，被积函数 $ f(x, y) $可作为曲顶柱体在点 $ (x, y) $处的柱体微元

的竖坐标(高)，用底面积  $ d\sigma $ 乘以高  $ f(x, y) $，得到一个“小竖条”的体积，再在区域 D 上把所有的“小竖条”累加起来，就得到了整个曲顶柱体的体积。

(2) 如果  $ f(x, y) $ 是负的，柱体就在 xOy 面的下方，二重积分的绝对值仍等于柱体的体积，但二重积分的值是负的。（类似于定积分）

<div style="text-align: center;"><img src="imgs/img_in_image_box_738_199_920_310.jpg" alt="Image" width="17%" /></div>


(3) 如果  $ f(x, y) $ 在 D 的若干部分区域上是正的，而在其他部分区域上是

<div style="text-align: center;">图 14-1</div>


负的，那么， $ f(x,y) $ 在 D 上的二重积分就等于 xOy 面上方的柱体体积减去 xOy 面下方的柱体体积所得之差。（类似于定积分）

## ② 性质(与一元函数类似)

性质 1(求区域面积)  $ \iint_{D}1\cdot d\sigma=\iint_{D}d\sigma=A $，其中A为D的面积.

性质 2(可积函数必有界) 当  $ f(x, y) $ 在有界闭区域 D 上可积时， $ f(x, y) $ 在 D 上必有界.

性质 3(积分的线性性质) 设  $ k_{1}, k_{2} $ 为常数，则

瓦解

敌人，

各个

击破

 $$ \iint\limits_{D}[k_{1}f(x,\ y)\pm k_{2}g(x,\ y)]\mathrm{d}\sigma=k_{1}\iint\limits_{D}f(x,\ y)\mathrm{d}\sigma\pm k_{2}\iint\limits_{D}g(x,\ y)\mathrm{d}\sigma. 和  的  积  分 = 积  分  的  和 $$ 

性质 4(积分的可加性) 设  $ f(x, y) $ 在有界闭区域 D 上可积，且  $ D_1 \cup D_2 = D $， $ D_1 \cap D_2 = \varnothing $，则

 $$ \iint\limits_{D}f(x,y)\mathrm{d}\sigma=\iint\limits_{D_{1}}f(x,y)\mathrm{d}\sigma+\iint\limits_{D_{2}}f(x,y)\mathrm{d}\sigma. $$ 

性质 5(积分的保号性) 当  $ f(x, y) $,  $ g(x, y) $ 在有界闭区域 D 上可积时，若在 D 上有

 $$ f(x,\ y)\leqslant g(x,\ y), $$ 

则有

 $$ \iint\limits_{D}f(x,y)\mathrm{d}\sigma\leqslant\iint\limits_{D}g(x,y)\mathrm{d}\sigma\xrightarrow{ 保持原有的不等关系 } $$ 

特殊地，有

 $$ \left|\iint\limits_{D}f(x,y)\mathrm{d}\sigma\right|\leqslant\iint\limits_{D}\left|f(x,y)\right|\mathrm{d}\sigma. $$ 

性质 6(二重积分的估值定理) 设 M, m 分别是  $ f(x, y) $ 在有界闭区域 D 上的最大值和最小值，A 为 D 的面积，则有

 $$ mA\leqslant\iint\limits_{D}f(x,\ y)\mathrm{d}\sigma\leqslant MA.\longrightarrow m\leqslant f(x,\ y)\leqslant M $$ 

性质 7(二重积分的中值定理) 设函数  $ f(x, y) $ 在有界闭区域 D 上连续，A 为 D 的面积，则在 D 上至少存在一点  $ (\xi, \eta) $，使得

 $$ \iint_{D}f(x,y)\mathrm{d}\sigma=f(\xi,\eta)A.\quad\overrightarrow{\int_{a}^{b}f(x)\mathrm{d}x=f(\xi)(b-a)},\xi\in(a,b) $$ 