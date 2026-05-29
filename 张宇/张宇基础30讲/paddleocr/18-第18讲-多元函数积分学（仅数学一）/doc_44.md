## 考研数学基础30讲·高等数学分册

注 必须注意，上式等号左边是第二型曲面积分， $ \iint_{\Sigma} $ 表明了这件事，其中  $ \mathrm{d}x\mathrm{d}y $ 为有向曲面微元在 xOy 平面上的投影分量；等式右边是 xOy 平面上的二重积分， $ \iint_{D_{y}} $ 表明了这件事，其中  $ \mathrm{d}x\mathrm{d}y $ 为二重积分的面积微元，R 中的 z 已用  $ \Sigma $ 的方程  $ z = z(x, y) $ 代入了，它是 x, y 的函数。两个  $ \mathrm{d}x\mathrm{d}y $ 虽然写法一样，但其意义不一样。

其他两个第二型曲面积分的计算与此类似，请考生参照“②，③”两条自行写出.

④计算已转化成的二重积分.

例 18.22 设直线  $ L $ 过点  $ A(-1, 0, 1) $ 与  $ B(0, 0, 0) $， $ L $ 绕  $ z $ 轴旋转一周得曲面  $ \Sigma_0 $，计算  $ I = \oint_{\Sigma} \frac{e^z}{\sqrt{x^2 + y^2}} \, dx \, dy $，其中  $ \Sigma $ 是由  $ \Sigma_0 $， $ z = 1 $， $ z = 2 $ 所围有界闭区域的边界曲面，取外侧。就是铅直方向的流量

分析 先写出曲面  $ \Sigma_{0} $，然后选面求积分，之后加起来即可.

解 L 的方程为  $ \frac{x+1}{1}=\frac{y}{0}=\frac{z-1}{-1} $，可得其参数方程为  $ \left\{\begin{aligned}x&=-1+t,\\ y&=0,\\ z&=1-t,\end{aligned}\right. $ 即  $ \left\{\begin{aligned}x&=-z,\\ y&=0.\end{aligned}\right. $

由第 17 讲 “三、2.(4)” 中的注，有  $ \Sigma_{0} $ 的方程为  $ x^{2} + y^{2} = z^{2} + 0 = z^{2} $

如图 18-23 所示，记  $ \Sigma = \Sigma_{1} + \Sigma_{2} + \Sigma_{3} $，其中  $ \Sigma_{1}: z = 1, x^{2} + y^{2} \leqslant 1 $； $ \Sigma_{2}: z = 2, x^{2} + y^{2} \leqslant 4 $； $ \Sigma_{3}: z = \sqrt{x^{2} + y^{2}}, 1 \leqslant z \leqslant 2 $。则

 $$ I=\oint_{\Sigma}=\iint_{\Sigma_{1}}+\iint_{\Sigma_{2}}+\iint_{\Sigma_{3}}, $$ 

 $$ \iint_{\Sigma_{1}}=-\iint_{D_{1}}\frac{\mathrm{e}^{1}}{\sqrt{x^{2}+y^{2}}}\mathrm{d}x\mathrm{d}y=-\mathrm{e}\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{1}\frac{1}{r}\cdot r\mathrm{d}r=-2\pi\mathrm{e} $$ 

 $$ \iint_{\Sigma_{2}}=\iint_{D_{2}}\frac{\mathrm{e}^{2}}{\sqrt{x^{2}+y^{2}}}\mathrm{d}x\mathrm{d}y=\mathrm{e}^{2}\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{2}\frac{1}{r}\cdot r\mathrm{d}r=4\pi\mathrm{e}^{2}\ , $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_756_900_935_1101.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">图 18-23</div>


 $$ \iint_{\Sigma_{1}}=-\iint_{D_{1}}\frac{\mathrm{e}^{\sqrt{x^{2}+y^{2}}}}{\sqrt{x^{2}+y^{2}}}\mathrm{d}x\mathrm{d}y=-\int_{0}^{2\pi}\mathrm{d}\theta\int_{1}^{2}\frac{\mathrm{e}^{r}}{r}\cdot r\mathrm{d}r=-2\pi(\mathrm{e}^{2}-\mathrm{e}), $$ 

其中  $ D_{1}=\left\{(x,y)\mid x^{2}+y^{2}\leqslant1\right\} $， $ D_{2}=\left\{(x,y)\mid x^{2}+y^{2}\leqslant4\right\} $， $ D_{3}=\left\{(x,y)\mid1\leqslant x^{2}+y^{2}\leqslant4\right\} $．故

 $ I=-2\pi e+4\pi e^{2}-2\pi(e^{2}-e)=2\pi e^{2} $

(2) 转换投影法.

①转换投影法中有向曲面正向单位法向量的求法.

设  $ \Sigma: z = z(x, y) $，其中 z 有一阶连续偏导数，则