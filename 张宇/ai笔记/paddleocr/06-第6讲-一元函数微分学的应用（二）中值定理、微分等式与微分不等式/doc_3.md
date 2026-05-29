# 第6讲 一元函数微分学的应用（二）——中值定理、微分等式与微分不等式

拉格朗日中值定理

<div style="text-align: center;"><img src="imgs/img_in_image_box_223_153_497_191.jpg" alt="Image" width="26%" /></div>


定积分/积分

中值定理

泰勒公式



## ② 涉及导数（微分）的中值定理

<div style="text-align: center;"><img src="imgs/img_in_image_box_833_175_943_306.jpg" alt="Image" width="10%" /></div>


历史故事：费马，被称为最业余的数学家，比牛顿大42岁，是个律师。

1637年他在图书馆看书时，看到了“ $ x^{2}+y^{2}=z^{2} $必存在正整数解”，他违反规定写了一段话：

<div style="text-align: center;">费马</div>


 $$ \left.\begin{array}{r}{x^{3}+y^{3}=z^{3}}\\ {x^{4}+y^{4}=z^{4}}\\ {\cdots}\\ {x^{n}+y^{n}=z^{n}}\\ \end{array}\right\} $$ 

(1601—1665)

费马说：“此处太小写不下，不予证明了”。费马大定理提出了好的问题，实际上，比解决它更好！怀尔斯于1994年证明出了该定理，此时已超40岁

定理 5(费马定理) 设  $ f(x) $ 在点  $ x_{0} $ 处满足  $ \left\{\begin{aligned}&①\text{可导},\\&②\text{取极值},\end{aligned}\right. $ 则  $ f'(x_{0})=0 $

注 $ ^{(1)} $证明费马定理.

不妨假设  $ f(x) $ 在点  $ x_0 $ 处取得极大值，则存在  $ x_0 $ 的邻域  $ U(x_0) $，对任意的  $ x \in U(x_0) $，都有  $ \Delta f = f(x) - f(x_0) \leq 0 $，于是根据导数的定义与极限的保号性，有

 $$ f_{-}^{\prime}(x_{0})=\lim_{x\to x_{0}^{-}}\frac{f(x)-f(x_{0})}{x-x_{0}}\geqslant0, $$ 

 $$ f_{+}^{\prime}(x_{0})=\lim_{x\to x_{0}^{+}}\frac{f(x)-f(x_{0})}{x-x_{0}}\leqslant0\quad. $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_706_751_872_833.jpg" alt="Image" width="16%" /></div>


又 $ f(x) $在点 $ x_0 $处可导，于是 $ f_{-}'(x_0)=f_{+}'(x_0) $，故 $ f'(x_0)=0 $。

(2) 当一个人跑到最远处时，他的速度为零；当一个人跑得最快时，他的加速度为零。这些都是费马定理在生活中的通俗应用。

例 6.3 (导数零点定理) 设  $ f(x) $ 在  $ [a, b] $ 上可导，证明当  $ f_{+}^{\prime}(a) \cdot f_{-}^{\prime}(b) < 0 $ 时，存在  $ \xi \in (a, b) $

使得  $ f^{\prime}(x) $ 存在

由此知最大值取在区间内，而

 $$ f^{\prime}(\xi)=0\;. $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_749_1060_962_1191.jpg" alt="Image" width="20%" /></div>


证 不妨设 $ f_{+}^{\prime}(a)>0,f_{-}^{\prime}(b)<0 $，于是

由 $ f_{+}^{\prime}(a)=\lim_{x\to a^{+}}\frac{f(x)-f(a)}{x-a}>0 $，可得存在 $ \delta_{1}>0 $，在 $ (a,a+\delta_{1}) $内， $ f(x)>f(a) $；



由 $ f_{-}^{\prime}(b)=\lim_{x\to b^{-}}\frac{f(x)-f(b)}{x-b}<0 $，可得存在 $ \delta_{2}>0 $，在 $ (b-\delta_{2},b) $内， $ f(x)>f(b) $。

故 $ f(a) $与 $ f(b) $均不是 $ f(x) $在 $ [a,b] $上的最大值，则 $ f(x) $在 $ (a,b) $内取得最大值，根据费马定理可知，存在 $ \xi\in(a,b) $，使得 $ f'(\xi)=0 $。