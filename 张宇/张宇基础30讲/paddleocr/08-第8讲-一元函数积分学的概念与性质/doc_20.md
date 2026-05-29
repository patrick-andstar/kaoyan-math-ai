★★★ (2) 函数  $ f(x) $ 在 I 上连续，则函数  $ F(x)=\int_{a}^{x}f(t)dt $ 在 I 上可导且  $ F'(x)=f(x) $.

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_244_348_355.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_420_186_560_373.jpg" alt="Image" width="13%" /></div>


(3) 若  $ x = x_0 \in I $ 是  $ f(x) $ 唯一的跳跃间断点，则  $ F(x) = \int_a^x f(t) \, dt $ 在  $ x_0 $ 处不可导，且  $ \left\{ \begin{array}{l} F_-(x_0) = \lim_{x \to x_0} f(x), \\ F_+(x_0) = \lim_{x \to x_0} f(x). \end{array} \right. $

若  $ x = x_0 \in I $ 是  $ f(x) $ 唯一的可去间断点，则  $ F(x) = \int_a^x f(t) \, dt $ 在  $ x_0 $ 处可导，且  $ F'(x_0) = \lim_{x \to x_0} f(x) \neq f(x_0) $。

注 (1) 第一个性质的证明如下.  $ \rightarrow $ 该证明不需掌握，看懂即可.

证 对任意  $ x, x + \Delta x \in I $，有

 $$ F(x+\Delta x)-F(x)=\int_{x}^{x+\Delta x}f(t)\mathrm{d}t $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_666_599_871_704.jpg" alt="Image" width="19%" /></div>


由可积的必要条件可知，存在 M > 0，使得在 I 上有  $ |f(x)| \leq M $，所以有

 $$ 0\leqslant\left|F(x+\Delta x)-F(x)\right|\leqslant M\left|\Delta x\right|, $$ 

则  $ \lim_{\Delta x \to 0} |F(x + \Delta x) - F(x)| = 0 $，即  $ \lim_{\Delta x \to 0} [F(x + \Delta x) - F(x)] = 0 $ 或  $ \lim_{\Delta x \to 0} F(x + \Delta x) = F(x) $，得证。

由此可见，对于变限积分  $ F(x)=\int_{a}^{x}f(t)dt $，只要它存在，就必然是连续的。

(2) 第二个性质的证明如下.

证 对任意的  $ x, x + \Delta x \in I $，由于函数  $ f(x) $ 连续，因此

 $$ \begin{aligned}\lim_{\Delta x\rightarrow0}\frac{F(x+\Delta x)-F(x)}{\Delta x}&=\lim_{\Delta x\rightarrow0}\frac{\int_{a}^{x+\Delta x}f(t)\mathrm{d}t-\int_{a}^{x}f(t)\mathrm{d}t}{\Delta x}\\&=\lim_{\Delta x\rightarrow0}\frac{\int_{x}^{x+\Delta x}f(t)\mathrm{d}t}{\Delta x}=\lim_{\Delta x\rightarrow0}\frac{f(\xi)\Delta x}{\Delta x}=\lim_{\Delta x\rightarrow0}f(\xi)=f(x),\end{aligned} $$ 

其中  $ \xi $ 介于  $ x $ 与  $ x + \Delta x $ 之间。

由此可见，如果函数$f(x)$在区间$I$上连续，则$F(x)=\int_{a}^{x}f(t)dt$是$f(x)$在区间$I$上的一个原函数。

(3) 第三个性质的证明如下.