若把x与y对调后，Γ不变，则 $ \int_{r}f(x,y,z)\mathrm{d}s=\int_{r}f(y,x,z)\mathrm{d}s $，这就是轮换对称性。关于其他情况与此类似。

具体应用见后面的例子。因为 $ \mathrm{d}s=\sqrt{(\mathrm{d}x)^{2}+(\mathrm{d}y)^{2}+(\mathrm{d}z)^{2}} $在加法上有交换律，交换x与y后， $ \mathrm{d}s $不变

## 4 计算

由于第一型曲线积分就是由定积分推广而来的，因此计算第一型曲线积分的基本方法就是将其化为定积分.口诀为“一投二代三计算”.从定积分来，回到定积分去

(1) 平面情形.

①若平面曲线 L 由  $ y = y(x)(a \leqslant x \leqslant b) $ 给出，则  $ ds = \sqrt{1 + [y'(x)]^2} \, dx $，且

掌握三种体系下曲线积分的计算：①直角坐标系下：

②参数式下：

③极坐标系下



一报二代三计算，这是基本方法的口诀。

\[\begin{aligned}&\int_{L}f(x,\ y)\mathrm{d}s\\=&\int_{a}^{b}f[x,\ y(x)]\sqrt{1+[y^{\prime}(x)]^{2}}\mathrm{d}x.\end{aligned}

<div style="text-align: center;"><img src="imgs/img_in_image_box_698_516_826_628.jpg" alt="Image" width="12%" /></div>


一投：把L投到x轴上去，写成 $ \int_{a}^{b} $

②若平面曲线 L 由参数式  $ \begin{cases} x = x(t), \\ y = y(t) \end{cases} (\alpha \leqslant t \leqslant \beta) $ 给出，则  $ ds = \sqrt{[x'(t)]^2 + [y'(t)]^2} dt $，且

二代：注意这里的 x, y 不是独立的，它是受约束于方程  $ y = y(x) $ 的，一定要把  $ y = y(x) $ 代入  $ f(x, y) $ （这是曲线（曲面）积分的特点，因为这里的变量是定义在线上（面上）的，不具有独立性，所以这里必须代入）；

三、第 2 章：



 $$ \mathrm{d}s=\sqrt{\left(\mathrm{d}x\right)^{2}+\left(\mathrm{d}y\right)^{2}}=\sqrt{1+\left[y^{\prime}(x)\right]^{2}}\mathrm{d}x. $$ 

 $$ \begin{aligned}&\int_{L}f(x,\ y)\mathrm{d}s\\=&\int_{\alpha}^{\beta}f[x(t),\ y(t)]\sqrt{[x^{\prime}(t)]^{2}+[y^{\prime}(t)]^{2}}\mathrm{d}t.\end{aligned} 经过一 $$ 

③若平面曲线 L 由极坐标形式  $ r = r(\theta)(\alpha \leqslant \theta \leqslant \beta) $ 给出，则  $ \mathrm{d}s = \sqrt{[r(\theta)]^2 + [r'(\theta)]^2} \, \mathrm{d}\theta $，且

\[\begin{aligned}&\int_{L}f(x,\ y)\mathrm{d}s\\=&\int_{\alpha}^{\beta}f[r(\theta)\cos\theta,\ r(\theta)\sin\theta]\sqrt{[r(\theta)]^{2}+[r^{\prime}(\theta)]^{2}}\mathrm{d}\theta.\end{aligned}

(2) 空间情形.

若空间曲线Γ由参数式 $ \begin{cases}x=x(t),\\y=y(t),(\alpha\leqslant t\leqslant\beta)\\z=z(t)\end{cases} $给出，则

 $$ \mathrm{d}s=\sqrt{\left[x^{\prime}(t)\right]^{2}+\left[y^{\prime}(t)\right]^{2}+\left[z^{\prime}(t)\right]^{2}}\mathrm{d}t, $$ 

且

 $$ \begin{aligned}&\int_{\Gamma}f(x,y,z)\mathrm{d}s\\=&\int_{\alpha}^{\beta}\underbrace{f[x(t),y(t),z(t)]\sqrt{[x^{\prime}(t)]^{2}+[y^{\prime}(t)]^{2}+[z^{\prime}(t)]^{2}}\mathrm{d}t.\end{aligned} $$ 