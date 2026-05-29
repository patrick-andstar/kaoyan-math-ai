注 当  $ a \neq 1 $ 时， $ F'(0) = 1 \neq a = f(0) $，在包含  $ x = 0 $ 的区间上， $ F(x) $ 不是  $ f(x) $ 的原函数。

例 8.14 设  $ a > 0 $，函数  $ f(x) $ 在  $ [0, +\infty) $ 内连续有界，C 为任意常数，证明： $ y = e^{-ax} \left[ \int_0^x f(t) e^{at} dt + C \right] $ 有界。

证 由 $ f(x) $在 $ [0,+\infty) $内有界，设 $ \left|f(x)\right|\leq M $，则当 $ x\geq0 $时，有

 $$ \begin{aligned}|\mathrm{y}(x)|=&\mathrm{e}^{-\mathrm{a}x}\left[C+\int_{0}^{x}f(t)\mathrm{e}^{\mathrm{a}t}\mathrm{d}t\right]\leq\left|C\mathrm{e}^{-\mathrm{a}x}\right|+\mathrm{e}^{-\mathrm{a}x}\left|\int_{0}^{x}f(t)\mathrm{e}^{\mathrm{a}t}\mathrm{d}t\right|\longrightarrow 使用 |\mathrm{a}\pm\mathrm{b}|\leq|\mathrm{a}|+|\mathrm{b}|\\ \leq&\left|C\right|+\mathrm{e}^{-\mathrm{a}x}\int_{0}^{x}\left|f(t)\mathrm{e}^{\mathrm{a}t}\right|\mathrm{d}t\leq|C|+M\mathrm{e}^{-\mathrm{a}x}\int_{0}^{x}\mathrm{e}^{\mathrm{a}t}\mathrm{d}t\\ =&|C|+\frac{M}{a}(1-\mathrm{e}^{-\mathrm{a}x})\leq|C|+\frac{M}{a},\quad\int_{0}^{x}\mathrm{e}^{\mathrm{a}t}\mathrm{d}t=\frac{1}{a}\int_{0}^{x}\mathrm{e}^{\mathrm{a}t}\mathrm{d}(at)=\frac{1}{a}(\mathrm{e}^{\mathrm{a}x}-1)\end{aligned} $$ 

得证.

## 四 反常积分

<div style="text-align: center;"><img src="imgs/img_in_image_box_834_605_937_712.jpg" alt="Image" width="9%" /></div>


## 概念

前面已经指出，定积分存在有两个必要条件：一是积分区间有限，二是被积函数有界。如果破坏了积分区间的有限性，就引出无穷区间上的反常积分；如果破坏了被积函数的有界性，就引出无界函数的反常积分。

定积分（常义积分） $ \left\{\begin{array}{l} 区间有限  \\  被积函数有界  \end{array}\right. $

反常积分（广义积分）

(1) 无穷区间上反常积分的概念与敛散性.

定义 1 设  $ F(x) $ 是  $ f(x) $ 在相应区间上的一个原函数.

①

 $$ \int_{a}^{+\infty}f(x)\mathrm{d}x=\lim_{x\to+\infty}F(x)-F(a) $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_366_1003_846_1102.jpg" alt="Image" width="46%" /></div>


若上述极限存在，则称反常积分收敛，否则称发散。

②

 $$ \int_{-\infty}^{b}f(x)dx=F(b)-\lim_{x\to-\infty}F(x) $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_370_1128_877_1219.jpg" alt="Image" width="49%" /></div>


若上述极限存在，则称反常积分收敛，否则称发散。

③

 $$ \int_{-\infty}^{+\infty}f(x)\mathrm{d}x=\int_{-\infty}^{x_{0}}f(x)\mathrm{d}x+\int_{x_{0}}^{+\infty}f(x)\mathrm{d}x, $$ 

若右端两个积分都收敛，则称反常积分收敛，否则称发散。

只要有一个发散，则原反常积分就发散

<div style="text-align: center;"><img src="imgs/img_in_image_box_618_1292_820_1371.jpg" alt="Image" width="19%" /></div>
