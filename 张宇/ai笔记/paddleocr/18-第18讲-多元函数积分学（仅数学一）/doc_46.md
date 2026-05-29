注证 因为

 $$ \begin{aligned}\boldsymbol{n}=&“\pm\frac{1}{\sqrt{1+\left(\frac{\partial z}{\partial x}\right)^{2}+\left(\frac{\partial z}{\partial y}\right)^{2}}}\left(-\frac{\partial z}{\partial x},-\frac{\partial z}{\partial y},1\right),\\\mathrm{d}S=&\sqrt{1+\left(\frac{\partial z}{\partial x}\right)^{2}+\left(\frac{\partial z}{\partial y}\right)^{2}}\mathrm{d}x\mathrm{d}y,\end{aligned} $$ 

并记  $  F = (P, Q, R)  $， $  \mathrm{d}S = (\mathrm{d}y \mathrm{d}z, \mathrm{d}z \mathrm{d}x, \mathrm{d}x \mathrm{d}y)  $，则

 $$ \begin{aligned}\iint_{\Sigma}P\mathrm{d}y\mathrm{d}z+Q\mathrm{d}z\mathrm{d}x+R\mathrm{d}x\mathrm{d}y=&\iint_{\Sigma}F(x,y,z)\bullet\mathrm{d}S=\iint_{\Sigma}F(x,y,z)\bullet\boldsymbol{n}\mathrm{d}S\\=&\iint_{\Sigma}(P,Q,R)\bullet\left[“\pm\frac{1}{\sqrt{1+\left(\frac{\partial z}{\partial x}\right)^{2}+\left(\frac{\partial z}{\partial y}\right)^{2}}}\left(-\frac{\partial z}{\partial x},-\frac{\partial z}{\partial y},1\right)\right]\mathrm{d}S\\=&“\pm”\iint_{D}\left(-P\frac{\partial z}{\partial x}-Q\frac{\partial z}{\partial y}+R\right)\mathrm{d}x\mathrm{d}y,\end{aligned} $$ 

其中，“±”的选取显然就是前述①的情形。

例 18.25 设  $ \Sigma $ 为曲面  $ z = x^2 + y^2 (z \leq 1) $ 的上侧，计算曲面积分

 $$ I=\iint\limits_{\Sigma}(x-1)^{3}\mathrm{d}y\mathrm{d}z+(y-1)^{3}\mathrm{d}z\mathrm{d}x+(z-1)\mathrm{d}x\mathrm{d}y. $$ 

解 曲面Σ在xOy坐标面上投影域为 $ D=\left\{(x,y)\mid x^{2}+y^{2}\leq1\right\} $.因为 $ \frac{\partial z}{\partial x}=2x $， $ \frac{\partial z}{\partial y}=2y $，所以

 $$ \begin{aligned}I=&\iint\limits_{\Sigma}(x-1)^{3}\mathrm{d}y\mathrm{d}z+(y-1)^{3}\mathrm{d}z\mathrm{d}x+(z-1)\mathrm{d}x\mathrm{d}y\\=&\iint\limits_{D}\Big[(x-1)^{3}\bullet(-2x)+(y-1)^{3}\bullet(-2y)+(x^{2}+y^{2}-1)\Big]\mathrm{d}x\mathrm{d}y\\=&-\iint\limits_{D}(2x^{4}-6x^{3}+5x^{2}-2x+2y^{4}-6y^{3}+5y^{2}-2y+1)\mathrm{d}x\mathrm{d}y.\end{aligned} $$ 

因为区域D关于坐标轴对称，所以 $ \iint_{D}(-6x^{3}-2x-6y^{3}-2y)dxdy=0 $，从而

 $$ \begin{aligned}I=&-\iint\limits_{D}(2x^{4}+5x^{2}+2y^{4}+5y^{2}+1)\mathrm{d}x\mathrm{d}y\\=&-\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{1}\Big[2r^{4}(\cos^{4}\theta+\sin^{4}\theta)+5r^{2}+1\Big]r\mathrm{d}r\end{aligned} $$ 