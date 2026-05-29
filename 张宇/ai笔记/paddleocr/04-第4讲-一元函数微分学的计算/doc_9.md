 $$ \frac{\mathrm{d}y}{\mathrm{d}x}=\frac{(y^{2}-\mathrm{e}^{t})(1+t^{2})}{2(1-ty)} $$ 

☑ 方法总结 本题是一个综合型求导题目，根据它的类型套用相应公式！

公式  $ (\arctan t)' = \frac{1}{1 + t^2} $

## 8 对数求导法

<div style="text-align: center;"><img src="imgs/img_in_image_box_404_302_488_352.jpg" alt="Image" width="8%" /></div>


称为对数求导法，实际问题中出现多项相乘、相除等问题利用对数，将乘除变成加减。

对于多项相乘、相除、开方、乘方的式子，一般先取对数再求导。

设  $ y = f(x) (f(x) > 0) $，则

①等式两边取对数，得  $ \ln y = \ln f(x) $;

②两边对自变量x求导（同样注意 $ y=f(x) $，即将y看作中间变量），得 $ \frac{1}{y}y'=\left[\ln f(x)\right]' $，则

 $ y'=\frac{yf'(x)}{f(x)} $．复杂的表达式转化为简单的表达式运算.

例 4.11 设函数  $ y = y(x) $ 由方程  $ xe^{f(y)} = e^{y} \ln 2 $ 确定，其中  $ f $ 具有二阶导数，且  $ f' \neq 1 $，则  $ \frac{d^2 y}{dx^2} = $

这部分可能出现在分母中

(2) 分析 本题中有 “ $ e^{f(y)} $” “ $ e^{y} $” 这种复杂的形式，可以考虑两边取对数，同时，经分析可知  $ e^{y} \ln 2 > 0 $，所以 x > 0，满足取对数条件，此时变为简单的隐函数方程，两边直接对 x 求导。因为本题是求二阶导数，所以需要再次求导。

解 应填 $ -\frac{\left[1-f'(y)\right]^{2}-f''(y)}{x^{2}\left[1-f'(y)\right]^{3}} $

方程  $ xe^{f(y)} = e^y \ln 2 $ 两端取对数，得  $ \ln x + f(y) = y + \ln(\ln 2) $。两端关于  $ x $ 求导，得  $ \frac{1}{x} + f'(y) \cdot y' = y' $，两端继续关于  $ x $ 求导，得  $ -\frac{1}{x^2} + f''(y) \cdot (y')^2 + f'(y) \cdot y'' = y'' $，由此可得

 $$ y^{\prime \prime}=-\frac{\left[1-f^{\prime}(y)\right]^{2}-f^{\prime \prime}(y)}{x^{2}\left[1-f^{\prime}(y)\right]^{3}}. $$ 

方法总结 对于多项式相乘、相除、开方、乘方的式子，先取对数将形式复杂的表达式化为形式简单的表达式，再去求导.

公式  $ \left[f'(y)y'\right]' = f''(y) \cdot y' \cdot y' + f'(y) \cdot y'' $

## 9 幂指函数求导法

对于  $ u(x)^{\nu(x)}(u(x)>0 $，且  $ u(x)\neq1) $，除了用上面的对数求导法外，还可以先化成指数函数

 $$ u(x)^{\nu(x)}=e^{\nu(x)\ln u(x)},\quad 复合函数 $$ 

然后求导，得