## ③ 方向导数与梯度的关系

由方向导数的计算公式  $ \left.\frac{\partial u}{\partial l}\right|_{P_{0}}=u_{x}^{\prime}(P_{0})\cos\alpha+u_{y}^{\prime}(P_{0})\cos\beta+u_{z}^{\prime}(P_{0})\cos\gamma $ 与梯度的定义

 $$ \left.\operatorname{grad}u\right|_{P_{0}}=\left(u_{x}^{\prime}(P_{0}),u_{y}^{\prime}(P_{0}),u_{z}^{\prime}(P_{0})\right), $$ 

可得到

 $$ \begin{aligned}\left.\frac{\partial u}{\partial\boldsymbol{l}}\right|_{P_{0}}=&(u_{x}^{\prime}(P_{0}),u_{y}^{\prime}(P_{0}),u_{z}^{\prime}(P_{0}))\cdot(\cos\alpha,\cos\beta,\cos\gamma)=\mathbf{grad}u\big|_{P_{0}}\cdot\boldsymbol{l}^{\circ}\\=&\left|\mathbf{grad}u\right|_{P_{0}}\big|\left|\boldsymbol{l}^{\circ}\right|\cos\theta=\left|\mathbf{grad}u\right|_{P_{0}}\big|\cos\theta,\end{aligned} $$ 

其中  $ \theta $ 为  $ \left.\operatorname{grad} u\right|_{P} $ 与  $ l^{\circ} $ 的夹角.

①当 $ \cos\theta=1 $时， $ \left.\frac{\partial u}{\partial l}\right|_{P_{0}} $有最大值.

②当 $ \cos\theta=0 $，即 $ \theta=\frac{\pi}{2} $时，向量l与梯度垂直，有 $ \left.\frac{\partial u}{\partial l}\right|_{P_{0}}=0 $，即变化率为0.

于是有重要结论：函数在某点的梯度是一个向量，它的方向与取得最大方向导数的方向一致，而它的模为方向导数的最大值，为

 $$ \left|\mathbf{grad}u\right|=\sqrt{\left(u_{x}^{\prime}\right)^{2}+\left(u_{y}^{\prime}\right)^{2}+\left(u_{z}^{\prime}\right)^{2}}. $$ 

## 4 散度

定义 设向量场  $ A(x,y,z)=P(x,y,z)i+Q(x,y,z)j+R(x,y,z)k $，则

 $$ \mathrm{div}\boldsymbol{A}=\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z} $$ 

叫作向量场A的散度.

<div style="text-align: center;"><img src="imgs/img_in_image_box_301_940_386_1019.jpg" alt="Image" width="8%" /></div>


表示向外（内）流的强度

5 旋度

定义 设向量场  $ A(x,y,z)=P(x,y,z)i+Q(x,y,z)j+R(x,y,z)k $，则

 $$ \mathbf{rot}\boldsymbol{A}=\begin{vmatrix}\boldsymbol{i}&\boldsymbol{j}&\boldsymbol{k}\\ \frac{\partial}{\partial x}&\frac{\partial}{\partial y}&\frac{\partial}{\partial z}\\ \boldsymbol{P}&\boldsymbol{Q}&\boldsymbol{R}\end{vmatrix} $$ 

叫作向量场 A 的旋度．描述向量场中向量旋转量的强度

例 17.10 函数  $ f(x, y, z) = x^2y + z^2 $ 在点  $ (1, 2, 0) $ 处沿向量  $ \boldsymbol{n} = (1, 2, 2) $ 的方向导数为（）.

(A) 12 (B) 6 (C) 4 (D) 2

解 应选(D).

因为函数可微分，且