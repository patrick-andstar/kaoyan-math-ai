由 (1) 知， $ \int_{a}^{x}g(u)du \leqslant x - a $，即  $ a + \int_{a}^{x}g(u)du \leqslant x, x \in [a, b] $。又因为  $ f(x) $ 单调增加，且  $ g(x) \geqslant 0 $ 所以  $ F'(x) \leqslant 0 $，从而  $ F(x) $ 在区间  $ [a, b] $ 上单调减少。

又  $ F(a)=0 $ ，故  $ F(b)\leqslant0 $ ，即  $ \int_{a}^{a+\int_{a}^{b}g(t)dt}f(x)dx\leqslant\int_{a}^{b}f(x)g(x)dx $

<div style="text-align: center;"><img src="imgs/img_in_image_box_710_185_938_295.jpg" alt="Image" width="22%" /></div>


## 2 用拉格朗日中值定理

此方法多用于所给条件为“ $ f(x) $一阶可导”且某一端点值较简单（甚至为0）的题目。

例 11.8 设  $ f(x) $ 在  $ [0,1] $ 上具有一阶连续导数，且  $ f(0)=f(1)=0 $ 。记  $ M=\max_{x\in[0,1]}\left\{\left|f'(x)\right|\right\} $ 。证明：

★ 见到  $ f(x) $， $ f'(x) $ 。想括格朗日中值定理  $ \left|\int_{0}^{1}f(x)dx\right|\leqslant\frac{1}{4}M $ 。

## 证 将大区间  $ [0,1] $ 分成两个小区间  $ [0,x] $ 和  $ [x,1] $

在  $ [0, x] $ 上对  $ f(x) $ 使用拉格朗日中值定理，得  $ f(x) - f(0) = f(x) = f'(\xi_1)x $，其中  $ \xi_1 \in (0, x) $，于是  $ \begin{array}{c}0 \\ \xi_1 \quad x \quad \xi_2\end{array} $  $ \begin{array}{c}1 \\ \end{array} $  $ \begin{array}{c}|f(x)| = |f'(\xi_1)|x\end{array} $

<div style="text-align: center;"><img src="imgs/img_in_image_box_174_603_314_658.jpg" alt="Image" width="13%" /></div>


在  $ [x, 1] $ 上对  $ f(x) $ 使用拉格朗日中值定理，得  $ f(1) - f(x) = -f(x) = f'(\xi_2)(1 - x) $，其中  $ \xi_2 \in (x, 1) $，于是  $ \left|f(x)\right| = \left|f'(\xi_2)\right|(1 - x) $。

当 $ x\in[0,1] $时，因为 $ M=\max\left\{\left|f'(x)\right|\right\} $，所以

 $$ \left|f(x)\right|\leqslant Mx,\left|f(x)\right|\leqslant M(1-x), $$ 

于是

利用不等式 $ |a+b|\leq|a|+|b| $，见第2讲“6.夹逼准则”的注(2) $ ^{①} $

 $$ \begin{aligned}\left|\int_{0}^{1}f(x)\mathrm{d}x\right|=&\left|\int_{0}^{x}f(t)\mathrm{d}t+\int_{x}^{1}f(t)\mathrm{d}t\right|\leqslant\left|\int_{0}^{x}f(t)\mathrm{d}t\right|+\left|\int_{x}^{1}f(t)\mathrm{d}t\right|\leqslant\int_{0}^{x}\left|f(t)\right|\mathrm{d}t+\int_{x}^{1}\left|f(t)\right|\mathrm{d}t\\ \leqslant&M\int_{0}^{x}t\mathrm{d}t+M\int_{x}^{1}(1-t)\mathrm{d}t=M\left[\frac{x^{2}}{2}+\frac{(1-x)^{2}}{2}\right],\end{aligned} $$ 

其中， $ \frac{x^{2}}{2}+\frac{(1-x)^{2}}{2}=x^{2}-x+\frac{1}{2}=\left(x-\frac{1}{2}\right)^{2}+\frac{1}{4}\geqslant\frac{1}{4} $，故得证.

## 3 用泰勒公式

此方法多用于所给条件为“ $ f(x) $二阶可导”且题中有简单函数值（甚至为0）的题目。

例 11.9 设  $ f(x) $ 在  $ [0, 2] $ 上二阶导数连续，且  $ f(1) = 0 $。当  $ x \in [0, 2] $ 时，记  $ M = \max\left\{\left|f''(x)\right|\right\} $，证明： $ \left|\int_{0}^{2} f(x) \, dx\right| \leqslant \frac{1}{3} M $。

♂分析 当无法用牛顿－莱布尼茨公式时，可考虑用泰勒公式将被积函数 $ f(x) $展开成多项式再做.

根据题设，选取点  $ x_{0}=1 $ 展开成泰勒公式，则