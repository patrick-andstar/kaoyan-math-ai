## ② 二阶常系数非齐次线性微分方程

(1) 概念.  $ \rightarrow y^{*}+py'+qy=0 $ 也称为非齐次方程  $ y^{*}+py'+qy=f(x)(f(x)\neq0) $ 的“导出方程”.

方程  $ y'' + py' + qy = f(x)(f(x) \neq 0) $ 称为二阶常系数非齐次线性微分方程，其中 p, q 为常数， $ f(x) $ 为已知的连续函数，叫作自由项。

(2) 解的结构.

①若 $ y_{1}^{*}(x) $是 $ y''+py'+qy=f_{1}(x) $的解， $ y_{2}^{*}(x) $是 $ y''+py'+qy=f_{2}(x) $的解，则 $ y_{1}^{*}(x)+y_{2}^{*}(x) $是 $ y''+py'+qy=f_{1}(x)+f_{2}(x) $的解．

②设 $ y_{1}^{*} $， $ y_{2}^{*} $都是 $ y''+py'+qy=f(x) $的特解，则 $ y_{1}^{*}-y_{2}^{*} $是对应齐次方程的解.

## (3) 特解的设定 → 待定系数法 + 微分算子法

对于  $ y'' + py' + qy = f(x) $，《全国硕士研究生招生考试数学考试大纲》规定我们需要会求以下两种情况下的特解．

设 $ P_{n}(x) $， $ P_{m}(x) $分别为x的n次、m次多项式.

①当自由项 $ f(x)=P_{n}(x)\mathrm{e}^{\alpha x} $时，特解要设为 $ y^{*}=\mathrm{e}^{\alpha x}Q_{n}(x)x^{k} $，其中

 $ e^{\alpha x} $ 照抄，

 $ Q_n(x) $ 为  $ x $ 的  $ n $ 次多项式，

 $ k = \begin{cases} 0, & \alpha \text{不是特征根}, \\ 1, & \alpha \text{是单特征根}, \\ 2, & \alpha \text{是二重特征根}. \end{cases} $

注  $ y'' + py' + qy = P_n(x)e^{ax} $.

设  $ y^* = Q_n(x)e^{ax} \cdot x^k $，其中

 $ e^{ax} $ 照抄（若没有  $ e^{ax} $，表明  $ \alpha = 0 $），

 $ P_n(x) $ 写成  $ Q_n(x) $，为  $ x $ 的  $ n $ 次多项式，

 $ k = \begin{cases} 0, & \alpha \neq r_1, \\ 1, & \alpha = r_1 \end{cases} $ 或  $ \alpha = r_2(r_1 \neq r_2) $，

 $ 2, & \alpha = r_1 = r_2. $

总结：一看，二算，三比较。

自由项中的  $ \alpha r_1, r_2 $

如： $ y'' - 2y' + 5y = 1 \cdot e^x $。

设  $ y^* = ae^x \cdot x^0 $，

 $ \alpha = 1, r_{1,2} = 1 \pm 2i $，

 $ \alpha \neq r_1, r_2 = ae^x $，

代回方程得  $ ae^x - 2ae^x + 5ae^x = e^x \Rightarrow 4a = 1 \Rightarrow a = \frac{1}{4} $，

则  $ y^* = \frac{1}{4}e^x $，故通解为

 $ \rightarrow $ 齐次方程

的通解

 $ \rightarrow $ 非常次方程

的特解

其中  $ C_1, C_2 $ 为任意常数。



②当自由项 $ f(x)=\mathrm{e}^{ax}\left[P_{m}(x)\cos\beta x+P_{n}(x)\sin\beta x\right] $时，特解要设为

 $$ \begin{array}{r}{y^{*}=\mathrm{e}^{\alpha x}[Q_{l}^{(1)}(x)\cos\beta x+Q_{l}^{(2)}(x)\sin\beta x]x^{k},}\end{array} $$ 