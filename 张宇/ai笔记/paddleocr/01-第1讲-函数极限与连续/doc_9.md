由不等式 $ \frac{a+b}{2}\geq\sqrt{ab}(a,b>0) $，有 $ \frac{1}{|x|}+|x|\geq2\sqrt{\frac{1}{|x|}|x}|=2 $，即 $ |f(x)|\leq\frac{1}{2} $。

当x=0时， $ f(0)=0 $．综上，函数 $ f(x) $在 $ (-∞,+∞) $内有界．

方法二 当  $ x \neq 0 $ 时， $ \frac{1 + x^{2}}{2} \geqslant \sqrt{1 \cdot x^{2}} \Rightarrow |x| $，则  $ 1 + x^{2} \geqslant 2|x| $，故  $ \frac{1}{1 + x^{2}} \leqslant \frac{1}{2|x|} $，则

 $$ \left|f(x)\right|=\frac{\left|x\right|}{1+x^{2}}\leqslant\frac{\left|x\right|}{2\left|x\right|}=\frac{1}{2}\ . $$ 

当x=0时， $ f(0)=0 $．综上，函数 $ f(x) $在 $ (-∞,+∞) $内有界．

☎ 方法总结 用基本不等式，找 M，使  $ |f(x)| \leqslant M $。

 $$ \frac{a+b}{2}\geqslant\sqrt{ab}(a,b>0);\quad\frac{2}{\frac{1}{a}+\frac{1}{b}}\leqslant\sqrt{ab}\leqslant\frac{a+b}{2}\leqslant\sqrt{\frac{a^{2}+b^{2}}{2}}(a,b>0). $$ 

(2) 单调性.  $ \rightarrow $ 整个考研数学，离不开单调性这个话题

设 $ f(x) $的定义域为D，区间 $ I\subset D $。如果对于区间I上任意两点 $ x_{1},x_{2} $，当 $ x_{1}<x_{2} $时，恒有 $ f(x_{1})<f(x_{2}) $，则称 $ f(x) $在区间I上单调增加。如果对于区间I上任意两点 $ x_{1},x_{2} $，当 $ x_{1}<x_{2} $时，恒有 $ f(x_{1})>f(x_{2}) $，则称 $ f(x) $在区间I上单调减少。

注 $ ^{1} $ (1) 以上是定义法，是充要条件。

(2) 后面会看到，在考研试题中常常用求导的方法来讨论函数在某个区间上的单调性，但是定义法不可以忘记。试题中也常用到如下定义法的判别形式，请考生留意。

对任意 $ x_{1}, x_{2} \in D, x_{1} \neq x_{2} $，有

f(x) 是单调增函数  $ \Leftrightarrow (x_{1}-x_{2})[f(x_{1})-f(x_{2})]>0 $；

严格单调减  $ \Leftrightarrow $

f(x) 是单调减函数  $ \Leftrightarrow (x_{1}-x_{2})[f(x_{1})-f(x_{2})]<0 $；

f(x) 是单调不减函数  $ \Leftrightarrow (x_{1}-x_{2})[f(x_{1})-f(x_{2})]\geq0 $；

f(x) 是单调不增函数  $ \Leftrightarrow (x_{1}-x_{2})[f(x_{1})-f(x_{2})]\leq0 $。

在考研数学中，函数的单调性虽然是基础知识，但也会有综合应用。

例 1.7 设  $ f(x) $ 在  $ (-\infty, +\infty) $ 上有定义，任给  $ x_1, x_2, x_1 \neq x_2 $，均有  $ (x_1 - x_2) \cdot [f(x_1) - f(x_2)] > 0 $，则以下函数一定单调增加的是（ ）。

(A)  $ |f(x)| $  

(B)  $ f(|x|) $  

(C)  $ f(-x) $  

(D)  $ -f(-x) $

☐ 分析 由条件知  $ f(x) $ 是严格单调增加函数，利用图形的变换，去讨论其他函数的单调性.