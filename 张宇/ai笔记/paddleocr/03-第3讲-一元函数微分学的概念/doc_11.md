解 显然，在 x=0 处  $ \frac{\Delta y}{\Delta x}=\frac{f(0+\Delta x)-f(0)}{\Delta x}=\frac{(\Delta x)^{\frac{1}{3}}}{\Delta x}=\frac{1}{(\Delta x)^{\frac{2}{3}}} $

当  $ \Delta x > 0 $ 时， $ f_{+}^{\prime}(0) = \lim_{\Delta x \to 0^{+}} \frac{1}{(\Delta x)^{\frac{2}{3}}} = +\infty $;

当  $ \Delta x < 0 $ 时， $ f_{-}^{\prime}(0) = \lim_{\Delta x \to 0^-} \frac{1}{(\Delta x)^{\frac{2}{3}}} = +\infty $.

这样的结果称为无穷导数. 又±∞被叫作广义的数，所以无穷导数在有些数学场合也可被视为导数存在的特殊情形. 不过要强调的是，学习“高等数学”这门课程的考生，还是将无穷导数视为导数不存在为好，因为这是“高等数学”里的“规矩”.

<div style="text-align: center;"><img src="imgs/img_in_image_box_744_343_906_489.jpg" alt="Image" width="15%" /></div>


<div style="text-align: center;">图 3-12</div>


还要指出，如图 3-12 和图 3-13 所示， $ y = f(x) = x^{\frac{1}{3}} $ 与  $ y = f(x) = -x^{\frac{1}{3}} $ 在 x = 0 处有垂直于 x 轴的切线 x = 0 。我们说，若曲线  $ y = f(x) $ 在点  $ P(x_{0}, y_{0}) $ 处有垂直于 x 轴的切线，则等价于

<div style="text-align: center;"><img src="imgs/img_in_image_box_724_565_911_697.jpg" alt="Image" width="18%" /></div>


 $$ f^{\prime}(x_{0})=+\infty 或 -\infty( 为无穷导数 ). $$ 

<div style="text-align: center;">图 3-13</div>


总结：① $ f_{+}^{\prime}(x_{0})\neq f_{-}^{\prime}(x_{0}) $，出现角点（尖点），则 $ f(x) $在 $ x_{0} $处不可导，没有切线；

② $ f(x) $在点 $ x_{0} $的导数是无穷导数时，在该点有切线但无导数.

例 3.8 设曲线  $ y = f(x) = x^n $ 在点  $ (1, 1) $ 处的切线与  $ x $ 轴的交点为  $ (\xi_n, 0) $，则  $ \lim_{n \to \infty} f(\xi_n) = $ ___.

♣ 分析 由  $ f_n(x) = x^n $（其中  $ \{f_n(x)\} $ 是函数列），知

 $$ f_{1}(x)=x^{1}\Rightarrow f_{1}^{\prime}(1)=1, $$ 

 $$ f_{2}(x)=x^{2}\Rightarrow f_{2}^{\prime}(1)=2, $$ 

 $$ f_{n}(x)=x^{n}\Rightarrow f_{n}^{\prime}(1)=n. $$ 

## 解 应填 $ \frac{1}{e} $

由于  $ f'(1)=\left.\frac{dy}{dx}\right|_{x=1}=nx^{n-1}\bigg|_{x=1}=n,n=1,2,\cdots $ ，故过点  $ (1,1) $ 的切线方程为  $ y-1=n(x-1) $ ，令 y=0 得  $ x=\xi_{n}=1-\frac{1}{n} $ 。于是

 $$ \lim_{n\to\infty}f(\xi_{n})=\lim_{n\to\infty}\left(1-\frac{1}{n}\right)^{n}=\frac{1}{\mathrm{e}}. $$ 