 $$ \begin{cases}x-x_{0}=\Delta x=t\underline{\cos\alpha},\\y-y_{0}=\Delta y=t\underline{\cos\beta},\\z-z_{0}=\Delta z=t\underline{\cos\gamma}.\end{cases} 三个方向向量 $$ 

以  $ t=\sqrt{(\Delta x)^{2}+(\Delta y)^{2}+(\Delta z)^{2}} $ 表示 P 与  $ P_{0} $ 之间的距离，如图 17-4 所示，若极限

 $$ \lim_{t\to0^{+}}\frac{u(P)-u(P_{0})}{t}=\lim_{t\to0^{+}}\frac{u(x_{0}+t\cos\alpha,\ y_{0}+t\cos\beta,\ z_{0}+t\cos\gamma)-u(x_{0},\ y_{0},\ z_{0})}{t} $$ 

存在，则称此极限为函数  $ u = u(x, y, z) $ 在点  $ P_0 $ 沿方向  $ I $ 的方向导数，记

作  $ \left.\frac{\partial u}{\partial I}\right|_{P_0} $。

定理 (方向导数的计算公式) 设三元函数  $ u = u(x, y, z) $ 在点  $ P_{0}(x_{0}, y_{0}, z_{0}) $ 处可微分，则  $ u = u(x, y, z) $ 在点  $ P_{0} $ 处沿任一方向 l 的方向导数都存在，且

<div style="text-align: center;"><img src="imgs/img_in_image_box_699_366_943_588.jpg" alt="Image" width="23%" /></div>


<div style="text-align: center;">图 17-4</div>


 $$ \begin{aligned}\frac{\partial u}{\partial l}\bigg|_{P_{0}}&=\lim_{t\to0^{+}}\frac{u(x_{0}+\Delta x,\ y_{0}+\Delta y,\ z_{0}+\Delta z)-u(x_{0},\ y_{0},\ z_{0})}{\sqrt{(\Delta x)^{2}+(\Delta y)^{2}+(\Delta z)^{2}}}\xrightarrow{\Delta u}\\&=\lim_{t\to0^{+}}\frac{u_{x}^{\prime}(P_{0})\Delta x+u_{y}^{\prime}(P_{0})\Delta y+u_{z}^{\prime}(P_{0})\Delta z+o(t)}{\sqrt{(\Delta x)^{2}+(\Delta y)^{2}+(\Delta z)^{2}}}\xrightarrow{\Delta x}\\&=u_{x}^{\prime}(P_{0})\cos\alpha+u_{y}^{\prime}(P_{0})\cos\beta+u_{z}^{\prime}(P_{0})\cos\gamma,\quad\frac{\Delta y}{\sqrt{(\Delta x)^{2}+(\Delta y)^{2}}}\end{aligned} $$ 

 $$ \frac{\Delta x}{\sqrt{(\Delta x)^{2}+(\Delta y)^{2}+(\Delta z)^{2}}}=\cos\alpha\ , $$ 

其中  $ \cos\alpha,\cos\beta,\cos\gamma $ 为方向 l 的方向余弦.

 $ \left(\cos\alpha,\cos\beta,\cos\gamma\right) $一定是单位向量

 $$ \frac{\Delta y}{\sqrt{(\Delta x)^{2}+(\Delta y)^{2}+(\Delta z)^{2}}}=\cos\beta, $$ 

 $$ \frac{\Delta z}{\sqrt{(\Delta x)^{2}+(\Delta y)^{2}+(\Delta z)^{2}}}=\cos\gamma $$ 

注 二元函数 $ f(x,y) $的情况与三元函数类似.

## 2 梯度

定义 设三元函数  $ u = u(x, y, z) $ 在点  $ P_{0}(x_{0}, y_{0}, z_{0}) $ 处具有一阶连续偏导数，则定义

 $$ \left.\operatorname{grad}u\right|_{P_{0}}=\left(u_{x}^{\prime}(P_{0}),u_{y}^{\prime}(P_{0}),u_{z}^{\prime}(P_{0})\right)\longrightarrow 等于该点处切平面的法向量 $$ 

为函数  $ u = u(x, y, z) $ 在点  $ P_{0} $ 处的梯度.

注  $ \text{grad}(u \pm v) = \text{grad} u \pm \text{grad} v $;

 $$ \operatorname{grad}(u v)=v\operatorname{grad}u+u\operatorname{grad}v; $$ 

 $$ \operatorname{grad}\left(\frac{u}{v}\right)=\frac{\nu\operatorname{grad}u-u\operatorname{grad}v}{v^{2}}\left(v\neq0\right). $$ 