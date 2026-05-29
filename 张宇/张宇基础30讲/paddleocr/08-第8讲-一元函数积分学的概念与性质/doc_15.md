例 8.4 设可导函数  $ y = f(x) $ 在  $ [0, +\infty) $ 上的值域是  $ [0, +\infty) $， $ f(0) = 0 $， $ f''(x) > 0 $， $ \boxed{x = \varphi(y)} $ 是  $ y = f(x) $ 的反函数。记  $ I = \int_{0}^{a} f(x) \, dx + \int_{0}^{b} \varphi(y) \, dy $，常数  $ a, b > 0 $，当  $ a < \varphi(b) $ 时，则（）.

(A) I > ab

(B) I < ab

(C) I = ab

(D) I 与 ab 的大小关系不确定

解 应选(A).

由题设易知， $ f(x) $ 是过原点且在  $ [0, +\infty) $ 上单调递增的函数。已知  $ x = \varphi(y) $ 是  $ y = f(x) $ 的反函数，则  $ x = \varphi(y) $ 与  $ y = f(x) $ 在同一坐标系下共线，如图 8-3 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_379_449_627_596.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;">图 8-3</div>


由图 8-3 可知，

 $$ \begin{aligned}&I=\int_{0}^{a}f(x)\mathrm{d}x+\int_{0}^{b}\varphi(y)\mathrm{d}y\\ &\quad=S_{1}+S_{2}+S_{3}>S_{1}+S_{2}=ab\ ,\\ \end{aligned} $$ 

故  $ I > ab $ 。因此选 (A).

例 8.5  $ y = e^{-x} \sin x $ 在  $ [0, +\infty) $ 上与 x 轴所围平面区域的面积写成如下表达式：

 $$ \textcircled{1}\int_{0}^{+\infty}\mathrm{e}^{-x}\left|\sin x\right|\mathrm{d}x\;;\quad\textcircled{2}\left|\int_{0}^{+\infty}\mathrm{e}^{-x}\sin x\mathrm{d}x\right|\;;\quad\textcircled{3}\lim_{n\to\infty}\sum_{k=0}^{n}\left|\int_{k\pi}^{(k+1)\pi}\mathrm{e}^{-x}\sin x\mathrm{d}x\right|. $$ 

其中正确表达式的个数是（）.

(A) 0          (B) 1          (C) 2          (D) 3

解 应选(C).

由 “二、1.(2)” 定积分的几何意义，因  $ y = e^{-x} \sin x $ 在  $ [0, +\infty) $ 上既有正值，也有负值，故  $ \int_{0}^{+\infty} e^{-x} \sin x \, dx $

表示其在x轴上方所围图形的面积减去其在x轴下方所围图形的面积，如图8-4所示． $ \left|\int_{0}^{+\infty}e^{-x}\sin xdx\right| $表示面积差的绝对值，不符合题意，排除②．

<div style="text-align: center;"><img src="imgs/img_in_image_box_758_1083_927_1158.jpg" alt="Image" width="16%" /></div>


而  $ \int_{0}^{+\infty}e^{-x}\left|\sin x\right|dx=\int_{0}^{+\infty}\left|e^{-x}\sin x\right|dx $，表示  $ \left|e^{-x}\sin x\right| $ 在  $ [0,+\infty) $ 上与 x 轴所围图形的面积，如图 8-5 所示，符合题意，故①正确。

<div style="text-align: center;">图 8-4</div>


对于③， $ \left|\int_{k\pi}^{e^{-(k+1)\pi}} e^{-x} \sin x \, dx\right| $表示在  $ [k\pi, (k+1)\pi] $ 上  $ e^{-x} \sin x $ 与  $ x $ 轴所围图形的面积，故  $ \lim_{n \to \infty} \sum_{k=0}^{n} \left|\int_{k\pi}^{(k+1)\pi} e^{-x} \sin x \, dx\right| $ 亦符合题意，故③正确。所以正确的表达式有 2 个。

<div style="text-align: center;"><img src="imgs/img_in_image_box_743_1272_926_1339.jpg" alt="Image" width="17%" /></div>
