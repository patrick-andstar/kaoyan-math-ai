解 应填 $ \frac{\pi}{6}(5\sqrt{5}-1) $

曲线  $ y = \sqrt{x - 1} (1 \leq x \leq 2) $ 绕 x 轴旋转一周所得到的旋转体的表面积为

 $$ S=\int_{1}^{2}2\pi y\sqrt{1+(y^{\prime})^{2}}\mathrm{d}x=\pi\int_{1}^{2}\sqrt{4x-3}\mathrm{d}x=\frac{\pi}{6}(5\sqrt{5}-1) $$ 

算出来多少就是多少，不用担心结果古怪。

例 10.13 已知星形线的方程为  $ \begin{cases} x = 2\cos^{3}t, \\ y = 2\sin^{3}t, \end{cases} $ 则它绕 x 轴旋转一周而成的旋转体的表面积为

分析 利用对称性算出 y 轴右侧的表面积，再乘以 2 即可.

套公式： $ S=\int_{\alpha}^{\beta}2\pi|y(t)|\sqrt{(x_{t}^{\prime})^{2}+(y_{t}^{\prime})^{2}}dt $，再做计算。

<div style="text-align: center;"><img src="imgs/img_in_image_box_801_432_954_568.jpg" alt="Image" width="14%" /></div>


解 应填 $ \frac{48}{5}\pi $

旋转体的表面积为

 $$ \begin{aligned}S&=2\int_{0}^{\frac{\pi}{2}}2\pi y\sqrt{(x_{t}^{\prime})^{2}+(y_{t}^{\prime})^{2}}\mathrm{d}t&\Rightarrow\sqrt{[6\cos^{2}t(-\sin t)]^{2}+(6\sin^{2}t\cos t)^{2}}\\ &=4\pi\int_{0}^{\frac{\pi}{2}}2\sin^{3}t\cdot6\sin t\cos t\mathrm{d}t&\begin{aligned}\\ &=\sqrt{36\sin^{2}t\cos^{2}t(\cos^{2}t+\sin^{2}t)}\\&=6\sin t\cos t\\ &\end{aligned}\\ &=48\pi\int_{0}^{\frac{\pi}{2}}\sin^{4}t\mathrm{d}(\sin t)\\ &=48\pi\cdot\frac{\sin^{5}t}{5}\bigg|_{0}^{\frac{\pi}{2}}=\frac{48}{5}\pi.\\ \end{aligned} $$ 

(4) 平行截面面积为已知的立体体积。（考研来考过）

考研历史上尚未出现过，考题不太好出

如图 10-11 所示，在区间 [a, b] 上，垂直于 x 轴的平面截立体  $ \Omega $ 所得到的截面面积为 x 的连续函数  $ A(x) $，取体积微元： $ dV = A(x)dx $，则  $ \Omega $ 的体积为

 $$ V=\int_{a}^{b}A(x)\mathrm{d}x\ . $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_397_1157_657_1281.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">图 10-11</div>


旋转体体积是其特例.

例 10.14 曲线  $ y = \sqrt{x} $ 与 y = x 所围平面有界区域绕直线 y = x 旋转一周所得旋转体的体积