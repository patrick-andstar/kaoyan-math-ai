 $$ \lim_{x\to+\infty}\frac{\frac{\ln x}{1+x^{2}}}{\frac{1}{x^{\frac{3}{2}}}}=0, $$ 

且反常积分 $ \int_{1}^{+\infty}\frac{1}{x^{\frac{3}{2}}}dx $收敛，所以反常积分 $ \int_{1}^{+\infty}\frac{\ln x}{1+x^{2}}dx $收敛.

综上可知，反常积分 $ \int_{0}^{+\infty}\frac{\ln x}{1+x^{2}}dx $收敛.

对于(C)，由于 $ \lim_{x\to0^{+}}\frac{\frac{1}{\sin x}}{\frac{1}{x}}=1 $，因此 $ \int_{0}^{1}\frac{1}{\sin x}dx $发散。而 $ \int_{-1}^{1}\frac{1}{\sin x}dx=\int_{-1}^{0}\frac{1}{\sin x}dx+\int_{0}^{1}\frac{1}{\sin x}dx $，可知 $ \int_{-1}^{1}\frac{1}{\sin x}dx $发散。

对于(D)， $ \int_{-\infty}^{+\infty}\frac{\sin x}{1+x^{2}}dx=\int_{-\infty}^{0}\frac{\sin x}{1+x^{2}}dx+\int_{0}^{+\infty}\frac{\sin x}{1+x^{2}}dx $，且有

 $$ \int_{0}^{+\infty}\frac{\sin x}{1+x^{2}}\mathrm{d}x\leqslant\int_{0}^{+\infty}\left|\frac{\sin x}{1+x^{2}}\right|\mathrm{d}x\leqslant\int_{0}^{+\infty}\frac{1}{1+x^{2}}\mathrm{d}x=\left.\arctan x\right|_{0}^{+\infty}=\frac{\pi}{2} $$ 

由对称区间反常积分结论（见下面的注），可知 $ \int_{-\infty}^{+\infty}\frac{\sin x}{1+x^{2}}dx $收敛.

注 当 $ f(x) $为偶函数且 $ \int_{0}^{+\infty}f(x)dx $收敛时，

 $$ \int_{-\infty}^{+\infty}f(x)\mathrm{d}x=2\int_{0}^{+\infty}f(x)\mathrm{d}x $$ 

当 $ f(x) $为奇函数且 $ \int_{0}^{+\infty}f(x)dx $收敛时，

 $$ \int_{-\infty}^{+\infty}f(x)\mathrm{d}x=0 $$ 

例8.18 已知  $ \alpha > 0 $，则对于反常积分  $ \int_{0}^{1} \frac{\ln x}{x^{\alpha}} dx $ 的敛散性的判别，正确的是（）.

(C) 敛散性与  $ \alpha $ 的取值无关，必收敛 (D) 敛散性与  $ \alpha $ 的取值无关，必发散

①放缩  $ 0 \leqslant f(x) \leqslant g(x) $;

②计算极限  $ \left\{\begin{aligned}0\\0\\-\infty\end{aligned}\right. $

解 应选(B).

当 $ \alpha<1 $时，取充分小的正数 $ \varepsilon $，使得 $ \alpha+\varepsilon<1 $，由于