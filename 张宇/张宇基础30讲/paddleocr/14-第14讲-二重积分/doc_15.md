☐分析 积分区域关于 y = x 对称，同时观察被积函数的特点，所以考虑轮换对称性.又因为积分区域是  $ \frac{1}{4} $ 个圆环，且被积函数含有平方和，所以考虑极坐标计算.

因为本题最终求的是  $ y(x) $ 的二阶导数，即  $ f(x) $ 的一阶导数，所以不必要真正计算出二重积分，只转化为变限积分即可.

解 由轮换对称性，根据例 14.4 知，有

 $$ \begin{aligned}f(x)&=\frac{1}{4}\iint\limits_{D(x)}\ln(u^{2}+v^{2})\mathrm{d}u\mathrm{d}v\\&=\frac{1}{4}\int_{0}^{\frac{\pi}{2}}\mathrm{d}\theta\int_{\frac{1}{2}}^{x}\ln r^{2}\cdot r\mathrm{d}r\\&=\frac{\pi}{4}\int_{\frac{1}{2}}^{x}r\ln r\mathrm{d}r,\end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_784_351_944_487.jpg" alt="Image" width="15%" /></div>


故 $ y'(x)=f(x) $， $ y''(x)=f'(x)=\frac{\pi}{4}x\ln x\xlongequal{\text{令}}0 $，得x=1。当 $ \frac{1}{2}<x<1 $时， $ y''(x)<0 $，当x>1时， $ y''(x)>0 $，于是 $ (1,0) $为 $ y(x) $的拐点。

方法总结 积分区域 $D$ 关于 $y = x$ 对称，考虑轮换对称性，即利用 $\iint_{D} f(x, y) \, \mathrm{d}\sigma = \frac{1}{2} \iint_{D} [f(x, y) + f(y, x)] \, \mathrm{d}\sigma$。

例 14.11 计算 $\int_{0}^{+\infty} e^{-x^2} \, \mathrm{d}x$。

♂分析 因为  $ e^{ax^2 + bx + c} (a \neq 0) $ 没有初等函数形式下的原函数，积分与字母无关，所以  $ I = \int_0^{+\infty} e^{-x^2} \, dx = \int_0^{+\infty} e^{-y^2} \, dy $。又因为  $ \iint_D e^{-(x^2 + y^2)} \, d\sigma $ 易计算，所以计算  $ I^2 $。根据被积函数为  $ x^2 + y^2 $ 的表达式，选择极坐标计算，将第一象限看成广义的  $ \frac{1}{4} $ 个圆，其半径  $ r \to +\infty $。

解 设  $ I=\int_{0}^{+\infty}e^{-x^{2}}dx $，则简化版解法

 $$ \begin{aligned}I^{2}&=\int_{0}^{+\infty}\mathrm{e}^{-x^{2}}\mathrm{d}x\cdot\int_{0}^{+\infty}\mathrm{e}^{-x^{2}}\mathrm{d}x=\int_{0}^{+\infty}\mathrm{e}^{-x^{2}}\mathrm{d}x\cdot\int_{0}^{+\infty}\mathrm{e}^{-y^{2}}\mathrm{d}y\\ &=\int_{0}^{+\infty}\mathrm{d}x\int_{0}^{+\infty}\mathrm{e}^{-(x^{2}+y^{2})}\mathrm{d}y=\iint\limits_{0\leq x<+\infty\atop0\leq y<+\infty}\mathrm{e}^{-(x^{2}+y^{2})}\mathrm{d}x\mathrm{d}y\\ &=\int_{0}^{\frac{\pi}{2}}\mathrm{d}\theta\cdot\int_{0}^{+\infty}\mathrm{e}^{-r^{2}}\cdot r\mathrm{d}r=\frac{\pi}{2}\cdot\left(-\frac{1}{2}\right)\int_{0}^{+\infty}\mathrm{e}^{-r^{2}}\mathrm{d}(-r^{2})\\ &=-\frac{\pi}{4}\mathrm{e}^{-r^{2}}\bigg|_{0}^{+\infty}=\frac{\pi}{4},\\ \end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_786_1000_882_1084.jpg" alt="Image" width="9%" /></div>


 $ \int_{-\infty}^{+\infty}e^{-x^{2}}dx=\sqrt{\pi} $，这叫高斯积分。如同欧拉公式  $ e^{xi}+1=0 $ 一样美妙。它们都同时包含  $ e,\pi $

由积分的保号性知 I > 0，故  $ I = \int_{0}^{+\infty} e^{-x^{2}} dx = \frac{\sqrt{\pi}}{2} $