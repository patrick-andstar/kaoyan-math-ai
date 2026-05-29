注 更为简单的是平面的情形：设在二维平面上直线 L 的方程为  $ Ax + By + C = 0 $，点  $ P_{0} $ 的坐标为  $ (x_{0}, y_{0}) $，则点  $ P_{0} $ 到直线 L 的距离公式为  $ d = \frac{|Ax_{0} + By_{0} + C|}{\sqrt{A^{2} + B^{2}}} $.

 $$  若 B\neq0,\left\{\begin{aligned}S_{口}=&\left|\overrightarrow{P_{0}}P\times\tau\right|,\\ S_{口}=&\left|\tau\right|\cdot d,\end{aligned}\right. 则 d=\frac{\left|\begin{aligned}x-x_{0}&,\quad y_{0}-y_{0}\\1&,\quad-\frac{A}{B}\end{aligned}\right|}{\sqrt{1+\left(-\frac{A}{B}\right)^{2}}}=\frac{\left|Ax_{0}+By_{0}+C\right|}{\sqrt{A^{2}+B^{2}}}.\quad\begin{aligned}P_{0}(x_{0},y_{0})&\tau\\ \sqrt{d}&\quad\tau\left(1,-\frac{A}{B}\right)\\ \frac{h}{P(x,y)}&\end{aligned} $$ 

若  $ A \neq 0 $, B = 0. 则  $ Ax + C = 0 $,  $ x = -\frac{C}{A} $, 于是

 $$ d=\left|x-x_{0}\right|=\left|x_{0}+\frac{C}{A}\right|=\frac{\left|Ax_{0}+0y_{0}+C\right|}{\sqrt{A^{2}+0^{2}}}. $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_590_409_710_533.jpg" alt="Image" width="11%" /></div>


综上，成立

(2) 点到平面的距离.

点  $ P_{0}(x_{0}, y_{0}, z_{0}) $ 到平面  $ Ax + By + Cz + D = 0 $ 的距离  $ d = \frac{|Ax_{0} + By_{0} + Cz_{0} + D|}{\sqrt{A^{2} + B^{2} + C^{2}}} \cdot \frac{P_{0}}{0} \cdot \frac{n}{n} $

(3) 直线与直线.

设  $ \tau_{1}=(l_{1},m_{1},n_{1}),\tau_{2}=(l_{2},m_{2},n_{2}) $ 分别为直线  $ L_{1},L_{2} $ 的方向向量.

 $$ )L_{1}\perp L_{2}\Leftrightarrow\tau_{1}\perp\tau_{2}\Leftrightarrow l_{1}l_{2}+m_{1}m_{2}+n_{1}n_{2}=0. $$ 

 $$ \begin{aligned}d&=\frac{\left|\overrightarrow{P_{0}}\overrightarrow{P}\cdot\boldsymbol{n}\right|}{\left|\boldsymbol{n}\right|}=\frac{\left|\overrightarrow{P_{0}}\overrightarrow{P}\right|\left|\boldsymbol{n}\right|\cos\theta}{\left|\boldsymbol{n}\right|}\\&=\overrightarrow{\left|\boldsymbol{P}_{0}\right|}\cos\theta\\&=\frac{\left|\boldsymbol{A}(x-x_{0})+\boldsymbol{B}(y-y_{0})+\boldsymbol{C}(z-z_{0})\right|}{\sqrt{\boldsymbol{A}^{2}+\boldsymbol{B}^{2}+\boldsymbol{C}^{2}}}\\&=\frac{\left|\boldsymbol{A}x_{0}+\boldsymbol{B}y_{0}+\boldsymbol{C}z_{0}+\boldsymbol{D}\right|}{\sqrt{\boldsymbol{A}^{2}+\boldsymbol{B}^{2}+\boldsymbol{C}^{2}}}\\ \end{aligned} $$ 

 $$ \textcircled{3}L_{1}\mathbin{//}L_{2}\Leftrightarrow\tau_{1}\mathbin{//}\tau_{2}\Leftrightarrow\frac{l_{1}}{l_{2}}=\frac{m_{1}}{m_{2}}=\frac{n_{1}}{n_{2}}. $$ 

③直线 $ L_{1}, L_{2} $的夹角 $ \theta = \arccos \frac{|\boldsymbol{\tau}_{1} \cdot \boldsymbol{\tau}_{2}|}{|\boldsymbol{\tau}_{1}||\boldsymbol{\tau}_{2}|} $，其中 $ \theta = \min\{(\widehat{\boldsymbol{\tau}_{1}, \boldsymbol{\tau}_{2}}), \pi - (\widehat{\boldsymbol{\tau}_{1}, \boldsymbol{\tau}_{2}})\} \in \left[0, \frac{\pi}{2}\right] $.

(4) 平面与平面.

设平面  $ \pi_{1},\pi_{2} $ 的法向量分别为  $ \boldsymbol{n}_{1}=(A_{1},B_{1},C_{1}),\boldsymbol{n}_{2}=(A_{2},B_{2},C_{2}) $

①  $ \pi_1 \perp \pi_2 \Leftrightarrow \boldsymbol{n}_1 \perp \boldsymbol{n}_2 \Leftrightarrow A_1 A_2 + B_1 B_2 + C_1 C_2 = 0 $.

 $$ \pi_{1}\parallel\pi_{2}\Leftrightarrow\boldsymbol{n}_{1}\parallel\boldsymbol{n}_{2}\Leftrightarrow\frac{A_{1}}{A_{2}}=\frac{B_{1}}{B_{2}}=\frac{C_{1}}{C_{2}}. $$ 

③平面  $ \pi_{1} $， $ \pi_{2} $ 的夹角  $ \theta = \arccos \frac{\left| \boldsymbol{n}_{1} \cdot \boldsymbol{n}_{2} \right|}{\left| \boldsymbol{n}_{1} \right| \left| \boldsymbol{n}_{2} \right|} $，其中  $ \theta = \min \{ (\widehat{\boldsymbol{n}_{1}, \boldsymbol{n}_{2}}), \pi - (\widehat{\boldsymbol{n}_{1}, \boldsymbol{n}_{2}})) \in \left[ 0, \frac{\pi}{2} \right] $.

(5) 平面与直线.

设直线 L 的方向向量为  $ \boldsymbol{\tau} = (l, m, n) $，平面  $ \pi $ 的法向量为  $ \boldsymbol{n} = (A, B, C) $

① $ L \perp \pi \Leftrightarrow \tau \parallel n \Leftrightarrow \frac{l}{A} = \frac{m}{B} = \frac{n}{C} $. 平行方程

②  $ L \parallel \pi \Leftrightarrow \tau \perp n \Leftrightarrow Al + Bm + Cn = 0 $ 。垂直方程