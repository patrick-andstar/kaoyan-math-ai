 $$  \textcircled{3} \mathrm{d}x\mathrm{d}y\mathrm{d}z\rightarrow\left|\frac{\partial(x,\ y,\ z)}{\partial(u,\ v,\ w)}\right|\mathrm{d}u\mathrm{d}v\mathrm{d}w\xrightarrow{}\xrightarrow{ 类比：\textcircled{1} }\mathrm{d}x\mathrm{d}y=r\mathrm{d}r\mathrm{d}\theta\textcircled{.} $$ 

其中

a. $ \begin{cases}x=x(u,v,w),\\y=y(u,v,w),\\z=z(u,v,w)\end{cases} $是空间 $ (x,y,z) $到空间 $ (u,v,w) $的一一映射；

b.  $ x = x(u, v, w) $,  $ y = y(u, v, w) $,  $ z = z(u, v, w) $ 有一阶连续偏导数，且

 $$ \frac{\partial(x,\;y,\;z)}{\partial(u,\;v,\;w)}=\begin{vmatrix}\frac{\partial x}{\partial u}&\frac{\partial x}{\partial v}&\frac{\partial x}{\partial w}\\ \frac{\partial y}{\partial u}&\frac{\partial y}{\partial v}&\frac{\partial y}{\partial w}\\ \frac{\partial z}{\partial u}&\frac{\partial z}{\partial v}&\frac{\partial z}{\partial w}\end{vmatrix}\neq0. $$ 

柱面坐标系

另外，令 $ \begin{cases}x=r\cos\theta,\\y=r\sin\theta,\\z=z,\end{cases} $则

 $$ \begin{aligned}\iiint\limits_{\Omega_{y\theta z}}f(x,y,z)\mathrm{d}x\mathrm{d}y\mathrm{d}z=&\iiint\limits_{\Omega_{z\theta z}}f(r\cos\theta,r\sin\theta,z)\left|\begin{matrix}\frac{\partial(x,y,z)}{\partial(r,\theta,z)}\\\end{matrix}\right|\mathrm{d}r\mathrm{d}\theta\mathrm{d}z\\=&\iiint\limits_{\Omega_{z\theta z}}f(r\cos\theta,r\sin\theta,z)\left|\begin{matrix}\frac{\partial x}{\partial r}&\frac{\partial x}{\partial\theta}&\frac{\partial x}{\partial z}\\\frac{\partial y}{\partial r}&\frac{\partial y}{\partial\theta}&\frac{\partial y}{\partial z}\\\frac{\partial z}{\partial r}&\frac{\partial z}{\partial\theta}&\frac{\partial z}{\partial z}\\\end{matrix}\right|\mathrm{d}r\mathrm{d}\theta\mathrm{d}z\\=&\iiint\limits_{\Omega_{z\theta z}}f(r\cos\theta,r\sin\theta,z)\left|\begin{matrix}\cos\theta&-r\sin\theta&0\\\sin\theta&r\cos\theta&0\\0&0&1\\\end{matrix}\right|\mathrm{d}r\mathrm{d}\theta\mathrm{d}z\\=&\iiint\limits_{\Omega_{z\theta z}}f(r\cos\theta,r\sin\theta,z)r\mathrm{d}r\mathrm{d}\theta\mathrm{d}z.\end{aligned} $$ 

这就是直角坐标系到柱面坐标系的换元过程.

令 $ \begin{cases}x=r\sin\varphi\cos\theta,\\y=r\sin\varphi\sin\theta,\\z=r\cos\varphi,\end{cases} $则

 $$ \iiint\limits_{\Omega_{xyz}}f(x,y,z)\mathrm{d}x\mathrm{d}y\mathrm{d}z=\iiint\limits_{\Omega_{r\theta p}}f(r\sin\varphi\cos\theta,r\sin\varphi\sin\theta,r\cos\varphi)\left|\frac{\partial(x,y,z)}{\partial(r,\theta,\varphi)}\right|\mathrm{d}r\mathrm{d}\varphi\mathrm{d}\theta $$ 