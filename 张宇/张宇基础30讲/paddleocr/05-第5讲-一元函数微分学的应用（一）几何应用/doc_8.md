## 2 二阶可导点是拐点的必要条件

设 $ f''(x_{0}) $存在，且点 $ (x_{0},f(x_{0})) $为曲线的拐点，则 $ f''(x_{0})=0 $

 $ \downarrow $

二阶导数存在必为0

(2)  $ f''(x_0) $ 不存在，如  $ y = \sqrt[3]{x} $ 在  $ (0, 0) $ 处的情形，如图 5-4(b) 所示。

二阶导数不存在的点也有可能是拐点

<div style="text-align: center;"><img src="imgs/img_in_image_box_377_448_545_573.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_565_459_728_573.jpg" alt="Image" width="15%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 5-4</div>


3 判别拐点的第一充分条件  $ \rightarrow $ 判别拐点最常用的方法.

设 $ f(x) $在点 $ x=x_{0} $处连续，在点 $ x=x_{0} $的某去心邻域 $ U(x_{0},\delta) $内二阶导数存在，且在该点的左、右邻域内 $ f''(x) $变号（无论是由正变负，还是由负变正），则点 $ (x_{0},f(x_{0})) $为曲线的拐点.

需借助左、右邻域二阶导数的正负变化

注  $ (x_0, f(x_0)) $ 为曲线  $ y = f(x) $ 的拐点，并不要求  $ f(x) $ 在点  $ x_0 $ 的导数存在，如  $ y = \sqrt[3]{x} $ 在  $ x = 0 $ 的情形，如图 5-5 所示，其中  $ y' = \frac{1}{3}x^{-\frac{2}{3}} $， $ y'' = -\frac{2}{9}x^{-\frac{5}{3}} $，当  $ x > 0 $ 时， $ y'' < 0 $；当  $ x < 0 $ 时， $ y'' > 0 $，故点  $ (0, 0) $ 为曲线  $ y = \sqrt[3]{x} $ 的拐点，但在该点的导数不存在。

<div style="text-align: center;"><img src="imgs/img_in_image_box_784_856_949_968.jpg" alt="Image" width="15%" /></div>


<div style="text-align: center;">图 5-5</div>


## 4 判别拐点的第二充分条件

设 $ f(x) $在 $ x=x_{0} $处三阶可导，且 $ f''(x_{0})=0 $， $ f'''(x_{0})\neq0 $，则点 $ (x_{0},f(x_{0})) $为曲线的拐点.

注 上述第二充分条件的证明如下: 由于  $ f''(x_0) = \lim_{x \to x_0} \frac{f''(x) - f''(x_0)}{x - x_0} = \lim_{x \to x_0} \frac{f''(x)}{x - x_0} \neq 0 $，不妨设  $ f''(x_0) > 0 $。由保号性可知：

①当  $ x \in (x_0 - \delta, x_0) $ 时， $ x - x_0 < 0 $，所以  $ f''(x) < 0 $，即曲线在  $ x_0 $ 的左邻域为凸的；

②当  $ x \in (x_0, x_0 + \delta) $ 时， $ x - x_0 > 0 $，所以  $ f''(x) > 0 $，即曲线在  $ x_0 $ 的右邻域为凹的。