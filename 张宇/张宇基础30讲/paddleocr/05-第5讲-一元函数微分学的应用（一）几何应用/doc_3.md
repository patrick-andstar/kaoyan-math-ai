## 2 一阶可导点是极值点的必要条件

设 $ f(x) $在 $ x=x_{0} $处可导，且在点 $ x_{0} $处取得极值，则必有 $ f'(x_{0})=0 $。

注1 事实上，若  $ x = x_{0} $ 为曲线  $ y = f(x) $ 的极值点，则只有以下两种情况.

驻点与不可导点

(1) $ f'(x_{0})=0 $，如 $ y=x^{2} $在 $ (0,0) $处的情形，如图5-1(a)所示.



<div style="text-align: center;"><img src="imgs/img_in_image_box_701_271_800_363.jpg" alt="Image" width="9%" /></div>


(2)  $ f'(x_0) $ 不存在，如  $ y = |x| $ 在  $ (0, 0) $ 处的情形，如图 5-1(b) 所示。

<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_813_272_906_356.jpg" alt="Image" width="9%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 5-1</div>


极小值点，但不可导.

注2  $ f'(x_0) = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} = 0 $ 仅能说明在  $ x \to x_0 $ 时， $ f(x) - f(x_0) $ 为  $ x - x_0 $ 的高阶无穷小，不能说明  $ f(x) = f(x_0) $，即当  $ f'(x_0) = 0 $ 时， $ f(x) $ 仍然可能是单调的，所以  $ f'(x_0) = 0 $ 仅为  $ f(x) $ 在  $ x = x_0 $ 处取得极值的必要条件。

找极值时的两种情况：①驻点；②不可导点。

## 3 判别极值的第一充分条件

需借助左、右邻域的一阶导数的正负来判断这一点处的极值情况

设 $ f(x) $在 $ x=x_{0} $处连续，且在 $ x_{0} $的某去心邻域 $ U(x_{0},\delta)(\delta>0) $内可导.

①若  $ x \in (x_{0} - \delta, x_{0}) $ 时， $ f'(x) < 0 $，而  $ x \in (x_{0}, x_{0} + \delta) $ 时， $ f'(x) > 0 $，则  $ f(x) $ 在  $ x = x_{0} $ 处取得极小值；

②若  $ x \in (x_0 - \delta, x_0) $ 时， $ f'(x) > 0 $，而  $ x \in (x_0, x_0 + \delta) $ 时， $ f'(x) < 0 $，则  $ f(x) $ 在  $ x = x_0 $ 处取得极大值；

③若  $ f'(x) $ 在  $ (x_0 - \delta, x_0) $ 和  $ (x_0, x_0 + \delta) $ 内不变号，则点  $ x_0 $ 不是极值点。

注  $ f(x) $ 在  $ x=x_{0} $ 处不一定可导，可能出现角点.

<div style="text-align: center;"><img src="imgs/img_in_image_box_546_973_668_1072.jpg" alt="Image" width="11%" /></div>


## 4 判别极值的第二充分条件

需借助 $ x=x_{0} $一点处的二阶导数的正负，当一点处的信息较强时使用

设 $ f(x) $在 $ x=x_{0} $处二阶可导，且 $ f'(x_{0})=0 $， $ f''(x_{0})\neq0 $。

①若 $ f''(x_0)<0 $，则 $ f(x) $在 $ x_0 $处取得极大值；

②若 $ f''(x_0)>0 $，则 $ f(x) $在 $ x_0 $处取得极小值。

借助保号性推导如下.

设 $ f''(x_0)=\lim_{x\to x_0}\frac{f'(x)-f'(x_0)}{x-x_0}=\lim_{x\to x_0}\frac{f'(x)}{x-x_0}>0 $，由保号性可知：