## 注 $ ^{(1)} $主值区间

 $ y = \arcsin x $ 的主值区间为  $ \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] $， $ y = \arccos x $ 的主值区间为  $ [0, \pi] $.

(2) 反三角函数的恒等式有

 $$ \sin(\arcsin x)=x,\ x\in[-1,1],\ \sin(\arccos x)=\sqrt{1-x^{2}},\ x\in[-1,1];\ \sin(\arccos x)=\sqrt{1-x^{2}},\ x\in[-1,1]. $$ 

 $$ \cos(\arccos x)=x,\ x\in[-1,\ 1],\ \cos(\arcsin x)=\sqrt{1-x^{2}},\ x\in[-1,\ 1]; $$ 

 $$  又 \sin^{2}t+\cos^{2}t=1 $$ 

 $$ \arcsin(\sin x)=x,\;x\in\left[-\frac{\pi}{2},\;\frac{\pi}{2}\right];\quad\begin{aligned} 因此 \sin t&=\sqrt{1-x^{2}}\;.\end{aligned} 即 \sin(\arccos x)&=\sqrt{1-x^{2}}\;.\end{aligned} $$ 

 $$ \arccos(\cos x)=x,\;x\in\left[0,\;\pi\right]; $$ 

 $ \arcsin x + \arccos x = \frac{\pi}{2} (-1 \leqslant x \leqslant 1) $. 这个结论记住，证明中值定理处讲.

(3) 特殊函数值：

 $$ \arcsin0=0,\arcsin\frac{1}{2}=\frac{\pi}{6},\arcsin\frac{\sqrt{2}}{2}=\frac{\pi}{4},\arcsin\frac{\sqrt{3}}{2}=\frac{\pi}{3},\arcsin1=\frac{\pi}{2}, $$ 

 $$ \arccos1=0,\arccos\frac{\sqrt{3}}{2}=\frac{\pi}{6},\arccos\frac{\sqrt{2}}{2}=\frac{\pi}{4},\arccos\frac{1}{2}=\frac{\pi}{3},\arccos0=\frac{\pi}{2} $$ 

例1.12 设  $ y = \sin x $,  $ 0 \leq x \leq 2\pi $，求其所有单调区间上的反函数.

分析分单调区间，分别讨论反函数（用诱导公式）.

只有当x落在 $ \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] $上时，才有反函数 $ x = \arcsin y $， $ y \in [-1, 1] $。

解 当  $ 0 \leqslant x \leqslant \frac{\pi}{2} $ 时，对  $ y = \sin x $，有  $ x = \arcsin y $， $ y \in [0, 1] $，此时反函数为  $ y = \arcsin x $， $ x \in [0, 1] $。

当  $ \frac{\pi}{2} < x \leqslant \frac{3\pi}{2} $ 时（见图 1-14），有  $ -\frac{\pi}{2} < x - \pi \leqslant \frac{\pi}{2} $，此时  $ \sin(x - \pi) = -\sin(\pi - x) = -\sin x = -y $，于是有  $ x - \pi = -\arcsin y $，故  $ x = \pi - \arcsin y, y \in [-1, 1) $，此时反函数为  $ y = \pi - \arcsin x, x \in [-1, 1) $。

当  $ \frac{3\pi}{2} < x \leq 2\pi $ 时（见图 1-14），有  $ -\frac{\pi}{2} < x - 2\pi \leq 0 $，此时  $ \sin(x - 2\pi) = \sin x = y $，于是有  $ x - 2\pi = \arcsin y $，故  $ x = 2\pi + \arcsin y, y \in (-1, 0] $，此时反函数为  $ y = 2\pi + \arcsin x, x \in (-1, 0] $。

<div style="text-align: center;"><img src="imgs/img_in_image_box_388_1222_651_1349.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">图 1-14</div>
