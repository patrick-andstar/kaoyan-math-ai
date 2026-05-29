 $$ \frac{1}{1+\mathbf{D}}=1-\mathbf{D}+\mathbf{D}^{2}+\cdots, $$ 

于是

由于 $ x^{2}+1 $为2次多项式，故 $ \frac{1}{1+D} $展开到2次

 $$ \begin{aligned}y^{*}&=\frac{1}{\mathrm{D}}\bullet\frac{\left(1-\mathrm{D}+\mathrm{D}^{2}\right)}{2}(x^{2}+1)=\left(\frac{1}{\mathrm{D}}-1+\mathrm{D}\right)(x^{2}+1)\\&=\frac{1}{\mathrm{D}}(x^{2}+1)-(x^{2}+1)+\mathrm{D}(x^{2}+1)\\&=\frac{1}{3}x^{3}+x-x^{2}-1+2x=\frac{1}{3}x^{3}-x^{2}+3x-1\end{aligned} $$ 

④ $ \frac{1}{F(D)}e^{ax}v(x) $型.

先将 $ e^{ax} $放到最前面.

 $ y^* = \frac{1}{F(D)} \mathbf{e}^{\alpha x} v(x) = \mathbf{e}^{\alpha x} \cdot \frac{1}{F(D + \alpha)} v(x) $，这里  $ v(x) $ 是实函数。

注例 8 已知  $ y'' + 4y' + 5y = e^{-2x} \sin x $，求  $ y^* $

解

 $$ \begin{aligned}y^{*}&=\frac{1}{\mathrm{D}^{2}+4\mathrm{D}+5}\mathrm{e}^{-2x}\sin x=\mathrm{e}^{-2x}\cdot\frac{1}{(\mathrm{D}-2)^{2}+4(\mathrm{D}-2)+5}\sin x\\&=\mathrm{e}^{-2x}\cdot\frac{1}{\mathrm{D}^{2}+1}\sin x=\mathrm{e}^{-2x}\cdot x\frac{1}{(\mathrm{D}^{2}+1)},\sin x\\&=\mathrm{e}^{-2x}\cdot x\frac{1}{2\mathrm{D}}\sin x=\frac{1}{2}\mathrm{e}^{-2x}\cdot x(-\cos x)=-\frac{1}{2}x\mathrm{e}^{-2x}\cos x.\end{aligned} $$ 

注例 9 已知  $ y'' - 3y' + 2y = 2xe^{x} $，求  $ y^{*} $。综合以上多种方法。

解

 $$ \begin{aligned}y^{*}&=\frac{1}{\mathrm{D}^{2}-3\mathrm{D}+2}2\mathrm{e}^{x}=2\mathrm{e}^{x}\cdot\frac{1}{(\mathrm{D}+1)^{2}-3(\mathrm{D}+1)+2}x=2\mathrm{e}^{x}\cdot\frac{1}{\mathrm{D}^{2}-\mathrm{D}}x\\&=2\mathrm{e}^{x}\cdot\frac{1}{\mathrm{D}}\cdot\frac{1}{\mathrm{D}-1}x=2\mathrm{e}^{x}\cdot\frac{1}{\mathrm{D}}\cdot(-1-\mathrm{D})x=2\mathrm{e}^{x}\cdot\left(-\frac{1}{\mathrm{D}}-1\right)x\\&=2\mathrm{e}^{x}\cdot\left(-\frac{1}{2}x^{2}-x\right)=-x(x+2)\mathrm{e}^{x}\ .\\ \end{aligned} $$ 

(4) 通解.

若  $ y(x)=C_{1}y_{1}(x)+C_{2}y_{2}(x) $ 是  $ y''+py'+qy=0 $ 的通解， $ y^{*}(x) $ 是

 $$ y^{\prime \prime}+p y^{\prime}+q y=f(x) $$ 

的一个特解，则  $ y(x) + y^{*}(x) $ 是  $ y'' + py' + qy = f(x) $ 的通解。

齐通解+非齐特解

例 15.17 求  $ y'' - 3y' + 2y = 2e^{-x} \cos x $ 的通解.