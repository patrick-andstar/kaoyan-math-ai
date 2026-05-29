切线方程： $ \frac{x-x_{0}}{A}=\frac{y-y_{0}}{B}=\frac{z-z_{0}}{C} $

法平面方程： $ A(x-x_{0})+B(y-y_{0})+C(z-z_{0})=0 $

## 2 空间曲面的切平面与法线

(1) 用隐式方程给出曲面： $ F(x, y, z) = 0 $，其中 F 的一阶偏导数连续．F 在  $ P_{0} $ 的梯度向量

其在 $ P_{0}(x_{0},y_{0},z_{0}) $处的法向量 $ \boldsymbol{n}=(F_{x}^{\prime}\big|_{P_{0}},F_{y}^{\prime}\big|_{P_{0}},F_{z}^{\prime}\big|_{P_{0}}) $

切平面方程： $ F_{x}^{\prime}\big|_{P_{0}}\cdot(x-x_{0})+F_{y}^{\prime}\big|_{P_{0}}\cdot(y-y_{0})+F_{z}^{\prime}\big|_{P_{0}}\cdot(z-z_{0})=0 $

<div style="text-align: center;"><img src="imgs/img_in_image_box_717_335_830_455.jpg" alt="Image" width="10%" /></div>


法线方程： $ \frac{x-x_{0}}{F_{x}^{\prime}\big|_{P_{0}}}=\frac{y-y_{0}}{F_{y}^{\prime}\big|_{P_{0}}}=\frac{z-z_{0}}{F_{z}^{\prime}\big|_{P_{0}}} $ 或  $ z-f(x,y)=0 $ 。则曲面在  $ P_{0} $ 处的法向量为  $ (-f_{x}^{\prime}(x_{0},y_{0}),-f_{y}^{\prime}(x_{0},y_{0}),1) $

(2) 用显式函数给出曲面： $ z = f(x, y) \Rightarrow f(x, y) - \frac{1}{z} = 0 $，其中  $ f $ 的一阶偏导数连续。

 $ _{0} $处的法向量  $ \boldsymbol{n}=(f_{x}^{\prime}(x_{0},y_{0}),f_{y}^{\prime}(x_{0},y_{0}),-1) $ 。此法向量方向向下。

切平面方程： $ f_{x}^{\prime}(x_{0},y_{0})(x-x_{0})+f_{y}^{\prime}(x_{0},y_{0})(y-y_{0})-(z-z_{0})=0 $

若为正值，与z轴正方向夹角为锐角，即法向量向上；若为负值，与z轴正方向夹角为钝角，即法向量向下

法线方程： $ \frac{x-x_{0}}{f_{x}^{\prime}(x_{0},y_{0})}=\frac{y-y_{0}}{f_{y}^{\prime}(x_{0},y_{0})}=\frac{z-z_{0}}{-1} $

例 17.6 空间曲线  $ \Gamma $:  $ \begin{cases} x = \int_{0}^{t} e^{u} \cos u \, du, \\ y = 2 \sin t + \cos t, \\ z = 1 + e^{3t} \end{cases} $ 在  $ t = 0 $ 处的切线方程为 ___.

♡分析 x, y, z 分别对 t 求导，然后代入 t=0 。

解 应填  $ \frac{x-0}{1}=\frac{y-1}{2}=\frac{z-2}{3} $

当 $t=0$ 时，$x=0, y=1, z=2$；由 $x' = e^t \cos t, y' = 2 \cos t - \sin t, z' = 3e^{3t}$，得 $x'(0) = 1, y'(0) = 2$，$z'(0) = 3$。于是，切线方程为 $\frac{x-0}{1} = \frac{y-1}{2} = \frac{z-2}{3}$。

例 17.7 设函数  $  z = f(x, y)  $ 在点 (0, 0) 附近有定义，且  $  f'(0, 0) = 3  $，则曲线  $ \begin{cases} z = f(x, y), \\ y = 0 \end{cases} $ 在点 (0, 0, f(0, 0)) 处的法平面方程为 ___.

解 应填  $ x+3z-3f(0,0)=0 $

曲线 $ \begin{cases}z=f(x,y),\\y=0\end{cases} $可写成参数式： $ \begin{cases}x=t,\\y=0,\\z=f(t,0),\end{cases} $则

 $$ \tau=(x_{t}^{\prime},\ y_{t}^{\prime},\ z_{t}^{\prime})\big|_{t=0}=(1,\ 0,\ f_{x}^{\prime}(0,\ 0))=(1,\ 0,\ 3)\ . $$ 