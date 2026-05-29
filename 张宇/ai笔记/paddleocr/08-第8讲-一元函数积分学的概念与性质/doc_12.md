③若 $ f(x) $在 $ [a,b] $上有界，且只有有限个间断点，则 $ \int_{a}^{b}f(x)dx $存在.

不包含无穷间断点，因为无穷间断点会导致无界

④若 $ f(x) $在 $ [a,b] $上有有限个第一类间断点，则 $ \int_{a}^{b}f(x)dx $存在.

(2) 定积分存在的必要条件.

可积函数必有界，即若定积分 $ \int_{a}^{b}f(x)dx $存在，则 $ f(x) $在 $ [a,b] $上必有界。

注1 关于定积分存在的必要条件，不妨这样理解：当我们任意分割图形底边为若干小段时，若  $ f(x) $ 在区间  $ [a, b] $ 上无界，则至少存在一个小段  $ \Delta x $，在  $ \Delta x $ 上， $ f(x) $ 可以任意大，于是一个“小竖条”的面积  $ f(x)\Delta x $ 便可以无穷大，这样整个曲边梯形的面积就是无穷大，于是极限就不存在了，所以可积函数必有界。

注意与反常积分作区分：反常积分有可能出现函数无界的情况。

注2 函数不定积分存在定理与定积分存在定理的区别与联系见例 8.3.

## 3 性质（假设以下积分均存在）

两个规定：

(1) 当 b = a 时，  $ \int_{a}^{a} f(x) \, dx = 0 $;

(2) 当 a > b 时， $ \int_{a}^{b} f(x) \, \mathrm{d}x = -\int_{b}^{a} f(x) \, \mathrm{d}x $.

性质 1(求区间长度) 假设 a < b，则  $ \int_{a}^{b} \mathrm{d}x = \frac{1}{b - a} = L $，其中 L 为区间  $ [a, b] $ 的长度.



<div style="text-align: center;"><img src="imgs/img_in_image_box_478_786_694_917.jpg" alt="Image" width="20%" /></div>


性质 2(积分的线性性质) 设  $ k_{1}, k_{2} $ 为常数，则  $ \int_{a}^{b}\left[k_{1}f(x) \pm k_{2}g(x)\right]dx = k_{1}\int_{a}^{b}f(x)dx \pm k_{2}\int_{a}^{b}g(x)dx $

性质 3(积分的可加（拆）性） 无论 a, b, c 的大小如何，总有  $ \int_{a}^{b} f(x) \, \mathrm{d}x = \int_{a}^{c} f(x) \, \mathrm{d}x + \int_{c}^{b} f(x) \, \mathrm{d}x $.

性质 4(积分的保号性) 若在区间  $ [a, b] $ 上  $ f(x) \leqslant g(x) $，则有  $ \int_{a}^{b} f(x) \, dx \leqslant \int_{a}^{b} g(x) \, dx $。

特殊地，有

<div style="text-align: center;"><img src="imgs/img_in_image_box_130_1154_584_1291.jpg" alt="Image" width="43%" /></div>


由图可得， $ \left|\int_{a}^{b}f(x)dx\right|=\left|5-3\right|=2 $， $ \int_{a}^{b}\left|f(x)\right|dx=5+3=8 $，则有 $ \left|\int_{a}^{b}f(x)dx\right|\leqslant\int_{a}^{b}\left|f(x)\right|dx $。