注 $ ^{*} $处得来过程如图18-18所示，若L所围区域D内有奇点Q，则用 $ L_{1} $“挖去”它，并记挖去奇点后的阴影区域为 $ D' $，于是负负得正

 $$ \begin{aligned}&\oint_{L}P\mathrm{d}x+Q\mathrm{d}y=\oint_{L+L_{1}^{-}}P\mathrm{d}x+Q\mathrm{d}y-\oint_{L_{1}^{-}}P\mathrm{d}x+Q\mathrm{d}y\\ &=\iint\limits_{D^{\prime}}\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\mathrm{d}\sigma+\oint_{L_{1}}P\mathrm{d}x+Q\mathrm{d}y\\ &=\oint_{L_{1}}P\mathrm{d}x+Q\mathrm{d}y.\\ \end{aligned}\begin{aligned} 在边界线上做功换为  在  里 \\  面的线 L_{1} 上做功 , 对于 \\  L_{1}, 一般令分母 =\varepsilon\\ \end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_787_160_966_421.jpg" alt="Image" width="17%" /></div>


例 18.19 计算曲线积分  $ I = \oint_L \frac{4x - y}{4x^2 + y^2} \, \mathrm{d}x + \frac{x + y}{4x^2 + y^2} \, \mathrm{d}y $，其中  $ L $ 是  $ x^2 + y^2 = 2 $，方向为逆时针方向。

分析 分母  $ 4x^2 + y^2 $ 在  $ (0, 0) $ 处为零，即在积分区域内有奇点，影响一阶偏导数连续这一条件，因此不可用格林公式。

解 经计算有

 $$ \frac{\partial}{\partial x}\left(\frac{x+y}{4x^{2}+y^{2}}\right)=\frac{y^{2}-4x^{2}-8xy}{\left(4x^{2}+y^{2}\right)^{2}}=\frac{\partial}{\partial y}\left(\frac{4x-y}{4x^{2}+y^{2}}\right)\quad\overrightarrow{\frac{\partial Q}{\partial x}}=\frac{\partial P}{\partial y}\quad( 无旋场 ) $$ 

但是这里不能用格林公式，因为在$L$围成的区域内点$O(0,0)$处，$P,Q$均不连续，故在该区域内作一曲线$L_{1}:4x^{2}+y^{2}=\varepsilon^{2}(\varepsilon>0)$，取逆时针方向，从而

 $$ \begin{aligned}&\oint_{L}\frac{4x-y}{4x^{2}+y^{2}}\mathrm{d}x+\frac{x+y}{4x^{2}+y^{2}}\mathrm{d}y\\=&\oint_{L_{1}}\frac{4x-y}{4x^{2}+y^{2}}\mathrm{d}x+\frac{x+y}{4x^{2}+y^{2}}\mathrm{d}y\\=&\frac{1}{\varepsilon^{2}}\oint_{L_{1}}\left(4x-y\right)\mathrm{d}x+\left(x+y\right)\mathrm{d}y\\=&\frac{1}{\varepsilon^{2}}\iint_{D_{1}}2\mathrm{d}x\mathrm{d}y=\pi,\end{aligned} $$ 

其中 $ D_{1} $为 $ L_{1} $围成的区域.

(3)平面曲线积分与路径无关.  $ \longrightarrow $ 与格林公式联系紧密（若  $ \frac{\partial Q}{\partial x} \equiv \frac{\partial P}{\partial y} $，则平面旋度为0，也即曲线积分与路径无关）

①概念.

设 G 是一个区域， $ P(x, y) $ 以及  $ Q(x, y) $ 在区域 G 内具有一阶连续偏导数。如果对于 G 内任意指定的两个点 A, B 以及 G 内从点 A 到点 B 的任意两条曲线  $ L_{1} $， $ L_{2} $（见图 18-19），等式

 $$ \int_{L_{1}}P\mathrm{d}x+Q\mathrm{d}y=\int_{L_{2}}P\mathrm{d}x+Q\mathrm{d}y $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_791_1240_968_1389.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">图 18-19</div>
