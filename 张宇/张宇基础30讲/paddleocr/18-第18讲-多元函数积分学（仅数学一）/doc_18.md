 $$ I_{z}=\iiint_{\Omega}(x^{2}+y^{2})\rho(x,y,z)\mathrm{d}v,I_{O}=\iiint_{\Omega}(x^{2}+y^{2}+z^{2})\rho(x,y,z)\mathrm{d}v\cdot\underbrace{\mathrm{d}m}_{(x,y,z)}\overbrace{(0,0,z)}^{z} $$ 

(4)对于空间物体，若体密度为  $ \rho(x, y, z) $， $ \Omega $ 是物体所占的空间区域，则  $ r^{2}dm $ 为微元对z轴的转动惯量。计算该物体对物体外一点  $ M_{0}(x_{0}, y_{0}, z_{0}) $ 处的质量为 m 的质点的引力  $ (F_{x}, F_{y}, F_{z}) $ 公式为

 $$ F_{x}=Gm\iiint\limits_{\Omega}\frac{\rho(x,y,z)(x-x_{0})}{\left[\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}+\left(z-z_{0}\right)^{2}\right]^{\frac{3}{2}}}\mathrm{d}v, $$ 

 $$ F_{y}=Gm\iiint\limits_{\Omega}\frac{\rho(x,y,z)\left(y-y_{0}\right)}{\left[\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}+\left(z-z_{0}\right)^{2}\right]^{\frac{3}{2}}}\mathrm{d}\nu, $$ 

 $$ F_{z}=Gm\iiint\limits_{\Omega}\frac{\rho(x,y,z)(z-z_{0})}{\left[(x-x_{0})^{2}+(y-y_{0})^{2}+(z-z_{0})^{2}\right]^{\frac{3}{2}}}\mathrm{d}\nu. $$ 

例 18.6 设  $ \Omega = \{(x, y, z) \mid 4x^2 + y^2 + z^2 - 2z \leq 3\} $，则  $ \iiint_{\Omega} z \, \mathrm{d}v = $ ___.

解 应填  $ \frac{16}{3}\pi $ .  $ x^{2}+\frac{y^{2}}{4}+\frac{(z-1)^{2}}{4}\leq1 $ 为椭球体

由于  $ \Omega=\left\{(x,y,z)\middle|x^{2}+\frac{y^{2}}{4}+\frac{(z-1)^{2}}{4}\leqslant1\right\} $，其形心坐标为  $ (0,0,1) $，于是

 $$ \iiint_{\Omega}z\mathrm{d}v=\overline{z}\cdot V_{\Omega}=1\cdot\frac{4}{3}\cdot\pi\cdot\frac{1}{a}\cdot\frac{2}{b}\cdot\frac{2}{c}=\frac{16}{3}\pi\cdot\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}+\frac{z^{2}}{c^{2}}\leq1 $$ 

例 18.7 设  $ \Omega = \{(x, y, z) \mid x^2 + y^2 \leq z \leq 1\} $，则  $ \Omega $ 的形心的竖坐标  $ \overline{z} = $ ___.

解 应填  $ \frac{2}{3} $



设 $ D=\left\{(x,y)\mid x^{2}+y^{2}\leqslant1\right\} $，则

<div style="text-align: center;"><img src="imgs/img_in_image_box_651_856_946_998.jpg" alt="Image" width="28%" /></div>


 $$ \iiint_{\Omega}\mathrm{d}x\mathrm{d}y\mathrm{d}z=\iint_{D}\mathrm{d}x\mathrm{d}y\int_{x^{2}+y^{2}}^{1}\mathrm{d}z=\iint_{D}(1-x^{2}-y^{2})\mathrm{d}x\mathrm{d}y=\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{1}(1-r^{2})r\mathrm{d}r=\frac{\pi}{2}, $$ 

 $$ \iiint\limits_{Q}z\mathrm{d}x\mathrm{d}y\mathrm{d}z=\iint\limits_{D}\mathrm{d}x\mathrm{d}y\int_{x^{2}+y^{2}}^{1}z\mathrm{d}z=\frac{1}{2}\iint\limits_{D}[1-(x^{2}+y^{2})^{2}]\mathrm{d}x\mathrm{d}y=\frac{1}{2}\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{1}(1-r^{4})r\mathrm{d}r=\frac{\pi}{3}, $$ 

所以  $ \overline{z}=\frac{\iiint\limits_{D}z\mathrm{d}x\mathrm{d}y\mathrm{d}z}{\iiint\limits_{D}\mathrm{d}x\mathrm{d}y\mathrm{d}z}=\frac{2}{3} $