因为  $ n=\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},-1\right)\bigg|_{(0,0)} $，所以  $ \boldsymbol{n}\cdot(\boldsymbol{x},\boldsymbol{y},\boldsymbol{f}(\boldsymbol{x},\boldsymbol{y}))=\frac{\partial f}{\partial x}\bigg|_{(0,0)}x+\frac{\partial f}{\partial y}\bigg|_{(0,0)}y-f(x,y) $，从而

 $$ \lim_{(x,y)\to(0,0)}\frac{n\cdot(x,y,f(x,y))}{\sqrt{x^{2}+y^{2}}}=0\ . $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_823_257_926_362.jpg" alt="Image" width="9%" /></div>


## 空间平面与直线

## 平面方程（三元一次方程）

已知  $ \begin{array}{c} \uparrow n=(A, B, C) \\ \downarrow P_{0}(x_{0}, y_{0}, z_{0}). \end{array} $ 一定平面的二要素法向量  $ n $ 过一点  $ P_{0} $

以下假设平面的法向量  $ \boldsymbol{n} = (A, B, C) $

 $$ \overrightarrow{P_{0}P}=(x-x_{0},\ y-y_{0},\ z-z_{0})\ ,\  由 \ \overrightarrow{P_{0}P}\perp\boldsymbol{n}\Rightarrow(\overrightarrow{P_{0}P},\ \boldsymbol{n})=0\ . $$ 

 $$  即 A(x-x_{0})+B(y-y_{0})+C(z-z_{0})=0. $$ 

①一般式： $ Ax+By+Cz+D=0 $

将点法式展开，记 $ D_{1}=Ax_{0}+By_{0}+Cz_{0} $，则得到一般式的形式

②点法式： $ A(x-x_{0})+B(y-y_{0})+C(z-z_{0})=0 $

③三点式： $ \begin{vmatrix} x-x_{1} & y-y_{1} & z-z_{1} \\ x-x_{2} & y-y_{2} & z-z_{2} \\ x-x_{3} & y-y_{3} & z-z_{3} \end{vmatrix}=0 $（平面过不共线的三点 $ P_{i}(x_{i},y_{i},z_{i}),i=1,2,3 $）.

④截距式： $ \frac{x}{a}+\frac{y}{b}+\frac{z}{c}=1 $（平面过 $ (a,0,0) $， $ (0,b,0) $， $ (0,0,c) $三点）.

三点直线构成一个平面



<div style="text-align: center;"><img src="imgs/img_in_image_box_445_783_594_907.jpg" alt="Image" width="14%" /></div>


⑤平面束方程：设  $ \pi_{i}: A_{i}x + B_{i}y + C_{i}z + D_{i} = 0, i = 1, 2, A_{1}, B_{1}, C_{1} $ 与  $ A_{2}, B_{2}, C_{2} $ 不成比例，则过  $ L: \begin{cases} A_{1}x + B_{1}y + C_{1}z + D_{1} = 0, \\ A_{2}x + B_{2}y + C_{2}z + D_{2} = 0 \end{cases} $ 的平面束方程为

(交面式方程)

 $$ A_{1}x+B_{1}y+C_{1}z+D_{1}+\lambda(A_{2}x+B_{2}y+C_{2}z+D_{2})=0( 不含 \pi_{2}), $$ 

 $$ A_{2}x+B_{2}y+C_{2}z+D_{2}+\lambda(A_{1}x+B_{1}y+C_{1}z+D_{1})=0( 不含 \pi_{1}). $$ 

或

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_1138_416_1298.jpg" alt="Image" width="24%" /></div>


 $ \pi_{1} $， $ \pi_{2} $的法向量分别为 $ \boldsymbol{n}_{1}=(A_{1},B_{1},C_{1}) $， $ \boldsymbol{n}_{2}=(A_{2},B_{2},C_{2}) $

 $ \lambda n_{1} + \mu n_{2} $ 生成整个平面，

 $ \lambda(A_1x + B_1y + C_1z + D_1) + \mu(A_2x + B_2y + C_2z + D_2) = 0 $ 表示过交线的所有平面。

令  $ \lambda = 1 $，则不包含  $ \pi_{2} $，令  $ \mu = 1 $，则不包含  $ \pi_{1} $