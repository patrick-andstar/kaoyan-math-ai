→概念可以联系前面所学的定积分！

## 概念、性质与对称性

设有界函数

 $ f(x) $

 $ a $

 $ b $

 $ f(x, y) $

 $ O $

 $ D $

<div style="text-align: center;"><img src="imgs/img_in_image_box_461_254_645_403.jpg" alt="Image" width="17%" /></div>


## 1 概念

<div style="text-align: center;"><img src="imgs/img_in_image_box_854_250_958_357.jpg" alt="Image" width="10%" /></div>


按照第8讲中给出定积分定义的方法，可以得到二重积分的定义。 $ \rightarrow $ 记积分中是对该段的分割，这是平面区域的分割！

设 $ f(x,y) $是有界闭区域D上的有界函数，将闭区域D任意分成n个小闭区域

小柱体体积的近似，定积分 $ f(\xi)\Delta x $是面积的近似  $ \Delta\sigma,\Delta\sigma,\cdots,\Delta\sigma $

其中  $ \Delta\sigma_i $ 表示第  $ i $ 个小闭区域，也表示它的面积。在每个  $ \Delta\sigma_i $ 上任取一点  $ (\xi_i, \eta_i) $，作乘积  $ f(\xi_i, \eta_i) \Delta \sigma_i (i=1, 2, \cdots, n) $，并作和  $ \sum_{i=1}^{n} f(\xi_i, \eta_i) \Delta \sigma_i $，如果当各小闭区域的直径中的最大值  $ \lambda $ 趋于零时，和的极限总存在（与  $ \Delta\sigma_i $ 的分法及点  $ (\xi_i, \eta_i) $ 的取法均无关），则称此极限值为函数  $ f(x, y) $ 在闭区域  $ D $ 上的二重积分，记作  $ \iint_D f(x, y) \, \mathrm{d}\sigma $，即  $ \int_{D} f(\xi_i) \, \Delta x_i \, \mathrm{d}x_i $ 的取值范围。

 $$ \iint\limits_{D}f(x,y)\mathrm{d}\sigma=\lim_{\substack{\lambda\to0\\ \frac{1}{i}=1}}\sum_{i=1}^{n}f(\xi_{i},\eta_{i})\Delta\sigma_{i} $$ 

 $$ \max\{\Delta\sigma_{i}\}=\lambda\rightarrow0 $$ 

其中 $ f(x,y) $称为被积函数， $ f(x,y)\mathrm{d}\sigma $称为被积表达式， $ \mathrm{d}\sigma $称为面积元素，x与y称为积分变量，D称为积分区域， $ \sum_{i=1}^{n}f(\xi_{i},\eta_{i})\Delta\sigma_{i} $称为积分和.

若 $ f(x,y) $在有界闭区域D上连续，则二重积分 $ \iint_{D}f(x,y)d\sigma $一定存在.

实际问题：

细质杆（可看成一条线） $ \rightarrow $定积分

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_1135_197_1198.jpg" alt="Image" width="5%" /></div>


通常它们的每一点处的密度不同，如何求它们的总质量？

 $$ \iiint\limits_{\Omega}f(x,y,z)\mathrm{d}v $$ 

数学思想：先把它们分得足够细，也就是测度足够小，在这个测度上近似认为函数值是常数，则一小块的质量为 $ f(\xi_i, \eta_i)\Delta\sigma_i $（定积分是 $ f(\xi_i)\Delta x_i $），再求和；最后求极限！

后面所讲的三重积分也是这个思想！ $ \left(\lim_{\lambda\to0}\sum_{i=1}^{n}f(\xi_{i},\eta_{i},\zeta_{i})\cdot\Delta v_{i}=\iiint_{\Omega}f(x,y,z)\mathrm{d}v\right) $