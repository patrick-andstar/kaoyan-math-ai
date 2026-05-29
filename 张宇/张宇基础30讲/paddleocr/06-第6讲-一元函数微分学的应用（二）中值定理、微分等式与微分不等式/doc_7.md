## 定理 7(拉格朗日中值定理)

设 $ f(x) $满足 $ \left\{\begin{aligned}&①在[a,b]上连续,\\&②在(a,b)内可导,\end{aligned}\right. $则存在 $ \xi\in(a,b) $，使得

 $$ f(b)-f(a)=\underline{f^{\prime}(\xi)}\underline{(b-a)},\\  变化率 \quad 定值 $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_636_151_823_270.jpg" alt="Image" width="18%" /></div>


或者写成

若在区间 $ (a,b) $上处处变化率为0，则 $ f(b)=f(a) $为常数

<div style="text-align: center;"><img src="imgs/img_in_image_box_831_138_960_314.jpg" alt="Image" width="12%" /></div>


 $$ f^{\prime}(\xi)=\frac{f(b)-f(a)}{b-a}. $$ 

拉格朗日

(1736—1813)

注 见到  $ f(a)-f(b) $ 或  $ f $ 与  $ f' $ 的关系，一般想到用拉格朗日中值定理。拉格朗日中值定理的作用是用导函数的值来控制函数值的增减。

 $$ \left|f^{\prime}(x)\right|\leqslant k\leqslant 見到 f 与 f^{\prime}，用拉格朗日中值定理 \leqslant $$ 

例 6.8 若  $ f(x) $ 在  $ (a, b) $ 内可导且  $ f'(x) $ 有界，证明： $ f(x) $ 在  $ (a, b) $ 内有界.

证 因为  $ f(x) $ 在  $ (a, b) $ 内可导，所以  $ f(x) $ 在  $ (a, b) $ 内连续，因此对任意  $ x_0 \in (a, b) $， $ f(x_0) $ 存在，对任意  $ x \in (a, b) $，不妨设  $ x < x_0 $，对  $ f(x) $ 在  $ [x, x_0] $ 上应用拉格朗日中值定理，有  $ \rightarrow $ 在  $ (a, b) $ 内取闭区间  $ [x, x_0] $

 $$ f(x)-f(x_{0})=f^{\prime}(\xi)(x-x_{0}),\xi\in(x,x_{0}) $$ 

则 $ \left|f(x)\right|\leqslant\left|f(x_{0})\right|+\left|f'(\xi)\right|\left|x-x_{0}\right| $，由于 $ f'(x) $有界，故存在k>0，使得对任意 $ x\in(a,b) $，有 $ \left|f'(x)\right|\leqslant k $，学会翻译数学名词★关系式

 $$ \left|f^{\prime}(\xi)\right|\leq k $$ 

 $$ \left|f(x)\right|\leqslant\left|f(x_{0})\right|+k\left|x-x_{0}\right|\leqslant\left|f(x_{0})\right|+k(b-a)\xlongequal{ 记 }M $$ 

 $$ \begin{aligned}\left|f(x)\right|=&\left|f(x_{0})+f^{\prime}(\xi)(x-x_{0})\right|\\\leqslant&\left|f(x_{0})\right|+\left|f^{\prime}(\xi)\right|\left|x-x_{0}\right|\\&\xlongequal[]{\quad}\\ \leqslant& 数 +k\bullet(b-a)\\\star&\left|A\right|-\left|B\right|\leqslant\left|A+B\right|\leqslant\left|A\right|+\left|B\right|\end{aligned} $$ 

即 $ f(x) $在 $ (a,b) $内有界.

例 6.9 设  $ f(x) $ 在  $ [0,1] $ 上连续，在  $ (0,1) $ 内可导， $ f(0)=0 $，且  $ f(x) $ 在  $ [0,1] $ 上不恒等于零。证明：存在  $ \xi \in (0,1) $，使得  $ f(\xi)f'(\xi)>0 $。

♀分析 令  $ F(x)=\frac{1}{2}f^{2}(x) $， $ \frac{1}{2}f^{2}\rightarrow ff'\rightarrow(f')^{2}+ff'' $，欲证  $ F'(\xi)=0 $ 想到罗尔定理；欲证  $ F'(\xi)>0 $ 想到拉格朗日中值定理.

证 令  $  F(x) = \frac{1}{2} f^2(x)  $，则  $  F(0) = \frac{1}{2} f^2(0) = 0  $，因为  $  f(x)  $ 不恒为 0，于是必存在某点  $  a \in (0, 1]  $，使得  $  f(a) \neq 0  $，则  $  F(a) = \frac{1}{2} f^2(a) > 0  $，由拉格朗日中值定理可知，存在  $  \xi \in (0, a) \subset (0, 1)  $，使得  $  F'(\xi) = \frac{F(a) - F(0)}{a - 0} > 0  $，即  $  f(\xi) f'(\xi) > 0  $。

★例6.10 设函数 $ f(x) $满足 $ f(0)=0 $，且当x>0时， $ f(x)<0 $， $ f'(x)<0 $， $ f''(x)>0 $，则当0<a<x<b时，有（）.