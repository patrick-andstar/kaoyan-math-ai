 $$ =4\left[\iint\limits_{x^{2}+y^{2}\leq1\atop x,y\geq0}xy\right.\left.\mathrm{d}x\mathrm{d}y+\iint\limits_{x^{2}+y^{2}\leq1\atop x,y\geq0}xy(x^{2}+y^{2})^{2}(-\mathrm{d}x\mathrm{d}y)\right]=\frac{1}{4}, $$ 

其中  $ \Sigma_{1} $ 为图 18-25 所示卦限的上面， $ \Sigma_{2} $ 为图 18-25 所示卦限的侧面。

本题也可利用高斯公式去解题。方法见解。

解 由题设得， $ I=\oint_{\Sigma}\left|xy\right|z^{2}\mathrm{d}x\mathrm{d}y+\oint_{\Sigma}\left|x\right|y^{2}z\mathrm{d}y\mathrm{d}z\xlongequal{记}I_{1}+I_{2} $，如图 18-25 所示，则

 $$ \begin{aligned}&I_{1}\xlongequal[ 公式 ]{ 高斯 }\iiint_{\Omega}\left|xy\right|\bullet2z\mathrm{d}v=\iiint_{\Omega}2\left|xy\right|z\mathrm{d}v\\ &\begin{aligned}\\ &=8\iiint\limits_{x,y\geq0}^{}\xyz\mathrm{d}v=8\iint\limits_{x^{2}+y^{2}\leq1\atop x,y\geq0}^{}\mathrm{d}\sigma\int_{x^{2}+y^{2}}^{1}xyz\mathrm{d}z\\&=4\iint\limits_{x^{2}+y^{2}\leq1\atop x,y\geq0}^{}xy\left\lbrack1-(x^{2}+y^{2})^{2}\right\rbrack\mathrm{d}\sigma\\&=4\int_{0}^{\frac{\pi}{2}}\mathrm{d}\theta\int_{0}^{1}r^{2}\cos\theta\sin\theta(1-r^{4})r\mathrm{d}r=\frac{1}{4}\ .\\ &\end{aligned}\\ \end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_736_490_943_688.jpg" alt="Image" width="20%" /></div>


<div style="text-align: center;">图 18-25</div>


$I_{2}$ 不能用高斯公式，因 $\frac{\partial}{\partial x}(|x|^{2}z)$ 在 $x=0$，$yz \neq 0$ 处不存在。而在点 $(x, y, z)$ 与点 $(-x, y, z)$ 处的通量分别为 $|x|^{2}yz$ ∂ydz 与 $|x|^{2}yz(-\mathrm{dydz})$，又在面 $z=1$ 上 dz=0，故 $I_{2}=\oint_{\frac{x}{y}}|x|^{2}yz\mathrm{dydz}=0$。于是 $I=\frac{1}{4}$。

## 六 空间第二型曲线积分的计算

<div style="text-align: center;"><img src="imgs/img_in_image_box_841_880_943_987.jpg" alt="Image" width="9%" /></div>


①一投二代三计算。(基本方法)

设  $ \Gamma $:  $ \begin{cases} x = x(t), \\ y = y(t), \\ z = z(t), \end{cases} $  $ t: \alpha \to \beta $，则有

 $$ \begin{aligned}&\int_{r}P\mathrm{d}x+Q\mathrm{d}y+R\mathrm{d}z\\ &\\=&\int_{\alpha}^{\beta}\left\{P[x(t),y(t),z(t)]x^{\prime}(t)+Q[x(t),y(t),z(t)]y^{\prime}(t)+R[x(t),y(t),z(t)]z^{\prime}(t)\right\}\mathrm{d}t.\\ \end{aligned} $$ 

②用斯托克斯公式．→实现边界与内部的转换

设  $ \Omega $ 为某空间区域，  $ \Sigma $ 为  $ \Omega $ 内的分片光滑有向曲面片，  $ \Gamma $ 为逐段光滑的  $ \Sigma $ 的边界，它的方向与  $ \Sigma $ 的法向量成右手系，函数  $ P(x, y, z) $， $ Q(x, y, z) $ 与  $ R(x, y, z) $ 在  $ \Omega $ 内具有连续的一阶偏导数，则有斯托克斯公式：