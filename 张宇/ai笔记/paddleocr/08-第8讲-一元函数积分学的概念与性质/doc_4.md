(2) 函数  $ f(x) $ 存在与  $ f'(x) $ 存在的区别.

① a.  $ f(x) $ 在  $ x = x_0 $ 处的极限存在不能得出  $ f(x) $ 在  $ x = x_0 $ 处连续。

如  $ \lim_{x \to x_0} f(x) = a $，但  $ f(x_0) $ 有可能等于 a，也有可能不等于 a。

<div style="text-align: center;"><img src="imgs/img_in_image_box_430_303_682_441.jpg" alt="Image" width="24%" /></div>


b.  $ f(x) $ 可导，且  $ \lim_{x\to x_0}f'(x)=a $，则  $ f'(x) $ 在  $ x_0 $ 处连续。

证

 $$ f^{\prime}(x_{0})=\lim_{x\to x_{0}}\frac{f(x)-f(x_{0})}{x-x_{0}}\xlongequal{\quad\frac{0}{0}\quad}\lim_{x\to x_{0}}f^{\prime}(x)=a. $$ 

②a.  $ f(x) $ 存在不能得出  $ f(x) $ 有介值性.

介值定理：函数 $ f(x) $在 $ [a,b] $上连续，且 $ f(a)=A $， $ f(b)=B $，则当 $ A<u<B $时，存在 $ \xi\in(a,b) $，使 $ f(\xi)=u $。

b.  $ f'(x) $ 存在，可得  $ f'(x) $ 有介值性.

达布定理： $ f(x) $ 在  $ [a, b] $ 上可导， $ f'_+(a) \neq f'_-(b) $，则对任意介于  $ f'_+(a) $ 与  $ f'_-(b) $ 之间的  $ u $，存在  $ \xi \in (a, b) $，使得

<div style="text-align: center;"><img src="imgs/img_in_image_box_600_707_867_876.jpg" alt="Image" width="25%" /></div>


 $$ f^{\prime}(\xi)=u\;. $$ 

证 令  $ F(x)=f(x)-ux $，则  $ F'(x)=f'(x)-u $

不妨设 $ f_{+}^{\prime}(a)<u<f_{-}^{\prime}(b) $，则 $ f_{+}^{\prime}(a)-u<0 $， $ f_{-}^{\prime}(b)-u>0 $，即 $ F_{+}^{\prime}(a)<0 $， $ F_{-}^{\prime}(b)>0 $

由例 6.3，可知存在  $ \xi \in (a, b) $，使  $ F'(\xi) = 0 $，即  $ f'(\xi) = u $。

③由②b.可得$\left\{\begin{aligned}f^{\prime}(x)& 存在 \neq 0，则 f^{\prime}(x) 必保号（恒正或恒负）\\ 在 [a,b] 上 f^{\prime}(x) 存在，则 f^{\prime}(x) 无第一类间断点.\end{aligned}\right.$ 反证：假设存在$f^{\prime}(a)<0$，$f^{\prime}(b)>0$ 则存在$\xi\in(a,b)$，$f^{\prime}(\xi)=0$，矛盾.

注2 证 设  $ F(x) $ 为  $ f(x) $ 在 I 内的一个原函数，则  $ F(x) $ 在 I 内可导，且  $ F'(x) = f(x) $，并设  $ x = x_0 \in I $ 为  $ F'(x) $ 的间断点，我们讨论如下三种情况：

(1)  $ x = x_{0} $ 为可去间断点，即  $ \lim_{x \to x_{0}} F'(x) $ 存在且为 A，但  $ A \neq F'(x_{0}) $，而

<div style="text-align: center;"><img src="imgs/img_in_image_box_792_1228_950_1313.jpg" alt="Image" width="15%" /></div>


 $$ F^{\prime}(x_{0})=\lim_{x\to x_{0}}\frac{F(x)-F(x_{0})}{x-x_{0}}\xlongequal{ 洛必达法则 }\lim_{x\to x_{0}}F^{\prime}(x)=A, 矛盾； $$ 