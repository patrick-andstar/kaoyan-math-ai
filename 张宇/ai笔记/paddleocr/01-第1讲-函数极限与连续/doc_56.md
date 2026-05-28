本题的结果要记住，以后直接使用，这就是通常说的“抓大头”，即当 $ x \to \infty $时，分别抓分子、分母中关于x的最高次项，忽略其他项，如 $ \lim_{x \to -\infty} \frac{\sqrt{4x^2 + x - 1} + \frac{x + 1}{\sqrt{x^2 + \sin x}}} = 1 $。另外特别注意，若 $ x \to 0 $，则应该分别抓分子、分母中关于x的最低次项。 $ \left|2x\right| = -2x $

例 1.26 设函数  $ f(x)=\lim_{n\to\infty}\frac{x^2+nx(1-x)\sin^2\pi x}{1+n\sin^2\pi x} $，则  $ f(x)= $ ___.

(2) 分析 这道题是近几年常考的用极限来定义对应法则的题。在本讲开头，我讲过一些求对应法则的内容，可以由关系式或复合函数的表达式求对应法则。在这里再加一条，由极限求对应法则。用什么样的题目来创造这些对应法则，这需要通过做题逐渐地积累起来。

找特点：抓带头大哥，n在变，x在求极限过程中视为常数.

<div style="text-align: center;"><img src="imgs/img_in_image_box_417_528_656_586.jpg" alt="Image" width="23%" /></div>


解 应填 $ \begin{cases}x^{2},&x=0,\pm1,\pm2,\cdots,\\x(1-x),& 其他.\end{cases} $

当  $ \sin \pi x = 0 $ ，即 x = k （整数）时， $ f(x) = \lim_{n \to \infty} \frac{x^2 + nx(1 - x) \cdot 0}{1 + n \cdot 0} = x^2 $;

当  $ \sin\pi x \neq 0 $ ，即  $ x \neq k $ （整数）时， $ f(x) = \lim_{n \to \infty} \frac{\frac{x^2}{n} + x(1 - x) \sin^2 \pi x}{\frac{1}{n} + \sin^2 \pi x} = \frac{x(1 - x) \sin^2 \pi x}{\sin^2 \pi x} = x(1 - x) $.

综上， $ f(x)=\left\{\begin{aligned}&x^{2},&x=0,\pm1,\pm2,\cdots,\\ &x(1-x),& 其他.\end{aligned}\right. $

☑ 方法总结 主要关注 n 前面的系数.

∂公式  $ \lim_{n\to\infty}n\cdot0=0 $

这个题目精彩的地方在于，若 n 的系数为零，即  $ \sin^{2} \pi x = 0 $ 。此时，含 n 的项消失了，结果就是  $ x^{2} $ 。

这个题目有“前世今生”，后面我们仍会用到它。这个例子记住了，后面再遇到类似由这种用极限定义函数的问题不在话下，这是构造函数的最高难度了，不会再超过这个难度。

例 1.27 已知极限  $ \lim_{x\to0}\frac{\tan2x+xf(x)}{\sin x^3}=0 $，则  $ \lim_{x\to0}\frac{2+f(x)}{x^2}= $（）.

(A) $ \frac{13}{9} $ (B)4 (C) $ \frac{10}{3} $ (D) $ -\frac{8}{3} $

♡分析 建立已知和未知的联系.一是脱帽法,二是泰勒展开.

解 应选(D).