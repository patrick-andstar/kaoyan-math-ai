 $$ \begin{aligned}\oint_{r}P\mathrm{d}x+Q\mathrm{d}y+R\mathrm{d}z&=\iint_{\Sigma}\begin{vmatrix}\mathrm{d}y\mathrm{d}z&\mathrm{d}z\mathrm{d}x&\mathrm{d}x\mathrm{d}y\\\frac{\partial}{\partial x}&\frac{\partial}{\partial y}&\frac{\partial}{\partial z}\\P&Q&R\end{vmatrix}( 此为第二型曲面积分形式 )\\&=\iint_{\Sigma}\begin{vmatrix}\cos\alpha&\cos\beta&\cos\gamma\\\frac{\partial}{\partial x}&\frac{\partial}{\partial y}&\frac{\partial}{\partial z}\\P&Q&R\end{vmatrix}\mathrm{d}S( 此为第一型曲面积分形式 ),\end{aligned} $$ 

其中  $ n^{\circ}=(\cos\alpha,\cos\beta,\cos\gamma) $ 为  $ \Sigma $ 的单位外法向量.

注 可以证明 (这里不证)，公式的成立与绷在  $ \Gamma $ 上的曲面大小、形状无关，如图 18-26 所示，有  $ \oint_{\Gamma} = \iint_{\Sigma_1} = \iint_{\Sigma_2} \cdot $

举个容易理解的例子，小孩玩的泡泡棒（泡泡机），蘸了肥皂水吹一下泡泡就出来了，T就是蘸肥皂水的塑料圈，上面绷着的就是泡泡，在这些泡泡中无论是哪个，不管大小和形状，都可以作为计算公式中的Σ。

再问大家，绷在厂上的什么曲面最简单？答得好，平面！在泡泡还没有脱离圈圈之前可以

再问大家，绷在Γ上的什么曲面最简单？答得好，平面！在泡泡还没有脱离圈圈之前可以有各种形状，但最简单的形状是平面，是吹之前的最原始的形状！

<div style="text-align: center;"><img src="imgs/img_in_image_box_781_533_937_658.jpg" alt="Image" width="15%" /></div>


<div style="text-align: center;">图 18-26</div>


例 18.30 已知曲线  $ L $ 的方程为  $ \begin{cases} z = \sqrt{2 - x^2 - y^2} \\ z = x \end{cases} $，起点为  $ A(0, \sqrt{2}, 0) $，终点为  $ B(0, -\sqrt{2}, 0) $，计算曲线积分  $ I = \int_L (y + z) \, dx + (z^2 - x^2 + y) \, dy + x^2 y^2 \, dz $。

分析 方法一利用基本方法（参数法）

方法二利用斯托克斯公式.



<div style="text-align: center;"><img src="imgs/img_in_image_box_456_853_592_955.jpg" alt="Image" width="13%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_331_969_472_1055.jpg" alt="Image" width="13%" /></div>


方法三利用做功取微元分析.

对于 i 方向做功微元： $ (-y+z)(-dx)+(y+z)dx=2ydx $；

对于j方向做功微元： $ (-y)\mathrm{d}y+y\mathrm{d}y=0 $；

对于 k 方向做功微元： $ x^{2}y^{2}(-\mathrm{d}z)+x^{2}y^{2}\mathrm{d}z=0 $

解 方法一 由  $ \begin{cases} z = \sqrt{2 - x^2 - y^2}, \\ z = x \end{cases} $ 得  $ \sqrt{2 - x^2 - y^2} = x $，即  $ 2x^2 + y^2 = 2 $，亦即  $ x^2 + \frac{y^2}{2} = 1 $。

于是曲线  $ L $ 的参数方程为  $ \begin{cases} x = \cos t, \\ y = \sqrt{2} \sin t, t \text{从} \frac{\pi}{2} (\text{起点} A) \text{到} -\frac{\pi}{2} (\text{终点} B) \end{cases} $。