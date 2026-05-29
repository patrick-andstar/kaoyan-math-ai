解 特征方程为  $ r^{2}-3r+2=0 $，其解为  $ r_{1}=2, r_{2}=1 $，因此对应的齐次微分方程的通解是

 $$ \overline{y}=C_{1}\mathbf{e}^{x}+C_{2}\mathbf{e}^{2x}. $$ 

下面用两种方法求特解．

方法一 待定系数法.

方程的一个特解可设为  $ y^* = e^{-x}(A\cos x + B\sin x) $，求得

 $$ y^{*}=\mathrm{e}^{-x}[(B-A)\cos x-(A+B)\sin x], $$ 

 $$ y^{**}=\mathrm{e}^{-x}(-2B\cos x+2A\sin x), $$ 

代入方程解得  $ A=\frac{1}{5} $， $ B=-\frac{1}{5} $，即  $ y^{*}=\frac{e^{-x}}{5}(\cos x-\sin x) $.

方法二 微分算子法.

 $$ \begin{aligned}y^{*}&=\frac{1}{\mathrm{D}^{2}-3\mathrm{D}+2}2\mathrm{e}^{-x}\cos x\\&=2\mathrm{e}^{-x}\frac{1}{(\mathrm{D}-1)^{2}-3(\mathrm{D}-1)+2}\cos x\\&=2\mathrm{e}^{-x}\frac{1}{\mathrm{D}^{2}-5\mathrm{D}+6}\cos x\\&=2\mathrm{e}^{-x}\frac{1}{-5\mathrm{D}+5}\cos x\\&=-\frac{2}{5}\mathrm{e}^{-x}\frac{1}{\mathrm{D}-1}\cos x\\&=-\frac{2}{5}\mathrm{e}^{-x}\frac{\mathrm{D}+1}{\mathrm{D}^{2}-1}\cos x\\&=\frac{1}{5}\mathrm{e}^{-x}(\mathrm{D}+1)\cos x\\&=\frac{1}{5}\mathrm{e}^{-x}(-\sin x+\cos x)\ .\\ \end{aligned} $$ 

从而原方程的通解为

 $$ y=\overline{y}+y^{*}=C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{2x}+\frac{1}{5}\mathrm{e}^{-x}(\cos x-\sin x), $$ 

其中 $ C_{1} $， $ C_{2} $为任意常数.

待定系数法易设出形式，难点在于计算量大，建议考生作为练习尝试书写过程。微分算子法计算量较小，难点在于需记住大量形式。

例 15.18 设二阶常系数线性微分方程  $ y'' + \alpha y' + \beta y = \gamma e^x $ 的一个特解为  $ y^* = e^{2x} + (1 + x)e^x $。确定常数  $ \alpha, \beta, \gamma $，并求该方程的通解。