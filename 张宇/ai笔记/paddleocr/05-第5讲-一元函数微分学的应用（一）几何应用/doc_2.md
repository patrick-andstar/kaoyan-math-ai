注2 结合第1讲的知识，一个常见的问题：间断点可以是极值点吗？答案是肯定的。举四个例子供考生分析。

在0处有定义，且在0处的函数值比两边的函数值大，符合极大值点定义。

(1)  $ f(x)=\begin{cases}1,&x=0,\\|x|,&x\neq0,\end{cases} $  $ x=0 $ 是  $ f(x) $ 的可去间断点，但它是  $ f(x) $ 的极大值点。



(2)  $ f(x)=\begin{cases}1,&x>0,\\-x,&x\leq0,\end{cases} $ x=0 是  $ f(x) $ 的跳跃间断点，但它是  $ f(x) $ 的极小值点.

<div style="text-align: center;"><img src="imgs/img_in_image_box_767_223_940_343.jpg" alt="Image" width="16%" /></div>


(3)  $ f(x)=\begin{cases}-1,&x=0,\\\frac{1}{x^{2}},&x\neq0,\end{cases} $ x=0 是  $ f(x) $ 的无穷间断点，但它是  $ f(x) $ 的极小值点.

(4) $ f(x)=\begin{cases}2,&x=0,\\\sin\frac{1}{x},&x\neq0,\end{cases} $ x=0 是  $ f(x) $ 的振荡间断点，但它是  $ f(x) $ 的极大值点.



<div style="text-align: center;"><img src="imgs/img_in_image_box_768_356_879_452.jpg" alt="Image" width="10%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_771_475_965_578.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_742_598_967_778.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_119_850_150_884.jpg" alt="Image" width="3%" /></div>


## 单调性与极值的判别

<div style="text-align: center;"><img src="imgs/img_in_image_box_869_801_974_907.jpg" alt="Image" width="10%" /></div>


若任意  $ x \in (a, b) $， $ f'(x) > 0 $。则  $ f(x) $ 在  $ [a, b] $ 上严格单调增加。即  $ (a, b) $ 内的每一点  $ x $，对  $ x $ 的左边点  $ x_1 $ 有  $ f(x_1) < f(x) $。对  $ x $ 的右边点  $ x_2 $ 有  $ f(x_2) > f(x) $。这样  $ f(x) $ 就在  $ [a, b] $ 上严格单调增加。

## 单调性的判别

设函数  $ y = f(x) $ 在  $ [a, b] $ 上连续，在  $ (a, b) $ 内可导.

①如果在 $ (a, b) $内 $ f'(x) \geq 0 $，且等号仅在有限个点处成立，那么函数 $ y = f(x) $在 $ [a, b] $上严格单调增加；

②如果在 $ (a,b) $内 $ f'(x)\leq0 $，且等号仅在有限个点处成立，那么函数 $ y=f(x) $在 $ [a,b] $上严格单调减少。

注 导数为 0 仅能说明在某点处的函数值变化充分小，而不能说明没变化，即导数大于 0 一定严格单调增加，而严格单调增加不一定导数大于 0.

例如，函数  $ y = x^3 $ 在  $ (-\infty, +\infty) $ 上连续且可导，且导函数  $ y' = 3x^2 \geq 0 $，等号仅在  $ x = 0 $ 处成立，则函数  $ y = x^3 $ 在  $ (-\infty, +\infty) $ 上严格单调增加。注意  $ \delta > 0 $，这个  $ \delta $ 是一个无穷小量， $ f(x) = x^3 $ 在  $ x = 0 $ 处导数为 0。

任意  $ \delta > 0 $ ，这个  $ \delta $ 是一个无穷小量， $ f(x) = x^{3} $ 在 x = 0 处导数为 0 ，代表  $ f(\delta) - f(0) $ 和  $ f(0) - f(-\delta) $ 都是无穷小量，即  $ f(x) = x^{3} $ 在 x = 0 的无穷小邻域内，函数值变化率极小，所以  $ f(x) = x^{3} $ 在 x = 0 处导数值为 0