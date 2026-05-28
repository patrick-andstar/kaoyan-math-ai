### 例1.22 证明：

(1) 当  $ x \to 0 $ 时，  $ \ln\left(x + \sqrt{1 + x^{2}}\right) \sim x $;

(2) 当  $ x \to 0 $ 时， $ 1 - (\cos x)^{a} \sim \frac{1}{2} ax^{2} $， $ a \neq 0 $。

<div style="text-align: center;"><img src="imgs/img_in_image_box_745_166_961_350.jpg" alt="Image" width="20%" /></div>


(P 分析) 求极限 “ $ \frac{0}{0} $” 型，用洛必达法则.

证 (1) 由于  $ \lim_{x\to0}\frac{\ln\left(x+\sqrt{1+x^{2}}\right)}{x} $ 洛必达法则  $ \lim_{x\to0}\frac{\frac{1}{\sqrt{1+x^{2}}}}{1}=1 $ ，因此当  $ x\to0 $ 时，  $ \ln\left(x+\sqrt{1+x^{2}}\right)\sim x $ 。洛必达



(2) 当  $ x \to 0 $ 时， $ \lim_{x \to 0} \frac{1 - (\cos x)^a}{\frac{1}{2} a x^2} \xlongequal{\text{法则}} \lim_{x \to 0} \frac{-a (\cos x)^{a-1} (- \sin x)}{a x} = \lim_{x \to 0} (\cos x)^{a-1} = 1 $ 。证毕。

方法总结 用洛必达法则解决 “ $ \frac{0}{0} $” 型未定式.

∅公式 当  $ x \to 0 $ 时，  $ \ln(x + \sqrt{1 + x^2}) \sim x \sim \sin x \sim \tan x \sim \arctan x \sim e^x - 1 \sim \ln(1 + x) $.

当  $ x \to 0 $ 时，  $ 1 - (\cos x)^{a} \sim \frac{1}{2} ax^{2} $，  $ a \neq 0 $ ，如：当  $ x \to 0 $ 时，  $ 1 - \cos x \sim \frac{1}{2} x^{2} $，  $ 1 - \sqrt{\cos x} \sim \frac{1}{4} x^{2} $

这个题目的价值：①练习了洛必达法则；②得到了两个重要结论。

这两个重要结论，在未来会经常出现。

凡是在《考研数学基础 30 讲》中给出的结论，都可以直接用，不必证明，这都是一些常见的、经典的结论。

下面还有一个话题. 当遇到 “ $ \frac{0}{0} $” 型未定式时, 是看分子、分母中谁趋于零的速度快, 在超实数体系中, 以 0 作为标准实数部分的超实数它们的比值是多少? 比如:

 $$ \mathrm{std}\left(\frac{x-\sin x}{x^{3}}\right)=\frac{1}{6}, $$ 

 $$ \lim_{x\to0}\frac{x-\sin x}{x^{3}}=\frac{1}{6} $$ 

在考研数学中，无穷小的关键是阶数，无穷小争先恐后趋于0，趋于0的速度是不一样的。接下来我们讨论无穷大的比阶问题，用例1.23来说明。

例1.23 设 $ f(x)=\ln^{10}x $,  $ g(x)=x $,  $ h(x)=\mathrm{e}^{\frac{1}{10}} $, 则当x充分大时, 有( ).

(A)  $ g(x) < h(x) < f(x) $

(B)  $ h(x) < g(x) < f(x) $

(C)  $ f(x) < g(x) < h(x) $

(D)  $ g(x) < f(x) < h(x) $

分析 用洛必达法则，计算极限.

解 应选(C).