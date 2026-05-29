 $$ \begin{aligned}I&=\int_{L}(y+z)\mathrm{d}x+(z^{2}-x^{2}+y)\mathrm{d}y+x^{2}y^{2}\mathrm{d}z\\&=\int_{\frac{\pi}{2}}^{\frac{\pi}{2}}[\left(\sqrt{2}\sin t+\cos t\right)\bullet\left(-\sin t\right)+\sqrt{2}\sin t\bullet\sqrt{2}\cos t+\cos^{2}t\bullet2\sin^{2}t\bullet\left(-\sin t\right)]\mathrm{d}t\\&=\int_{\frac{\pi}{2}}^{\frac{\pi}{2}}(-\sqrt{2}\sin^{2}t)\mathrm{d}t=\int_{\frac{\pi}{2}}^{\frac{\pi}{2}}\sqrt{2}\sin^{2}t\mathrm{d}t\\&=2\sqrt{2}\int_{0}^{\frac{\pi}{2}}\sin^{2}t\mathrm{d}t=2\sqrt{2}\bullet\frac{1}{2}\bullet\frac{\pi}{2}=\frac{\sqrt{2}}{2}\pi.\\ \end{aligned} $$ 

方法二 设  $ L_1 $ 是从点  $ B $ 到点  $ A $ 的直线段， $ \Sigma $ 为平面  $ z = x $ 上由  $ L $ 与  $ L_1 $ 围成的半圆面下侧，其法向量的方向余弦为  $ \left(\frac{1}{\sqrt{2}}, 0, -\frac{1}{\sqrt{2}}\right) $，且在  $ L $ 与  $ L_1 $ 上，均有  $ z^2 - x^2 = 0 $。

由斯托克斯公式，

 $$ \begin{aligned}&\oint_{L+L_{1}}(y+z)\mathrm{d}x+(z^{2}-x^{2}+y)\mathrm{d}y+x^{2}y^{2}\mathrm{d}z\\=&\iint\limits_{x}\left|\begin{matrix}\displaystyle\frac{1}{\sqrt{2}}&0&-\displaystyle\frac{1}{\sqrt{2}}\\\displaystyle\frac{\partial}{\partial x}&\displaystyle\frac{\partial}{\partial y}&\displaystyle\frac{\partial}{\partial z}\\y+z&y&x^{2}y^{2}\\\end{matrix}\right|\mathrm{d}S=\displaystyle\frac{1}{\sqrt{2}}\iint\limits_{\Sigma}(2x^{2}y+1)\mathrm{d}S.\end{aligned} $$ 

因为曲面Σ关于xOz平面对称，所以 $ \iint_{\Sigma}2x^{2}ydS=0 $，故

 $$ \oint_{L+L_{1}}(y+z)\mathrm{d}x+(z^{2}-x^{2}+y)\mathrm{d}y+x^{2}y^{2}\mathrm{d}z=\frac{1}{\sqrt{2}}\iint_{\Sigma}\mathrm{d}S=\frac{\sqrt{2}}{2}\pi. $$ 

 $ L_{1} $ 的参数方程为 x=0, y=y, z=0 (y从  $ -\sqrt{2} $ 到  $ \sqrt{2} $), 所以

 $$ \int_{L_{1}}(y+z)\mathrm{d}x+(z^{2}-x^{2}+y)\mathrm{d}y+x^{2}y^{2}\mathrm{d}z=\int_{-\sqrt{2}}^{\sqrt{2}}y\mathrm{d}y=0 $$ 

因此 $ I=\oint_{L+L_{1}}-\int_{L_{1}}=\frac{\sqrt{2}}{2}\pi $

方法三 如图 18-27 所示，在点  $ (x, y, z) $ 和  $ (x, -y, z) $ 处的三个方向的通量分别为

 $$ (y+z)\mathrm{d}x,\;(-y+z)(-\mathrm{d}x), $$ 

 $$ y(-\mathrm{d}y),(-y)(-\mathrm{d}y), $$ 

 $$ x^{2}y^{2}\mathrm{d}z,x^{2}y^{2}(-\mathrm{d}z). $$ 

于是

 $$ I=\int_{L}y\mathrm{d}x\xlongequal{ 由方法一 }\int_{\frac{\pi}{2}}^{-\frac{\pi}{2}}\sqrt{2}\sin t\mathrm{d}(\cos t)=2\sqrt{2}\int_{0}^{\frac{\pi}{2}}\sin^{2}t\mathrm{d}t=2\sqrt{2}\cdot\frac{1}{2}\cdot\frac{\pi}{2}=\frac{\sqrt{2}}{2}\pi $$ 