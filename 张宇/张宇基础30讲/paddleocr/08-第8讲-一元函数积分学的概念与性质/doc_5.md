<div style="text-align: center;"><img src="imgs/img_in_image_box_748_155_906_247.jpg" alt="Image" width="15%" /></div>


(2)  $ x = x_{0} $ 为跳跃间断点，即  $ \lim_{x \to x_{0}^{+}} F'(x) $ 存在且为  $ A_{+} $， $ \lim_{x \to x_{0}^{-}} F'(x) $ 存在且为  $ A_{-} $，但  $ A_{+} \neq A_{-} $，而

 $$ F_{+}^{\prime}(x_{0})=\lim_{x\rightarrow x_{0}^{+}}\frac{F(x)-F(x_{0})}{x-x_{0}}\xlongequal{ 洛必达法则 }\lim_{x\rightarrow x_{0}^{+}}F^{\prime}(x)=A_{+}, $$ 

 $ F(x) $ 在 I 上处处可导.

 $$ F_{-}^{\prime}(x_{0})=\lim_{x\to x_{0}^{-}}\frac{F(x)-F(x_{0})}{x-x_{0}}\xlongequal{ 洛必达法则 }\lim_{x\to x_{0}^{-}}F^{\prime}(x)=A_{-}, $$ 

又  $ F'(x_0) $ 是存在的，则  $ F'_+(x_0)=F'_-(x_0) $，即  $ A_+=A_- $，矛盾；

(3)  $ x = x_{0} $ 为无穷间断点，即  $ \lim_{x \to x_{0}} F'(x) = \infty $，而

 $$ F^{\prime}(x_{0})=\lim_{x\to x_{0}}\frac{F(x)-F(x_{0})}{x-x_{0}}\xlongequal{ 洛必达法则 }\lim_{x\to x_{0}}F^{\prime}(x)=\infty, $$ 

又 $ F'(x_{0}) $是存在的，矛盾.

综上所述，(1)，(2)和(3)的情形均不存在原函数，即导函数 $ F'(x) $在I内必定没有第一类间断点和无穷间断点，也即含有第一类间断点和无穷间断点的函数 $ f(x) $在包含该间断点的区间内没有原函数 $ F(x) $.

注3 含有振荡间断点的函数是否有原函数呢？这是不确定的.举例来说，对于

 $$ f(x)=\begin{cases}2x\sin\frac{1}{x}-\cos\frac{1}{x},&x\neq0,\\0,&x=0,\end{cases} $$ 

 $ \lim_{x\to0}f(x) $ 不存在，其在  $ (-\infty,+\infty) $ 上不连续，它有一个振荡间断点 x=0，但是它在  $ (-\infty,+\infty) $ 上存在原函数

 $$ F(x)=\begin{cases}x^{2}\sin\frac{1}{x},&x\neq0,\\0,&x=0.\end{cases} $$ 

经验证，当  $ x \neq 0 $ 时， $ F'(x) = 2x \sin \frac{1}{x} - \cos \frac{1}{x} $；当 x = 0 时， $ F'(0) = \lim_{x \to 0} \frac{x^2 \cdot \sin \frac{1}{x} - 0}{x - 0} = 0 $，即对于  $ (- \infty, + \infty) $ 上任一点都有  $ F'(x) = f(x) $ 成立.

当然，对于

 $$ f(x)=\begin{cases}\displaystyle\frac{1}{x}\sin\frac{1}{x},&x\neq0,\\0,&x=0,\end{cases} $$ 

其在 $ (-∞,+∞) $上也有一个振荡间断点x=0，但其在 $ (-∞,+∞) $上没有原函数。