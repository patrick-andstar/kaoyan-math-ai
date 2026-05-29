 $$ \begin{aligned}\iint\limits_{D}\frac{1}{3x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y&=\int_{0}^{\frac{\pi}{3}}\mathrm{d}\theta\int_{\frac{1}{\sqrt{1-\cos\theta\sin\theta}}}^{\frac{2}{1-\cos\theta\sin\theta}}\cdot\frac{1}{r^{2}(3\cos^{2}\theta+\sin^{2}\theta)}r\mathrm{d}r\\&=\int_{0}^{\frac{\pi}{3}}\mathrm{d}\theta\int_{\frac{1}{\sqrt{1-\cos\theta\sin\theta}}}^{\frac{2}{1-\cos\theta\sin\theta}}\cdot\frac{1}{3\cos^{2}\theta+\sin^{2}\theta}\cdot\frac{1}{r}\mathrm{d}r\\&=\frac{\ln2}{2}\int_{0}^{\frac{\pi}{3}}\frac{1}{3\cos^{2}\theta+\sin^{2}\theta}\mathrm{d}\theta\\&\quad\text{评}y=\sqrt{3}x\end{aligned} $$ 

 $$ \begin{aligned}\int\frac{\mathrm{d}x}{a^{2}+x^{2}}&=\frac{1}{a}\arctan\frac{x}{a}+C(a>0)\quad&\leftarrow\\ &\left.\frac{1}{2}\left(\frac{1}{\sqrt{3}}\arctan\frac{\tan\theta}{\sqrt{3}}\right)\right|_{0}^{\frac{\pi}{3}}\\ &=\frac{\sqrt{3}\ln2}{24}\pi.\end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_749_313_941_501.jpg" alt="Image" width="18%" /></div>


注 本题有两个办法画出 D 的边界图形.

第一，描点法．显然， $ x^{2}+y^{2}-xy=1 $ 与  $ x^{2}+y^{2}-xy=2 $ 分别与 x 轴、y 轴和 y=x 交于  $ (1,0) $ 与  $ (\sqrt{2},0) $， $ (0,1) $ 与  $ (0,\sqrt{2}) $， $ (1,1) $ 与  $ (\sqrt{2},\sqrt{2}) $，将这些点连起来即可得到其大致图形．

第二，事实上， $ x^{2}+y^{2}-xy=[x,y]\begin{bmatrix}1&-\frac{1}{2}\\ -\frac{1}{2}&1\end{bmatrix}\begin{bmatrix}x\\ y\end{bmatrix} $，其二次型矩阵为 $ A=\begin{bmatrix}1&-\frac{1}{2}\\ -\frac{1}{2}&1\end{bmatrix} $， $ |\lambda E-A|= $

 $ \begin{vmatrix}\lambda-1&\frac{1}{2}\\\frac{1}{2}&\lambda-1\end{vmatrix}=0 $，得 $ \lambda_{1}=\frac{1}{2} $， $ \lambda_{2}=\frac{3}{2} $（或用配方法 $ x^{2}+y^{2}-xy=\left(x-\frac{1}{2}y\right)^{2}+\frac{3}{4}y^{2} $）。故 $ x^{2}+y^{2}-xy $可经正

交变换化为 $ \frac{1}{2}y_{1}^{2}+\frac{3}{2}y_{2}^{2} $，于是 $ \frac{1}{2}y_{1}^{2}+\frac{3}{2}y_{2}^{2}=1 $与 $ \frac{1}{2}y_{1}^{2}+\frac{3}{2}y_{2}^{2}=2 $均为椭圆，即可画出图形。

☑ 方法总结 当积分区域给出的不是常见曲线时，可考虑描点法画积分区域图.

公式  $ \int\frac{1}{3\cos^{2}\theta+\sin^{2}\theta}d\theta=\int\frac{d(\tan\theta)}{3+\tan^{2}\theta}=\frac{1}{\sqrt{3}}\arctan\frac{\tan\theta}{\sqrt{3}}+C $

例 14.10 设  $ f(x)=\iint_{D(x)}\frac{v\ln\sqrt{u^{2}+v^{2}}}{u+v}\mathrm{d}u\mathrm{d}v $,  $ D(x)=\left\{(u,v)\mid\frac{1}{4}\leq u^{2}+v^{2}\leq x^{2},u>0,v>0\right\} $, 求曲线  $ y(x)=\int_{1}^{x}f(t)\mathrm{d}t\left(x>\frac{1}{2}\right) $ 的拐点.