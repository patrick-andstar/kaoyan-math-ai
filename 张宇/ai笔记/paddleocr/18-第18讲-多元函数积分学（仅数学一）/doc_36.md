其中  $ L = L_{AB} + C_{BA} $，公式中的 “±” 号由  $ L $ 的方向而定。若  $ L $ 为正向则取正号，若  $ L $ 为负则取负号。 $ C_{AB} $ 为  $ C_{BA} $ 的反向弧。如果上式右边的二重积分和  $ \int_{C_{AB}} $ 容易计算的话，那么就可利用上述转换方法计算原积分  $ \int_{L_{AB}} $。

例18.18 已知L是第一象限中从点(0,0)沿圆周 $ x^2 + y^2 = 2x $到点(2,0)，再沿圆周 $ x^2 + y^2 = 4 $到点(0,2)的曲线段，计算曲线积分 $ I = \int_L 3x^2 y \, dx + (x^3 + x - 2y) \, dy $。

解 如图 18-17 所示，取有向线段  $ L_{1} $ 的方程为 x = 0，起点  $ (0, 2) $，终点  $ (0, 0) $。由  $ L $ 与  $ L_{1} $ 围成的平面区域记为  $ D $，于是有

 $$ I=\int_{L}3x^{2}y\mathrm{d}x+(x^{3}+x-2y)\mathrm{d}y $$ 

 $$ \oint_{L+L_{1}}3x^{2}y\mathrm{d}x+(x^{3}+x-2y)\mathrm{d}y-\int_{L_{1}}3x^{2}y\mathrm{d}x+(x^{3}+x-2y)\mathrm{d}y $$ 

根据格林公式，得

 $$ \begin{aligned}&\oint_{L+L_{1}}3x^{2}y\mathrm{d}x+(x^{3}+x-2y)\mathrm{d}y\\=&\iint_{D}\left[\frac{\partial}{\partial x}(x^{3}+x-2y)-\frac{\partial}{\partial y}(3x^{2}y)\right]\mathrm{d}x\mathrm{d}y\\=&\iint_{D}\mathrm{d}x\mathrm{d}y=\frac{1}{4}\pi\bullet2^{2}-\frac{1}{2}\pi\bullet1^{2}=\frac{\pi}{2}\ .\\ \end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_720_570_932_743.jpg" alt="Image" width="20%" /></div>


<div style="text-align: center;">图 18-17</div>


又

 $$ \int_{L_{1}}3x^{2}y\mathrm{d}x+(x^{3}+x-2y)\mathrm{d}y=\int_{2}^{0}(-2y)\mathrm{d}y=4, $$ 

所以

 $$ I=\frac{\pi}{2}-4. $$ 

③曲线封闭但有奇点在其内部，且除奇点外  $ \frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y} $，则换路径。（一般令分母等于常数作为路径，路径的起点和终点无须与原路径重合。）

若给的是封闭曲线的曲线积分  $ \oint_L P \, dx + Q \, dy $，满足条件“在  $ D $ 内除了奇点外， $ P $ 和  $ Q $ 具有一阶连续偏导数，并且除奇点外，均有  $ \frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y} $”，则可以换一条封闭曲线  $ L_1 $ 代替  $ L $，它全在  $ D $ 内，并能将奇点包含在  $ L_1 $ 的内部。则有公式

 $$ \oint_{L}P\mathrm{d}x+Q\mathrm{d}y\xlongequal{(*)}\oint_{L_{1}}P\mathrm{d}x+Q\mathrm{d}y. $$ 

这里要求 $ L_{1} $与L的方向相同.如果后者容易计算,就可达到目的.