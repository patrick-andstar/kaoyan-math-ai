<div style="text-align: center;"><img src="imgs/img_in_image_box_211_137_314_220.jpg" alt="Image" width="9%" /></div>


解 设  $ x = a \sin t $，则  $ dx = a \cos t dt $， $ t = \arcsin \frac{x}{a} $，所以

 $$ \begin{aligned}\int\sqrt{a^{2}-x^{2}}\mathrm{d}x=&\int\sqrt{a^{2}-a^{2}}\sin^{2}t\cdot a\cos t\mathrm{d}t=a^{2}\int\cos^{2}t\mathrm{d}t=\frac{a^{2}}{2}\int(1+\cos2t)\mathrm{d}t\\=&\frac{a^{2}}{2}t+\frac{a^{2}}{4}\sin2t+C=\frac{a^{2}}{2}t+\frac{a^{2}}{2}\sin t\cos t+C\\=&\frac{a^{2}}{2}\arcsin\frac{x}{a}+\frac{x}{2}\sqrt{a^{2}-x^{2}}+C.\end{aligned} $$ 

## 3 分部积分法

(1)  $ \int u \, dv = uv - \int v \, du $.

 $ \downarrow $

难算 易算

这个方法主要适用于求  $ \int u dv $ 比较困难，而  $ \int v du $ 比较容易的情形.

 $ \underline{\text{注2}} $ 积分后会“简单”些的函数宜取作v；微分后会“简单”些的函数宜取作u.故u,v的选取原则为指、三均可为u

<div style="text-align: center;"><img src="imgs/img_in_image_box_117_850_631_911.jpg" alt="Image" width="49%" /></div>


相对位置在左边的宜选作 u，用来求导；相对位置在右边的宜选作 v，用来积分，即

(1) 被积函数为  $ P_n(x)e^{kx} $， $ P_n(x)\sin ax $， $ P_n(x)\cos ax $ 等形式时，一般来说选取  $ u = P_n(x) $

(2) 被积函数为  $ e^{ax} \sin bx $， $ e^{ax} \cos bx $ 等形式时，u 可以取两因子中的任意一个；

(3) 被积函数为  $ P_n(x)\ln x $， $ P_n(x)\arcsin x $， $ P_n(x)\arctan x $ 等形式时，一般分别选取

 $$ u=\ln x,\;u=\arcsin x,\;u=\arctan x. $$ 

 $$ \begin{aligned}\oint_{D}\int\limits_{U}\ln(1+x^{2})\mathrm{d}x&=\int\limits_{U}\ln(1+x^{2})\cdot x^{\prime}\mathrm{d}x\\&=\ln(1+x^{2})\cdot x-\int_{U}x\cdot\frac{2x}{1+x^{2}}\mathrm{d}x\\&=x\ln(1+x^{2})-2\int\limits_{U}\frac{x^{2}+1-1}{x^{2}+1}\mathrm{d}x\\&=x\ln(1+x^{2})-2x+2\arctan x+\end{aligned} $$ 

 $$ \begin{aligned} 故 \int x^{3}\mathrm{e}^{x}\mathrm{d}x&=\int x^{3}\mathrm{d}(\mathrm{e}^{x})=x^{3}\mathrm{e}^{x}-\int\mathrm{e}^{x}\cdot3x^{2}\mathrm{d}x\\&=x^{3}\mathrm{e}^{x}-3\int x^{2}\mathrm{d}(\mathrm{e}^{x})\\&=x^{3}\mathrm{e}^{x}-3\left(x^{2}\mathrm{e}^{x}-\int\mathrm{e}^{x}\cdot2x\mathrm{d}x\right)\\&=x^{3}\mathrm{e}^{x}-3x^{2}\mathrm{e}^{x}+6x\mathrm{e}^{x}-6\mathrm{e}^{x}+C\end{aligned} $$ 