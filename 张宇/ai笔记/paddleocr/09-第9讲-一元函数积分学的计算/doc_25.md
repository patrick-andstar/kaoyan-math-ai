例9.29 设 $ f(x)=\begin{cases}\dfrac{4x^{2}}{a^{3}\sqrt{\pi}}e^{-\dfrac{x^{2}}{a^{2}}}, & x>0, \\ 0, & x\leq0,\end{cases} $为正常数，则 $ \int_{0}^{+\infty}x^{2}f(x)dx= $___。

解 应填 $ \frac{3}{2}a^{2} $

 $$ \begin{aligned}\int_{0}^{+\infty}x^{2}f(x)\mathrm{d}x&=\frac{2a^{2}}{\sqrt{\pi}}\bullet2\int_{0}^{+\infty}\left(\frac{x}{a}\right)^{2\bullet\frac{5}{2}-1}\mathrm{e}^{-\left(\frac{x}{a}\right)^{2}}\mathrm{d}\left(\frac{x}{a}\right)=\frac{2a^{2}}{\sqrt{\pi}}\bullet\Gamma\left(\frac{5}{2}\right)\\&=\frac{2a^{2}}{\sqrt{\pi}}\bullet\frac{3}{2}\bullet\frac{1}{2}\bullet\Gamma\left(\frac{1}{2}\right)=\frac{3}{2}a^{2}\ .\end{aligned} $$ 

注

 $$ \Gamma(\alpha)=\int_{0}^{+\infty}x^{\alpha-1}\mathrm{e}^{-x}\mathrm{d}x=\int_{0}^{1}x^{\alpha-1}\mathrm{e}^{-x}\mathrm{d}x+\int_{1}^{+\infty}x^{\alpha-1}\mathrm{e}^{-x}\mathrm{d}x\;. $$ 

①当 $ \alpha-1\geq0 $时，

 $$ \lim_{x\to+\infty}\frac{x^{\alpha-1}\mathrm{e}^{-x}}{\frac{1}{x^{2}}}\xlongequal{\frac{0}{0}}\lim_{x\to+\infty}x^{\alpha+1}\mathrm{e}^{-x}=0, $$ 

由于 $ \int_{1}^{+\infty}\frac{1}{x^{2}}dx $收敛，因此 $ \int_{1}^{+\infty}x^{\alpha-1}e^{-x}dx $收敛.

②当  $ \alpha-1<0 $ 时， $ \int_{0}^{1}\frac{1}{x^{1-\alpha}}e^{-x}dx $ 等价于研究  $ \int_{0}^{1}\frac{1}{x^{1-\alpha}}dx $ 的敛散性，则  $ 1-\alpha<1 $，即当  $ 0<\alpha<1 $ 时， $ \int_{0}^{1}\frac{1}{x^{1-\alpha}}e^{-x}dx $ 收敛，显然  $ \int_{1}^{+\infty}\frac{1}{x^{1-\alpha}}e^{-x}dx $ 收敛。

综上所述，当  $ \alpha > 0 $ 时， $ \Gamma(\alpha) $ 收敛。

<div style="text-align: center;"><img src="imgs/img_in_image_box_73_1000_151_1058.jpg" alt="Image" width="7%" /></div>


## 基础习题精练

## 习题

9.1 若  $ \int xf(x)dx = \arcsin x + C $，则  $ \int \frac{1}{f(x)} dx = $ ___.

9.2 若  $ f(x)=\frac{1}{1+x^{2}}+x^{3}\int_{0}^{1}f(x)dx $，则  $ \int_{0}^{1}f(x)dx= $ ___.

9.3 极限  $ \lim_{x\to+\infty}\frac{\int_{e}^{x}\left(1-\frac{1}{t}\right)^{t}\cdot e^{et}dt}{e^{ex}}= $ ___.