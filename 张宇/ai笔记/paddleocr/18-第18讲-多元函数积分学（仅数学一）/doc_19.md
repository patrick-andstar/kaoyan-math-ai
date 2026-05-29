## 1 概念

设 $L$ 为 $xOy$ 面内的一条光滑曲线弧，函数 $f(x, y)$ 在 $L$ 上有界，在 $L$ 上任意插入一系列点 $M_1, M_2, \cdots, M_{n-1}$ 把 $L$ 分成 $n$ 个小段。设第 $i$ 个小弧段的长度为 $\Delta s_i$，又 $(\xi_i, \eta_i)$ 为第 $i$ 个小弧段上任意取定的一点，作乘积 $f(\xi_i, \eta_i) \Delta s_i (i=1, 2, \cdots, n)$，并作和 $\sum_{i=1}^{n} f(\xi_i, \eta_i) \Delta s_i$，如果当各小弧段长度的最大值 $\lambda$ 趋于零时，这和的极限总存在（与 $\Delta s_i$ 的分法及 $(\xi_i, \eta_i)$ 的取法均无关），则称此极限为函数 $f(x, y)$ 在曲线弧 $L$ 上对弧长的曲线积分或第一型曲线积分，记作 $\int_t f(x, y) ds$，即

 $$ \int_{L}f(x,\ y)\mathrm{d}s=\lim_{\lambda\rightarrow0}\sum_{i=1}^{n}f(\xi_{i},\eta_{i})\Delta s_{i}, $$ 

其中 $ f(x,y) $称为被积函数， $ f(x,y) $ds称为被积表达式，x与y称为积分变量，L称为积分弧段.

<div style="text-align: center;"><img src="imgs/img_in_image_box_768_584_880_709.jpg" alt="Image" width="10%" /></div>


 $$ \begin{aligned}\mathrm{d}s&=\sqrt{(\mathrm{d}x)^{2}+(\mathrm{d}y)^{2}+(\mathrm{d}z)^{2}}\\&=\sqrt{1+\left(y_{x}^{\prime}\right)^{2}+\left(z_{x}^{\prime}\right)^{2}}\mathrm{d}x\end{aligned} $$ 

此定义可以类似地推广到积分弧段为空间曲线弧  $ \Gamma $ 的情形，即函数  $ f(x, y, z) $ 在曲线弧  $ \Gamma $ 上对弧长的曲线积分

区别：

 $$ \int_{r}f(x,y,z)\mathrm{d}s=\lim_{\lambda\rightarrow0}\sum_{i=1}^{n}f(\xi_{i},\eta_{i},\zeta_{i})\Delta s_{i} $$ 

①底部直线变曲线。

 $$ \begin{aligned}ds=\sqrt{(\mathrm{d}x)^{2}+(\mathrm{d}y)^{2}}\\ \uparrow\end{aligned} $$ 

注 但事实上，如果仅理解到此，还是不够的。不妨把定积分和第一型曲线积分放在一起作个对比，加深我们对概念的理解。定积分定义在“直线段”上，而第一型曲线积分定义在“曲线段”上，如图18-9、图18-10所示，由于 $ f(x,y) $定义在 $ L:y=y(x) $上，故曲线方程L可代入被积函数，从而化简计算。

<div style="text-align: center;"><img src="imgs/img_in_image_box_213_1038_859_1236.jpg" alt="Image" width="62%" /></div>


定积分  $ \int_{a}^{b} f(x) dx $

<div style="text-align: center;">图 18-9</div>


<div style="text-align: center;">图 18-10</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_128_1315_159_1342.jpg" alt="Image" width="3%" /></div>


## 性质

以下总假设  $ \Gamma $ 为空间有限长分段光滑曲线.