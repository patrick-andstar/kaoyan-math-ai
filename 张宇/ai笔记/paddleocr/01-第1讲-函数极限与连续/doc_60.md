能体现它的优越性。

公式 当  $ x \to 0 $ 时， $ x - \ln(1 + x) \sim \frac{1}{2} x^{2} $

注 作为常见考题，在历年的考研数学题中，总会出现什么情况呢？命题老师觉得这个题是送给你的，送你们一些分数，叠高分数底线，提高点下限，可是很多同学他不要，他说：“老师，我不好意思要这个分数。”这个实在不应该，这是基本问题，它常考，这种分数一定要拿到手.下面我们来看没有分母怎么办.

例1.31 求极限  $ \lim_{x\to+\infty}\left[x^{2}\left(\mathrm{e}^{\frac{1}{x}}-1\right)-x\right] $.

☑分析 对于“ $ \infty-\infty $”型，若无分母可以考虑倒代换，造出分母，或者考虑提公因式出来。

解

 $$ \begin{aligned} 原式 &=\lim_{x\to+\infty}x\cdot\left[x\left(\mathrm{e}^{\frac{1}{x}}-1\right)-1\right]\\&=\lim_{x\to+\infty}\frac{x\left(\mathrm{e}^{\frac{1}{x}}-1\right)-1}{\frac{1}{x}}\xrightarrow{ 设置分母有原则，简单因子才下放 , 先不用浩必达法则 , 分子 , 分母求导毅烦琐 }\quad\\&\xleftarrow[ 1 ]{ 1}\end{aligned} $$ 

 $$ \lim_{u\to0^{+}}\frac{e^{u}-1-u}{u^{2}}=\lim_{u\to0^{+}}\frac{e^{u}-1}{2u}=\frac{1}{2} $$ 

或者直接用公式：当  $ u \rightarrow 0 $ 时， $ e^{u} - 1 - u \sim \frac{1}{2}u^{2} $

注 建议考生把这类题也练练，在《张宇考研数学题源探析经典 1000 题》中布置了这类题目，一定要把里面的每一道题反复地练，熟练地掌握这类题目的计算，为全面的综合题的学习、解题打下坚实的基础.

(3) “ $ \infty^{0} $” 和 “ $ 0^{0} $”

例1.32 求极限  $ \lim_{x\to+\infty}\left(x+\sqrt{1+x^{2}}\right)^{\frac{1}{x}} $

♡分析 幂指函数的恒等变形： $ u(x)^{v(x)} = e^{v(x)\ln u(x)} $

解 这是 “ $ \infty^{0} $” 型未定式，是幂指函数的极限，对于 “ $ \infty^{0} $” 和 “ $ 0^{0} $” 型这两种未定式，一般来说，用恒等变形

 $$ \lim u^{\nu}=\mathrm{e}^{\lim\nu\ln u}\xlongequal{ 记 }\exp\{\lim\nu\ln u\}, $$ 

将其化成“ $ \frac{0}{0} $”“ $ \frac{\infty}{\infty} $”“ $ 0\cdot\infty $”这三种类型，然后计算，故原式= $ \exp\left\{\lim_{x\to+\infty}\frac{1}{x}\ln\left(x+\sqrt{1+x^2}\right)\right\} $