<div style="text-align: center;"><img src="imgs/img_in_image_box_77_133_141_204.jpg" alt="Image" width="6%" /></div>


## 基础内容精讲

假设以下曲线都是光滑的。

①直角坐标系下（直接算）

三大体系下的图形：

②参数方程下 $ \left\{\begin{array}{l} 直接算 (岁) \\  换元法 \end{array}\right. $



③极坐标系下（直接算）

用定积分表达和计算平面图形的面积

可以推广为用收敛的反常积分进行表示

推广：可能用到在收敛情况下的反常积分 及时回看，补上，以免遗忘

(1) 曲线  $ y = y_{1}(x) $ 与  $ y = y_{2}(x) $ 及 x = a, x = b (a < b) 所围成的平面图形的面积



<div style="text-align: center;"><img src="imgs/img_in_image_box_815_222_920_330.jpg" alt="Image" width="10%" /></div>


 $$ S=\int_{a}^{b}\left|y_{1}(x)-y_{2}(x)\right|\mathrm{d}x $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_720_393_903_511.jpg" alt="Image" width="17%" /></div>


计算一个带绝对值的函数的定积分

小提示：随着学习的进行，知识会遗忘，所以要及时进行复习，因此在学面积之前，可以先回看前面学到的平面图形。

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_565_343_679.jpg" alt="Image" width="22%" /></div>


及时复习的话，遗忘曲线就会出现许多跳跃间断点

记忆小曲线→复习2~3次，遗忘内容大幅度减少

微元法.

用大的面积减去小的面积，即  $ S=\int_{a}^{b}y_{1}dx-\int_{a}^{b}y_{2}dx $

①取微元： $ \Delta S=\left|y_{1}(x)-y_{2}(x)\right|\mathrm{d}x $

②积分： $  S = \int_{a}^{b} |y_{1} - y_{2}| \, dx  $

<div style="text-align: center;"><img src="imgs/img_in_image_box_463_716_653_829.jpg" alt="Image" width="18%" /></div>


(2) 曲线  $ r = r_{1}(\theta) $ 与  $ r = r_{2}(\theta) $ 与两射线  $ \theta = \alpha $ 与  $ \theta = \beta \left(0 < \beta - \alpha \leq 2\pi\right) $ 所围成的曲边扇形的面积

 $$ S=\frac{1}{2}\int_{\alpha}^{\beta}\left|r_{1}^{2}(\theta)-r_{2}^{2}(\theta)\right|\mathrm{d}\theta $$ 

绝对值：保证差值非负

<div style="text-align: center;"><img src="imgs/img_in_image_box_608_870_801_974.jpg" alt="Image" width="18%" /></div>


当  $ d\theta \to 0 $ 时，可将扇形区域近似看作三角形，计算三角形面积： $ \frac{1}{2}r_{2}(\theta) \cdot r_{2}(\theta)d\theta - \frac{1}{2}r_{1}(\theta) \cdot r_{1}(\theta)d\theta $

微元法.

①用经过 O 的射线去切分扇形区域.

②取微元：用大“三角形”面积-小“三角形”面积.

<div style="text-align: center;"><img src="imgs/img_in_image_box_627_1058_744_1127.jpg" alt="Image" width="11%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_819_1057_915_1128.jpg" alt="Image" width="9%" /></div>


 $$ \Delta S=\frac{1}{2}r_{2}(\theta)\bullet r_{2}(\theta)\mathrm{d}\theta-\frac{1}{2}r_{1}(\theta)\bullet r_{1}(\theta)\mathrm{d}\theta=\frac{1}{2}\Big|r_{2}^{2}(\theta)-r_{1}^{2}(\theta)\Big|\mathrm{d}\theta. $$ 

③积分： $  S = \int_{\alpha}^{\beta} \frac{1}{2} \left| r_{2}^{2}(\theta) - r_{1}^{2}(\theta) \right| \, \mathrm{d}\theta  $

例 10.1 设  $ A_n $ 是曲线  $ y = x^n $ 与  $ y = x^{n+1} (n=1,2,\cdots) $ 所围区域的面积，则  $ \lim_{n \to \infty} \left(2 \sum_{k=1}^{n} A_k\right)^n = $ ___.