☑ 分析 有第一类间断点和无穷间断点的函数  $ f(x) $ 在包含该间断点的区间内必没有原函数。

定积分存在的充分条件：① $ f(x) $在 $ [a,b] $上连续；② $ f(x) $在 $ [a,b] $上有界，且只有有限个间断点；③ $ f(x) $在 $ [a,b] $上单调.

定积分存在的必要条件：① $ [a,b] $有限长度；② $ f(x) $在 $ [a,b] $上有界。

解 应选(B).

本题通过具体的例子考查考生是否能够明确区分不定积分与定积分的存在性.逐个分析即可.

对于 $ f(x)=\begin{cases}2,&x>0,\\1,&x=0,\\-1,&x<0,\end{cases} $，由于 $ x=0 $是其跳跃间断点，根据不定积分存在定理，在任意一个包含 $ x=0 $的区间 $ [a,b] $上， $ f(x) $一定不存在原函数，但由于 $ f(x) $满足定积分存在定理，故定积分 $ \int_{a}^{b}f(x)dx $存在，所以①错误。

对于 $ f(x)=\begin{cases}2x\sin\frac{1}{x^{2}}-\frac{2}{x}\cos\frac{1}{x^{2}},&x\neq0,\\0,&x=0,\end{cases} $ x=0 是其振荡间断点，但是容易验证：

若  $ F(x)=\begin{cases}x^2\sin\frac{1}{x^2}, & x\neq0,\\0, & x=0,\end{cases} $，则  $ F'(x)=f(x)(-\infty<x<+\infty) $，所以  $ f(x) $ 存在原函数，但在任意一个包

含 x=0 的区间  $ [a, b] $ 上，定积分  $ \int_{a}^{b} f(x) \, dx $ 不存在，因为在 x=0 的邻域内  $ f(x) $ 无界，所以②错误.

 $$ \begin{aligned}\lim_{x\to0}\left(2x\cdot\sin\frac{1}{x^{2}}-\frac{2}{x}\cos\frac{1}{x^{2}}\right)\\\downarrow\\\infty\cdot\cos\infty 是无界振荡 \end{aligned} $$ 

对于 $ f(x)=\begin{cases}\dfrac{1}{x},&x\neq0,\\0,&x=0,\end{cases} $因为x=0是其无穷间断点，所以 $ f(x) $在包含x=0的区间 $ [a,b] $上不存在原函数，定积分 $ \int_{a}^{b}f(x)dx $也不存在，所以③正确.

对于 $ f(x)=\begin{cases}2x\cos\frac{1}{x}+\sin\frac{1}{x},&x\neq0,\\0,&x=0,\end{cases} $，它在 $ (-∞,+∞) $内存在原函数 $ F(x)=\begin{cases}x^{2}\cos\frac{1}{x},&x≠0,\\0,&x=0,\end{cases} $，并且在任意一个包含x=0的区间 $ [a,b] $上，定积分 $ \int_{a}^{b}f(x)dx $也存在，因为 $ \underline{\frac{f(x)有界}{x}} $且只有一个振荡间断点，所以④正确．

综上所述，答案选择(B).