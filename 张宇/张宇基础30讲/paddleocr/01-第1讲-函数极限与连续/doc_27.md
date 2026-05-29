部位置”，比如“点 $ x_{0} $的 $ \delta $邻域”就可以称为“点 $ x_{0} $的附近”。于是，函数 $ f(x) $在点 $ x_{0} $的某 $ \delta $邻域内有定义也就是函数 $ f(x) $在点 $ x_{0} $的附近有定义，这个“附近”到底有多近多远，既难以说明也没有必要说明。

注 (1) 邻域是区间（区域），但是这个区间是为定义极限才创建的区间。

(2) 关于邻域的一组概念非常重要，因为我们将要“在一个局部位置”细致地研究问题。

## 2 函数极限的定义

设函数$f(x)$在点$x_0$的某一去心邻域内有定义.若存在常数$A$,对于任意给定的$\varepsilon>0$（不论它多么小），总存在正数$\delta$,使得当$0<|x-x_0|<\delta$时，对应的函数值$f(x)$都满足不等式$|f(x)-A|<\varepsilon$,则$A$叫作函数$f(x)$当$x\to x_0$时的极限，记为

 $$ \lim_{x\to x_{0}}f(x)=A 或 f(x)\to A(x\to x_{0}). $$ 

写成 “  $ \varepsilon - \delta $ 语言”：  $ \lim_{x \to x_0} f(x) = A \Leftrightarrow \forall \varepsilon > 0, \exists \delta > 0 $ ，当  $ 0 < |x - x_0| < \delta $ 时，有  $ |f(x) - A| < \varepsilon $

文字语言：任给的 $ \varepsilon>0 $，总能找到 $ \delta $邻域，使得我们的距离小于你这个尺度。

注 符号 “∀” 是英文 Arbitrary(任意的) 的首字母上下方向倒着写出来的；符号 “∃” 是英文 Exist(存在) 的首字母左右方向倒着写出来的.

画图理解．如图 1-23 所示．

<div style="text-align: center;"><img src="imgs/img_in_image_box_404_903_631_1078.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">图 1-23</div>


任给  $ \varepsilon_{1}>0 $，再给  $ \varepsilon_{2}>0 $，……，再给  $ \varepsilon_{n}>0 $，当  $ \varepsilon $ 一直取下去，越来越小，两条线越来越近。不管有多近，总能找到一个小邻域，使得在该邻域内，除了  $ x_{0} $ 之外，曲线被夹在宽度要多小有多小的这两条线中，则称  $ x\to x_{0} $， $ f(x)\to A $。这就是魏尔斯特拉斯给的极限的标准语言。