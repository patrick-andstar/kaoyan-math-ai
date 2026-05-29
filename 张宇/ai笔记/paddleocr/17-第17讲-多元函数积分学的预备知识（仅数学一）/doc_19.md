注 本题的问题可作如下推广：设  $ z = f(x, y) $ 可微，记任意一点  $ P_{0}(x_{0}, y_{0}) $，从  $ P_{0} $ 出发，沿两条不共线的方向  $ \boldsymbol{l}_{1}^{\circ} = (\cos \alpha_{1}, \cos \beta_{1}) $ 与  $ \boldsymbol{l}_{2}^{\circ} = (\cos \alpha_{2}, \cos \beta_{2}) $ 的方向导数分别为

 $$ \left|\frac{\partial f}{\partial\boldsymbol{l}_{1}^{\circ}}\right|_{P_{0}}=\frac{\partial f}{\partial x}\bigg|_{P_{0}}\cdot\cos\alpha_{1}+\frac{\partial f}{\partial y}\bigg|_{P_{0}}\cdot\cos\beta_{1}, $$ 

 $$ \left|\frac{\partial f}{\partial\boldsymbol{l}_{2}^{\circ}}\right|_{P_{0}}=\frac{\partial f}{\partial\boldsymbol{x}}\bigg|_{P_{0}}\cdot\cos\alpha_{2}+\frac{\partial f}{\partial y}\bigg|_{P_{0}}\cdot\cos\beta_{2}, $$ 

其中 $ \begin{vmatrix}\cos\alpha_{1}&\cos\beta_{1}\\ \cos\alpha_{2}&\cos\beta_{2}\end{vmatrix}\neq0 $

(1) 若  $ \left.\frac{\partial f}{\partial\dot{t}_{1}}\right|_{P_{0}} $， $ \left.\frac{\partial f}{\partial\dot{t}_{2}}\right|_{P_{0}} $ 不全为 0，则该非齐次方程组有唯一解，如例 17.12 的解答过程.

(2) 若  $ \left.\frac{\partial f}{\partial t}\right|_{P_0} = \left.\frac{\partial f}{\partial t}\right|_{P_0} = 0 $，则该齐次方程组只有零解，即  $ \left.\frac{\partial f}{\partial x}\right|_{P_0} = \left.\frac{\partial f}{\partial y}\right|_{P_0} = 0 $，故  $ \left.\left.\frac{\partial f}{\partial x}\right|_{P_0}\right|_{P_0} = \left.\frac{\partial f}{\partial x}\right|_{P_0} dx + $

 $ \left.\frac{\partial f}{\partial y}\right|_{P_0} dy = 0 $。由  $ P_0 $ 的任意性，有  $ \left.\frac{\partial f}{\partial x}\right|_{P_0} = 0 $，故  $ f(x, y) $ 为常数。

例17.13 设  $ F(x, y, z) = xy\mathbf{i} - yz\mathbf{j} + zx\mathbf{k} $，则  $ \mathbf{rot} F(1, 1, 0) = $ ___.

解 应填 i-k.

记三元向量函数  $ F(x, y, z) = (P, Q, R) $，则

 $$ \mathbf{r o t}\boldsymbol{F}(\boldsymbol{x},\boldsymbol{y},\boldsymbol{z})=\begin{vmatrix}\boldsymbol{i}&\boldsymbol{j}&\boldsymbol{k}\\ \frac{\partial}{\partial\boldsymbol{x}}&\frac{\partial}{\partial\boldsymbol{y}}&\frac{\partial}{\partial\boldsymbol{z}}\\ \boldsymbol{P}&\boldsymbol{Q}&\boldsymbol{R}\end{vmatrix}, $$ 

其中 P = xy, Q = -yz, R = zx，于是

 $$ \mathbf{r o t}\boldsymbol{F}(1,1,0)=\begin{vmatrix}{{{i}}}&{{{j}}}&{{{k}}} \\{{{\frac{\partial}{\partial x}}}}&{{{\frac{\partial}{\partial y}}}}&{{{\frac{\partial}{\partial z}}}} \\{{{xy}}}&{{{-yz}}}&{{{zx}}}\end{vmatrix}_{(1,1,0)}=(y\boldsymbol{i}-z\boldsymbol{j}-\boldsymbol{x}\boldsymbol{k})\big|_{(1,1,0)}=\boldsymbol{i}-\boldsymbol{k}. $$ 