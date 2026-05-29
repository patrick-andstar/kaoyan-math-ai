直线L的两点式方程为 $ \frac{x}{0}=\frac{y+1}{1}=\frac{z-1}{-1} $，参数方程为 $ \begin{cases}x=0,\\y=-1+t,\\z=1-t,\end{cases} $，t为参数，即 $ \begin{cases}x=0,\\y=-z,\end{cases} $由“三、2.(4)

注”，得  $ \Sigma_{1} $ 的方程为  $ x^{2} + y^{2} = 0^{2} + (-z)^{2} = z^{2} $，也即  $ z = \sqrt{x^{2} + y^{2}} $。

将 $ \begin{cases}z=\sqrt{x^{2}+y^{2}}\\z^{2}=2x\end{cases} $，中的z消去，得 $ x^{2}+y^{2}=2x $，即得到投影曲线方程为

 $ \left\{\begin{aligned}x^{2}+y^{2}&=2x,\\ z&=0.\end{aligned}\right. $ 曲线Γ和其在xOy面上的投影如图17-3所示.



<div style="text-align: center;"><img src="imgs/img_in_image_box_733_276_931_432.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;">图 17-3</div>


## 四 多元函数微分学的几何应用

<div style="text-align: center;"><img src="imgs/img_in_image_box_840_505_944_612.jpg" alt="Image" width="10%" /></div>


## 1 空间曲线的切线与法平面

(1) 用参数方程给出曲线： $ \begin{cases}x=x(t),\\y=y(t),\\z=z(t),\end{cases} $  $ t\in I $

其中  $ x(t) $,  $ y(t) $,  $ z(t) $ 在 I 上可导，且三个导数不同时为 0，则曲线在  $ P_{0}(x_{0}, y_{0}, z_{0}) $ 处的切向量  $ \boldsymbol{\tau} = (x'(t_{0}), y'(t_{0}), z'(t_{0})) $.

切线方程： $ \frac{x-x_{0}}{x^{\prime}(t_{0})}=\frac{y-y_{0}}{y^{\prime}(t_{0})}=\frac{z-z_{0}}{z^{\prime}(t_{0})} $

法平面方程： $ x'(t_{0})(x-x_{0})+y'(t_{0})(y-y_{0})+z'(t_{0})(z-z_{0})=0 $

(2) 用方程组给出曲线： $ \begin{cases}F(x,y,z)=0,\\G(x,y,z)=0.\end{cases} $

当 $ \frac{\partial(F,G)}{\partial(y,z)}=\begin{vmatrix}\frac{\partial F}{\partial y}&\frac{\partial F}{\partial z}\\\frac{\partial G}{\partial y}&\frac{\partial G}{\partial z}\end{vmatrix}\neq0 $ 时，可确定 $ \begin{cases}x=x,\\y=y(x),\\z=z(x).\end{cases} $

雅可比行列式

其在  $ P_{0}(x_{0}, y_{0}, z_{0}) $ 处的切向量  $ \boldsymbol{\tau} = \begin{vmatrix} i & j & k \\ F_{x}^{\prime} & F_{y}^{\prime} & F_{z}^{\prime} \\ G_{x}^{\prime} & G_{y}^{\prime} & G_{z}^{\prime} \\ \downarrow & \downarrow & P_{0} \end{vmatrix} = (A, B, C) $.

两个梯度向量的叉乘： $ n_{1} \times n_{2} $ G 在  $ P_{0} $ 的梯度向量  $ n_{2} $

<div style="text-align: center;"><img src="imgs/img_in_image_box_725_1220_895_1329.jpg" alt="Image" width="16%" /></div>
