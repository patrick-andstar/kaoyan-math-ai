<div style="text-align: center;"><img src="imgs/img_in_image_box_73_135_138_205.jpg" alt="Image" width="6%" /></div>


## 基础内容精讲

## 三 重积分

<div style="text-align: center;"><img src="imgs/img_in_image_box_287_244_558_367.jpg" alt="Image" width="26%" /></div>


1 概念

<div style="text-align: center;"><img src="imgs/img_in_image_box_816_239_920_347.jpg" alt="Image" width="10%" /></div>


设 $ f(x, y, z) $是空间有界闭区域 $ \Omega $上的有界函数，将 $ \Omega $任意分成 $ n $个小闭区域

 $$ \Delta\nu_{1},\Delta\nu_{2},\cdots,\Delta\nu_{n}, $$ 

其中  $ \Delta v_{i} $ 表示第 i 个小闭区域，也表示它的体积。在每个  $ \Delta v_{i} $ 上任取一点  $ (\xi_{i}, \eta_{i}, \zeta_{i}) $，作乘积  $ f(\xi_{i}, \eta_{i}, \zeta_{i}) \Delta v_{i} (i=1, 2, \cdots, n) $，并作和  $ \sum_{i=1}^{n} f(\xi_{i}, \eta_{i}, \zeta_{i}) \Delta v_{i} $。如果当各小闭区域直径中的最大值  $ \lambda $ 趋于零时，这和的极限总存在（与  $ \Delta v_{i} $ 的分法及  $ (\xi_{i}, \eta_{i}, \zeta_{i}) $ 的取法均无关），则称此极限值为函数  $ f(x, y, z) $ 在闭区域  $ \Omega $ 上的三重积分，记作  $ \iiint_{\Omega} f(x, y, z) \, \mathrm{d}v $，即

知识回顾

二重积分：分割、近似、求和、取极限



<div style="text-align: center;"><img src="imgs/img_in_image_box_640_500_822_690.jpg" alt="Image" width="17%" /></div>


$$\lim_{\lambda\to0}\sum_{k=1}^{n}f(\xi_k,\eta_k)\Delta\sigma_k=\iint\limits_D f(x,y)\mathrm{d}\sigma$$

$$\iint\limits_D f(x,y)\mathrm{d}\sigma\xrightarrow{D}\text{平面}$$

$$\iiint\limits_{\Omega}f(x,y,z)\mathrm{d}v$$

体积微分

 $$ \iiint_{\Omega}f(x,y,z)\frac{\mathrm{d}v}{\mathrm{d}x}=\lim_{\lambda\rightarrow0}\sum_{i=1}^{n}f(\xi_{i},\eta_{i},\zeta_{i})\Delta v_{i}, $$ 

其中 $ f(x,y,z) $称为被积函数， $ f(x,y,z)\mathrm{d}v $称为被积表达式， $ \mathrm{d}v $称为体积元素，x，y与z称为积分变量， $ \Omega $称为积分区域， $ \sum_{i=1}^{n}f(\xi_{i},\eta_{i},\zeta_{i})\Delta v_{i} $称为积分和．

若 $ f(x,y,z) $在 $ \Omega $上连续，则三重积分

 $$ \iiint\limits_{\Omega}f(x,y,z)\mathrm{d}v $$ 

一定存在.

注 三重积分的物理意义：设一物体占有 Oxyz 上的闭区域  $ \Omega $，在点  $ (x, y, z) $ 处的体密度为  $ \rho(x, y, z) $，假定  $ \rho(x, y, z) $ 在  $ \Omega $ 上连续，则物体的质量

 $$ M=\iiint\limits_{\Omega}\rho(x,\ y,\ z)\mathrm{d}v. $$ 