## 五 第二型曲面积分

思考：第二型曲面积分和谁一脉相承呢？答：与第二型曲线积分一脉相承。

<div style="text-align: center;"><img src="imgs/img_in_image_box_856_161_961_267.jpg" alt="Image" width="10%" /></div>


## 向量场的通量（第二型曲面积分的背景）

简单回顾一下向量场的概念。如果  $ \Omega $ 上的每一点  $ M(x, y, z) $ 都对应着一个向量  $ F $，则在  $ \Omega $ 上就确定了一个向量函数  $ F(x, y, z) = P(x, y, z)i + Q(x, y, z)j + R(x, y, z)k $，它表示一个向量场。

在一点处切平面的法向量，若该点可微，它的方向就是指向曲面在这点处变化率最快的方向

在一个向量场（比如电场、磁场或者某种不可压缩流体的速度场）中，Σ为该场中的某一有向分片光滑曲面，并指定了曲面的外侧，则向量函数 $ F(x,y,z) $通过曲面Σ的通量（比如电场中的电通量，磁场中的磁通量，或者某流体的流量）为

<div style="text-align: center;"><img src="imgs/img_in_image_box_584_473_788_632.jpg" alt="Image" width="19%" /></div>


面微分向量：

大小和我们前面讲的第一型曲面积分的大小是一个概念

向量场v(水流)

 $$ \iint\limits_{\Sigma}\boldsymbol{F}\bullet\mathrm{d}\boldsymbol{S}=\iint\limits_{\Sigma}\boldsymbol{F}\bullet\boldsymbol{n}^{\circ}\mathrm{d}S, $$ 

其中  $ \boldsymbol{n}^{\circ} = (\cos \alpha, \cos \beta, \cos \gamma) $ 是有向曲面  $ \Sigma $ 在指定侧的单位法向量，且由  $ \mathrm{d}S = (\mathrm{d}y \mathrm{d}z, \mathrm{d}z \mathrm{d}x, \mathrm{d}x \mathrm{d}y) $，得

 $$ \iint\limits_{\Sigma}F\bullet\mathrm{d}S=\iint\limits_{\Sigma}P(x,y,z)\mathrm{d}y\mathrm{d}z+Q(x,y,z)\mathrm{d}z\mathrm{d}x+R(x,y,z)\mathrm{d}x\mathrm{d}y. $$ 

于是就引出了第二型曲面积分的概念.

## 2 概念

第二型曲面积分的被积函数  $ F(x, y, z) = P(x, y, z)i + Q(x, y, z)j + R(x, y, z)k $ 定义在光滑的空间有向曲面  $ \Sigma $ 上，其物理背景是向量函数  $ F(x, y, z) $ 通过曲面  $ \Sigma $ 的通量：

 $$ \iint\limits_{\Sigma}P(x,\ y,\ z)\mathrm{d}y\mathrm{d}z+Q(x,\ y,\ z)\mathrm{d}z\mathrm{d}x+R(x,\ y,\ z)\mathrm{d}x\mathrm{d}y. $$ 

由此可以看出，第二型曲面积分是一个向量函数通过某有向曲面的通量（无几何量可言）。要加强和前面所学积分的横向对比，理解它们的区别和联系，不要用错或者用混了。

## 3 性质 与第二型曲线积分是一样的

以下总假设  $ \Sigma $ 是有向分片光滑曲面.

性质 1(积分的线性性质) 设  $ k_{1}, k_{2} $ 为常数，则  $ \iint_{\Sigma} \left( k_{1} F_{1} \pm k_{2} F_{2} \right) \cdot \mathrm{d}S = k_{1} \iint_{\Sigma} F_{1} \cdot \mathrm{d}S \pm k_{2} \iint_{\Sigma} F_{2} \cdot \mathrm{d}S $