<div style="text-align: center;"><img src="imgs/img_in_image_box_145_136_754_250.jpg" alt="Image" width="59%" /></div>


② $ \begin{vmatrix}a_{x}&a_{y}&a_{z}\\b_{x}&b_{y}&b_{z}\\c_{x}&c_{y}&c_{z}\end{vmatrix}=0\Leftrightarrow $三向量共面.

<div style="text-align: center;"><img src="imgs/img_in_image_box_474_271_651_355.jpg" alt="Image" width="17%" /></div>


## 3 向量的方向角和方向余弦

(1) 非零向量 a 与 x 轴、y 轴和 z 轴正向的夹角  $ \alpha, \beta, \gamma $ 称为 a 的方向角.

<div style="text-align: center;"><img src="imgs/img_in_image_box_214_451_347_573.jpg" alt="Image" width="12%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_540_477_692_564.jpg" alt="Image" width="14%" /></div>


(2) $ \cos\alpha,\cos\beta,\cos\gamma $称为a的方向余弦，且 $ \cos\alpha=\frac{a_{x}}{|a|},\cos\beta=\frac{a_{y}}{|a|},\cos\gamma=\frac{a_{z}}{|a|} $

(3) $ a^{\circ}=\frac{a}{|a|}=(\cos\alpha,\cos\beta,\cos\gamma) $称为向量a的单位向量（表示方向的向量）.

(4)任意向量  $ \boldsymbol{r} = x\boldsymbol{i} + y\boldsymbol{j} + z\boldsymbol{k} = (r\cos\alpha, r\cos\beta, r\cos\gamma) = r(\cos\alpha, \cos\beta, \cos\gamma) $，其中  $ \cos\alpha, \cos\beta, \cos\gamma $ 为 r 的方向余弦，r 为 r 的模， $ \cos\alpha = \frac{x}{\sqrt{x^2 + y^2 + z^2}} $， $ \cos\beta = \frac{y}{\sqrt{x^2 + y^2 + z^2}} $， $ \cos\gamma = \frac{z}{\sqrt{x^2 + y^2 + z^2}} $， $ r = \sqrt{x^2 + y^2 + z^2} $。

例 17.1 设函数  $  f(x, y)  $ 在点 (0, 0) 处可微， $  f(0, 0) = 0  $， $  n = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, -1 \right)_{(0, 0)}  $，则  $  \lim_{(x, y) \to (0, 0)} \frac{n \cdot (x, y, f(x, y))}{\sqrt{x^2 + y^2}} =  $ ___.

例  $  a = (1, 1, 2)  $， $  |a| = \sqrt{1^2 + 1^2 + 2^2} = \sqrt{6}  $.

则  $  a^* = \left( \frac{1}{\sqrt{6}}, \frac{1}{\sqrt{6}}, \frac{2}{\sqrt{6}} \right)  $.

 $  \cos \alpha \cos \beta \cos \gamma  $



♡分析 可微： $ \Delta z - dz = o(\rho) $

解 应填 0.

因为 $ f(x,y) $在点 $ (0,0) $处可微，且 $ f(0,0)=0 $，所以

 $$ f(x,y)=f(x,y)-f(0,0)=\frac{\partial f}{\partial x}\bigg|_{(0,0)}(x-0)+\frac{\partial f}{\partial y}\bigg|_{(0,0)}(y-0)+o\left(\sqrt{x^{2}+y^{2}}\right), $$ 

故 $ \left.\frac{\partial f}{\partial x}\right|_{(0,0)}x+\left.\frac{\partial f}{\partial y}\right|_{(0,0)}y-f(x,y)=o\left(\sqrt{x^{2}+y^{2}}\right) $，即

 $$ \lim_{(x,y)\to(0,0)}\frac{\left.\frac{\partial f}{\partial x}\right|_{(0,0)}x+\left.\frac{\partial f}{\partial y}\right|_{(0,0)}y-f(x,y)}{\sqrt{x^{2}+y^{2}}}=0 $$ 