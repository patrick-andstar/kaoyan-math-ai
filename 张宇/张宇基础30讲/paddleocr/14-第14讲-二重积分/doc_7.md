例 14.3 设  $ J_i = \iint_{D_i} \sqrt[3]{x - y} \, \mathrm{d}x \, \mathrm{d}y \, (i = 1, 2, 3) $，其中  $ D_1 = \{(x, y) \mid 0 \leq x \leq 1, 0 \leq y \leq 1\} $， $ D_2 = \{(x, y) \mid 0 \leq x \leq 1, 0 \leq y \leq 1\} $， $ D_3 = \{(x, y) \mid 0 \leq x \leq 1, x^2 \leq y \leq 1\} $，则（ ）。

(A)  $ J_1 < J_2 < J_3 $  

(B)  $ J_3 < J_1 < J_2 $  

(C)  $ J_2 < J_3 < J_1 $  

(D)  $ J_2 < J_1 < J_3 $

☑分析 本题先画出每部分的积分区域图，然后研究同一函数在不同区域的积分值的大小.

本题是结合对称性和被积函数正负的问题。

因. $ D_{1} $关于y=x对称， $ f(y,x)=-f(x,y) $，故 $ J_{1}=0 $

 $ D_{2} $ 不对称，但可以作辅助曲线，创造对称性，对称部分积分为 0，另一部分  $ f(x, y) \geqslant 0 $，故  $ J_{2} > 0 $

同理， $ D_{3} $ 也可作辅助曲线，对称部分积分为 0，另一部分  $ f(x, y) \leqslant 0 $，故  $ J_{3} < 0 $。

## 解 应选(B)

如图 14-5(a) 所示， $ D_1 $ 被直线  $ y = x $ 分成  $ D_{11} $ 和  $ D_{12} $ 两部分，故  $ \iint_{D_1} \sqrt[3]{x - y} \, \mathrm{d}x \, \mathrm{d}y = \iint_{D_{11}} \sqrt[3]{x - y} \, \mathrm{d}x \, \mathrm{d}y $，由于  $ \sqrt[3]{x - y} = -\sqrt[3]{y - x} $，故由普通对称性，有  $ J_1 = \iint \sqrt[3]{x - y} \, \mathrm{d}x \, \mathrm{d}y = 0 $。

如图 14-5(b) 所示，作辅助线  $ y = x^2 $，将  $ D_2 $ 分为  $ D_{21} $ 和  $ D_{22} $ 两部分，由普通对称性知， $ \iint_{D_{21}} \sqrt[3]{x - y} \, dx \, dy = 0 $。而在  $ D_{22} $ 上， $ \sqrt[3]{x - y} \geq 0 $，由保号性知，

 $$ J_{2}=\iint\limits_{D_{2}}^{}\sqrt[3]{x-y}\mathrm{d}x\mathrm{d}y=\iint\limits_{D_{22}}^{}\sqrt[3]{x-y}\mathrm{d}x\mathrm{d}y>0\quad. $$ 

如图 14-5(c) 所示，作辅助线  $ y = \sqrt{x} $，将  $ D_3 $ 分为  $ D_{31} $ 和  $ D_{32} $ 两部分，由普通对称性知， $ \iint_{D_{32}} \sqrt[3]{x - y} \, dx \, dy = 0 $。而在  $ D_{31} $ 上， $ \sqrt[3]{x - y} \leq 0 $，由保号性知，

 $$ J_{3}=\iint\limits_{D_{3}}^{}\sqrt[3]{x-y}\mathrm{d}x\mathrm{d}y=\iint\limits_{D_{31}}^{}\sqrt[3]{x-y}\mathrm{d}x\mathrm{d}y<0\enspace. $$ 

综上， $ J_{3}<J_{1}<J_{2} $

<div style="text-align: center;"><img src="imgs/img_in_image_box_199_1089_373_1291.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_432_1089_618_1297.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 14-5</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_659_1088_835_1289.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">(c)</div>


☑ 方法总结 遇到二重积分的题目，首先应考虑对称性，看能否化简.