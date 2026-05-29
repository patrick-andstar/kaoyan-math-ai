公式当D关于y=x对称， $ f(x,y)=-f(y,x) $时， $ \iint_{D}f(x,y)=0 $

(2) 轮换对称性（一定是直角坐标系下）.

引例 1

将x, y对调后，相等吗？

 $$ \iint\limits_{D_{1}:\frac{x^{2}}{4}+\frac{y^{2}}{3}\leqslant1}(2x^{2}+3y^{2})\mathrm{d}x\mathrm{d}y\xlongequal{?}\iint\limits_{D_{2}:\frac{y^{2}}{4}+\frac{x^{2}}{3}\leqslant1}(2y^{2}+3x^{2})\mathrm{d}y\mathrm{d}x $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_728_219_842_318.jpg" alt="Image" width="11%" /></div>


解 因为上述两个积分只是将 x 与 y 这两个字母对调了，而积分值与用什么字母表示是无关的，故它们是相等的.

引例 2

 $$ \iint\limits_{D:\frac{x^{2}}{4}+\frac{y^{2}}{4}\leqslant1}(2x^{2}+3y^{2})\mathrm{d}x\mathrm{d}y=\iint\limits_{D:\frac{x^{2}}{4}+\frac{y^{2}}{4}\leqslant1}(2y^{2}+3x^{2})\mathrm{d}y\mathrm{d}x $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_711_397_892_525.jpg" alt="Image" width="17%" /></div>


解 理由如上，它们也是相等的.

引例 2 中的区域 D 有个特点，就是当你把 x 与 y 对调后，区域 D 不变（事实上，区域 D 关于 y = x 对称）。于是抽象化写出的式子为

 $$ \iint\limits_{D}f(x,y)\mathrm{d}x\mathrm{d}y=\iint\limits_{D}f(y,x)\mathrm{d}y\mathrm{d}x. $$ 

整理一下，我们可以这样来描述：

在直角坐标系下，若把x与y对调后，区域D不变（或区域D关于y=x对称），则

 $$ \iint\limits_{D}f(x,\ y)\mathrm{d}\sigma=\iint\limits_{D}f(y,\ x)\mathrm{d}\sigma,\longrightarrow\mathrm{d}\sigma=\mathrm{d}x\mathrm{d}y=\mathrm{d}y\mathrm{d}x $$ 

这就是轮换对称性。

轮换对称性的应用： $ \iint_{D}f(x,y)\mathrm{d}\sigma\left(\iint_{D}f(y,x)\mathrm{d}\sigma\right) $ 难计算，但 $ f(x,y)+f(y,x) $ 之和式子简单，如注(1).

 $$ D=\left\{\left(x,y\right)\mid x^{2}+y^{2}\leqslant1,x>0,y>0\right\} $$ 

 $$ \begin{aligned}&\iint\limits_{D}\frac{a\sqrt{f(x)}+b\sqrt{f(y)}}{\sqrt{f(x)}+\sqrt{f(y)}}\mathrm{d}\sigma\\=&\iint\limits_{D}\frac{a\sqrt{f(y)}+b\sqrt{f(x)}}{\sqrt{f(y)}+\sqrt{f(x)}}\mathrm{d}\sigma\\=&\frac{1}{2}\iint\limits_{D}(a+b)\mathrm{d}\sigma\\=&\frac{a+b}{2}\cdot\frac{1}{4}\cdot\pi\cdot1^{2}\quad.\quad\frac{1}{4} 个圆的面积 \end{aligned} $$ 

普通对称性 $ \left\{\begin{aligned}&①D关于y=x对称；\\ &②f(x,y)=f(y,x)或f(x,y)=-f(y,x).\end{aligned}\right. $ 轮换对称性 $ \left\{\begin{aligned}&①D关于y=x对称；\\ &②利用f(x,y)+f(y,x)简化计算.\end{aligned}\right. $