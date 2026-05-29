故所求法平面方程为 $ x+3z-3f(0,0)=0 $。

例 17.8 曲面  $ z - e^{z} + 2xy = 3 $ 在点  $ (1, 2, 0) $ 处的切平面方程为 ___.

解 应填  $ 2x + y - 4 = 0 $.

令  $ F(x,y,z)=z-e^{z}+2xy-3 $ ，则  $ \boldsymbol{n}=(F_{x}^{\prime},F_{y}^{\prime},F_{z}^{\prime})_{\left|(1,2,0\right)} $ ，其中

 $$ F_{x}^{\prime}\big|_{(1,2,0)}=2y\big|_{(1,2,0)}=4,\ F_{y}^{\prime}\big|_{(1,2,0)}=2x\big|_{(1,2,0)}=2,\ F_{z}^{\prime}\big|_{(1,2,0)}=(1-\mathrm{e}^{z})\big|_{(1,2,0)}=0 $$ 

故切平面方程为  $ 4(x-1)+2(y-2)+0\cdot(z-0)=0 $ ，即  $ 2x+y-4=0 $

★例 17.9 设  $ f $ 可微，则曲面  $ e^{2x-z} = f(\pi y - \sqrt{2}z) $ 是（）.

(A) 旋转抛物面 (B) 双叶双曲面 (C) 单叶双曲面 (D) 柱面

解 应选(D).

设  $ F = f(\pi y - \sqrt{2}z) - e^{2x - z} $，则曲面上任一点处的法向量为

 $$ \boldsymbol{n}=(-2\mathrm{e}^{2x-z},\pi f^{\prime},-\sqrt{2}f^{\prime}+\mathrm{e}^{2x-z}) $$ 

设某定向量  $ \tau = (a, b, c) $ ( $ a, b, c $ 不同时为零) 与 n 垂直，即

<div style="text-align: center;"><img src="imgs/img_in_image_box_752_531_943_665.jpg" alt="Image" width="18%" /></div>


 $$ \boldsymbol{n}\cdot(\boldsymbol{a},\boldsymbol{b},\boldsymbol{c})=-2a\boldsymbol{e}^{2x-z}+\pi b f^{\prime}+(-\sqrt{2}f^{\prime}+\boldsymbol{e}^{2x-z})c\equiv0 $$ 

解得  $ a=\frac{c}{2} $， $ b=\frac{\sqrt{2}}{\pi}c $，令 c=1，则  $ a=\frac{1}{2} $， $ b=\frac{\sqrt{2}}{\pi} $，这样曲面上任一点处的法向量 n 均与定向量  $ \left(\frac{1}{2},\frac{\sqrt{2}}{\pi},1\right) $ 垂直，这说明该曲面是柱面。

## 五 场论初步

<div style="text-align: center;"><img src="imgs/img_in_image_box_837_857_941_963.jpg" alt="Image" width="10%" /></div>


什么叫“场”？从数学上说，场就是空间区域 $ \Omega $上的一种对应法则。

(1) 如果  $ \Omega $ 上的每一点  $ M(x, y, z) $ 都对应着一个数量 u，则在  $ \Omega $ 上就确定了一个数量函数  $ u = u(x, y, z) $，它表示一个数量场。数量场的例子很多，比如温度场，温度场只讲大小，不讲方向。

(2) 如果  $ \Omega $ 上的每一点  $ M(x, y, z) $ 都对应着一个向量 F，则在  $ \Omega $ 上就确定了一个向量函数

 $$ F(x,y,z)=P(x,y,z)i+Q(x,y,z)j+R(x,y,z)k $$ 

它表示一个向量场。向量场的例子也很多，比如引力场，引力场既讲大小，也讲方向。

## 方向导数

定义 设三元函数  $ u = u(x, y, z) $ 在点  $ P_0(x_0, y_0, z_0) $ 的某空间邻域  $ U \subset \mathbb{R}^3 $ 内有定义， $ l $ 为从点  $ P_0 $ 出发的射线， $ P(x, y, z) $ 为  $ l $ 上且在  $ U $ 内的任一点，则