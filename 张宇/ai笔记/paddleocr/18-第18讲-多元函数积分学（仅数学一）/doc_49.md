 $$ \oint_{\Sigma}P\mathrm{d}y\mathrm{d}z+Q\mathrm{d}z\mathrm{d}x+R\mathrm{d}x\mathrm{d}y=\oint_{\Sigma}P\mathrm{d}y\mathrm{d}z+Q\mathrm{d}z\mathrm{d}x+R\mathrm{d}x\mathrm{d}y $$ 

 $$ \Sigma $$ 

如果后一积分比前一积分容易计算，就达到化难为易的目的了.

 $$ =\varepsilon^{2} $$ 

例18.28 设Σ是椭球面 $ \frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1 $，法向量指向外侧，则 $ \iint_{\Sigma}\frac{xdydz+ydzdx+zdxdy}{(x^2+y^2+z^2)^{3/2}}= $

(2)分析与格林公式的挖洞法是一样的，除奇点外，通量全是零，包围奇点的任一曲面的积分都是相等的.

解 应填 $ 4\pi $

经计算有

 $$ \frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}\equiv0,\mathrm{ 当 }\left(x,y,z\right)\neq\left(0,0,0\right)\text{．} $$ 

但是这里不能用高斯公式，因为在  $ \Sigma $ 内部的点  $ O(0,0,0) $ 处，P, Q, R 都不连续，故在  $ \Sigma $ 内部作一球面

 $$ \Sigma_{1}\colon x^{2}+y^{2}+z^{2}=r^{2}(r>0)\;, $$ 

它的法向量指向球面外侧，于是有

<div style="text-align: center;"><img src="imgs/img_in_image_box_847_596_949_673.jpg" alt="Image" width="9%" /></div>


 $$ \begin{aligned}&\oint_{\Sigma}\frac{x\mathrm{d}y\mathrm{d}z+y\mathrm{d}z\mathrm{d}x+z\mathrm{d}x\mathrm{d}y}{\left(x^{2}+y^{2}+z^{2}\right)^{3/2}}\\=&\oint_{\Sigma_{1}}\frac{x\mathrm{d}y\mathrm{d}z+y\mathrm{d}z\mathrm{d}x+z\mathrm{d}x\mathrm{d}y}{\left(x^{2}+y^{2}+z^{2}\right)^{3/2}}\\=&\frac{1}{r^{3}}\oint_{\Sigma_{1}}x\mathrm{d}y\mathrm{d}z+y\mathrm{d}z\mathrm{d}x+z\mathrm{d}x\mathrm{d}y\\=&\frac{\left(*\right)}{r^{3}}\iiint_{\Omega_{1}}3\mathrm{d}v=\frac{1}{r^{3}}\bullet3\bullet\frac{4}{3}\pi r^{3}=4\pi\ ,\end{aligned} $$ 

其中 $ ^{*} $处来自高斯公式， $ \Omega_{1} $为 $ \Sigma_{1} $所包围的闭球域.

☑ 方法总结 挖洞后利用高斯公式，在包围奇点的任一曲面上的积分都是相等的。

例 18.29 计算

 $$ \begin{aligned}I=&\oint\limits_{x}\left|xy\right|z^{2}\mathrm{d}x\mathrm{d}y+\left|x\right|y^{2}z\mathrm{d}y\mathrm{d}z\text{,}& 在平面 z=1 和曲面 z=x^{2}+y^{2} 上 .\\ & 由通量的概念可得 \oint\left|x\right|y^{2}z\mathrm{d}y\mathrm{d}z=0\end{aligned} $$ 

 $$ z=x^{2}+y^{2} $$ 

由通量的概念可得  $ \oint_{L}\left|x\right|y^{2}z\,dy\,dz=0 $

(♂分析) 这个题稍难，但并非难题，可以利用概念解题，一个卦限的通量×4即可。

 $$ I=4\left(\iint\limits_{\Sigma_{1}}+\iint\limits_{\Sigma_{2}}\right) $$ 