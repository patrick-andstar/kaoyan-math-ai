 $$ n=\pm\frac{1}{\sqrt{1+\left(\frac{\partial z}{\partial x}\right)^{2}+\left(\frac{\partial z}{\partial y}\right)^{2}}}\left(-\frac{\partial z}{\partial x},-\frac{\partial z}{\partial y},1\right) $$ 

当上侧为正时，取“+”；下侧为正时，取“-”。（上正下负）

注 同理，设  $ \Sigma: y = y(x, z) $，其中  $ y $ 有一阶连续偏导数，则

 $$ n=\pm\frac{1}{\sqrt{1+\left(\frac{\partial y}{\partial x}\right)^{2}+\left(\frac{\partial y}{\partial z}\right)^{2}}}\left(-\frac{\partial y}{\partial x},1,-\frac{\partial y}{\partial z}\right), $$ 

当右侧为正时，取“+”；左侧为正时，取“-”。（右正左负）

设  $ \Sigma: x = x(y, z) $，其中  $ x $ 有一阶连续偏导数，则

 $$ n=“\pm\frac{1}{\sqrt{1+\left(\frac{\partial x}{\partial y}\right)^{2}+\left(\frac{\partial x}{\partial z}\right)^{2}}}\left(1,-\frac{\partial x}{\partial y},-\frac{\partial x}{\partial z}\right), $$ 

当前侧为正时，取“+”；后侧为正时，取“-”。（前正后负）

例 18.23 已知曲面  $ \Sigma: z = \sqrt{x^2 + y^2} $，下侧为正，求其正向单位法向量。

解 因为  $ \frac{\partial z}{\partial x} = \frac{x}{\sqrt{x^{2} + y^{2}}} $， $ \frac{\partial z}{\partial y} = \frac{y}{\sqrt{x^{2} + y^{2}}} $，且下侧为正，所以其正向单位法向量为

 $$ n=-\frac{1}{\sqrt{1+\left(\frac{\partial z}{\partial x}\right)^{2}+\left(\frac{\partial z}{\partial y}\right)^{2}}}\left(-\frac{\partial z}{\partial x},-\frac{\partial z}{\partial y},1\right)=\frac{\sqrt{2}}{2}\left(\frac{x}{\sqrt{x^{2}+y^{2}}},\frac{y}{\sqrt{x^{2}+y^{2}}},-1\right) $$ 

例 18.24 若柱面  $ \Sigma: x^{2} + y^{2} = 1 $ 的外侧为正，求其后半柱面正向单位法向量。

解 后半柱面，后侧为正， $ x = -\sqrt{1 - y^{2}} $， $ n = -\sqrt{1 - y^{2}}\left(1, -\frac{y}{\sqrt{1 - y^{2}}}, 0\right) $.

②转换投影定理.

设曲面  $ \Sigma: z = z(x, y) $，z 有一阶连续偏导数，且  $ P(x, y, z) $， $ Q(x, y, z) $， $ R(x, y, z) $ 在  $ \Sigma $ 上连续，则

 $$ \begin{aligned}&\iint\limits_{\Sigma}P(x,y,z)\mathrm{d}y\mathrm{d}z+Q(x,y,z)\mathrm{d}z\mathrm{d}x+R(x,y,z)\mathrm{d}x\mathrm{d}y\\=&“\pm”\iint\limits_{D}\left(-P\frac{\partial z}{\partial x}-Q\frac{\partial z}{\partial y}+R\right)\mathrm{d}x\mathrm{d}y\ ,\end{aligned} $$ 

其中  $ P = P[x, y, z(x, y)] $， $ Q = Q[x, y, z(x, y)] $， $ R = R[x, y, z(x, y)] $。