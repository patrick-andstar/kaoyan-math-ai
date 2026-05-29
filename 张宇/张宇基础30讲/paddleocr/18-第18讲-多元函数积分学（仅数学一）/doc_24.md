 $$ I_{x}=\int_{L}(y^{2}+z^{2})\rho(x,y,z)\mathrm{d}s,I_{y}=\int_{L}(z^{2}+x^{2})\rho(x,y,z)\mathrm{d}s, $$ 

 $$ I_{z}=\int_{L}(x^{2}+y^{2})\rho(x,y,z)\mathrm{d}s,I_{O}=\int_{L}(x^{2}+y^{2}+z^{2})\rho(x,y,z)\mathrm{d}s. $$ 

例 18.11 设 C 是曲线  $ x^2 + y^2 = 2(x + y) $，则  $ \oint_C (2x^2 + 3y^2) \, ds = $ ___。

☐分析 将曲线中x与y对调，此时曲线不变，故可以考虑用轮换对称性解题.

解 应填  $ 20\sqrt{2}\pi $

C是圆 $ (x-1)^{2}+(y-1)^{2}=2 $，关于y=x对称，由轮换对称性知

 $$ \oint_{C}x^{2}\mathrm{d}s=\oint_{C}y^{2}\mathrm{d}s, $$ 

故

 $$ \begin{aligned}\oint_{C}(2x^{2}+3y^{2})\mathrm{d}s&=\frac{5}{2}\oint_{C}(x^{2}+y^{2})\mathrm{d}s=5\oint_{C}(x+y)\mathrm{d}s\\ &=5\overline{x}\bullet\underline{l_{C}}+5\overline{y}\bullet l_{C}=\underline{10l_{C}}=20\sqrt{2}\pi.\end{aligned} $$ 

第一型曲面积分  $ \longrightarrow $ “从二重积分来，回到二重积分去”

<div style="text-align: center;"><img src="imgs/img_in_image_box_837_602_939_708.jpg" alt="Image" width="9%" /></div>


## 1 概念

①分割  $ \rightarrow $ ②近似

设曲面Σ是光滑的，函数 $ f(x,y,z) $在Σ上有界，把Σ任意分成n个小块 $ \Delta S_i $（ $ \Delta S_i $同时也代表第i个小块曲面的面积），设 $ (\xi_i, \eta_i, \zeta_i) $是 $ \Delta S_i $上任意取定的一点，作乘积 $ f(\xi_i, \eta_i, \zeta_i) $ $ \Delta S_i $（ $ i=1,2,\cdots,n $），并作和 $ \sum_{i=1}^{n} f(\xi_i, \eta_i, \zeta_i) $ $ \Delta S_i $。如果当各小块曲面的直径的最大值 $ \lambda $趋于零时，该和的极限总存在（与 $ \Delta S_i $的 $ \rightarrow $④取极限）的分法及 $ (\xi_i, \eta_i, \zeta_i) $的取法均无关），则称此极限值为函数 $ f(x, y, z) $在曲面Σ上对面积的曲面积分或第一型曲面积分，记作 $ \iint_{\Sigma} f(x, y, z)\,\mathrm{d}S $，即

 $$ \iint_{\Sigma}f(x,y,z)\mathrm{d}S=\lim_{\lambda\rightarrow0}\sum_{i=1}^{n}f(\xi_{i},\eta_{i},\zeta_{i})\Delta S_{i}, $$ 

其中 $ f(x,y,z) $称为被积函数， $ \Sigma $称为积分曲面.

注 (1) 第一型曲面积分的物理背景是以  $ f(x, y, z) $ 为面密度的空间物质曲面的质量.

(2) 把二重积分和第一型曲面积分放在一起作个对比，如图 18-11 所示。