这个题目的难度低，不行；超过这个题目的难度，不需要！

## 2 反函数 → 前提：符合铅直画线法

设函数  $ y = f(x) $ 的定义域为  $ D $，值域为  $ R $。如果对于每一个  $ y \in R $，必存在唯一的  $ x \in D $，使得  $ y = f(x) $ 成立，则由此定义了一个新的函数  $ x = \varphi(y) $，这个函数称为函数  $ y = f(x) $ 的反函数，一般记作  $ x = f^{-1}(y) $，它的定义域为  $ R $，值域为  $ D $。相对于反函数来说，原来的函数也称为直接函数。以下两点需要说明。

第一，严格单调函数必有反函数，比如函数  $ y = x^2 (x \in [0, +\infty)) $ 是严格单调函数，故它有反函数  $ x = \sqrt{y} $。

第二，若把  $ x = f^{-1}(y) $ 与  $ y = f(x) $ 的图形画在同一坐标系中，则它们完全重合。只有把  $ y = f(x) $ 的反函数  $ x = f^{-1}(y) $ 写成  $ y = f^{-1}(x) $ 后，它们的图形才关于  $ y = x $ 对称。事实上，这也是字母  $ x $ 与  $ y $ 互换的结果。

 $$ \begin{aligned} 如 y=x^{2}(x\geq0) 与 y=\sqrt{x} 关于 y=x 对称 \end{aligned} $$ 

注 $ ^{1} $(1)单值函数（符合铅直画线法）才谈反函数.

(2) 有反函数的函数不一定是单调函数。比如

 $$ f(x)=\begin{cases}x,&x\geqslant0,\\\frac{1}{x},&x<0,\end{cases} $$ 

其图像如图 1-2 所示，其反函数即为  $ f(x) $ 本身，但  $ f(x) $ 不是单调函数。

<div style="text-align: center;"><img src="imgs/img_in_image_box_794_684_941_805.jpg" alt="Image" width="14%" /></div>


<div style="text-align: center;">图 1-2</div>


判断一个函数是否具有反函数：用水平画线法。

水平画线法——在符合铅直画线法的条件下，作水平直线，若任一条水平直线与 $ f(x) $至多有一个交点，则 $ f(x) $有反函数.

口诀：

{

    铅直直线定单、多（单值函数、多值函数），

    水平直线定反、直（反函数、直接函数）。

}

重要关系： $ \begin{cases}f[f^{-1}(x)]=x,\\f^{-1}[f(x)]=x.\end{cases} $ 如： $ e^{\ln2^{x}}=2^{x} $

<div style="text-align: center;"><img src="imgs/img_in_image_box_849_991_962_1114.jpg" alt="Image" width="10%" /></div>


关注公众号获取更多免费帮

例 1.3 求函数  $ y = f(x) = \ln\left(x + \sqrt{x^2 + 1}\right) $ 的反函数  $ f^{-1}(x) $ 的表达式及其定义域.

♡分析 对数函数是一个极为重要的研究对象，三个基本公式要掌握 $ (a, b > 0) $

 $$ \begin{cases}\ln ab=\ln a+\ln b( 积变和 ),\\\ln\frac{a}{b}=\ln a-\ln b( 商变差 ),\\\ln a^{b}=b\ln a( 幂次变倍数 ).\end{cases} $$ 