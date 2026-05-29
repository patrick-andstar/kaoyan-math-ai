解 应填  $ y^{(4)} - 2y^{(3)} + 5y'' = 0 $

该方程有解  $ y_1(x) = e^x \cos 2x $，必有另一解  $ y_3(x) = e^x \sin 2x $，可知对应的特征根为  $ 1 \pm 2i $；该方程有解  $ y_2(x) = x $，必有另一解  $ y_4(x) = C $（ $ C $ 为常数），可知  $ r = 0 $ 为二重根。由以上分析可知，原微分方程的特征方程有 4 个特征根： $ 1 \pm 2i $， $ 0 $（二重），故特征方程为

 $$ [r-(1+2\mathrm{i})][r-(1-2\mathrm{i})]\,r^{2}=0\ , $$ 

即

 $$ r^{4}-2r^{3}+5r^{2}=0, $$ 

所以满足条件的微分方程为

 $$ y^{(4)}-2y^{(3)}+5y^{\prime \prime}=0. $$ 

## 4 能写成  $ x^2 - y'' + pxy' + qy = f(x) $ 形式的微分方程（欧拉方程）（仅数学一）

形如  $ x^2 \frac{d^2 y}{dx^2} + px \frac{dy}{dx} + qy = f(x) $ 的方程称为欧拉方程，其中  $ p $ 与  $ q $ 为常数， $ f(x) $ 为已知的连续函数。欧拉方程有固定的解法。

注意到  $ \frac{dy}{dx} $ 是关于  $ t $ 的函数，但我们需

①当x>0时，令 $ x=e^{t} $，则 $ t=\ln x,\frac{dt}{dx}=\frac{1}{x} $，于是要对x求导，即 $ \left(\frac{dy}{dt}\right)_{x}^{t}=\frac{d^{2}y}{dt^{2}}\cdot\frac{dt}{dx} $



 $$ \frac{\mathrm{d}y}{\mathrm{d}x}=\frac{\mathrm{d}y}{\mathrm{d}t}\cdot\frac{\mathrm{d}t}{\mathrm{d}x}=\frac{1}{x}\frac{\mathrm{d}y}{\mathrm{d}t},\quad\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}=\frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{1}{x}\frac{\mathrm{d}y}{\mathrm{d}t}\right)=-\frac{1}{x^{2}}\frac{\mathrm{d}y}{\mathrm{d}t}+\frac{1}{x}\frac{\mathrm{d}\left(\frac{\mathrm{d}y}{\mathrm{d}t}\right)}{x^{2}}=\frac{1}{x^{2}}\frac{\mathrm{d}y}{\mathrm{d}t}+\frac{1}{x^{2}}\frac{\mathrm{d}^{2}y}{\mathrm{d}t^{2}}, $$ 

方程化为

 $$ \frac{\mathrm{d}^{2}y}{\mathrm{d}t^{2}}+(p-1)\frac{\mathrm{d}y}{\mathrm{d}t}+q y=f(\mathrm{e}^{t}), $$ 

即可求解（最后结果别忘了用  $ t=\ln x $ 回代成 x 的函数）.

②当x<0时，令 $ x=-e^{t} $，同理可得.

注 $ ^{1} $（1）建议考生自己写一遍以上推导过程。

(2) 数学二、数学三的考纲中不要求掌握欧拉方程，但以上推导仍应掌握.

例 15.20 欧拉方程  $ x^2 \frac{d^2 y}{dx^2} + 4x \frac{dy}{dx} + 2y = 0 $ (x > 0) 的通解为 ___.

解 应填  $ y=\frac{C_{1}}{x}+\frac{C_{2}}{x^{2}} $， $ C_{1} $， $ C_{2} $ 为任意常数.

由题设，x>0，令 $ x=e^{t} $，则

 $$ \frac{\mathrm{d}y}{\mathrm{d}x}=\frac{\mathrm{d}y}{\mathrm{d}t}\bullet\frac{\mathrm{d}t}{\mathrm{d}x}=\frac{1}{x}\frac{\mathrm{d}y}{\mathrm{d}t}, $$ 

 $$ \frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}=-\frac{1}{x^{2}}\frac{\mathrm{d}y}{\mathrm{d}t}+\frac{1}{x}\frac{\mathrm{d}^{2}y}{\mathrm{d}t^{2}}\bullet\frac{\mathrm{d}t}{\mathrm{d}x}=\frac{1}{x^{2}}\left(\frac{\mathrm{d}^{2}y}{\mathrm{d}t^{2}}-\frac{\mathrm{d}y}{\mathrm{d}t}\right), $$ 