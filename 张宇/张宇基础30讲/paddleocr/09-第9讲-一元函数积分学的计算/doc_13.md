 $$ \begin{aligned}=&\ln(x^{2}-x+1)+4\int\frac{1}{\left(x-\frac{1}{2}\right)^{2}+\left(\frac{\sqrt{3}}{2}\right)^{2}}\mathrm{d}\left(x-\frac{1}{2}\right)\\=&\ln(x^{2}-x+1)+\frac{8\sqrt{3}}{3}\arctan\frac{2x-1}{\sqrt{3}}+C.\end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_97_364_129_400.jpg" alt="Image" width="3%" /></div>


## 定积分的计算

牛顿—莱布尼茨公式及其推广

<div style="text-align: center;"><img src="imgs/img_in_image_box_700_362_805_469.jpg" alt="Image" width="10%" /></div>


设函数  $ F(x) $ 是连续函数  $ f(x) $ 在  $ [a, b] $ 上的一个原函数，则

<div style="text-align: center;"><img src="imgs/img_in_image_box_827_340_945_512.jpg" alt="Image" width="11%" /></div>


 $$ \int_{a}^{b}f(x)\mathrm{d}x=\left.F(x)\right|_{a}^{b}=F(b)-F(a)\ . $$ 

牛顿

(1643—1727)

注1 证 令  $ G(x)=\int_{a}^{x}f(t)dt $,  $ a\leq x\leq b $，则有

 $$ G(b)=\int_{a}^{b}f(t)\mathrm{d}t,\;G(a)=0\;, $$ 

又  $ F'(x) = f(x) $ 且  $ G(x) = F(x) + C $，则

小故事：莱布尼茨写信给康熙皇帝请求在北京创立研究院被拒绝，否则可能此公式会被称为康熙公式

 $$ \int_{a}^{b}f(x)\mathrm{d}x=G(b)-G(a)=F(b)-F(a). $$ 

注2 牛顿－莱布尼茨公式推广.

(1) 若  $ f(x) $ 在  $ [a, b] $ 上有原函数  $ F(x) $，则  $ \int_{a}^{b} f(x) \, dx = F(b) - F(a) $

★ (2) 若  $ f(x) $ 在  $ [a, b] $ 上分段有原函数，如  $ [a, c) $ 上有原函数  $ F_{1}(x) $， $ (c, b] $ 上有原函数  $ F_{2}(x) $，则

 $$ \begin{aligned}\int_{a}^{b}f(x)\mathrm{d}x=&\int_{a}^{c}f(x)\mathrm{d}x+\int_{c}^{b}f(x)\mathrm{d}x\\=&F_{1}(c-0)-F_{1}(a)+F_{2}(b)-F_{2}(c+0)\ .\end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_637_1036_750_1107.jpg" alt="Image" width="10%" /></div>


若  $ F_{1}(c-0) $,  $ F_{2}(c+0) $ 存在，则  $ \int_{a}^{b} f(x) \, dx $ 收敛，见习题 9.10.

若  $ F_{1}(c-0) $， $ F_{2}(c+0) $ 至少有一个不存在，则  $ \int_{a}^{b} f(x) \, dx $ 发散.

例9.11 设 $ f\left(x+\frac{1}{x}\right)=\frac{x+x^{3}}{1+x^{4}} $，则 $ \int_{2}^{2\sqrt{2}}f(x)dx= $ ___.

莱布尼茨

(1646—1716)

<div style="text-align: center;"><img src="imgs/img_in_image_box_824_866_951_1038.jpg" alt="Image" width="12%" /></div>


♡分析 求 $ f(x) $→计算积分.