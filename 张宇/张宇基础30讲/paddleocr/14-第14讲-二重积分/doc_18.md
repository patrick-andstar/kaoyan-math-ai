∅公式  $ \int\cos\theta\,d\theta=\sin\theta+C $， $ \int\sin\theta\,d\theta=-\cos\theta+C $。

## 4 换元法

二重积分亦有和定积分一脉相承的换元法，有时很有用，现介绍于此，供参考，若能够用上，可直接使用，不必证明。

先回顾一元函数积分换元法，见“ $ ① $”，再看二重积分换元法，见“ $ ② $”。

① $ \int_{a}^{b}f(x)\mathrm{d}x\xlongequal{x=\varphi(t)}\int_{\alpha}^{\beta}f[\varphi(t)]\varphi'(t)\mathrm{d}t $

a.  $ f(x) \to f[\varphi(t)] $

b.  $ \int_{a}^{b} \to \int_{\alpha}^{\beta} $

c.  $ \mathrm{d}x \to \varphi'(t)\mathrm{d}t $

注意： $ x=\varphi(t) $ 单调，存在一阶连续导数.

 $$ \iint\limits_{D_{xy}}f(x,y)\mathrm{d}x\mathrm{d}y\xlongequal{x=x(u,v)}\iint\limits_{D_{yz}}f[x(u,v),y(u,v)]\left|\frac{\partial(x,y)}{\partial(u,v)}\right|\mathrm{d}u\mathrm{d}v $$ 

a.  $  f(x, y) \to f[x(u, v), y(u, v)]  $.

b.  $ \iint_{D_{xy}} \rightarrow \iint_{D_{yz}}  $.

c.  $ \mathrm{dxdy} \rightarrow \left| \frac{\partial(x, y)}{\partial(u, v)} \right| \mathrm{dudv} $

J行列式的绝对值

注意：其中 $ \left\{\begin{aligned}x=x(u,v),\\ y=y(u,v)\end{aligned}\right. $是 $ (x,y) $面到 $ (u,v) $面的一对一映射， $ x=x(u,v) $， $ y=y(u,v) $存在一阶连

续偏导数， $ \frac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}\frac{\partial x}{\partial u}&\frac{\partial x}{\partial v}\\ \frac{\partial y}{\partial u}&\frac{\partial y}{\partial v}\end{vmatrix}\neq0 $

二阶行列式，称为J行列式

另外，令 $ \begin{cases}x=r\cos\theta,\\y=r\sin\theta,\end{cases} $则

 $$ \begin{aligned}&\iint\limits_{D_{xy}}f(x,y)\mathrm{d}x\mathrm{d}y=\iint\limits_{D_{xy}}f(r\cos\theta,r\sin\theta)\left\|\begin{matrix}\frac{\partial x}{\partial r}&\frac{\partial x}{\partial\theta}\\ \frac{\partial y}{\partial r}&\frac{\partial y}{\partial\theta}\end{matrix}\right\|\mathrm{d}r\mathrm{d}\theta\quad\text{“换元法”}\\ &\\ =&\iint\limits_{D_{xy}}f(r\cos\theta,r\sin\theta)\left\|\begin{matrix}\cos\theta&-r\sin\theta\\ \sin\theta&r\cos\theta\end{matrix}\right\|\mathrm{d}r\mathrm{d}\theta=\iint\limits_{D_{xy}}f(r\cos\theta,r\sin\theta)r\mathrm{d}r\mathrm{d}\theta.\\ \end{aligned} $$ 

这就是直角坐标系到极坐标系的换元过程。