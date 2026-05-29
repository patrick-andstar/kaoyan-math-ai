明：在区间 $ (-1,1) $内至少存在一点 $ \xi $，使 $ f^{m}(\xi)=3 $

♡分析）遇到 $ f $与 $ f^{(n)}(n \geqslant 2) $的关系，考虑泰勒公式。

证 将 $ f(x) $在x=0处展开成带拉格朗日余项的二阶泰勒公式，得

 $$ f(x)=f(0)+f^{\prime}(0)x+\frac{1}{2!}f^{\prime \prime}(0)x^{2}+\frac{1}{3!}f^{\prime \prime \prime}(\eta)x^{3}, $$ 

其中  $ \eta $ 介于 0 与 x 之间，  $ x \in [-1, 1] $.

分别令 x = -1 和 x = 1，并结合已知条件，得

 $$ 0=f(-1)=f(0)+\frac{1}{2}f^{\prime \prime}(0)-\frac{1}{6}f^{\prime \prime \prime}(\eta_{1}),-1<\eta_{1}<0, $$ 

 $$ 1=f(1)=f(0)+\frac{1}{2}f^{\prime \prime}(0)+\frac{1}{6}f^{\prime \prime \prime}(\eta_{2}),0<\eta_{2}<1, $$ 

两式相减，可得 $ f''(\eta_{1})+f'''(\eta_{2})=6 $

由 $ f'''(x) $的连续性知， $ f'''(x) $在区间 $ [\eta_1, \eta_2] $上有最大值和最小值，设它们分别为M和m，则有

 $$ m\leqslant\frac{1}{2}[f^{\prime \prime \prime}(\eta_{1})+f^{\prime \prime \prime}(\eta_{2})]\leqslant M,\quad\begin{aligned}& 由 m\leqslant f^{\prime \prime \prime}(x)\leqslant M\quad,\quad 则 m\leqslant f^{\prime \prime \prime}(\eta_{1})\leqslant M\quad,\end{aligned} $$ 

再由连续函数的介值定理知，至少存在一点  $ \xi \in [\eta_1, \eta_2] \subset (-1, 1) $，使

 $$ f^{m}(\xi)=\frac{1}{2}\left[f^{m}(\eta_{1})+f^{m}(\eta_{2})\right]=3\quad. $$ 

## 注 泰勒公式：

 $$ f(x)=f(x_{0})+f^{\prime}(x_{0})(x-x_{0})+\frac{1}{2!}f^{\prime \prime}(x_{0})(x-x_{0})^{2}+\frac{1}{3!}f^{\prime \prime \prime}(\eta)(x-x_{0})^{3}(\eta 介于 x,x_{0} 之间 ), $$ 

关键是把握好展开点  $ x_{0} $ （取已知导数值的点或待证导数值的点）和被展开点  $ x $ （取已知函数值的点或特殊点，如端点、中间点等），同时要想办法消去未知的函数项或导数项，向结论靠拢。

<div style="text-align: center;"><img src="imgs/img_in_image_box_93_1088_129_1125.jpg" alt="Image" width="3%" /></div>


## 微分等式

<div style="text-align: center;"><img src="imgs/img_in_image_box_845_1058_950_1163.jpg" alt="Image" width="10%" /></div>


方程 $ f(x)=0 $的根就是函数 $ f(x) $的零点。从几何上讲，方程的根作为两条曲线的交点，代数语言“ $ f(x)=g(x) $的根”与几何语言“曲线 $ f(x) $与 $ g(x) $的交点”，两者概念不同，但描述的是同一件事。基于此，为讨论方程的根，有时可改为讨论曲线的交点。讨论方程根的问题（也称为函数的零点问题）通常可以考虑下面这些方法。