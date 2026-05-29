如果能得出 $ f(1) $， $ f'(x) $，即可求解本题.

令x=1，由 $ f(x) $表达式可得 $ f(1)=\int_{1}^{1}e^{-t^{2}}dt=0 $，又 $ f'(x)=e^{-x^{4}}(x^{2})'=2xe^{-x^{4}} $，因此

 $$ \begin{aligned}\int_{0}^{1}x f(x)\mathrm{d}x&=-\int_{0}^{1}\frac{x^{2}}{2}\bullet2x\mathrm{e}^{-x^{4}}\mathrm{d}x=-\int_{0}^{1}x^{3}\mathrm{e}^{-x^{4}}\mathrm{d}x=\frac{1}{4}\int_{0}^{1}\mathrm{e}^{-x^{4}}\mathrm{d}(-x^{4})\\&=\frac{1}{4}\mathrm{e}^{-x^{4}}\bigg|_{0}^{1}=\frac{1}{4}(\mathrm{e}^{-1}-1)\end{aligned} $$ 

故选(B).

## 四 变限积分的计算

<div style="text-align: center;"><img src="imgs/img_in_image_box_842_433_946_541.jpg" alt="Image" width="10%" /></div>


## 求导公式

设  $ F(x)=\int_{\varphi_{1}(x)}^{\varphi_{2}(x)}f(t)dt $，其中  $ f(x) $ 在  $ [a,b] $ 上连续，可导函数  $ \varphi_{1}(x) $ 和  $ \varphi_{2}(x) $ 的值域在  $ [a,b] $ 上，则在函数  $ \varphi_{1}(x) $ 和  $ \varphi_{2}(x) $ 的公共定义域上，有

 $$ \begin{aligned}F^{\prime}(x)=\frac{\mathrm{d}}{\mathrm{d}x}\left[\int_{\varphi_{1}(x)}^{\varphi_{2}(x)}f(t)\mathrm{d}t\right]=f[\varphi_{2}(x)]\varphi_{2}^{\prime}\left(x\right)-f[\varphi_{1}(x)]\varphi_{1}^{\prime}\left(x\right)\\ \stackrel{\downarrow}{\underset{}{\mathrm{d}x}}\left[\int_{x^{2}}^{\sin^{2}x}f(t^{2})\mathrm{d}t\right]^{\prime}=2\sin x\cos x\cdot f(\sin^{4}x)-2x\cdot f(x^{4})\end{aligned} $$ 

注 我们称上面公式中的 x 为 “求导变量”，t 为 “积分变量”。当被积函数中只含 “积分变量” t 时，才能用求导公式，若被积函数中有 “求导变量” x，则必须通过恒等变形（比如变量代换等）将其移出被积函数，才能使用变限积分求导公式。 $ \rightarrow $ 如  $ f(x) \text{ 中令 } x = u $ （x 当作常量）

例9.20 曲线  $ y=\int_{0}^{\sin x}e^{t^{2}}dt $ 在点  $ (0,0) $ 处的法线方程为（）.

(A)  $ y=\frac{1}{2}x $ (B)  $ y=-\frac{1}{2}x $ (C) y=x (D) y=-x

☑分析 欲求曲线在给定点处的法线方程，应先检查此点是否在曲线上，如果此点在曲线上，再求该点处切线的斜率，最后利用点斜式求法线方程。

解 应选(D).

易知点 $ (0,0) $在曲线 $ y=\int_{0}^{\sin x}e^{t^{2}}dt $上.

由于  $ y' = e^{\sin^2 x} \cdot \cos x $,  $ y'\big|_{x=0} = 1 $，可知切线斜率 k = 1，法线斜率为  $ -\frac{1}{k} = -1 $，因此所求法线方程为 y = -x。故选 (D).

例 9.21  $ F(x)=\int_{0}^{\frac{\pi}{2}}\left|\sin x-\sin t\right|dt(x\geq0) $ 在  $ x\to0^{+} $ 处的二次泰勒多项式为  $ a+bx+cx^{2} $，则后续更新去公众号[有机研]永久联系微信 4550060