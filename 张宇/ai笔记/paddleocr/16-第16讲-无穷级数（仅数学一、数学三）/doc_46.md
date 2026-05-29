②余弦级数展开.

 $$ f(x)\sim\frac{a_{0}}{2}+\sum_{n=1}^{\infty}a_{n}\cos\frac{n\pi}{l}x,\;x\in[0,\;l], $$ 

 $$ a_{n}=\frac{2}{l}\int_{0}^{l}f(x)\cos\frac{n\pi}{l}x\mathrm{d}x(n=0,1,2,\cdots). $$ 

例 16.38 设  $ f(x)=\begin{cases}x,&0\leqslant x\leqslant\frac{1}{2},\\2-2x,&\frac{1}{2}<x\leqslant1,\end{cases} $  $ S(x)=\frac{a_{0}}{2}+\sum_{n=1}^{\infty}a_{n}\cos n\pi x,-\infty<x<+\infty $，其中

 $$ a_{n}=2\int_{0}^{1}f(x)\cos n\pi x\mathrm{d}x\quad(n=0,\;1,\;2,\;\cdots)\;, $$ 

则  $ S\left(-\frac{5}{2}\right)= $ ___.

☑ 分析  $ S(x) $ 为余弦级数，为偶函数的展开式，题干给了定义在区间  $ [0,1] $ 上的函数，需进行偶延拓，再进行周期延拓。



解 应填 $ \frac{3}{4} $.

由余弦级数  $ S(x) $ 为函数  $ f(x) $ 作周期偶延拓的傅里叶级数，知  $ S(x) $ 以 2 为周期且为偶函数，故

<div style="text-align: center;"><img src="imgs/img_in_image_box_693_617_964_778.jpg" alt="Image" width="26%" /></div>


 $$ S\left(-\frac{5}{2}\right)=S\left(-2-\frac{1}{2}\right)=S\left(-\frac{1}{2}\right)=S\left(\frac{1}{2}\right) $$ 

周期为2 偶函数

又  $ x=\frac{1}{2} $ 为  $ f(x) $ 的第一类间断点，故由狄利克雷收敛定理，得

 $$ S\left(-\frac{5}{2}\right)=S\left(\frac{1}{2}\right)=\frac{f\left(\frac{1}{2}-0\right)+f\left(\frac{1}{2}+0\right)}{2}=\frac{\frac{1}{2}+\left(2-2\times\frac{1}{2}\right)}{2}=\frac{3}{4} $$ 

例 16.39 将函数  $ f(x) = 1 - x^2 $ ( $ 0 \leq x \leq \pi $) 展开成余弦级数，并求级数  $ \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n^2} $ 因为是余弦级数，将  $ f(x) $ 延拓成  $ [- \pi, \pi] $ 上的偶函数，则  $ b_n = 0, n = 1, 2, \cdots $.



 $$ a_{0}=\frac{2}{\pi}\int_{0}^{\pi}(1-x^{2})\mathrm{d}x=2\left(1-\frac{\pi^{2}}{3}\right), $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_782_1086_965_1205.jpg" alt="Image" width="17%" /></div>


表格法

 $$ a_{n}=\frac{2}{\pi}\int_{0}^{\pi}f(x)\cos nxdx=\frac{2}{\pi}\left(\int_{0}^{\pi}\cos nxdx-\int_{0}^{\pi}x^{2}\cos nxdx\right) $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_114_1270_387_1381.jpg" alt="Image" width="26%" /></div>


 $$ \frac{2}{\pi}\left(0-\int_{0}^{\pi}x^{2}\cos nxdx\right)=\frac{-2}{\pi}\left(\left.\frac{x^{2}\sin nx}{n}\right|_{0}^{\pi}-\int_{0}^{\pi}\frac{2x\sin nx}{n}\mathrm{d}x\right) $$ 