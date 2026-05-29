这个题实际上是个小综合题，注意两点：

①等价代换；②换元.

这不是一个非常简单的问题，而是一个具有一定综合性，也有一定可以讨论的余地的一个好题目，它在以后还有很多用处。

解 这是 “ $ 0 \cdot \infty $” 型未定式，注意一个事实：当  $ x \to 0 $ 时， $ \ln(1+x) \sim x $，将其广义化，得

 $$ \ln(1+u)\sim u(u\to0), $$ 

于是在考研中常考的一个式子是 $ \ln x=\ln(1+x-1)\sim x-1(x\rightarrow1) $，则这个公式出现的频率会更高

 $$ \begin{aligned}\lim_{x\to1^{-}}\ln x\ln(1-x)&=\lim_{x\to1^{-}}\ln(1+x-1)\ln(1-x)\\&=\lim_{x\to1^{-}}(x-1)\ln(1-x)\\&\xlongequal{ 令 1-x=t}-\lim_{t\to0^{+}}t\ln t=0\end{aligned} $$ 

极限换元（有二换）：

①表达式中的超实数换：

②极限符号的底下换

注 事实上，当  $ \alpha > 0 $ 时， $ \lim_{x \to 0^+} x^{\alpha} \ln x = \lim_{x \to 0^+} \frac{\ln x}{x^{-\alpha}} = \lim_{x \to 0^+} \frac{x^{-1}}{-\alpha x^{-\alpha-1}} = -\frac{1}{\alpha} \lim_{x \to 0^+} x^{\alpha} = 0 $，本题中  $ \alpha = 1 $。

只要是x的正次方即可， $ \alpha>0 $

 $$ \lim_{x\to0^{+}} $$ 

 $$ \ln x=0 $$ 

趋于无穷大速度太慢了

 $ x $的升一亿方根. $ x^a \rightarrow 0 $的速度很慢了，都能抵消掉 $ \ln x \rightarrow \infty $的速度

一般形式： $ \lim_{x\to0^{+}}x^{\alpha}\ln^{\beta}x=0(\beta,\alpha>0) $， $ \lim_{x\to0^{+}}\sqrt{x}\ln^{2}x=0 $

例 1.29 求  $ I = \lim_{x \to 0} x \left[ \frac{10}{x} \right] $，其中  $ [\cdot] $ 为取整符号。

分析该问题的解决用“夹逼准则”.[∞]特殊不存在.

解 当  $ x \to 0 $ 时， $ \frac{10}{x} \to \infty $，对于  $ [\infty] $，此时想到极限计算的利器——夹逼准则（当常规求极限的方法——比如等价无穷小代换、泰勒公式、洛必达法则——无法使用时，一定要能够想起这个“两边夹击”的重要方法）。

根据 $ x-1<[x]\leq x $，有

于是

 $$ \begin{cases}x>0 时 , 有 10-x<x\bullet\left[\frac{10}{x}\right]\leq10,\\x<0 时 , 有 10-x>x\bullet\left[\frac{10}{x}\right]\geq10.\end{cases} $$ 

可见，无论 x > 0，还是 x < 0，不等式两边均可趋于同一极限，故  $ I = \lim_{x \to 0} x \left[ \frac{10}{x} \right] = 10 $