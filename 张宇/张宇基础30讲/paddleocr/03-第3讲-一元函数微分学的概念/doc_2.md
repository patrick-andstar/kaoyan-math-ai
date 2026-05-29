注 这里有几点需要说明.

(1) 在考题中，增量  $ \Delta x $ 一般会被命题人广义化为“狗”：

 $$ \Delta x,(\Delta x)^{2} $$ 

增量式

 $$ f^{\prime}(x_{0})=\lim_{\Delta x\to0}\frac{f(x_{0}+\Delta x)-f(x_{0})}{\Delta x}\xlongequal{ 广义化 }\lim_{ 狗 \to0}\frac{f(x_{0}+ 狗 )-f(x_{0})}{ 狥 }. $$ 

(2) 若在上面  $ (*) $ 式中，令  $ x_{0} + \Delta x = x $，则可将导数定义式写成

增量式 $ \Leftrightarrow $函数式

 $$  函数式 f^{\prime}(x_{0})=\lim_{x\to x_{0}}\frac{f(x)-f(x_{0})}{x-x_{0}}, $$ 

(**)，(***)两式等价，考生将会在各种场合见到这两种等价写法。

(3) 下面这三种提法是等价的.

① $ y=f(x) $在点 $ x_{0} $处可导；

② $ y=f(x) $在点 $ x_{0} $处导数存在；

③ $ f'(x_{0})=A $（A为有限数）.

(4) 函数在一点可导的充要条件．考研必考

①单侧导数.

 $$ \lim_{\Delta x\to0^{-}}\frac{f(x_{0}+\Delta x)-f(x_{0})}{\Delta x}\xlongequal{ 记 }f_{-}^{\prime}(x_{0}) $$ 

 $$ \lim_{\Delta x\to0^{+}}\frac{f(x_{0}+\Delta x)-f(x_{0})}{\Delta x}\xlongequal{ 记 }f_{+}^{\prime}(x_{0}) $$ 

这里， $ f_{-}^{\prime}(x_{0}) $， $ f_{+}^{\prime}(x_{0}) $ 分别是  $ f(x) $ 在点  $ x_{0} $ 处的左导数、右导数，统称为单侧导数。

在几何上：有斜着的切线或水平的切线，但是没有铅直切线

② $ f'(x_0) $存在⇔其左导数 $ f'(-x_0) $与右导数 $ f'(+x_0) $均存在且相等。这一点当然是与极限存在的充分必要条件(左、右极限均存在且相等)对应。因为从本质上来说，导数的定义就是一个极限问题。

(5) 函数在一点可导的必要条件：若  $ f(x) $ 在一点可导，则  $ f(x) $ 在该点连续．反之未必．

如： $ f(x)=|x| $ 在 x=0 处的情形.

再如： $ f(x)=\begin{cases}x^{2}, & x\in\text{有理数}, \\ 0, & x\in\text{无理数}\end{cases}=x^{2}D(x) $ 在 x=0 处的

狄利克雷函数  $ D(x)=\begin{cases}1,x\in\text{有理数},\\0,x\in\text{无理数}\end{cases} $

 $$ \begin{aligned}&\begin{aligned}\\ &\downarrow& 证明 \\&\lim_{\Delta x\to0}\frac{f(x_{0}+\Delta x)-f(x_{0})}{\Delta x}=a\\&\Rightarrow\lim_{\Delta x\to0}f(x_{0}+\Delta x)-f(x_{0})=\lim_{\Delta x\to0}\frac{f(x_{0}+\Delta x)-f(x_{0})}{\Delta x}\Delta x\\&\Rightarrow f(x_{0})=\lim_{\Delta x\to0}f(x_{0}+\Delta x)\\ &\end{aligned}\\ \end{aligned} $$ 

 $$ f^{\prime}(0)=\lim_{x\to0}\frac{f(x)-f(0)}{x-0}=\lim_{x\to0}\frac{f(x)}{x}=\lim_{x\to0}\frac{x^{2}D(x)}{x}=\lim_{x\to0}xD(x)=0 $$ 

 $$ \frac{ 无穷小量 \times 有界量 }{ 爻 }= 无穷小量 $$ 

(6) 还记得在函数连续性那里的直观解释吗？现在把可导放进来，再看一遍。

存在是说，给了一个x，就有一个y对应在那里（见图3-2），它附近的点X们所对应的Y们，也是如此，它们只是在那里，无牵无挂；连续是说，Y们充分靠近y（见图3-3），它们彼此的距离小到无法用任何小的