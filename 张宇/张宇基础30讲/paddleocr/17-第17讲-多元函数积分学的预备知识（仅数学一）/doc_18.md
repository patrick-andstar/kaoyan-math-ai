 $$ \left.\frac{\partial f}{\partial x}\right|_{(1,2,0)}=2xy\Big|_{(1,2,0)}=4,\left.\frac{\partial f}{\partial y}\right|_{(1,2,0)}=x^{2}\Big|_{(1,2,0)}=1,\left.\frac{\partial f}{\partial z}\right|_{(1,2,0)}=2z\Big|_{(1,2,0)}=0, $$ 

与 n 同方向的单位向量为  $ \frac{n}{|n|} = \left(\frac{1}{3}, \frac{2}{3}, \frac{2}{3}\right) $，所以所求方向导数为

 $$ \left.\frac{\partial f}{\partial\boldsymbol{n}}\right|_{(1,2,0)}=4\times\frac{1}{3}+1\times\frac{2}{3}+0\times\frac{2}{3}=2 $$ 

例 17.11 设 a, b 为实数，函数  $ z = 2 + ax^2 + by^2 $ 在点 (3, 4) 处的方向导数中，沿方向 l = -3i - 4j 的方向导数最大，最大值为 10。则 a, b 的值分别为（）.

(A)-1, -1

(B)-1, 1

(C)1, -1

(D)1, 1

分析方向导数最大时，即为梯度方向，值为梯度的模.

解 应选(A).

函数 $ z=2+ax^{2}+by^{2} $在点(3,4)处的梯度为

 $$ \left.\mathbf{g r a d}z\right|_{(3,4)}=6a i+8b j. $$ 

由题设条件，知 $ \begin{cases}6a=-3k,\\8b=-4k,\\\sqrt{36a^{2}+64b^{2}}=10,\end{cases} $其中k>0，解得a=-1,b=-1

例 17.12 已知函数  $  z = f(x, y)  $ 可微，其在点  $  P_0(1, 2)  $ 处沿从  $  P_0  $ 到  $  P_1(2, 3)  $ 的方向的方向导数为  $  2\sqrt{2}  $，沿从  $  P_0  $ 到  $  P_2(1, 0)  $ 的方向的方向导数为 -3，则  $  z  $ 在点  $  P_0  $ 处的最大方向导数为 ___.

解 应填 $ \sqrt{10} $

如图 17-5 所示， $ l_{1}=\overrightarrow{P_{0}P_{1}}=(1,1) $， $ l_{2}=\overrightarrow{P_{0}P_{2}}=(0,-2) $，且

 $$ \boldsymbol{l}_{1}^{\circ}=(\cos\alpha_{1},\cos\beta_{1})=\left(\frac{1}{\sqrt{2}},\frac{1}{\sqrt{2}}\right), $$ 

 $$ \hat{L}_{2}=(\cos\alpha_{2},\cos\beta_{2})=(0,-1). $$ 

由方向导数计算公式，有

 $$ \left.\frac{\partial f}{\partial x}\right|_{P_{0}}\bullet\left.\frac{1}{\sqrt{2}}+\frac{\partial f}{\partial y}\right|_{P_{0}}\bullet\frac{1}{\sqrt{2}}=2\sqrt{2}, $$ 

 $$ \left.\frac{\partial f}{\partial x}\right|_{P_{0}}\bullet0+\left.\frac{\partial f}{\partial y}\right|_{P_{0}}\bullet(-1)=-3, $$ 

解得  $ z_{x}^{\prime}(P_{0})=1,\quad z_{y}^{\prime}(P_{0})=3 $ ，故 z 在点  $ P_{0} $ 处的最大方向导数为

 $$ \left|\mathbf{grad}z\right|_{P_{0}}=\sqrt{\left[z_{x}^{\prime}(P_{0})\right]^{2}+\left[z_{y}^{\prime}(P_{0})\right]^{2}}=\sqrt{10} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_682_1069_944_1373.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">图 17-5</div>
