如果在三重积分中，被积函数里出现  $ x^{2} + y^{2} + z^{2} $，那么  $ \iiint_{\Omega: x^{2} + y^{2} + z^{2} \leq 1} (x^{2} + y^{2} + z^{2}) \, \mathrm{d}v $ 是不能直接将被积函数代为 1 的.

(2)  $ \Gamma: \begin{cases} x^{2} + y^{2} + z^{2} = 1, \\ x + y + z = 0, \end{cases} $ 曲线既在单位球面上，又在平面上，即为两个面的交线，

故曲线、曲面积分的积分区域只有边界线或边界面.

<div style="text-align: center;"><img src="imgs/img_in_image_box_826_252_929_356.jpg" alt="Image" width="9%" /></div>


在第一型曲线、曲面积分中，可以将积分曲线或曲面代入被积函数，如本题中(*)处来自曲线方程 $ \left\{\begin{aligned}x^{2}+y^{2}+z^{2}=1,\\ x+y+z=0,\end{aligned}\right. $可直接代入被积函数，从而化简计算.

## 5 应用

(1)对于空间光滑曲线Γ，若其由参数式 $ \begin{cases}x=x(t),\\y=y(t),\\z=z(t)\end{cases} $给出，则计算空间曲线的长度（弧长）

的公式为

 $$ l=\int_{\alpha}^{\beta}\sqrt{\left[x^{\prime}(t)\right]^{2}+\left[y^{\prime}(t)\right]^{2}+\left[z^{\prime}(t)\right]^{2}}\mathrm{d}t. $$ 

(2)对于空间光滑曲线L，若线密度为 $ \rho(x,y,z) $，则计算重心 $ (\bar{x},\bar{y},\bar{z}) $的公式为

 $$ \overline{x}=\frac{\int_{L}x\rho(x,y,z)\mathrm{d}s}{\int_{L}\rho(x,y,z)\mathrm{d}s},\overline{y}=\frac{\int_{L}y\rho(x,y,z)\mathrm{d}s}{\int_{L}\rho(x,y,z)\mathrm{d}s},\overline{z}=\frac{\int_{L}z\rho(x,y,z)\mathrm{d}s}{\int_{L}\rho(x,y,z)\mathrm{d}s}. $$ 

注 $ ^{1} $ (1) 在考研的范畴内，重心就是质心.

(2) 当密度  $ \rho(x, y) $ 或者  $ \rho(x, y, z) $ 为常数时，重心就成了形心.

(3) 形心公式的逆用.

由  $ \overline{x} = \frac{\int_{L} x ds}{\int_{L} 1 ds} $，得  $ \int_{L} x ds = \overline{x} \cdot l $，其中  $ l = \int_{L} 1 ds $ 为曲线  $ L $ 的长度；

由  $ \overline{y}=\frac{\int_{L}yds}{\int_{L}1ds} $，得  $ \int_{L}yds=\overline{y}\cdot l $，其中  $ l=\int_{L}1ds $ 为曲线 L 的长度；

由  $ \overline{z} = \frac{\int_{L} z \, ds}{\int_{L} 1 \, ds} $，得  $ \int_{L} z \, ds = \overline{z} \cdot l $，其中  $ l = \int_{L} 1 \, ds $ 为曲线  $ L $ 的长度。

(3)对于光滑曲线L，线密度为 $ \rho(x,y,z) $，则计算该曲线对x轴、y轴、z轴和原点O的转动惯量 $ I_{x} $， $ I_{y} $， $ I_{z} $和 $ I_{O} $公式分别为