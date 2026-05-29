 $$ f^{\prime \prime}(x_{0})=\lim_{x\to x_{0}}\frac{f^{\prime}(x)-f^{\prime}(x_{0})}{x-x_{0}}<0\quad. $$ 

根据函数极限的局部保号性，存在 $ x_0 $的去心邻域 $ \mathring{U}(x_0, \delta) $，当 $ x \in \mathring{U}(x_0, \delta) $时，有 $ \frac{f'(x) - f'(x_0)}{x - x_0} < 0 $。因为 $ f'(x_0) = 0 $，所以上式为 $ \frac{f'(x)}{x - x_0} < 0 $。从而当 $ x \in \mathring{U}(x_0, \delta) $时， $ f'(x) $与 $ x - x_0 $符号相反。当 $ x - x_0 < 0 $时， $ f'(x) > 0 $；当 $ x - x_0 > 0 $时， $ f'(x) < 0 $。根据判别极值的第一充分条件， $ f(x) $在点 $ x_0 $处取得极大值。

(2) 因  $ f''(x_0) > 0 $，故按二阶导数的定义有

 $$ f^{\prime \prime}(x_{0})=\lim_{x\to x_{0}}\frac{f^{\prime}(x)-f^{\prime}(x_{0})}{x-x_{0}}>0\enspace. $$ 

根据函数极限的局部保号性，存在  $ x_0 $ 的去心邻域  $ \dot{U}(x_0, \delta) $，当  $ x \in \dot{U}(x_0, \delta) $ 时，有  $ \frac{f'(x) - f'(x_0)}{x - x_0} > 0 $。因为  $ f'(x_0) = 0 $，所以上式为  $ \frac{f'(x)}{x - x_0} > 0 $。从而当  $ x \in \dot{U}(x_0, \delta) $ 时， $ f'(x) $ 与  $ x - x_0 $ 符号相同。当  $ x - x_0 < 0 $ 时， $ f'(x) < 0 $；当  $ x - x_0 > 0 $ 时， $ f'(x) > 0 $。根据判别极值的第一充分条件， $ f(x) $ 在点  $ x_0 $ 处取得极小值。

## 4 微分的概念 一元函数可微  $ \Leftrightarrow $ 可导

(1) 引例.

如图 3-14 所示，设正方形边长为 1，当其边长增加  $ \Delta x $ 时，它的面积 S 增加了

面积变化的主要部分，也叫线性主部

<div style="text-align: center;"><img src="imgs/img_in_image_box_736_724_938_933.jpg" alt="Image" width="19%" /></div>


 $$ \frac{\Delta S}{(1+\Delta x)^{2}}-1^{2}=\frac{2\Delta x}{1+\Delta x}+\left(\Delta x\right)^{2} $$ 

<div style="text-align: center;">图 3-14</div>


上述面积的增量  $ \Delta S $ 由两部分组成，一部分是  $ 2\Delta x $（图 3-14 中两个小长

方形的面积），它是  $ \Delta x $ 的一次项；另一部分是  $ (\Delta x)^2 $（图 3-14 中右上角小正方形的面积），它满足  $ \lim_{\Delta x \to 0} \frac{(\Delta x)^2}{\Delta x} = 0 $，即  $ (\Delta x)^2 = o(\Delta x) $。故  $ \Delta S = 2\Delta x + o(\Delta x) $， $ 2\Delta x $ 为增量的主要部分，也叫线性主部， $ o(\Delta x) $ 为  $ \Delta x \to 0 $ 时  $ \Delta x $ 的高阶无穷小，是误差，当  $ \Delta x $ 足够小时，有  $ \Delta S \approx 2\Delta x $。

(2) 概念.

设函数  $ y = f(x) $ 在点  $ x_{0} $ 的某邻域内有定义，且  $ x_{0} + \Delta x $ 在该邻域内，对于函数增量

 $$ \Delta y=f(x_{0}+\Delta x)-f(x_{0}), $$ 

若存在与  $ \Delta x $ 无关的常数 A，使得

 $$ \Delta y=A\Delta x+o(\Delta x)\ , $$ 