其中

 $ e^{\alpha x} $ 照抄，

 $ l=\max\{m,n\},Q_{l}^{(1)}(x),Q_{l}^{(2)}(x) $ 分别为 x 的两个不同的 l 次多项式，

 $ k=\begin{cases}0,&\alpha\pm\beta\mathrm{i}\text{ 不是特征根},\\1,&\alpha\pm\beta\mathrm{i}\text{ 是特征根}.\end{cases} $



 $ y'' + py' + qy = e^{ax}[P_m(x)\cos\beta x + P_n(x)\sin\beta x] $

 $ y^* = e^{ax}[Q_l^{(1)}(x)\cos\beta x + Q_l^{(2)}(x)\sin\beta x]x^k $，其中

 $ \left\{\begin{array}{l}
e^{ax} 照抄（若没有  $ e^{ax} $，表明  $ \alpha = 0 $），\\
l = \max\{m, n\}, Q_l^{(1)}(x), Q_l^{(2)}(x) 分别为 x 的两个不同的 l 次多项式，\\
k = \begin{cases}
0, \alpha \pm \beta i \neq r_{1,2}, \\
1, \alpha \pm \beta i = r_{1,2}.
\end{cases}
\end{array}\right. $

按最高次写一般式

总结：一看，二算，三比较。

 $$ \begin{array}{r l r}&{}&{=\underbrace{\mathrm{e}^{1+x} [(-1)\cos 2x + 0\sin 2x ]}\end{array} $$ 

如： $ y'' - 2y' + 5y = -e^x \cos 2x $

设  $ y^* = \underline{e}^x (\underline{A} \cos 2x + \underline{B} \sin 2x) x^0 $.

一看： $ \alpha \pm \beta i = 1 \pm 2i $

二算： $ r_{1,2} = 1 \pm 2i $

自由项中的  $ \alpha, \beta \stackrel{\downarrow}{r_{1,2}} $

由英国物理学家海威塞德在19世纪末提出，“D”由他引入，使微分方程变为形式上的代数方程，许多数学家批评此方法不全面，不严谨，这让我又想起另一位物理学家，诺贝尔物理学奖得主费曼，他经常在积分号中求导，也被数学家批评不严谨甚至错误，但很多棘手的积分（甚至著名的积分，如Γ函数）在他“荒唐”的方法下，却可轻易得到正确结果，这在第9讲中已经讲过了。

## 注2 特解还可用微分算子法来求解

约定： $  \mathbf{D} = \frac{\mathbf{d}}{\mathbf{dx}}  $， $  \mathbf{D}y = \frac{\mathrm{d}y}{\mathrm{dx}}  $， $  \mathbf{D}^2 = \frac{\mathrm{d}^2}{\mathrm{dx}^2}  $， $  \mathbf{D}^2y = \frac{\mathrm{d}^2y}{\mathrm{dx}^2}  $，于是微分方程  $  y'' + py' + qy = f(x)  $ 即可写成  $  (\mathbf{D}^2 + p\mathbf{D} + q)y = f(x)  $，进一步记  $  \mathbf{D}^2 + p\mathbf{D} + q = F(\mathbf{D})  $，称为算子多项式，它满足普通多项式的运算规则，如因式分解等，则上述微分方程即可写成  $  F(\mathbf{D})y = f(x)  $，此时它的一个特解为

 $$ y^{*}=\frac{1}{F(\mathrm{D})}f(x)\ . $$ 

在约定 “D” 表示求导的条件下，约定 “ $ \frac{1}{D} $” 表示积分，如  $ D\sin x = \cos x $， $ \frac{1}{D}\sin x = -\cos x $（取 C = 0）.

① $ \frac{1}{F(D)}e^{\alpha x} $型.

若  $ F(D)|_{D=\alpha} \neq 0 $，有  $ y^* = \frac{1}{F(D)} |_{D=\alpha} e^{\alpha x} $ 注例1