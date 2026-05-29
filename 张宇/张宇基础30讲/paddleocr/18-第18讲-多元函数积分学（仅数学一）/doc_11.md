解 应填 $ \frac{1}{4} $

方法一 积分区域如图 18-6(a) 所示.

<div style="text-align: center;"><img src="imgs/img_in_image_box_238_266_437_450.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_450_247_637_441.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_651_263_830_451.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;">图 18-6</div>


由轮换对称性知，

 $$ \iiint\limits_{\Omega}x\mathrm{d}v=\iiint\limits_{\Omega}y\mathrm{d}v=\iiint\limits_{\Omega}z\mathrm{d}v, $$ 

则

 $$ I=\iiint\limits_{\Omega}(x+2y+3z)\mathrm{d}v=6\iiint\limits_{\Omega}z\mathrm{d}v. $$ 

记  $ \Omega $:  $ 0 \leq z \leq 1 $,  $ (x, y) \in D(z) $,  $ D(z) $ 是过 z 轴上  $ [0, 1] $ 中任一点 z 作垂直于 z 轴的平面截  $ \Omega $ 所得平面区域 [平移到 xOy 平面上，见图 18-6(b)]，其面积为  $ \frac{1}{2}(1-z)^2 $，于是由先二后一法（定限截面法），得

<div style="text-align: center;"><img src="imgs/img_in_image_box_803_588_972_765.jpg" alt="Image" width="16%" /></div>


D(z)的面积

 $$ \begin{aligned}\iint\limits_{Q}z\mathrm{d}v&=\int_{0}^{1}z\mathrm{d}z\iint\limits_{D(z)}\mathrm{d}x\mathrm{d}y=\int_{0}^{1}\frac{1}{2}(1-z)^{2}z\mathrm{d}z\\&=\int_{0}^{1}\frac{1}{2}(z-2z^{2}+z^{3})\mathrm{d}z\\&=\frac{1}{2}\Biggl(\frac{1}{2}z^{2}-\frac{2}{3}z^{3}+\frac{1}{4}z^{4}\Biggr)\Big|_{0}^{1}=\frac{1}{24},\end{aligned} $$ 

因此 $ I=6\times\frac{1}{24}=\frac{1}{4} $

方法二 同方法一，有  $ I = 6 \iint_{\Omega} z \, dv $.

记  $ \Omega: 0 \leqslant z \leqslant 1 - x - y $,  $ (x, y) \in D_{xy} $,  $ D_{xy} = \{(x, y) \mid 0 \leqslant x \leqslant 1, 0 \leqslant y \leqslant 1 - x\} $，如图 18-6(c) 所示。于是由先一后二法（投影穿线法），得