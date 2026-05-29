 $$ \iint\limits_{D}f(xy)\mathrm{d}x\mathrm{d}y=\int_{0}^{\pi}\mathrm{d}\theta\int_{0}^{2\sin\theta}f(r^{2}\cos\theta\sin\theta)r\mathrm{d}r, $$ 

可知(C)不正确，(D)正确．故选(D).

14.3 (D) 解 积分区域  $ D=\left\{(r,\theta)\mid0\leqslant\theta\leqslant\frac{\pi}{2},0\leqslant r\leqslant\cos\theta\right\} $ 化为直角坐标，可表示为

 $$ \begin{aligned}D=&\left\{(x,y)\middle|0\leqslant x\leqslant1,0\leqslant y\leqslant\sqrt{x-x^{2}}\right\}\\=&\left\{(x,y)\middle|0\leqslant y\leqslant\frac{1}{2},\frac{1}{2}-\sqrt{\frac{1}{4}-y^{2}}\leqslant x\leqslant\frac{1}{2}+\sqrt{\frac{1}{4}-y^{2}}\right\}.\end{aligned} $$ 

14.4 (B) 解 先画出积分区域 D，如图 14-13 所示，因积分区域 D 的边界曲线为  $ y = |x| $ 与

 $ y=\sqrt{2-x^{2}} $，其交点为 $ (1,1) $与 $ (-1,1) $，故D可用极坐标表示为

 $$ D=\left\{(r,\theta)\middle|0\leqslant r\leqslant\sqrt{2},\frac{\pi}{4}\leqslant\theta\leqslant\frac{3\pi}{4}\right\}, $$ 

则

<div style="text-align: center;"><img src="imgs/img_in_image_box_710_536_937_669.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">图 14-13</div>


 $$ \begin{aligned}&\int_{-1}^{1}\mathrm{d}x\int_{|x|}^{\sqrt{2-x^{2}}}\sin(x^{2}+y^{2})\mathrm{d}y=\int_{\frac{\pi}{4}}^{\frac{3\pi}{4}}\mathrm{d}\theta\int_{0}^{\sqrt{2}}r\sin r^{2}\mathrm{d}r\\ &\\ =&\frac{\pi}{2}\times\frac{1}{2}\left(-\cos r^{2}\right)\bigg|_{0}^{\sqrt{2}}=\frac{\pi}{4}\left(-\cos2+1\right).\\ \end{aligned} $$ 

14.5  $ a^{2} $ 解  $ g(y-x)=\begin{cases}a,&0\leqslant y-x\leqslant1,\\0,& 其他 \end{cases}\Rightarrow g(y-x)=\begin{cases}a,&x\leqslant y\leqslant1+x,\\0,& 其他 \end{cases} $

设 $ D_{1}=\left\{(x,y)\mid0\leqslant x\leqslant1,x\leqslant y\leqslant1+x\right\} $，如图14-14所示，令 $ D_{2}=D-D_{1} $，故

 $$ f(x)g(y-x)=\begin{cases}a^{2},(x,y)\in D_{1},\\0,(x,y)\in D_{2},\end{cases} $$ 

所以

 $$ \begin{aligned}&I=\iint\limits_{D}f(x)g(y-x)\mathrm{d}x\mathrm{d}y=\iint\limits_{D_{1}}a^{2}\mathrm{d}x\mathrm{d}y+\iint\limits_{D_{2}}0\mathrm{d}x\mathrm{d}y\\ &=\int_{0}^{1}\mathrm{d}x\int_{x}^{1+x}a^{2}\mathrm{d}y=a^{2}\int_{0}^{1}y\bigg|_{x}^{1+x}\mathrm{d}x\\ &=\left.a^{2}\int_{0}^{1}(1+x-x)\mathrm{d}x=a^{2}\right..\\ \end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_694_914_937_1184.jpg" alt="Image" width="23%" /></div>


<div style="text-align: center;">图 14-14</div>


14.6  $ (t-1)f(t) $ 解 所给积分为二次变限积分，它是变量 t 的函数，故求  $ F'(t) $ 需先将二次变限积分化为变限的单积分。为此考虑所给二次积分的特点，由于依给定的积分次序，不能化为变限单积分，因此先交换积分次序，可得

 $$ F(t)=\int_{1}^{t}\mathrm{d}y\int_{y}^{t}f(x)\mathrm{d}x=\int_{1}^{t}\mathrm{d}x\int_{1}^{x}f(x)\mathrm{d}y=\int_{1}^{t}(x-1)f(x)\mathrm{d}x, $$ 