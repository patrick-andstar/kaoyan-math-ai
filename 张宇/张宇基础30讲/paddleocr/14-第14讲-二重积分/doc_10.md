后积先定限，限内画条线，先交写下限，后交写上限。

<div style="text-align: center;"><img src="imgs/img_in_image_box_281_138_511_263.jpg" alt="Image" width="22%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_527_134_719_261.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 14-6</div>


先定x的上下限后积x 再定y的上下限注意，这里上限≥下限X型区域的特点是：穿过D内部且平行于y轴的直线与D的边界相交不多于两点

(1)  $ \iint_{D} f(x, y) \, \mathrm{d}\sigma = \int_{D} \left| \frac{\mathrm{d}x}{\mathrm{d}y} \right| \int_{\varphi_{1}(x)}^{z} f_{2}(x) \, f(x, y) \, \mathrm{d}y $，其中 D 为 X 型区域： $ \varphi_{1}(x) \leqslant y \leqslant \varphi_{2}(x) $， $ a \leqslant x \leqslant b $，如图 14-6(a) 所示。积分区域是 X 型区域的后积 x，类似还有其他几种（见批注图）。

<div style="text-align: center;"><img src="imgs/img_in_image_box_293_484_741_586.jpg" alt="Image" width="43%" /></div>


 $$ \iint\limits_{\Omega}f(x,\ y)\mathrm{d}\sigma=\int_{a}^{c}\mathrm{d}x\int_{\varphi_{1}(x)}^{\varphi_{2}(x)}f(x,\ y)\mathrm{d}y+\int_{c}^{b}\mathrm{d}x\int_{\varphi_{2}(x)}^{\varphi_{1}(x)}f(x,\ y)\mathrm{d}y $$ 

先定y的  $ \uparrow $ 再定x的上下限  $ \uparrow $ Y型区域的特点是：穿过D内部且平行于x上下限  $ \uparrow $ 后积y  $ \uparrow $ 注意，这里上限 $ \geq $下限  $ \uparrow $ 轴的直线与D的边界相交不多于两点

(2)  $ \iint_{D} f(x, y) \, \mathrm{d}\sigma = \iint_{D} \mathrm{d}y \iint_{\psi(y)} \phi(y) f(x, y) \, \mathrm{d}x $，其中  $ D $ 为  $ Y $ 型区域： $ \psi_1(y) \leqslant x \leqslant \psi_2(y) $， $ c \leqslant y \leqslant d $，如图 14-6(b) 所示。积分区域是  $ Y $ 型区域的后积  $ y $。

 $ \rightarrow $ 二重积分条接上下限港负号

 $$ \int_{a}^{b}\mathrm{d}x\int_{\varphi_{1}(x)}^{\varphi_{2}(x)}f(x,y)\mathrm{d}y=-\int_{a}^{b}\mathrm{d}x\int_{\varphi_{2}(x)}^{\varphi_{1}(x)}f(x,y)\mathrm{d}y\quad(a<b,\varphi_{1}(x)>\varphi_{2}(x)) $$ 

注 (1) 有一点需要指出，这里的下限都必须小于等于上限.

(2) 若被积函数  $ f(x, y) $ 易于对 y 积分或积分区域 D 是 X 型区域，则选择先 y 后 x 的积分次序；若被积函数  $ f(x, y) $ 易于对 x 积分或积分区域 D 是 Y 型区域，则选择先 x 后 y 的积分次序。

(3) 计算二重积分的关键是确定积分限，为此，要画好积分区域 D 的边界图形，当 D 的边界图形不易画出时，要写出 D 的不等式表达式，从而确定上下限。D 不易画时，采用分析法

例 14.5 设函数  $  f(x, y)  $ 连续，则二次积分  $  \int_{\frac{\pi}{2}}^{\pi} \mathrm{d}x \int_{\sin x}^{1} f(x, y) \mathrm{d}y =  $ （ ）

(A)  $  \int_{0}^{1} \mathrm{d}y \int_{\pi + \arcsin y}^{\pi} f(x, y) \mathrm{d}x  $

(B)  $  \int_{0}^{1} \mathrm{d}y \int_{\pi - \arcsin y}^{\pi} f(x, y) \mathrm{d}x  $

(C)  $  \int_{0}^{1} \mathrm{d}y \int_{\frac{\pi}{2}}^{\pi + \arcsin y} f(x, y) \mathrm{d}x  $

(D)  $  \int_{0}^{1} \mathrm{d}y \int_{\frac{\pi}{2}}^{\pi - \arcsin y} f(x, y) \mathrm{d}x  $

(♣分析) 题干是后积 x，选项是后积 y，可知本题考虑的是交换积分顺序，应先确定积分区域，然后先积 x，后积 y，写成累次积分的形式。后积 y，先定限，下限为 0，上限为 1，再定 x 的限，限内画平行于 x 轴的直线，当  $ \frac{\pi}{2} < x \leq \pi $ 时， $ x = \pi - \arcsin y $，所以下限为  $ x = \pi - \arcsin y $，上限为  $ x = \pi $。