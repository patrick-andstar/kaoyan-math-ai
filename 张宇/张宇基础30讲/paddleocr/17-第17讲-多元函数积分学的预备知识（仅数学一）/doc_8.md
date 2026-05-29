(C) $ \frac{\pi}{3} $ (D) $ \frac{\pi}{2} $

(♣分析) 先求出直线  $ L_{1} $， $ L_{2} $ 的方向向量  $ \boldsymbol{\tau}_{1} $， $ \boldsymbol{\tau}_{2} $，再利用公式  $ \varphi = \arccos \frac{|\boldsymbol{\tau}_{1} \cdot \boldsymbol{\tau}_{2}|}{|\boldsymbol{\tau}_{1}||\boldsymbol{\tau}_{2}|} $ 求出其夹角。

解 应选(C).

直线  $ L_{1} $ 的方向向量为  $ \boldsymbol{\tau}_{1}=(1,-2,1) $，直线  $ L_{2} $ 的方向向量为

 $$ \begin{aligned}\boldsymbol{\tau}_{2}&=\begin{vmatrix}{{{i}}}&{{{j}}}&{{{k}}} \\{{{1}}}&{{{-1}}}&{{{0}}} \\{{{0}}}&{{{2}}}&{{{1}}}\end{vmatrix}=-\boldsymbol{i}-\boldsymbol{j}+2\boldsymbol{k},\end{aligned} $$ 

从而直线 $ L_{1} $和 $ L_{2} $的夹角 $ \varphi $的余弦为 $ \cos\varphi=\frac{\left|\boldsymbol{\tau}_{1}\cdot\boldsymbol{\tau}_{2}\right|}{\left|\boldsymbol{\tau}_{1}\right|\left|\boldsymbol{\tau}_{2}\right|}=\frac{3}{\sqrt{6}\cdot\sqrt{6}}=\frac{1}{2} $，因此 $ \varphi=\frac{\pi}{3} $

## 三 空间曲线与曲面

<div style="text-align: center;"><img src="imgs/img_in_image_box_840_533_943_640.jpg" alt="Image" width="9%" /></div>


1 空间曲线

(1)一般式  $ \Gamma:\left\{\begin{array}{l}F(x,y,z)=0,\\G(x,y,z)=0.\end{array}\right. $

 $ G(x,y,z)=0 $

<div style="text-align: center;"><img src="imgs/img_in_image_box_217_669_640_789.jpg" alt="Image" width="40%" /></div>


注 其几何背景为两个曲面的交线.

(2) 参数方程  $ \Gamma:\begin{cases}x=\varphi(t),\\y=\psi(t),t\in[\alpha,\beta],\\z=\omega(t),\end{cases} $

注 在  $ \left\{\begin{array}{l}F(x,y,z)=0,\\G(x,y,z)=0\end{array}\right. $ 中选取某直角坐标变量为自变量（看作参数），解出其他两变量为此变量的函数，即得参数式.如曲线  $ \left\{\begin{array}{l}z=f(x,y),\\y=0,\end{array}\right. $ 令 x=t，则可写成参数式方程：  $ \left\{\begin{array}{l}x=t,\\y=0,\\z=f(t,0).\end{array}\right. $ 当然，有时由于后两变量解出为第一变量的函数表达式带来多值或根式等麻烦事，或者甚至“解不出”，故一般用新的变量作参数再写参数方程，如下面的注；亦或题设直接给出参数方程，如例 17.6.