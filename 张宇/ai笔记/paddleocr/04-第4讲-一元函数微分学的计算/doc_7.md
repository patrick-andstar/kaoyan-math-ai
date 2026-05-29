例 4.7 当x>0时，设 $ y=f(x)=3x^2+e^x $有反函数 $ x=\varphi(y) $，则 $ \varphi''(3+e)= $___.

♂分析 本题若想得式子 $ x=\varphi(y) $比较困难，它考查的是反函数求二阶导数知识，可以直接用公式

 $$ \varphi^{\prime \prime}(y)=-\frac{f^{\prime \prime}(x)}{\left[f^{\prime}(x)\right]^{3}}. $$ 

注意当 $ y=3+e $时，x=1

解 应填 $ -\frac{1}{(6+e)^{2}} $

当 $ f(x)=3x^{2}+e^{x}=3+e $时，有x=1，于是

 $$ \left.\varphi^{\prime \prime}(y)\right|_{y=3+e}=-\left.\frac{f^{\prime \prime}(x)}{\left[f^{\prime}(x)\right]^{3}}\right|_{x=1}=-\left.\frac{6+e^{x}}{\left(6x+e^{x}\right)^{3}}\right|_{x=1}=-\frac{1}{\left(6+e\right)^{2}} $$ 

方法总结 求反函数的二阶导数，可熟记公式，直接套公式即可.

∅公式  $ y = f(x) $， $ x = \varphi(y) $， $ \varphi''(y) = -\frac{f''(x)}{[f'(x)]^3} $。

## 6 隐函数求导法（实际问题中常见，要掌握好方法）

设函数  $ y = y(x) $ 是由方程  $ F(x, y) = 0 $ 确定的可导函数，则

①方程  $ \underline{F(x,y)=0} $ 两边对自变量 x 求导，注意  $ y=y(x) $，即将 y 看作中间变量，得到一个关于  $ y' $ 的方程； $ \underline{F[x,y(x)]=0} $ 涉及复合求导！

②解该方程便可求出 $ y' $

例 4.8 设函数  $ y = y(x) $ 由方程  $ y^3 + xy^2 + x^2y + 6 = 0 $ 确定，且  $ y'(1) = 0 $，求  $ y''(1) $ 的值.

(♂) 该方程不容易得到显式  $ y = y(x) $，但仍可以求导。只要方程两边对 x 求导即可！

解 在  $ y^{3}+xy^{2}+x^{2}y+6=0 $ 两边关于 x 求导，得

 $$ 3y^{2}y^{\prime}+y^{2}+2xyy^{\prime}+2xy+x^{2}y^{\prime}=0, $$ 

由  $ y'(1)=0 $ ，得  $ y^{2}(1)+2\cdot1\cdot y(1)=0 $ ，解得  $ y(1)=-2 $ 或  $ y(1)=0 $ （不满足题目所给方程，舍去）.

在  $ 3y^{2}y' + y^{2} + 2xyy' + 2xy + x^{2}y' = 0 $ 两边关于 x 求导，得

 $$ (3y^{2}+2xy+x^{2})y^{\prime \prime}+2(3y+x)(y^{\prime})^{2}+4(y+x)y^{\prime}+2y=0, $$ 

代入x=1， $ y(1)=-2 $与 $ y'(1)=0 $，解得 $ y''(1)=\frac{4}{9} $

☑ 方法总结 隐函数求导，直接两边对x求导，注意复合结构.

公式  $ (y^{2})'=2yy' $， $ (xyy')'=yy'+xy'y'+xyy'' $

## 7 参数方程所确定的函数的导数（在实际问题中用得最多）

设函数  $ y = y(x) $ 由参数方程  $ \begin{cases} x = \varphi(t), \\ y = \psi(t) \end{cases} $ 确定，其中  $ t $ 是参数，且  $ \varphi(t), \psi(t) $ 均可导， $ \varphi'(t) \neq 0 $，则