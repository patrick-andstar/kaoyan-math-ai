又由于  $ y_1 = x e^x + e^{-x} $ 为非齐次方程的特解， $ y = x e^x $ 为对应齐次方程的解，可知  $ y_1 - x e^x = e^{-x} = y^* $ 也为该非齐次方程的特解。设所求方程为

 $$ y^{\prime \prime}-2y^{\prime}+y=f(x), $$ 

将  $ y^{*} = e^{-x} $ 代入上面的方程，可得  $ f(x) = 4e^{-x} $，因此所求方程为  $ y'' - 2y' + y = 4e^{-x} $

15.10 解 显然  $ f(0)=1 $ 。由

 $$ \iint_{x^{2}+y^{2}\leq4t^{2}}f\left(\frac{1}{2}\sqrt{x^{2}+y^{2}}\right)\mathrm{d}x\mathrm{d}y=\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{2t}f\left(\frac{1}{2}r\right)r\mathrm{d}r=2\pi\int_{0}^{2t}r f\left(\frac{1}{2}r\right)\mathrm{d}r, $$ 

可知

 $$ f(t)=\mathrm{e}^{4\pi t^{2}}+2\pi\int_{0}^{2t}r f\left(\frac{1}{2}r\right)\mathrm{d}r,\ f^{\prime}(t)=8\pi t\mathrm{e}^{4\pi t^{2}}+8\pi t f(t)\ . $$ 

解上述关于 $ f(t) $的一阶非齐次线性微分方程，得

 $$ f(t)=\left(\int8\pi t\mathrm{e}^{4\pi t^{2}}\mathrm{e}^{-\int8\pi t\mathrm{d}t}\mathrm{d}t+C\right)\mathrm{e}^{\int8\pi t\mathrm{d}t}=\left(8\pi\int t\mathrm{d}t+C\right)\mathrm{e}^{4\pi t^{2}}=(4\pi t^{2}+C)\mathrm{e}^{4\pi t^{2}}, $$ 

将 $ f(0)=1 $代入，得C=1．因此 $ f(t)=(4\pi t^{2}+1)e^{4\pi t^{2}} $．

15.11 解 (1) 由  $ r^{4}-r^{3}+r^{2}-r=0 $，即  $ r^{3}(r-1)+r(r-1)=0 $，也即  $ r(r-1)(r^{2}+1)=0 $，得  $ r_{1}=0 $， $ r_{2}=1 $， $ r_{3,4}=\pm1 $，于是通解  $ y=C_{1}+C_{2}e^{x}+C_{3}\cos x+C_{4}\sin x $，其中  $ C_{1}, C_{2}, C_{3}, C_{4} $ 是任意常数.

(2) 要想在  $ x \rightarrow 0 $ 时保证 y 是 x 的三阶无穷小，最简单的办法就是对 y 作泰勒展开，

 $$ \begin{aligned}y&=C_{1}+C_{2}\mathrm{e}^{x}+C_{3}\cos x+C_{4}\sin x=C_{1}+C_{2}\left[1+x+\frac{1}{2}x^{2}+\frac{1}{6}x^{3}+o(x^{3})\right]+\\&\quad C_{3}\left[1-\frac{1}{2}x^{2}+0x^{3}+o(x^{3})\right]+C_{4}\left[x-\frac{1}{6}x^{3}+o(x^{3})\right]\\&=C_{1}+C_{2}+C_{3}+(C_{2}+C_{4})x+\left(\frac{C_{2}}{2}-\frac{C_{3}}{2}\right)x^{2}+\left(\frac{C_{2}}{6}-\frac{C_{4}}{6}\right)x^{3}+o(x^{3}),\end{aligned} $$ 

于是必须  $ C_{1}+C_{2}+C_{3}=0,\quad C_{2}+C_{4}=0,\quad\frac{C_{2}}{2}-\frac{C_{3}}{2}=0,\quad\frac{C_{2}}{6}-\frac{C_{4}}{6}\neq0 $ ，解得  $ C_{2}=C_{3}=-C_{4}=-\frac{C_{1}}{2} $ ，且  $ C_{1}\neq0 $ ，记  $ C_{1}=2C $ ，则

 $$ y=2C-C\mathrm{e}^{x}-C\cos x+C\sin x, 其中 C\neq0. $$ 

15.12 解 由导数的几何意义，有  $ y' = \tan \alpha $，即  $ \alpha = \arctan y' $，所以

 $$ \frac{\mathrm{d}\alpha}{\mathrm{d}x}=\frac{y^{\prime \prime}}{1+(y^{\prime})^{2}} $$ 

由题意 $ \frac{d\alpha}{dx}=\frac{dy}{dx} $，得 $ \frac{y''}{1+(y')^2}=y' $，即

 $$ y^{\prime \prime}=y^{\prime}[1+(y^{\prime})^{2}], $$ 