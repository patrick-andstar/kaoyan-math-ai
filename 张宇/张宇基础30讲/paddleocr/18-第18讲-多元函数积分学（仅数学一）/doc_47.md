 $$ \begin{aligned}&=-\int_{0}^{2\pi}\left[\frac{1}{3}(\cos^{4}\theta+\sin^{4}\theta)+\frac{7}{4}\right]\mathrm{d}\theta\\ &\\&=-\frac{7\pi}{2}-\frac{8}{3}\int_{0}^{\frac{\pi}{2}}\sin^{4}\theta\mathrm{d}\theta=-\frac{7\pi}{2}-\frac{8}{3}\times\frac{3}{4}\times\frac{1}{2}\times\frac{\pi}{2}=-4\pi.\\ \end{aligned} $$ 

(3) 高斯公式. 联想到格林公式

设空间有界闭区域  $ \Omega $ 由有向分片光滑封闭曲面  $ \Sigma $ 围成， $ P(x, y, z) $， $ Q(x, y, z) $， $ R(x, y, z) $ 在  $ \Omega $ 上具有一阶连续偏导数，则有公式边界曲面上的第二型曲面积分化为内部立体的三重积分

 $$ \begin{aligned}\oint_{\frac{\pi}{2}}P\mathrm{d}y\mathrm{d}z+Q\mathrm{d}z\mathrm{d}x+R\mathrm{d}x\mathrm{d}y=\iiint_{\frac{\pi}{2}}\left(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}\right)\mathrm{d}v,\end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_590_407_945_533.jpg" alt="Image" width="34%" /></div>


其中， $ \Sigma $ 是  $ \Omega $ 的整个边界曲面的外侧。

注 第二型曲面积分与“源”的概念是紧密联系的，所以就有了散度的概念，在空间区域上的某点处的散度是指这个点发散的强度。如果在一个空间区域上，每一点处的三个偏导数加起来都是零，那就说明每一点处的散度都是零，即这个场是没有源头的，也就是说每一点都没有发散，也没有吸收，是个安安静静的场，称之为“无源场”。

如  $ \iint_{D}P\mathrm{d}y\mathrm{d}z + Q\mathrm{d}z\mathrm{d}x + R\mathrm{d}x\mathrm{d}y \equiv 0 $，即任何一点都是没有散度的，是个“无源场”，则  $ \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} = 0 $。

①封闭曲面且内部无奇点，直接用高斯公式.

例18.26 设空间有界区域  $ \Omega $ 由柱面  $ x^{2} + y^{2} = 1 $ 与平面 z = 0 和  $ x + z = 1 $ 围成． $ \Sigma $ 为  $ \Omega $ 的边界曲面的外侧．计算曲面积分

 $$ I=\oint\limits_{\Sigma}2xz\mathrm{d}y\mathrm{d}z+xz\cos y\mathrm{d}z\mathrm{d}x+3yz\sin x\mathrm{d}x\mathrm{d}y. $$ 

☑ 分析 首先将该曲面积分通过高斯公式转化为三重积分，然后利用概念、对称性化简，最后再计算剩下的部分。

<div style="text-align: center;"><img src="imgs/img_in_image_box_793_916_949_1060.jpg" alt="Image" width="15%" /></div>


<div style="text-align: center;">进入多少</div>


解 根据高斯公式，得

 $$ I=\iiint\limits_{\Omega}(2z-xz\sin y+3y\sin x)\mathrm{d}x\mathrm{d}y\mathrm{d}z. $$ 

因为Ω关于xOz坐标面对称，所以

因为 $ y\to-y $时， $ \Omega $不变，故 $ \Omega $关 $ \iiint_{\Omega}xz\sin y\,dx\,dy\,dz=0 $， $ \iiint_{\Omega}3y\sin x\,dx\,dy\,dz=0 $于xOz坐标面对称。

记 $ D=\left\{(x,y)\mid x^{2}+y^{2}\leqslant1\right\} $，则

 $$ \begin{aligned}I=&\iiint\limits_{\Omega}2z\mathrm{d}x\mathrm{d}y\mathrm{d}z=\iint\limits_{D}\mathrm{d}x\mathrm{d}y\int_{0}^{1-x}2z\mathrm{d}z\\=&\iint\left(1+x^{2}\right)\mathrm{d}x\mathrm{d}y=\pi+\frac{1}{2}\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{1}r^{3}\mathrm{d}r=\frac{5\pi}{4}.\end{aligned} $$ 