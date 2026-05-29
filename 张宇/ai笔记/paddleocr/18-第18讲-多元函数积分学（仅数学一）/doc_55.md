根据斯托克斯公式，得

 $$ \begin{aligned}\oint_{L}xz\mathrm{d}x+x\mathrm{d}y+\frac{y^{2}}{2}\mathrm{d}z=&\iint_{s}\begin{vmatrix}-\frac{1}{\sqrt{3}}&-\frac{1}{\sqrt{3}}&\frac{1}{\sqrt{3}}\\\frac{\partial}{\partial x}&\frac{\partial}{\partial y}&\frac{\partial}{\partial z}\\x z&x&\frac{y^{2}}{2}\end{vmatrix}\mathrm{d}S\\=&\iint_{s}\frac{1}{\sqrt{3}}(1-x-y)\mathrm{d}S\\=&\iint_{\partial}\frac{1}{\sqrt{3}}(1-x-y)\sqrt{3}\mathrm{d}x\mathrm{d}y=\pi.\end{aligned} $$ 

18.4  $ \frac{1}{2}\pi a^{2} $ 解 先将 L 的方程  $ x^{2} + y^{2} = a^{2} $ 代入，得

 $$ \begin{aligned} 原式 &=\frac{1}{a^{2}}\oint_{L}\left(\mathrm{e}^{x^{2}}-x^{2}y\right)\mathrm{d}x+\left(xy^{2}-\sin y^{2}\right)\mathrm{d}y\\&=\frac{1}{a^{2}}\iint_{x^{2}+y^{2}\leqslant a^{2}}\left(x^{2}+y^{2}\right)\mathrm{d}x\mathrm{d}y=\frac{1}{a^{2}}\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{a}r^{2}\bullet r\mathrm{d}r=\frac{1}{2}\pi a^{2}\ .\end{aligned} $$ 

18.5  $ \frac{16\pi}{3} $ 分析 本题考查关于轮换对称性的判断.

①函数xz在Σ的8个卦限内，4正4负，且对应点有相同的绝对值，故 $ \oint_{\Sigma}xz\,dS=0 $；

②根据轮换对称性得到  $ \oint_{\Sigma} x^{2} \mathrm{d}S = \oint_{\Sigma} y^{2} \mathrm{d}S = \oint_{\Sigma} z^{2} \mathrm{d}S $.

解  $ \iint_{\Sigma}x(4x-z)\mathrm{d}S=\iint_{\Sigma}4x^{2}\mathrm{d}S=\frac{4}{3}\iint_{\Sigma}(x^{2}+y^{2}+z^{2})\mathrm{d}S=\frac{4}{3}\iint_{\Sigma}\mathrm{d}S=\frac{16\pi}{3} $

18.6  $ \frac{4}{3}\sqrt{3} $ 解 曲面Σ对称于yOz平面，x为关于x的奇函数，所以 $ \oint_{\Sigma}x\mathrm{d}S=0 $ 。又因Σ关于x，y，z轮换对称，所以

 $$ \begin{aligned}\oint_{\Sigma}\left|y\right|\mathrm{d}S=\oint_{\Sigma}\left|z\right|\mathrm{d}S=\oint_{\Sigma}\left|x\right|\mathrm{d}S,\end{aligned} $$ 

 $$ \begin{aligned}\oint_{\Sigma}|y|\mathrm{d}S&=\frac{1}{3}\oint_{\Sigma}(|x|+|y|+|z|)\mathrm{d}S=\frac{1}{3}\oint_{\Sigma}\mathrm{d}S\\&=\frac{1}{3}\times A_{\Sigma},\end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_751_1098_960_1275.jpg" alt="Image" width="20%" /></div>


其中  $ A_{\Sigma} $ 为  $ \Sigma $ 的面积。而  $ \Sigma $ 由 8 块同样的等边三角形组成，每块等边三角形的边长为  $ \sqrt{2} $，所以

 $$ A_{\Sigma}=8\times\frac{1}{2}\times(\sqrt{2})^{2}\times\sin\frac{\pi}{3}=4\sqrt{3}, $$ 