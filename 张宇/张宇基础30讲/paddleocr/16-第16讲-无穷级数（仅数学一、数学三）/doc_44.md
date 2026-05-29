 $$ \begin{aligned}\sum_{n=0}^{\infty}(-1)^{n}\cdot\frac{2n+2}{(2n+1)!}&=\sum_{n=0}^{\infty}(-1)^{n}\frac{2n+1}{(2n+1)!}+\sum_{n=0}^{\infty}(-1)^{n}\frac{1}{(2n+1)!}\\&\downarrow\\ 因为分母是 (2n+1)!, 所以分子拆为 2n+1+1\\&=\sum_{n=0}^{\infty}(-1)^{n}\frac{1}{(2n)!}+\sum_{n=0}^{\infty}(-1)^{n}\frac{1}{(2n+1)!}\\&=\cos1+\sin1.\end{aligned} $$ 

六傅里叶级数（仅数学一）

幂级数展开，一般是n阶可导。傅里叶级数，不需要n阶可导。一般情况下函数具有周期性。



<div style="text-align: center;"><img src="imgs/img_in_image_box_847_429_953_537.jpg" alt="Image" width="10%" /></div>


周期为 2/ 的傅里叶级数

识记水平的考查



定义 4 设函数  $ f(x) $ 是周期为 2l 的周期函数，且在  $ [-l, l] $ 上可积，则称

 $$ \begin{aligned}n=0 时 ,\ a_{0}=\frac{1}{l}\int_{-l}^{l}f(x)\mathrm{d}x\xleftarrow{\quad}a_{n}=\frac{1}{l}\int_{-l}^{l}f(x)\cos\frac{n\pi}{l}x\mathrm{d}x(n=0,1,2,\cdots),\\b_{n}=\frac{1}{l}\int_{-l}^{l}f(x)\sin\frac{n\pi}{l}x\mathrm{d}x(n=1,2,3,\cdots)\end{aligned} 需要记住 $$ 

为 $ f(x) $的以2l为周期的傅里叶系数.称级数

 $$ \frac{a_{0}}{2}+\sum_{n=1}^{\infty}\left(a_{n}\cos\frac{n\pi}{l}x+b_{n}\sin\frac{n\pi}{l}x\right) $$ 

为 $ f(x) $的以2l为周期的傅里叶级数，记作

这个符号的意思是  $ f(x) \sim \frac{a_{0}}{2} + \sum_{n=1}^{\infty} \left( a_{n} \cos \frac{n\pi}{l} x + b_{n} \sin \frac{n\pi}{l} x \right) = S(x) $.

## 2 狄利克雷收敛定理

设 $ f(x) $是以2l为周期的可积函数，如果在 $ [-l,l] $上 $ f(x) $满足：

①连续或只有有限个第一类间断点；

②至多只有有限个极值点.

则 $ f(x) $的傅里叶级数在 $ [-l,l] $上处处收敛.记其和函数为 $ S(x) $，则

 $$ ↳ 逄缜时 f(x)=\frac{f(x-0)+f(x+0)}{2} $$ 

 $$ S(x)=\left\{\begin{aligned}&f(x),&x 为连续点 ,\\ &\frac{f(x-0)+f(x+0)}{2},&x 为间断点 ,\\ &\frac{f(-l+0)+f(l-0)}{2},&x=\pm l.\end{aligned}\right. $$ 

因为 $ f(x) $是周期函数，所以-1处的右极限就是1处的右极限，所以

 $$ \frac{f(-l+0)+f(l-0)}{2}=\frac{f(l-0)+f(l+0)}{2} $$ 