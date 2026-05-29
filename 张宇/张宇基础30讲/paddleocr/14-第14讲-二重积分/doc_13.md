(3)  $ \iint_{D}f(x,y)\mathrm{d}\sigma=\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{r(\theta)}f(r\cos\theta,r\sin\theta)r\mathrm{d}r $（极点 O 在区域 D 内部）.

注 极坐标系与直角坐标系选择的一般原则.

一般来说，给出一个二重积分． $ \rightarrow $是否用极坐标系计算主要看①.

①看被积函数是否为 $ f(x^{2}+y^{2}) $， $ f\left(\frac{y}{x}\right) $， $ f\left(\frac{x}{y}\right) $等形式；

②看积分区域是否为圆或者圆的一部分.

如果①，②至少满足其中之一，那么优先选用极坐标系，否则，就优先考虑直角坐标系。

例 14.8 设区域  $ D=\left\{(x,y)\mid x^{2}+y^{2}\leqslant\sqrt{2}\right\} $，则  $ \iint_{D}\left(x^{2}+\frac{y^{2}}{2}\right)dxdy= $ ___.

(2)分析 积分区域是圆，但被积函数不是平方和，这里注意到x与y互换时，积分区域D不变，说明D关于y=x对称，此时考虑轮换对称性，最后在极坐标系下计算此二重积分。

解 应填 $ \frac{3\pi}{4} $

用轮换对称性

 $$ \begin{aligned}\iint_{D}\left(x^{2}+\frac{y^{2}}{2}\right)\mathrm{d}x\mathrm{d}y=&\iint_{D}\left(y^{2}+\frac{x^{2}}{2}\right)\mathrm{d}x\mathrm{d}y=\frac{1}{2}\left(1+\frac{1}{2}\right)\iint_{D}(x^{2}+y^{2})\mathrm{d}x\mathrm{d}y\\=&\frac{1}{2}\left(1+\frac{1}{2}\right)\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{\frac{1}{2^{4}}}(r^{2}\cos^{2}\theta+r^{2}\sin^{2}\theta)r\mathrm{d}r=\frac{3\pi}{4}.\end{aligned} $$ 

(四) 方法总结 积分区域 D 关于 y = x 对称，考虑轮换对称性，即利用  $ \iint_{D} f(x, y) \, \mathrm{d}\sigma = \frac{1}{2} \iint_{D} [f(x, y) + f(y, x)] \, \mathrm{d}\sigma $。

★★★ 二重积分复习标杆

例 14.9 设平面有界区域 D 位于第一象限，由曲线  $ x^2 + y^2 - xy = 1 $， $ x^2 + y^2 - xy = 2 $ 与直线  $ y = \sqrt{3}x $， $ y = 0 $ 围成，计算  $ \iint_D \frac{1}{3x^2 + y^2} \, \mathrm{d}x \, \mathrm{d}y $。

(♣分析) 对于  $ x^2 + y^2 - xy = 1 $， $ x^2 + y^2 - xy = 2 $，将  $ x $， $ y $ 互换，式子不变，所以图像关于  $ y = x $ 对称，根据一些特殊的点及  $ y'(0) = \frac{1}{2} > 0 $， $ y'(1) = -1 < 0 $ 确定单调性，最后将积分区域草图确定下来，根据积分区域来确定  $ \theta $，而且曲线含有  $ x^2 + y^2 $，被积函数分母有平方，则考虑极坐标系下计算。

在考试时，有些D的边界图形不易画出，考生可根据D的表达式来确定上下限。

解 由  $ x^2 + y^2 - xy = 1 $，得  $ r^2 - r^2 \sin \theta \cos \theta = 1 $，故  $ r = \sqrt{\frac{1}{1 - \cos \theta \sin \theta}} $；由  $ x^2 + y^2 - xy = 2 $ 得  $ r^2 - r^2 \sin \theta \cos \theta = 2 $，故  $ r = \sqrt{\frac{2}{1 - \cos \theta \sin \theta}} $。又  $ y = \sqrt{3}x $，得  $ r \sin \theta = \sqrt{3} r \cos \theta $，有  $ \tan \theta = \sqrt{3} $，则  $ \theta = \frac{\pi}{3} $。