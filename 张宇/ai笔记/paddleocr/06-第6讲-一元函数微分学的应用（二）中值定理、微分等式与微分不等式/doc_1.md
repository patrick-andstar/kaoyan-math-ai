## 第6讲 一元函数微分学的应用（二）——中值定理、微分等式与微分不等式

<div style="text-align: center;"><img src="imgs/img_in_image_box_170_81_925_474.jpg" alt="Image" width="73%" /></div>


零点定理（证存在性）

微分等式

方程的根，函数的零点，曲线的交点

单调性（证唯一性）

配合起来考





罗尔原话

★罗尔定理的推论



实系数奇次方程至少有一个实根

微分不等式

数学一综合题中的一个小步骤

用函数性态证明



用常数变化证明

用中值定理证明

<div style="text-align: center;"><img src="imgs/img_in_image_box_82_518_157_591.jpg" alt="Image" width="7%" /></div>


基础内容精讲

<div style="text-align: center;"><img src="imgs/img_in_image_box_90_685_124_721.jpg" alt="Image" width="3%" /></div>


## 中值定理

<div style="text-align: center;"><img src="imgs/img_in_image_box_841_640_946_749.jpg" alt="Image" width="10%" /></div>


## 1 涉及函数的中值定理

设 $ f(x) $在 $ [a,b] $上连续，则

<div style="text-align: center;"><img src="imgs/img_in_image_box_413_770_610_870.jpg" alt="Image" width="19%" /></div>


有界 $ \left|f(x)\right|\leq M $

定理 1(有界与最值定理)  $ m \leqslant f(x) \leqslant M $，其中 m, M 分别为  $ f(x) $ 在  $ [a, b] $ 上的最小值与最大值.

定理 2(介值定理) 当  $ m \leqslant \mu \leqslant M $ 时，存在  $ \xi \in [a, b] $，使得  $ f(\xi) = \mu $。

如， $ f(x) $在 $ [0,2] $上连续， $ f(0)=0 $， $ f(1)=1 $，则存在 $ \xi\in(0,1) $，使 $ f(\xi)=\frac{1}{2} $

<div style="text-align: center;"><img src="imgs/img_in_image_box_771_910_947_1003.jpg" alt="Image" width="17%" /></div>


(离散的)平均值定理： $ f(\xi)=\frac{1}{n}\sum_{i=1}^{n}f(x_{i}) $

(连续的)平均值定理： $ f(\xi)=\frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x $.

定理 3(平均值定理) 当  $ a < x_{1} < x_{2} < \cdots < x_{n} < b $ 时，在  $ [x_{1}, x_{n}] $ 内至少存在一点  $ \xi $，使得

 $$ f(\xi)=\frac{f(x_{1})+f(x_{2})+\cdots+f(x_{n})}{n}. $$ 

注证 由闭区间连续函数的最值定理，得

 $$ m\leqslant f(x_{1})\leqslant M\ , $$ 

 $$ m\leqslant f(x_{2})\leqslant M\ , $$ 