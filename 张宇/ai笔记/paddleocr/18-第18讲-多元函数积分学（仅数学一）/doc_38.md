恒成立，就说曲线积分 $ \int_{L}Pdx+Qdy $在G内与路径无关，否则便说与路径有关.

在以上叙述中注意到，如果曲线积分与路径无关，那么

 $$ \int_{L_{1}}P\mathrm{d}x+Q\mathrm{d}y=\int_{L_{2}}P\mathrm{d}x+Q\mathrm{d}y\ . $$ 

因为

 $$ \int_{L_{2}}P\mathrm{d}x+Q\mathrm{d}y=\begin{aligned} 负负得正 \\\downarrow\\ \downarrow\\ \downarrow\\ L_{2}^{-}\end{aligned}P\mathrm{d}x+Q\mathrm{d}y, $$ 

所以

 $$ \int_{L_{1}}P\mathrm{d}x+Q\mathrm{d}y+\int_{L_{2}}P\mathrm{d}x+Q\mathrm{d}y=0\xrightarrow{L_{2}}\begin{array}{c}B\\ D\\ L_{1}\end{array} $$ 

从而

 $$ \oint_{L_{1}+L_{2}}P\mathrm{d}x+Q\mathrm{d}y=0\xrightarrow{}\begin{aligned}&\iint\limits_{\Omega}\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\mathrm{d}x\mathrm{d}y=0\\&\downarrow\\& 具有任意性 , 则 \frac{\partial Q}{\partial x}=\frac{\partial P}{\partial y}\end{aligned} $$ 

这里  $ L_{1} + L_{2} $ 是一条有向闭曲线。因此，在区域 G 内由曲线积分与路径无关可推得在 G 内沿闭曲线的曲线积分为零。反过来，如果在区域 G 内沿任意闭曲线的曲线积分为零，也可推得在 G 内曲线积分与路径无关。由此得出结论：曲线积分  $ \int_{L} Pdx + Qdy $ 在 G 内与路径无关相当于沿 G 内任意闭曲线 C 的曲线积分

 $$ \oint_{c}P\mathrm{d}x+Q\mathrm{d}y=0\quad. $$ 

②条件.

设  $ P(x, y) $， $ Q(x, y) $ 在单连通区域 G 内具有一阶连续偏导数，则曲线积分  $ \int_{L} P \mathrm{d}x + Q \mathrm{d}y $ 在 G 内与路径无关（或沿 G 内任意闭曲线的曲线积分为零）的充分必要条件是在 G 内处处有

<div style="text-align: center;"><img src="imgs/img_in_image_box_389_981_839_1131.jpg" alt="Image" width="43%" /></div>


注 (1) 设  $ D $ 为平面区域，若  $ D $ 内任一闭曲线所围的部分都属于  $ D $，则称  $ D $ 为平面单连通区域，否则称为复连通区域。通俗地说，平面单连通区域就是不含有“洞”（包含点“洞”）的区域，复连通区域是含有“洞”（包含点“洞”）的区域。例如，平面上的圆形区域  $ \left\{(x, y) \mid x^2 + y^2 < 1\right\} $，上半平面  $ \left\{(x, y) \mid y > 0\right\} $ 都是单连通区域，圆环形区域  $ \left\{(x, y) \mid 1 < x^2 + y^2 < 4\right\} $， $ \left\{(x, y) \mid 0 < x^2 + y^2 < 2\right\} $ 都是复连通区域。

(2) 平面曲线积分与路径无关.