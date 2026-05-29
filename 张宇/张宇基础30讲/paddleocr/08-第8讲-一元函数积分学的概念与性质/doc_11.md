将  $ [a, b] $ n 等分且取每个小区间的右端点为  $ \xi_{i} $ (见图 8-2)，即

①n等分并取右端点的函数值作为高；



 $$ \int_{a}^{b}f(x)\mathrm{d}x=\lim_{n\to\infty}\sum_{i=1}^{n}f\left(a+\frac{b-a}{n}i\right)\frac{b-a}{n} $$ 

③求和：

④取极限.

<div style="text-align: center;"><img src="imgs/img_in_chart_box_330_246_588_431.jpg" alt="Image" width="25%" /></div>


取左端点的函数值作为高：

 $$ \lim_{n\to\infty}\sum_{i=0}^{n-1}f\left(a+\frac{b-a}{n}i\right)\frac{b-a}{n}=\int_{a}^{b}f(x)\mathrm{d}x $$ 

<div style="text-align: center;">图 8-2</div>


若将式子中的 a, b 特殊化为 0, 1 这两个数，得出的形式更为简单：

 $$ \int_{0}^{1}f(x)\mathrm{d}x=\lim_{n\to\infty}\sum_{i=1}^{n}f\left(\frac{i}{n}\right)\frac{1}{n} $$ 

(4) 定积分的值与字母无关.

当定积分存在时，有

 $$ \int_{a}^{b}f(x)\mathrm{d}x=\int_{a}^{b}f(t)\mathrm{d}t=\int_{a}^{b}f(u)\mathrm{d}u, $$ 

注：积分与字母无关，无论x, t, u，都只是一个符号

这就是说， $ \underline{\text{定积分的值只与被积函数及积分区间有关，而与积分变量的记法无关。}} $

是个客观存在的数量值

## 2 存在定理

定积分的存在性，也称一元函数的（常义）可积性。这里的“常义”是指“区间有限，函数有界”，也有人称为“黎曼”可积性，与后面要谈到的“区间无穷，函数无界”的“反常”积分有所区别。在本讲中所谈到的可积性都是指常义可积性。



<div style="text-align: center;"><img src="imgs/img_in_image_box_682_937_887_1083.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;">函数与积分区间被限制在框之内.</div>


按照《全国硕士研究生招生考试数学考试大纲》，定积分存在定理包括下面两个方面。

(1) 定积分存在的充分条件.

①若 $ f(x) $在 $ [a,b] $上连续，则 $ \int_{a}^{b}f(x)dx $存在.

闭区间上连续函数一定有界；

连续函数一定存在不定积分；

连续函数一定存在定积分.



②若 $ f(x) $在 $ [a,b] $上单调，则 $ \int_{a}^{b}f(x)dx $存在.

由于函数单调，故 $ f(a) $， $ f(b) $即为函数的界，对任意 $ x\in(a,b) $， $ f(x) $一定介于 $ f(a) $， $ f(b) $之间