## 第18讲 多元函数积分学（仅数学一）

b. 积分区域为  $ \left\{\begin{array}{l} 球或球的部分,  \\  锥或锥的部分 .\end{array}\right. $

②计算方法.

 $$ \begin{aligned}\left.\begin{array}{l}x^{2}+y^{2}+z^{2}=r^{2}\\z=r\cos\varphi\\ 故 x^{2}+y^{2}=r^{2}\sin^{2}\varphi\end{array}\right.\end{aligned} $$ 

令

球面坐标系应该是整个高等数学或者说微积分里最复杂的一种计算方法，我们打一套事来把这个问题解决。

第一步，转：从xOz面出发，拉着一扇门缝z轴(从z轴正向向上看)逆时针旋转一周.见a.

第二步，开：从z轴出发，喇叭花开花，伸展运动，从0°升到180°.见b.

 $$ \begin{cases}x=r\sin\varphi\cos\theta,\\y=r\sin\varphi\sin\theta,\\z=r\cos\varphi,\end{cases} $$ 

第三步，穿：从原点发出一条射线，至无穷远处，见c.

这套拳可称为“球系太极拳”，在解决积分问题的同时，舒展筋骨，强身健体。

则  $ dv = r^2 \sin \varphi drd\varphi d\theta $.

测度的倍数

a. 过 z 轴的半平面与 xOz 面正向夹角为  $ \theta $（取值范围  $ [0, 2\pi] $） $ \left\{\begin{array}{l} 先碰到 \Omega, \\  后离开 \Omega, \\  记 \theta_{2}\end{array}\right. $

<div style="text-align: center;"><img src="imgs/img_in_image_box_349_525_502_740.jpg" alt="Image" width="14%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_560_554_714_739.jpg" alt="Image" width="14%" /></div>


b. 顶点在原点，以 z 轴为中心轴的圆锥面半顶角为  $ \varphi $（取值范围  $ [0, \pi] $） $ \left\{\begin{array}{l} 先碰到 \Omega, \\  后离开 \Omega, \end{array}\right. $ 记  $ \varphi_{1}(\theta) $，

<div style="text-align: center;"><img src="imgs/img_in_image_box_360_841_486_1033.jpg" alt="Image" width="12%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_534_842_705_1036.jpg" alt="Image" width="16%" /></div>


c. 从原点出发画一条长为 r 的线（取值范围  $ [0, +\infty) $） $ \left\{\begin{array}{l} 先碰到 \Omega, \\  后离开 \Omega, \end{array}\right. $ 记  $ r_{1}(\varphi, \theta) $，

<div style="text-align: center;"><img src="imgs/img_in_image_box_352_1171_500_1327.jpg" alt="Image" width="14%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_552_1129_717_1329.jpg" alt="Image" width="15%" /></div>
