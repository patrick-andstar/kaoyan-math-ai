例 3.7 设函数  $  f(x)  $ 处处可导， $  f(0) = -1  $， $  f'(0) = 1  $，令  $  g(x) = |f(x - 1)|  $，则（）.

(A)  $ g(x) $ 在 x=0 处必可导 (B)  $ g(x) $ 在 x=0 处必不可导

(C)  $ g(x) $ 在 x=1 处必可导 (D)  $ g(x) $ 在 x=1 处必不可导

解 应选(C).

因为 $ f(x) $处处可导，所以 $ g(x)=\left|f(x-1)\right| $可能不可导的点有且仅有 $ f(x-1)=0 $的点，而当x=0时， $ f(0-1) $的值不得而知，故 $ g(x) $可能可导也可能不可导；当x=1时， $ f(1-1)=f(0)\neq0 $，所以 $ g(x) $在x=1处必可导.

## 2 导数的几何意义

函数  $ y = f(x) $ 在点  $ x_0 $ 处的导数值  $ f'(x_0) $ 就是曲线  $ y = f(x) $ 在点  $ (x_0, y_0) $ 处切线（见图 3-10）的斜率  $ k $，即  $ k = f'(x_0) $，于是曲线  $ y = f(x) $ 在点  $ (x_0, y_0) $ 处的切线方程为  $ y - y_0 = f'(x_0)(x - x_0) $。

什么是切线？它就像一把锋利无比的刀，“嗖”地切过点  $ (x_0, y_0) $，在此瞬间，切线的方向就是点  $ (x_0, y_0) $ 运动的方向。想想看，掷铁饼（作为质点）时，运动员旋转轨迹的每一点的切线方向就是铁饼那一瞬时的运动方向。在那一瞬时脱手，铁饼就会沿着该点的切线方向飞出。



<div style="text-align: center;"><img src="imgs/img_in_image_box_388_588_562_695.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">图 3-10</div>


法线方程为

 $$ y-y_{0}=-\frac{1}{f^{\prime}(x_{0})}(x-x_{0})(f^{\prime}(x_{0})\neq0). $$ 

注 切线存在不代表导数存在，但导数存在切线一定存在.

注例 1 研究  $ y = f(x) = |x| $ 在 x = 0 处的切线问题.

解 从 x = 0 出发，取增量  $ \Delta x $，有  $ \Delta y = f(0 + \Delta x) - f(0) = |\Delta x| $.

当  $ \Delta x > 0 $ 时， $ \Delta y = \Delta x $，则  $ f_{+}^{\prime}(0) = \lim_{\Delta x \to 0^{+}} \frac{\Delta y}{\Delta x} = 1 \xlongequal{记} k_{+} $;

当  $ \Delta x < 0 $ 时， $ \Delta y = -\Delta x $，则  $ f_{-}^{\prime}(0) = \lim_{\Delta x \to 0^{+}} \frac{\Delta y}{\Delta x} = -1 \xlongequal{记} k_{-} $.

<div style="text-align: center;"><img src="imgs/img_in_image_box_725_919_893_1023.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">图3-11</div>


<div style="text-align: center;">尖点（角点）</div>


如图 3-11 所示，曲线  $ y = f(x) = |x| $ 在原点 O 处出现了两条单侧切线，这两条单侧切线形成了一个角，数学上称这里的原点 O 为一个角点。不过，虽然此曲线在角点 O 处有两条单侧切线，但按照前面讲到的  $ f(x) $ 在点  $ x_0 $ 处可导的充要条件，这里的  $ f'_{+}(0) = k_{+} \neq k_{-} = f_{-}'(0) $，显然  $ f'(0) $ 不存在，所以我们说  $ y = f(x) = |x| $ 在原点 O 处不可导，也就没有切线。

注例 2 研究  $ y = f(x) = x^{\frac{1}{3}} $ 在 x = 0 处的切线问题.