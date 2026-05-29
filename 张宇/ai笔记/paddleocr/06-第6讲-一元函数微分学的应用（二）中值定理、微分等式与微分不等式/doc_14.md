方法一 直接法. 令  $ F(x) = e^x - kx $，则  $ F'(x) = e^x - k $，当  $ k < 0 $ 时， $ F'(x) > 0 $， $ F(x) $ 单调增加，又  $ \lim_{x \to -\infty} F(x) = -\infty $， $ \lim_{x \to +\infty} F(x) = +\infty $，则  $ F(x) = 0 $ 有且仅有一个实根；

当 k=0 时， $ F(x)=\mathrm{e}^{x} $， $ F(x) $ 恒大于 0，显然不满足；

当k>0时，令 $ F'(x)=0 $，有 $ x=\ln k $，则当 $ x\in(-\infty,\ln k) $时， $ F(x) $单调减少，当 $ x\in(\ln k,+\infty) $时， $ F(x) $单调增加，又 $ \lim_{x\to+\infty}F(x)=+\infty $， $ \lim_{x\to-\infty}F(x)=+\infty $，则当且仅当 $ F(\ln k)=0 $时， $ F(x)=0 $有且仅有一个实根，解得 $ k=e $。

综上，当 k=e 或 k<0 时，方程  $ e^{x}=kx $ 有且仅有一个实根。

方法二 分离法. 联立方程组  $ \left\{\begin{aligned}y&=\frac{e^{x}}{x},\\ y&=k,\end{aligned}\right. $ 且由例 5.13，可得图 6-1.

<div style="text-align: center;"><img src="imgs/img_in_image_box_376_553_641_713.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">图 6-1</div>


故当 k=e 或 k<0 时， $ y=\frac{e^{x}}{x} $ 与 y=k 有且仅有一个交点，即方程  $ e^{x}=kx $ 有且仅有一个实根.

例 6.18 已知方程  $ x^n + nx - 1 = 0 $，其中  $ n $ 为正整数。证明此方程存在唯一正实根  $ x_n $。

证 记  $ f_{n}(x)=x^{n}+nx-1 $ 。当 x>0 时， $ f_{n}^{\prime}(x)=nx^{n-1}+n>0 $ ，故  $ f_{n}(x) $ 在  $ [0,+\infty) $ 上单调增加。由于  $ f_{n}(0)=-1<0, f_{n}(1)=n\geq1 $ ，根据连续函数的零点定理知方程  $ \frac{1}{n} $ 至多有一个实根

 $$ x^{n}+nx-1=0 $$ 

存在唯一正实根 $ x_{n} $，且 $ 0<x_{n}<1 $

注 新概念： $ \{f_{n}(x)\} $ 函数列——一族函数.

 $$ f_{n}(x)=x^{n}+nx-1=0, $$ 

 $$ f_{1}(x)=x+x-1=0\quad\Rightarrow x_{1}, $$ 

 $$ f_{2}(x)=x^{2}+2x-1=0\Rightarrow x_{2}, $$ 

 $$ f_{n}(x)=x^{n}+nx-1=0\Rightarrow x_{n}. $$ 