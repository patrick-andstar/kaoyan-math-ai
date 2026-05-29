分析 ① 求交点． $ \left\{\begin{aligned}y&=x^{n},\\ y&=x^{n+1}\end{aligned}\right.\Rightarrow x^{n}=x^{n+1}\Rightarrow x=0 $ 或 x=1

②画图（见图 10-1）.

<div style="text-align: center;"><img src="imgs/img_in_image_box_311_208_516_328.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;">图 10-1</div>


③套公式，做计算，得到 $ A_{n} $的具体表达式.

④代入 $ A_{n} $，求极限.

解 应填  $ e^{-2} $

由

 $$ \begin{cases}y=x^{n},\\y=x^{n+1}\end{cases}\Rightarrow x^{n+1}-x^{n}=0\Rightarrow x^{n}(x-1)=0\Rightarrow x=0,x=1\ , $$ 

得  $ y = x^{n} $ 与  $ y = x^{n+1} $ 的交点为  $ (0, 0) $， $ (1, 1) $，故

 $$ A_{n}=\int_{0}^{1}(x^{n}-x^{n+1})\mathrm{d}x=\left(\frac{1}{n+1}x^{n+1}-\frac{1}{n+2}x^{n+2}\right)\bigg|_{0}^{1}=\frac{1}{n+1}-\frac{1}{n+2} $$ 

则

 $$ \begin{aligned}\lim_{n\rightarrow\infty}\left(2\sum_{k=1}^{n}A_{k}\right)^{n}=&\lim_{n\rightarrow\infty}\left[\sum_{k=1}^{n}\left(\frac{2}{k+1}-\frac{2}{k+2}\right)\right]^{n}\\=&\lim_{n\rightarrow\infty}\left(\frac{2}{2}-\frac{2}{3}+\frac{2}{3}-\frac{2}{4}+\cdots+\frac{2}{n+1}-\frac{2}{n+2}\right)^{n}=\lim_{n\rightarrow\infty}\left(1-\frac{2}{n+2}\right)^{n}=\mathrm{e}^{-2}\ .\end{aligned} $$ 

可以把n当作x，无须用归结原则化为函数极限

例 10.2 求由摆线  $ \begin{cases} x = a(t - \sin t), \\ y = a(1 - \cos t) \end{cases} $ (a > 0) 的一拱（见图 10-2）与 x 轴所围平面图形的面积.

<div style="text-align: center;"><img src="imgs/img_in_image_box_388_1047_687_1204.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;">图 10-2</div>


给定参数方程，其实是对定积分计算的换元法的变相考查，当f复杂时，引进一个新的自变量t进行处理。

参数方程下的问题是重点。①$\begin{cases}x=x(t),\\y=y(t)\Rightarrow y=\sqrt{f(x)}\end{cases}$ 它们所有对应点的函数值均相同

②$S=\int_{0}^{2\pi}f(x)\mathrm{d}x$ （直角坐标系）

$\frac{x=x(t)}{y}=y(t)x'(t)\mathrm{d}t=\int_{0}^{2\pi}y(t)\mathrm{d}[x(t)]$