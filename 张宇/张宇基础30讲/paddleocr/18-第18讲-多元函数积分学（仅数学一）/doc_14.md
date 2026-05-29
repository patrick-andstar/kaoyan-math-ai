于是

 $$ \begin{aligned}\iiint\limits_{\Omega}f(x,y,z)\mathrm{d}v=&\iiint\limits_{\Omega}f(\underline{r\sin\varphi\cos\theta},r\sin\varphi\sin\theta,r\cos\varphi)\underline{r^{2}\sin\varphi}\mathrm{d}r\mathrm{d}\varphi\mathrm{d}\theta\\=&\int_{\theta}^{\theta_{2}}\mathrm{d}\theta\int_{\varphi_{1}(\theta)}^{\varphi_{2}(\theta)}\mathrm{d}\varphi\int_{\eta(\varphi,\theta)}^{\eta_{2}(\varphi,\theta)}f(r\sin\varphi\cos\theta,r\sin\varphi\sin\theta,r\cos\varphi)r^{2}\sin\varphi\mathrm{d}r.\end{aligned} $$ 

例 18.3 设  $ \Omega = \{(x, y, z) \mid x^2 + y^2 + z^2 \leq 1\} $，则  $ \iiint_{\Omega} z^2 \, dx \, dy \, dz = $ ___.

解 应填 $ \frac{4\pi}{15} $

由轮换对称性可知， $ \iiint_{\Omega}z^{2}\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z=\iiint_{\Omega}x^{2}\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z=\iiint_{\Omega}y^{2}\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z $，所以

 $$ \begin{aligned}\iiint_{\Omega}z^{2}\mathrm{d}x\mathrm{d}y\mathrm{d}z=&\frac{1}{3}\iiint_{\Omega}(x^{2}+y^{2}+z^{2})\mathrm{d}x\mathrm{d}y\mathrm{d}z=\frac{1}{3}\bullet\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{\pi}\mathrm{d}\varphi\int_{0}^{1}r^{2}\bullet r^{2}\sin\varphi\mathrm{d}r\\=&\frac{2\pi}{3}\int_{0}^{\pi}\sin\varphi\mathrm{d}\varphi\int_{0}^{1}r^{4}\mathrm{d}r=\frac{4\pi}{15}\ .\end{aligned} $$ 

例 18.4 设  $ \Omega = \left\{ (x, y, z) \middle| \sqrt{x^2 + y^2} \leq z \leq 1 \right\} $，则  $ \iiint_{\Omega} \frac{1}{\sqrt{x^2 + y^2 + z^2}} \, \mathrm{d}v = \_\_\_\_\_\_ . $

解 应填 $ (\sqrt{2}-1)\pi $

如图 18-8 所示，从原点引射线穿过  $ \Omega $，从 z=1 穿出，即  $ r\cos\varphi=1 $，则  $ r=\frac{1}{\cos\varphi} $ 为上限，于是

<div style="text-align: center;"><img src="imgs/img_in_image_box_793_756_934_924.jpg" alt="Image" width="13%" /></div>


<div style="text-align: center;">图 18-8</div>


 $$ \begin{aligned}&I=\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{\frac{\pi}{4}}\mathrm{d}\varphi\int_{0}^{\frac{1}{\cos\varphi}}\frac{1}{r}\cdot r^{2}\sin\varphi\mathrm{d}r=2\pi\int_{0}^{\frac{\pi}{4}}\frac{1}{2}r^{2}\bigg|_{0}^{\frac{1}{\cos\varphi}}\cdot\sin\varphi\mathrm{d}\varphi\\ &\\&=\pi\int_{0}^{\frac{\pi}{4}}\frac{1}{\cos^{2}\varphi}\cdot\sin\varphi\mathrm{d}\varphi=-\pi\int_{0}^{\frac{\pi}{4}}\frac{1}{\cos^{2}\varphi}\mathrm{d}(\cos\varphi)=\pi\cdot\frac{1}{\cos\varphi}\bigg|_{0}^{\frac{\pi}{4}}=(\sqrt{2}-1)\pi.\\ \end{aligned} $$ 

(4) 换元法.

 $$ \iiint\limits_{\Omega_{xy z}}\boldsymbol{f}(x,y,z)\mathrm{d}x\mathrm{d}y\mathrm{d}z $$ 

 $$ \begin{aligned}&x,y,z 换为 \left\{\begin{aligned}&x=x(u,v,w)\\ &\frac{y=y(u,v,w)}{z=z(u,v,w)}\end{aligned}\right.\iiint f[x(u,v,w),y(u,v,w),z(u,v,w)]\left.\begin{aligned} 古怪的 &\Omega_{yz}\rightarrow 常规的 &\Omega_{ww}\end{aligned}\right.\rightarrow 雅可比行列式 \\ &u,v,w\end{aligned} $$ 

① $ f(x,y,z)\rightarrow f[x(u,v,w),y(u,v,w),z(u,v,w)] $

②  $ \iint_{\Omega} \rightarrow \iiint_{\Omega} $