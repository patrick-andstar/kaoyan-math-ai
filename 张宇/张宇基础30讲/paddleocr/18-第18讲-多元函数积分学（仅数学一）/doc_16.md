 $$ \begin{aligned}&=\iiint\limits_{\Omega,\partial\rho}f(r\sin\varphi\cos\theta,r\sin\varphi\sin\theta,r\cos\varphi)\begin{vmatrix}\frac{\partial x}{\partial r}&\frac{\partial x}{\partial\theta}&\frac{\partial x}{\partial\varphi}\\\frac{\partial y}{\partial r}&\frac{\partial y}{\partial\theta}&\frac{\partial y}{\partial\varphi}\\\frac{\partial z}{\partial r}&\frac{\partial z}{\partial\theta}&\frac{\partial z}{\partial\varphi}\end{vmatrix}\mathrm{d}r\mathrm{d}\varphi\mathrm{d}\theta\\&=\iiint\limits_{\Omega,r\partial\rho}f(r\sin\varphi\cos\theta,r\sin\varphi\sin\theta,r\cos\varphi)\bullet\begin{vmatrix}\sin\varphi\cos\theta&-r\sin\varphi\sin\theta&r\cos\varphi\cos\theta\\\sin\varphi\sin\theta&r\sin\varphi\cos\theta&r\cos\varphi\sin\theta\\\cos\varphi&0&-r\sin\varphi\end{vmatrix}\mathrm{d}r\mathrm{d}\varphi\mathrm{d}\theta\\&=\iiint\limits_{\Omega,\partial\rho}f(r\sin\varphi\cos\theta,r\sin\varphi\sin\theta,r\cos\varphi)r^{2}\sin\varphi\mathrm{d}r\mathrm{d}\varphi\mathrm{d}\theta.\end{aligned} $$ 

这就是直角坐标系到球面坐标系的换元过程.

例 18.5 设  $ \Omega = \{(x, y, z) \mid x^2 + 4y^2 + z^2 \leq 1\} $，则  $ I = \iiint\limits_O (1 - x^2 - 4y^2 - z^2) \, dx \, dy \, dz = $ ___.

 $$ x^{2}+\frac{y^{2}}{\frac{1}{4}}+z^{2}\leq1 为椭球体 $$ 

分析 令  $ \left\{\begin{aligned} x &= x_{1}, \\ 2y &= y_{1}, \\ z &= z_{1}, \end{aligned}\right. $ 则  $ \iiint_{x^{2}+4y^{2}+z^{2}\leq1}(1-x^{2}-4y^{2}-z^{2})\mathrm{d}x\mathrm{d}y\mathrm{d}z = \iiint_{x_{1}^{2}+y_{1}^{2}+z_{1}^{2}\leq1}(1-x_{1}^{2}-y_{1}^{2}-z_{1}^{2})\mathrm{d}x_{1}\cdot\frac{1}{2}\mathrm{d}y_{1}\mathrm{d}z. $

<div style="text-align: center;"><img src="imgs/img_in_image_box_198_745_840_886.jpg" alt="Image" width="62%" /></div>


解 应填 $ \frac{4\pi}{15} $.

令

 $$ \begin{cases}x=r\sin\varphi\cos\theta,\\y=\frac{1}{2}r\sin\varphi\sin\theta,\\z=r\cos\varphi,\end{cases} $$ 

于是

 $$ J=\frac{\partial(x,\ y,\ z)}{\partial(r,\ \theta,\ \varphi)}=\begin{vmatrix}\frac{\partial x}{\partial r}&\frac{\partial x}{\partial\theta}&\frac{\partial x}{\partial\varphi}\\ \frac{\partial y}{\partial r}&\frac{\partial y}{\partial\theta}&\frac{\partial y}{\partial\varphi}\\ \frac{\partial z}{\partial r}&\frac{\partial z}{\partial\theta}&\frac{\partial z}{\partial\varphi}\end{vmatrix}=-\frac{1}{2}r^{2}\sin\varphi, $$ 

则