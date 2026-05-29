(4)旋转曲面：曲线  $ \Gamma $ 绕一条定直线旋转一周所形成的曲面.

曲线  $ \Gamma:\left\{\begin{aligned}F(x,y,z)&=0,\\ G(x,y,z)&=0\end{aligned}\right. $ 绕直线  $ L:\frac{x-x_{0}}{l}=\frac{y-y_{0}}{m}=\frac{z-z_{0}}{n} $ 旋转一周形成一个旋转曲面，旋转曲面方程的求法如下.

如图 17-1 所示，设  $ M_{0}(x_{0}, y_{0}, z_{0}) $，方向向量  $ \boldsymbol{\tau} = (l, m, n) $。在母线  $ \Gamma $ 上任取一点  $ M_{1}(x_{1}, y_{1}, z_{1}) $，则过  $ M_{1} $ 的纬圆上的任意一点  $ P(x, y, z) $ 满足条件

<div style="text-align: center;"><img src="imgs/img_in_image_box_755_131_949_306.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;">图 17-1</div>


 $$ \overrightarrow{M_{1}P}\perp\tau,\quad\left|\overrightarrow{M_{0}P}\right|=\left|\overrightarrow{M_{0}M_{1}}\right|, $$ 

即

 $$ \begin{cases}l(x-x_{1})+m(y-y_{1})+n(z-z_{1})=0,\ $ x-x_{0})^{2}+(y-y_{0})^{2}+(z-z_{0})^{2}=(x_{1}-x_{0})^{2}+(y_{1}-y_{0})^{2}+(z_{1}-z_{0})^{2},\end{cases} $$ 

与方程  $ F(x_{1}, y_{1}, z_{1}) = 0 $ 和  $ G(x_{1}, y_{1}, z_{1}) = 0 $ 联立消去  $ x_{1}, y_{1}, z_{1} $，便可得到旋转曲面的方程.

注 常考曲线  $ \Gamma:\begin{cases}F(x,y,z)=0,\\G(x,y,z)=0\end{cases} $ 绕 z 轴旋转一周而成的旋转曲面的方程.

如图 17-2 所示，在曲线  $ \Gamma $ 上任取一点  $ M_1(x_1, y_1, z_1) $，则过点  $ M_1 $ 的纬圆上的任意一点  $ P(x, y, z) $ 满足条件  $ \left|\overrightarrow{OP}\right| = \left|\overrightarrow{OM_1}\right| $ 和  $ z = z_1 $，即  $ x^2 + y^2 + z^2 = x_1^2 + y_1^2 + z_1^2 $ 且  $ z = z_1 $，得  $ \frac{1}{2} $ 因为  $ (x - x_1, y - y_1, z - z_1) \perp (0, 0, 1) $

 $$ x^{2}+y^{2}=x_{1}^{2}+y_{1}^{2} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_745_652_940_841.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;">图 17-2</div>


从方程组  $ \begin{cases} F(x_{1}, y_{1}, z) = 0, \\ G(x_{1}, y_{1}, z) = 0, \\ x^{2} + y^{2} = x_{1}^{2} + y_{1}^{2} \end{cases} $ 中消去  $ x_{1} $ 和  $ y_{1} $，便得到旋转曲面的方程.

如果能从方程组 $ \begin{cases}F(x,y,z)=0,\\G(x,y,z)=0\end{cases} $中解出 $ x=f_{1}(z) $和 $ y=f_{2}(z) $，则旋转曲面的方程为

 $ x^{2}+y^{2}=\left[f_{1}(z)\right]^{2}+\left[f_{2}(z)\right]^{2} $

如求  $ \begin{cases} y^2 - (z - 1)^2 = 1, \\ x = 0 \end{cases} $ 绕 z 轴旋转一周而成的旋转曲面的方程，由方程组知  $ \begin{cases} x = 0, \\ y^2 = 1 + (z - 1)^2 \end{cases} $，则旋转曲面的方程为  $ x^2 + y^2 = 0^2 + 1 + (z - 1)^2 $，即  $ x^2 + y^2 - (z - 1)^2 = 1 $。

例 17.5 设  $ \Sigma_1 $ 是由过点  $ (0, -1, 1) $ 与点  $ (0, 0, 0) $ 的直线  $ L $ 绕  $ z $ 轴旋转一周所得的旋转曲面位于  $ z \geq 0 $ 的部分， $ \Sigma_2 $ 的方程为  $ z^2 = 2x $，则  $ \Sigma_1 $ 与  $ \Sigma_2 $ 的交线  $ \Gamma $ 在  $ xOy $ 面上的投影曲线方程为___。

解 应填  $ \left\{\begin{aligned}x^{2}+y^{2}=2x,\\ z=0.\end{aligned}\right. $