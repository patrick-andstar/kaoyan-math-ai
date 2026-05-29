例 14.15 设平面区域  $ D=\left\{(x,y)\mid0\leq x\leq1-y,0\leq y\leq1\right\} $，计算二重积分  $ \iint_{D}e^{\frac{y}{x+y}}d\sigma $.

♀分析 虽然积分区域简单，但是无论是先积x，还是先积y，都比较困难。若考虑极坐标系，由于积分区域是三角形，计算量也很大，主要是e的指数为 $ \frac{y}{x+y} $，造成“头重脚轻”。可以考虑换元，令 $ \begin{cases} x+y=u, \\ y=v, \end{cases} $则 $ \frac{y}{x+y} $就变为 $ \frac{v}{u} $，此时积分区域变为另一个三角形区域，被积函数也变得简单。

解 令  $ \begin{cases} x + y = u, \\ y = v, \end{cases} $ 则  $ \begin{cases} x = u - v, \\ y = v, \end{cases} $

 $$ J=\begin{vmatrix}\frac{\partial x}{\partial u}&\frac{\partial x}{\partial v}\\ \frac{\partial y}{\partial u}&\frac{\partial y}{\partial v}\end{vmatrix}=\begin{vmatrix}1&-1\\ 0&1\end{vmatrix}=1, $$ 

且由 $ \begin{cases}0\leqslant x\leqslant1-y,\\0\leqslant y\leqslant1,\end{cases} $知 $ \begin{cases}v\leqslant u\leqslant1,\\0\leqslant v\leqslant1,\end{cases} $如图14-10所示.故

<div style="text-align: center;"><img src="imgs/img_in_image_box_791_485_941_591.jpg" alt="Image" width="14%" /></div>


<div style="text-align: center;">图 14-10</div>


 $$ \begin{aligned}I=&\iint\limits_{D}\mathbf{e}^{\frac{y}{x+y}}\mathrm{d}\sigma=\iint\limits_{D_{uv}}\mathbf{e}^{\frac{y}{u}}\mid J\mid\mathrm{d}u\mathrm{d}v=\int_{0}^{1}\mathrm{d}u\int_{0}^{u}\mathbf{e}^{\frac{y}{u}}\mathrm{d}v\\=&\int_{0}^{1}u\mathbf{e}^{\frac{y}{u}}\bigg|_{\nu=0}^{\nu=u}\mathrm{d}u=\int_{0}^{1}u(\mathbf{e}-1)\mathrm{d}u=\frac{1}{2}(\mathbf{e}-1).\end{aligned} $$ 

注 此题亦可用常规方法（极坐标系，见图 14-11）求解：

 $$ \begin{aligned}I=&\int_{0}^{\frac{\pi}{2}}\mathrm{d}\theta\int_{0}^{\frac{1}{\cos\theta+\sin\theta}}\mathrm{e}^{\frac{\sin\theta}{\cos\theta+\sin\theta}}r\mathrm{d}r\\=&\int_{0}^{\frac{\pi}{2}}\mathrm{e}^{\frac{\sin\theta}{\cos\theta+\sin\theta}}\cdot\frac{r^{2}}{2}\bigg|_{0}^{\frac{1}{\cos\theta+\sin\theta}}\mathrm{d}\theta\\=&\frac{1}{2}\int_{0}^{\frac{\pi}{2}}\mathrm{e}^{\frac{\sin\theta}{\cos\theta+\sin\theta}}\frac{1}{(\cos\theta+\sin\theta)^{2}}\mathrm{d}\theta\\=&\frac{1}{2}\int_{0}^{\frac{\pi}{2}}\mathrm{e}^{\frac{\sin\theta}{\cos\theta+\sin\theta}}\mathrm{d}\left(\frac{\sin\theta}{\cos\theta+\sin\theta}\right)\\=&\frac{1}{2}\mathrm{e}^{\frac{\sin\theta}{\cos\theta+\sin\theta}}\bigg|_{0}^{\frac{\pi}{2}}=\frac{1}{2}(\mathrm{e}-1)\ .\\\end{aligned} $$ 

<div style="text-align: center;">图 14-11</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_727_810_896_976.jpg" alt="Image" width="16%" /></div>


方法总结 二重积分的换元：注意“三换”，换积分区域，换被积函数，换积分变量。极坐标换元  $ \begin{cases} x = r \cos \theta, \\ y = r \sin \theta \end{cases} $ 仅是一种换元法。