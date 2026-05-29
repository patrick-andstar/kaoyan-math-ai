例 1.5 设  $ g(x)=\begin{cases}2-x, & x\leq0, \\ 2+x, & x>0,\end{cases} $  $ f(x)=\begin{cases}x^2, & x<0, \\ -x-1, & x\geq0,\end{cases} $ 则  $ g[f(x)]= $ ___.

♂分析 数与形结合.

华罗庚先生说：“数无形时少直觉，形少数时难入微，数形结合百般好”。

解 应填  $ \begin{cases}3+x,&x\geqslant0,\\2+x^{2},&x<0.\end{cases} $

<div style="text-align: center;"><img src="imgs/img_in_image_box_751_210_912_366.jpg" alt="Image" width="15%" /></div>


 $$ g[f(x)]=\begin{cases}2-f(x),f(x)\leqslant0,\\2+f(x),f(x)>0,\end{cases} $$ 

当 $ f(x)\leq0 $时， $ x\geq0 $，此时 $ f(x)=-x-1 $；当 $ f(x)>0 $时，x<0，此时 $ f(x)=x^{2} $

综上，

 $$ g[f(x)]=\begin{cases}2-(-x-1),&x\geqslant0,\\2+x^{2},&x<0\end{cases}=\begin{cases}3+x,&x\geqslant0,\\2+x^{2},&x<0.\end{cases} $$ 

☑ 方法总结 画出内层函数的图形，数形结合。

## 4 隐函数

前面讲了单值函数和多值函数的区别

 $ F(x,y)=0 $ 在上述区间内确定了一个隐函数  $ y=y(x) $.

<div style="text-align: center;"><img src="imgs/img_in_image_box_542_723_628_800.jpg" alt="Image" width="8%" /></div>


多值函数不适用于铅直画线法，比如，上图有两个交点，则不满足铅直画线法，这个对应的就是多值函数，不能确定隐函数，能确定隐函数就不能是多值函数，这是基本概念，关于隐函数存在定理，我们后面专门讲。

如  $ x + y^{3} - 1 = 0 $ 就表示一个隐函数，且可显化为  $ y = \sqrt[3]{1 - x} $；再如  $ \sin(xy) = \ln \frac{x + e}{y} + 1 $ 也表示一个隐函数，但不易显化，很难写出  $ y = y(x) $ 或  $ x = x(y) $。

一般来说，由  $ F(x, y) = 0 $ 所确定的隐函数求  $ y(x_0) $，若代入  $ x_0 $ 易求出  $ y(x_0) $，则直接求之；若不易求出  $ y(x_0) $，则用观察法。如：方程这个东西，解无定法，观察得之，有时“显然”，有时超越方程

无解析解，只有数值解。

①设函数  $ y = y(x) $ 由方程  $ \ln y - \frac{x}{y} + x = 0 (x > 0) $ 确定，当 x = 2 时， $ y(2) = 1 $

方程  $ \ln y - \frac{2}{y} + 2 = 0 $ 是可观察的，用画图法，如图 1-5 所示。

由  $ \ln y = \frac{2}{y} - 2 $，得  $ \begin{cases} z = \ln y, \\ z = \frac{2}{y} - 2, \end{cases} $ 看两条曲线交点。

 $ \ln y + e^{x-1} = 1 $，显然可看出，y = 1 时成立，画草图







<div style="text-align: center;"><img src="imgs/img_in_image_box_700_1067_919_1235.jpg" alt="Image" width="21%" /></div>


这些都是考研真题里面出现过的形式。

<div style="text-align: center;"><img src="imgs/img_in_image_box_527_1216_693_1340.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">图 1-5</div>


②设函数  $ y = y(x) $ 由方程  $ \ln y + e^{y-1} = \frac{x}{2} $ 确定，当 x = 2 时， $ y(2) = 1 $