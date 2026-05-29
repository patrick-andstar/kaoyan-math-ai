注 (1) 在直角坐标系中，若  $ f(x, y) + f(y, x) = a $，则

 $$ I=\frac{1}{2}\iint_{D}[f(x,y)+f(y,x)]\mathrm{d}x\mathrm{d}y=\frac{1}{(>)}2\iint_{D}a\mathrm{d}x\mathrm{d}y=\frac{a}{2}S_{D} $$ 

(2)要注意区分普通对称性中的④与这里轮换对称性的区别与联系.虽然它们都是D关于y=x对称，但普通对称性考查的是 $ f(x,y) $与 $ f(y,x) $是相等还是相反，轮换对称性考查的是 $ f(x,y)+f(y,x) $是否简单.事实上，当 $ f(x,y)=-f(y,x) $时，它们是一回事.

例 14.4 设  $ f(x)=\iint_{D(x)}\frac{v\ln\sqrt{u^{2}+v^{2}}}{u+v}\mathrm{d}u\mathrm{d}v $,  $ D(x)=\left\{(u,v)\middle|\frac{1}{4}\leq u^{2}+v^{2}\leq x^{2},u>0,v>0\right\}\left(x>\frac{1}{2}\right) $，则  $ f(x)= $（ ）.

(A)  $ \frac{1}{4}\iint_{D(x)}\ln(u^{2}+v^{2})\mathrm{d}u\mathrm{d}v $

(B)  $ \frac{1}{2}\iint_{D(x)}\ln(u^{2}+v^{2})\mathrm{d}u\mathrm{d}v $

(C)  $ \iint_{D(x)}\ln(u^{2}+v^{2})\mathrm{d}u\mathrm{d}v $

(D)  $ 2\iint_{D(x)}\ln(u^{2}+v^{2})\mathrm{d}u\mathrm{d}v $

(2) 分析 D 中 u，v 互换位置，D 不变，接着看  $ g(u, v) $ 与  $ g(v, u) $ 的关系既不相等，也不相反，考虑将其加起来， $ g(u, v) + g(v, u) $ 计算简单，所以考虑轮换对称性。

解 应选(A).

由轮换对称性，有

 $$ \begin{aligned}f(x)&=\iint\limits_{D(x)}\frac{\nu\ln\sqrt{u^{2}+\nu^{2}}}{u+\nu}\mathrm{d}u\mathrm{d}\nu=\iint\limits_{D(x)}\frac{u\ln\sqrt{u^{2}+\nu^{2}}}{u+\nu}\mathrm{d}u\mathrm{d}\nu\\&=\frac{1}{2}\iint\limits_{D(x)}\ln\sqrt{u^{2}+\nu^{2}}\mathrm{d}u\mathrm{d}\nu=\frac{1}{4}\iint\limits_{D(x)}\ln(u^{2}+\nu^{2})\mathrm{d}u\mathrm{d}\nu.\end{aligned} $$ 

方法总结 当 D 关于 y = x 对称， $ f(x, y) = -f(y, x) $ 或  $ f(x, y) = f(y, x) $ 时，考虑普通对称性，若不满足，可看  $ f(x, y) + f(y, x) $ 是否简单，考虑轮换对称性。

<div style="text-align: center;"><img src="imgs/img_in_image_box_83_1110_119_1146.jpg" alt="Image" width="3%" /></div>


## 计算

<div style="text-align: center;"><img src="imgs/img_in_image_box_836_1067_940_1172.jpg" alt="Image" width="10%" /></div>


## 直角坐标系下的计算方法

直角坐标系用平行于坐标系的线切割。

问题：先对 x 积分，还是对 y 积分？

在直角坐标系下，按照积分次序的不同，一般将二重积分的计算分为两种情况，如图 14-6 所示。



<div style="text-align: center;"><img src="imgs/img_in_image_box_574_1209_869_1309.jpg" alt="Image" width="28%" /></div>
