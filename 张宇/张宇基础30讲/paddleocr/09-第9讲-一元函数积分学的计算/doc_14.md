解 应填 $ \frac{1}{2}\ln3 $.

由例 1.1 知，当  $ x \geqslant 2 $ 时， $ f(x) = \frac{x}{x^{2} - 2} $，则

 $$ \int_{2}^{2\sqrt{2}}f(x)\mathrm{d}x=\int_{2}^{2\sqrt{2}}\frac{x}{x^{2}-2}\mathrm{d}x=\left.\frac{1}{2}\ln(x^{2}-2)\right|_{2}^{2\sqrt{2}}=\frac{1}{2}\ln3 $$ 

由牛顿-莱布尼茨公式结合不定积分的计算方法，有定积分的换元积分法和分部积分法，分别如下.

换元要三换：①被积函数要换；②积分变量要换；③上下限要换

 $$ \begin{array}{r} \left.\begin{array}{c} \downarrow \\ f(x)\rightarrow f[\varphi(t)]\qquad\qquad\mathrm{d}x\rightarrow\varphi^{\prime}(t)\mathrm{d}t\qquad\qquad\int_{a}^{b}\rightarrow\int_{a}^{\beta} \end{array} \right] \\ \left[\begin{array}{cc} \downarrow & \downarrow \\ \left[\begin{array}{c} \delta_{a} \\ \alpha \end{array} \right] \end{array} \right] \\ \succeq 0 \end{array} $$ 

(1) 定积分的换元积分法.

设  $ f(x) $ 在  $ [a, b] $ 上连续，函数  $ x = \varphi(t) $ 满足 ①  $ \varphi(\alpha) = a $， $ \varphi(\beta) = b $；②  $ x = \varphi(t) $ 在  $ [\alpha, \beta] $（或  $ [\beta, \alpha] $ 上有连续的导数，且其值域为  $ R_{\varphi} = [a, b] $，则有

常考：令  $ x = \frac{\pi}{2} \pm t $，则有  $ \begin{cases} \sin\left(\frac{\pi}{2} \pm t\right) = \cos t, \\ \cos\left(\frac{\pi}{2} \pm t\right) = \mp \sin t. \end{cases} $

 $$ \int_{a}^{b}f(x)\mathrm{d}x=\int_{\alpha}^{\beta}f[\varphi(t)]\varphi^{\prime}(t)\mathrm{d}t $$ 

令 $ x=\pi\pm t $，则有 $ \begin{cases}\sin(\pi\pm t)=\mp\sin t;\\\cos(\pi\pm t)=-\cos t\end{cases} $

注 当  $ \varphi(t) $ 的值域  $ R_{\varphi} $ 超出  $ [a, b] $，但  $ \varphi(t) $ 满足其余条件时，只要  $ f(x) $ 在  $ R_{\varphi} $ 上连续，则上述结论仍成立.

(2) 定积分的分部积分法.

 $$ \int_{a}^{b}u(x)\nu^{\prime}(x)\mathrm{d}x=u(x)\nu(x)\Big|_{a}^{b}-\int_{a}^{b}\nu(x)u^{\prime}(x)\mathrm{d}x, $$ 

这里要求  $ u'(x) $,  $ v'(x) $ 在  $ [a, b] $ 上连续.

注 在计算定积分时，下面这些结论是很有用的.

(1) 设  $ f(x) $ 为连续的偶函数，则

 $$ \int_{-a}^{a}f(x)\mathrm{d}x=2\int_{0}^{a}f(x)\mathrm{d}x $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_665_1042_818_1134.jpg" alt="Image" width="14%" /></div>


(2) 设  $ f(x) $ 为连续的奇函数，则

 $$ \int_{-a}^{a}f(x)\mathrm{d}x=0\ . $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_686_1143_865_1251.jpg" alt="Image" width="17%" /></div>


(3) 设  $ f(x) $ 是以 T 为周期的连续函数，则对任意的实数 a，都有

 $$ \int_{a}^{a+T}f(x)\mathrm{d}x=\int_{0}^{T}f(x)\mathrm{d}x, $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_293_1308_464_1406.jpg" alt="Image" width="16%" /></div>


 $$ \int_{\frac{T}{2}}^{\frac{T}{2}+T}f(x)\mathrm{d}x=\int_{0}^{T}f(x)\mathrm{d}x $$ 