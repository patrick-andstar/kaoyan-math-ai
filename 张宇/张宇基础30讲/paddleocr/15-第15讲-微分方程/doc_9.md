①两边同时除以 $ x^{2} $，并令 $ z=x^{-1} $，有 $ \frac{dz}{dy}=-\frac{1}{x^{2}}\frac{dx}{dy} $，于是方程化为 $ \frac{dz}{dy}+\frac{1}{y}z=-\frac{\ln y}{y} $.

②应用一阶线性微分方程的通解公式，得

 $$ \frac{1}{x}=z=\mathbf{e}^{-\ln y}\left[\int\left(-\frac{\ln y}{y}\mathbf{e}^{\ln y}\right)\mathrm{d}y+C\right]=\frac{1}{y}\left[y(1-\ln y)+C\right], $$ 

故通解为 $ \frac{1}{x}=1-\ln y+\frac{C}{y}(y>0,\ C $为任意常数）.

注 对于无法直接计算的微分方程  $ y' = f(x, y) $，重点在于通过什么形式的换元将其化成以上几种常见的形式.

## 5 二阶可降阶微分方程（用换元法化为一阶方程）(仅数学一、数学二)

(1) $ y''=f(x,y') $型（方程中不显含未知函数y）.

 $$ p=p(x) $$ 

①令  $ y' = p $,  $ y'' = p' $，则原方程变为一阶方程  $ \frac{dp}{dx} = f(x, p) $;

②若求得其通解为 $ p=\varphi(x,C_{1}) $，即 $ y'=\varphi(x,C_{1}) $，则原方程的通解为 $ y=\int\varphi(x,C_{1})\,\mathrm{d}x+C_{2} $

(2) $ y''=f(y,y') $型（方程中不显含自变量x）.

①令  $ y' = p $,  $ y'' = \frac{dp}{dx} = \frac{dp}{dy} \cdot \frac{dy}{dx} = \frac{dp}{dy} \cdot p $，则原方程变为一阶方程  $ p \frac{dp}{dy} = f(y, p) $;

②若求得其通解为 $ p=\varphi(y,C_{1}) $，则由 $ p=\frac{dy}{dx} $可得 $ \frac{dy}{dx}=\varphi(y,C_{1}) $，分离变量得 $ \frac{dy}{\varphi(y,C_{1})}=dx $；

③两边积分得 $ \int\frac{dy}{\varphi(y,C_{1})}=x+C_{2} $，即可求得原方程的通解.

注  $ y'' $ 若仅写成  $ p' $，则方程变为  $ p' = f(y, p) $

实际上，由于  $ p' = \frac{dp}{dx} $，则上式变为关于 x，y，p 的方程，会增加方程的复杂性。所以  $ y'' $ 不能写成  $ p' $，而应写成  $ y'' = \frac{dp}{dx} = \frac{dp}{dy} \cdot \frac{dy}{dx} = p \frac{dp}{dy} $，从而上式变为  $ p \frac{dp}{dy} = f(y, p) $，变为仅关于 y，p 的一阶方程。

(3) $ y''=f(y') $型.

此类型既不显含 y，又不显含 x，按(1)的办法，即不显含 y 来处理。

例 15.12 求微分方程  $ y'' = y'[1 + (y')^2] $ 满足  $ y(0) = 0 $,  $ y'(0) = 1 $ 的特解.