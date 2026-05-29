## 考研数学基础30讲·高等数学分册

性质 2(积分的方向性)  $ \iint\limits_{\Sigma^{-}}F\cdot dS=-\iint\limits_{\Sigma^{+}}F\cdot dS $，其中  $ \Sigma^{-} $为  $ \Sigma^{+} $的另一侧.

<div style="text-align: center;"><img src="imgs/img_in_image_box_107_198_659_330.jpg" alt="Image" width="53%" /></div>


性质 3(积分的可加性) 当  $ \Sigma_{1}\cup\Sigma_{2}=\Sigma,\Sigma_{1}\cap\Sigma_{2}=\varnothing $ 时， $ \iint_{\Sigma}F\cdot dS=\iint_{\Sigma_{1}}F\cdot dS+\iint_{\Sigma_{2}}F\cdot dS $

大曲面：分成两块，等于流过这两块曲面通量之和。

注 第二型曲面积分的“对称性”.(与第二型曲线积分类似，第二型曲面积分是没有几何上的对称性的，要说对称性，只是在计算出数量后，有一个形式上的抵消或者两倍，仅此而已.)

曲面  $ \Sigma $ 是关于 xOz 面对称的有向曲面，设函数  $ Q(x, y, z) = xy^2z $（关于 y 的偶函数），则有

 $$ \iint\limits_{\Sigma}Q(x,\ y,\ z)\mathrm{d}z\mathrm{d}x=\iint\limits_{\Sigma}x y^{2}z\mathrm{d}z\mathrm{d}x=0\ . $$ 

以下从两个角度解释上述结果：

①如图 18-21 所示，对称的两处 dS 的法向量在 j 方向上的投影方向相反，故  $ Q(x, y, z) $ dzdx =  $ xy^2 $ zdxdx,  $ Q(x, -y, z)(-dzdx) = -xy^2 $ zdxdx，于是  $ \iint_{\Sigma} xy^2 zdzdx = 0 $.

②从通量的角度来理解，一般规定，流入为负通量，流出为正通量。如图 18-22 所示，从 A 流入，从 B 流出，通量为 0，故积分为 0。

<div style="text-align: center;"><img src="imgs/img_in_image_box_224_871_742_1050.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">图 18-21</div>


<div style="text-align: center;">图 18-22</div>


## 4 计算

(1) 基本方法——化为二重积分．第一型曲面积分：

(1) 基本方法——化为二重积分．

①拆成三个积分（如果有的话），一个一个做： $ \iint_{D}f(x,y,z)\mathrm{d}S $．其中 $ \mathrm{d}S=\frac{\sqrt{1+(z_{x}^{\prime})^{2}+(z_{y}^{\prime})^{2}}}{\sqrt{1+(z_{x}^{\prime})^{2}+(z_{y}^{\prime})^{2}}}\mathrm{d}x\mathrm{d}y=\frac{1}{\cos\gamma}\mathrm{d}x\mathrm{d}y $

 $$ \begin{aligned}&\iint\limits_{\Sigma}P(x,\ y,\ z)\mathrm{d}y\mathrm{d}z+Q(x,\ y,\ z)\mathrm{d}z\mathrm{d}x+R(x,\ y,\ z)\mathrm{d}x\mathrm{d}y\\=&\iint\limits_{\Sigma}P(x,\ y,\ z)\mathrm{d}y\mathrm{d}z+\iint\limits_{\Sigma}Q(x,\ y,\ z)\mathrm{d}z\mathrm{d}x+\iint\limits_{\Sigma}R(x,\ y,\ z)\mathrm{d}x\mathrm{d}y.\end{aligned} $$ 