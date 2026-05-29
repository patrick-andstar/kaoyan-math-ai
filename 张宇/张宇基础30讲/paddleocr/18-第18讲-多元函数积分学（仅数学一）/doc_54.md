 $$ I=\int_{L}[\mathrm{e}^{x}\cos y+2(x+y)]\mathrm{d}x+\left(-\mathrm{e}^{x}\sin y+\frac{3}{2}x\right)\mathrm{d}y. $$ 

18.10 计算曲面积分  $ \iint_{\Sigma}(2x+z)dydz+zdx dy $，其中  $ \Sigma $ 为有向曲面  $ z = x^{2} + y^{2} (0 \leq z \leq 1) $，其法向量与 z 轴正向夹角为锐角．

18.11 设  $ \Sigma $ 为任意封闭曲面，

 $$ I=\oint_{\Sigma+\infty}\left(x-\frac{1}{3}x^{3}\right)\mathrm{d}y\mathrm{d}z-\frac{4}{3}y^{3}\mathrm{d}z\mathrm{d}x+\left(3y-\frac{1}{3}z^{3}\right)\mathrm{d}x\mathrm{d}y. $$ 

(1) 证明  $ \Sigma $ 为椭球面  $ x^{2} + 4y^{2} + z^{2} = 1 $ 时，I 达到最大值；

(2) 求 I 的最大值.

## 解答

18.1 (B) 解 由轮换对称性可得

 $$ \begin{aligned}\oint_{L}(3x^{2}-y^{2}-z^{2})\mathrm{d}s=&\oint_{L}x^{2}\mathrm{d}s=\oint_{L}\frac{x^{2}+y^{2}+z^{2}}{3}\mathrm{d}s\\=&3\oint_{L}\mathrm{d}s=3(2\pi\times3)=18\pi.\end{aligned} $$ 

18.2 (A) 解  $ \oint_{\Sigma}(2x+3y+z)\,\mathrm{d}S=2\oint_{\Sigma}x\,\mathrm{d}S+3\oint_{\Sigma}y\,\mathrm{d}S+\oint_{\Sigma}z\,\mathrm{d}S $，又有  $ \bar{x}=\frac{1}{S}\oint_{\Sigma}x\,\mathrm{d}S $， $ \bar{y}=\frac{1}{S}\oint_{\Sigma}y\,\mathrm{d}S $， $ \bar{z}=-\frac{1}{S}\oint_{\Sigma}z\,\mathrm{d}S $ 是球面  $ (x-1)^2+y^2+(z+1)^2=1 $ 的形心坐标公式，而球面的形心在球心  $ (1,0,-1) $ 处，故

 $$ \oint_{\Sigma}(2x+3y+z)\mathrm{d}S=(2\overline{x}+3\overline{y}+\overline{z})S=(2+0-1)\cdot4\pi=4\pi $$ 

18.3  $ \pi $ 解 方法一 将 L 的方程化为参数形式

 $$ \begin{cases}x=\cos t,&\\y=\sin t,&(0\leq t\leq2\pi),\\z=\cos t+\sin t\end{cases} $$ 

则

 $$ \begin{aligned}\oint_{L}xz\mathrm{d}x+x\mathrm{d}y+\frac{y^{2}}{2}\mathrm{d}z=&\int_{0}^{2\pi}\left[\cos t\bullet(\cos t+\sin t)\bullet(-\sin t)+\cos t\bullet\cos t+\frac{1}{2}\sin^{2}t\bullet(-\sin t+\cos t)\right]\mathrm{d}t\\=&\int_{0}^{2\pi}\cos^{2}t\mathrm{d}t=\int_{0}^{2\pi}\frac{1+\cos2t}{2}\mathrm{d}t=\pi.\end{aligned} $$ 

方法二 记 S 是平面  $ z = x + y $ 上位于柱面  $ x^2 + y^2 = 1 $ 内的部分，则 S 在 xOy 平面上的投影为  $ D = \left\{(x, y) \mid x^2 + y^2 \leq 1\right\} $，平面  $ z = x + y $ 向上的单位法向量为  $ \left(-\frac{1}{\sqrt{3}}, -\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}\right) $.