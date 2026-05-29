<div style="text-align: center;"><img src="imgs/img_in_image_box_434_142_633_267.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;">L正向</div>


<div style="text-align: center;">图 18-16</div>


①曲线封闭且无奇点在其内部，直接用格林公式.

没有破坏一阶偏导连续这一条件的点

若给的是封闭曲线  $ \oint_{L} P \, dx + Q \, dy $，可以验算  $ P $ 和  $ Q $ 是否满足“在该封闭曲线所包围的区域  $ D $ 内， $ P $ 和  $ Q $ 具有一阶连续偏导数”，若满足，则可用格林公式

 $$ \oint_{L}P\mathrm{d}x+Q\mathrm{d}y=\iint_{D}\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\mathrm{d}\sigma $$ 

计算.这里要求L为D的边界，且正向.

例18.17 设质点在力  $ F = -x^2y $ 和  $ i + xy^2 $ 作用下沿圆周  $ x^2 + y^2 = 1 $ 的顺时针方向运动一周，则 F 所做的功  $ W = $ ___。

(☐分析) 求做功即计算第二型曲线积分，恰好此题也满足格林公式的三个条件，故直接利用格林公式解题即可。此处不能代入 $ x^{2}+y^{2}=1 $，你代入了吗？如果代

解 应填  $ -\frac{1}{2}\pi $.

设曲线  $ C: x^{2} + y^{2} = 1 $ 围成的区域为 D，则

<div style="text-align: center;"><img src="imgs/img_in_image_box_622_804_740_926.jpg" alt="Image" width="11%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_798_790_962_921.jpg" alt="Image" width="15%" /></div>


顺时针做功，添负号即可

 $$ W=\oint_{C}(-x^{2}y)\mathrm{d}x+xy^{2}\mathrm{d}y=-\iint_{D}(y^{2}+x^{2})\mathrm{d}x\mathrm{d}y=-\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{1}r^{3}\mathrm{d}r=-\frac{\pi}{2} $$ 

②非封闭曲线且 $ \frac{\partial Q}{\partial x}\neq\frac{\partial P}{\partial y} $，可补线使其封闭（加线减线）.

<div style="text-align: center;"><img src="imgs/img_in_image_box_807_1004_964_1105.jpg" alt="Image" width="15%" /></div>


如果不是封闭曲线的曲线积分，可以考虑补一条线  $ C_{BA} $，使  $ \underline{L_{AB} + C_{BA}} $ 构成一封闭曲线，并且使其包围的区域为一单连通区域 D，在 D 上  $ P(x, y) $ 和  $ Q(x, y) $ 具有一阶连续偏导数，则有

 $$ \int_{L_{AB}}P\mathrm{d}x+Q\mathrm{d}y=\int_{L_{AB}}P\mathrm{d}x+Q\mathrm{d}y+\int_{C_{BA}}P\mathrm{d}x+Q\mathrm{d}y-\int_{C_{BA}}P\mathrm{d}x+Q\mathrm{d}y $$ 

 $$ \begin{aligned} 椿林公式 &\xleftarrow{}=\oint_{L}P\mathrm{d}x+Q\mathrm{d}y-\int_{C_{BA}}P\mathrm{d}x+Q\mathrm{d}y\\&=\pm\iint_{D}\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\mathrm{d}\sigma+\int_{C_{AB}}P\mathrm{d}x+Q\mathrm{d}y,\end{aligned} $$ 