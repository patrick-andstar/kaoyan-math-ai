证 由  $ f(x) $ 在  $ [0,1] $ 上连续，则  $ f(x) $ 在  $ [0,1] $ 上有最大值 M 和最小值 m，即  $ m \leqslant f(x) \leqslant M $，于是  $ mx^n \leqslant x^n f(x) \leqslant Mx^n $。根据积分的保号性，有  $ \int_0^1 mx^n dx \leqslant \int_0^1 x^n f(x) dx \leqslant \int_0^1 Mx^n dx $，即  $ \frac{m}{n+1} \leqslant \int_0^1 x^n f(x) dx \leqslant \frac{M}{n+1} $。根据夹逼准则，有  $ \lim_{n \to \infty} \int_0^1 x^n f(x) dx = 0 $。

如例 11.4 中所取的  $ f(x)=\begin{cases}x\left|\ln x\right|, & 0<x\leq1,\\0, & x=0,\end{cases} $ 则有  $ \lim_{n\to\infty}\int_{0}^{1}x^{n-1}x\left|\ln x\right|dx=\lim_{n\to\infty}\int_{0}^{1}x^{n}\left|\ln x\right|dx=0 $

例 11.5 设函数  $ f(x) = x - [x] $，其中  $ [x] $ 表示不超过  $ x $ 的最大整数，则  $ \lim_{x \to +\infty} \frac{1}{x} \int_0^x f(t) \, dt = $ ___.

 $ \rho $ 分析  $ \lim_{x \to +\infty} \frac{\int_0^x f(t) \, dt}{x} \left( \frac{\infty}{\infty} \right) $ 不能用洛必达法则，因为包含跳跃间断点的函数  $ f(x) $ 无原函数.

解 应填 $ \frac{1}{2} $

由例 1.13 可知  $ f(x) $ 是周期为 1 的周期函数，其图像如图 11-1 所示。

 $ \int_{0}^{n}f(t)\mathrm{d}t=n\int_{0}^{1}f(t)\mathrm{d}t $，表示n个三角形的面积，每个三角形的面积为 $ \frac{1}{2} $，故为 $ \frac{n}{2} $。

<div style="text-align: center;"><img src="imgs/img_in_image_box_354_677_692_800.jpg" alt="Image" width="32%" /></div>


<div style="text-align: center;">图 11-1</div>


当 $ \frac{n \leqslant x < n+1}{n+1}<\frac{1}{x} \leqslant \frac{1}{n} $时， $ \frac{n}{2}=\int_{0}^{n} f(t) dt \leqslant \int_{0}^{x} f(t) dt < \int_{0}^{n+1} f(t) dt = \frac{n+1}{2} $，于是

分母的取值范围

 $$ \frac{n}{2(n+1)}=\frac{1}{n+1}\int_{0}^{n}f(t)\mathrm{d}t<\frac{1}{x}\int_{0}^{x}f(t)\mathrm{d}t<\frac{1}{n}\int_{0}^{n+1}f(t)\mathrm{d}t=\frac{n+1}{2n} $$ 

当 $ x\to+\infty $时， $ n\to\infty $，由夹逼准则，有 $ \lim_{x\to+\infty}\frac{1}{x}\int_{0}^{x}f(t)dt=\frac{1}{2} $。当 $ 0<a<y<b,0<c<x<d $时

## 3 用积分法 → 恒等变形、换元法、分部积分法

例 11.6 设  $ f(x) $ 的二阶导数  $ f''(x) $ 在  $ [0,1] $ 上连续，且  $ f(0)=f(1)=0 $，证明：

(1)  $ \int_{0}^{1} f(x) \, dx = \frac{1}{2} \int_{0}^{1} x(x-1) f''(x) \, dx $;

(2)  $ \left|\int_{0}^{1}f(x)dx\right|\leqslant\frac{1}{12}\max_{0\leqslant x\leqslant1}\left\{\left|f''(x)\right|\right\}. $

♡分析 第(1)问出现函数和函数的二阶导数，用两次分部积分法.

证 (1)  $ \frac{1}{2}\int_{0}^{1}x(x-1)f''(x)dx=\frac{1}{2}\int_{0}^{1}\frac{x(x-1)d\left[\frac{f'(x)}{u}\right]}{u} $ 分配积分法： $ \int udv=uv-\int vdu $