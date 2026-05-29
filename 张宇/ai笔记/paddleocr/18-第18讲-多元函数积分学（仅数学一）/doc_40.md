则

 $$ \frac{\partial P}{\partial y}=\frac{-2xy}{\left(x^{2}+y^{2}-1\right)^{2}},\frac{\partial Q}{\partial x}=\frac{2axy}{\left(x^{2}+y^{2}-1\right)^{2}}. $$ 

由在 D 内曲线积分与路径无关知

 $$ \frac{\partial Q}{\partial x}=\frac{\partial P}{\partial y}, $$ 

解得a=-1

例 18.21 设曲线积分  $ \int_{C} xy^2 dx + y\varphi(x) dy $ 与路径无关，其中  $ \varphi(x) $ 具有连续的导数，且  $ \varphi(0) = 0 $。计算  $ \int_{(0,0)}^{(1,1)} xy^2 dx + y\varphi(x) dy $ 的值。

♡分析 由曲线积分与路径无关  $ \Leftrightarrow \frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y} $，求出  $ \varphi(x) $.

解 由  $ P(x, y) = xy^{2} $， $ Q(x, y) = y\varphi(x) $， $ \frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x} $，得

 $$ 2xy=y\varphi^{\prime}(x),\varphi(x)=x^{2}+C. $$ 

再由  $ \varphi(0)=0 $ ，得 C=0 ，故  $ \varphi(x)=x^{2} $ ，所以

 $$ \int_{(0,0)}^{(1,1)}x y^{2}\mathrm{d}x+y\varphi(x)\mathrm{d}y=\int_{(0,0)}^{(1,1)}x y^{2}\mathrm{d}x+x^{2}y\mathrm{d}y. $$ 

方法一 沿直线 y = x 从点  $ (0, 0) $ 到点  $ (1, 1) $ 积分，得

 $$ \int_{(0,0)}^{(1,1)}xy^{2}\mathrm{d}x+y\varphi(x)\mathrm{d}y=\int_{0}^{1}2x^{3}\mathrm{d}x=\frac{1}{2} $$ 

方法二 利用折线法求积分.

 $$ \begin{aligned} 原式 &=\int_{L_{1}}xy^{2}\mathrm{d}x+x^{2}y\mathrm{d}y+\int_{L_{2}}xy^{2}\mathrm{d}x+x^{2}y\mathrm{d}y\\&=0+\int_{0}^{1}x\mathrm{d}x\\&=\frac{1}{2}\end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_713_841_860_969.jpg" alt="Image" width="14%" /></div>


方法三 利用凑微分找全微分.

 $$ \begin{aligned} 原式 &=\int_{C}\overrightarrow{xy^{2}}\mathrm{d}x+\overrightarrow{yx^{2}}\mathrm{d}y\\&=\int_{C}y^{2}\mathrm{d}\left(\frac{1}{2}x^{2}\right)+x^{2}\mathrm{d}\left(\frac{1}{2}y^{2}\right)\xrightarrow{}\left.u\mathrm{d}v+v\mathrm{d}u=\mathrm{d}(uv)\right.\\&=\int_{C}\mathrm{d}\left(\frac{1}{2}x^{2}y^{2}\right)=\frac{1}{2}x^{2}y^{2}\bigg|_{(0,0)}^{(1,1)}=\frac{1}{2}\ .\\ \end{aligned} $$ 