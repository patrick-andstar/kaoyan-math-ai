 $ \lim_{x\to0^{+}}\frac{\frac{\ln x}{x^{\alpha}}}{\frac{1}{x^{\alpha+\varepsilon}}} $ 是比较判别法的极限形式

 $$ \lim_{x\to0^{+}}x^{\alpha+\varepsilon}\frac{\ln x}{x^{\alpha}}=\lim_{x\to0^{+}}x^{\varepsilon}\ln x=\lim_{x\to0^{+}}\frac{\ln x}{x^{-\varepsilon}}=\lim_{x\to0^{+}}\frac{\frac{1}{x}}{-x^{\varepsilon-1}}=\lim_{x\to0^{+}}\left(-\frac{1}{\varepsilon}x^{\varepsilon}\right)=0 $$ 

故当 $ x \to 0^{+} $时， $ \frac{1}{x^{\alpha+\varepsilon}} $是比 $ \frac{\ln x}{x^{\alpha}} $高阶的无穷大量，因为当 $ \alpha + \varepsilon < 1 $时， $ \int_{0}^{1} \frac{1}{x^{\alpha+\varepsilon}} dx $收敛，于是 $ \int_{0}^{1} \frac{\ln x}{x^{\alpha}} dx $收敛，选项(B)正确；

当  $ \alpha \geqslant 1 $ 时，由于  $ \lim_{x \to 0} x^{\alpha} \frac{\ln x}{x^{\alpha}} = \infty $，故当  $ x \to 0^{+} $ 时， $ \frac{1}{x^{\alpha}} $ 是比  $ \frac{\ln x}{x^{\alpha}} $ 低阶的无穷大量，因为当  $ \alpha \geqslant 1 $ 时， $ \int_{0}^{1} \frac{1}{x^{\alpha}} dx $ 发散，于是  $ \int_{0}^{1} \frac{\ln x}{x^{\alpha}} dx $ 发散。

注  $ \int_{0}^{1}\frac{\ln x}{x^{p}}dx $ 收敛， $ 0\leq p<1 $ 发散， $ p\geq1 $

例8.19 已知  $ \alpha > 0 $，则对于反常积分  $ \int_{1}^{+\infty} \frac{\ln x}{x^{\alpha}} \, dx $ 的敛散性的判别，正确的是（）.

(A) 当  $ 0 < \alpha \leq 1 $ 时，积分收敛

(B) 当  $ \alpha > 1 $ 时，积分收敛

(C) 敛散性与  $ \alpha $ 无关，必收敛

(D) 敛散性与  $ \alpha $ 无关，必发散

分析 反常积分判别敛散性.

①放缩法  $ 0 \leqslant f(x) \leqslant g(x) $;

比较判别法

②计算极限 $ \frac{0}{0},\frac{\infty}{\infty} $;



③4个结论$\left\{\begin{aligned}&\int_{0}^{1}\frac{1}{x^{p}}\mathrm{d}x\left\{\begin{aligned}& 收敛，0<p<1\\& 发散，p\geq1\end{aligned}\right.\\&\int_{1}^{+\infty}\frac{1}{x^{p}}\mathrm{d}x\left\{\begin{aligned}& 收敛，p>1\\& 发散，p\leq1\end{aligned}\right.\\&\int_{1}^{+\infty}\frac{1}{x^{p}}\mathrm{d}x\left\{\begin{aligned}& 收敛，p>1\\& 发散，p\leq1\end{aligned}\right.\end{aligned}\right.$ $\int_{1}^{+\infty}\frac{\ln x}{x^{p}}\mathrm{d}x\left\{\begin{aligned}& 收敛，p>1\\& 发散，p\leq1\end{aligned}\right.$

补充：若  $ \lim_{x\to+\infty}x^{p}f(x)=\lambda\geq0 $ ，且  $ p>1 $ ，则  $ \int_{1}^{+\infty}f(x)dx $ 收敛.

 $ \lim_{x\to+\infty}\frac{f(x)}{\frac{1}{x^p}}=0 $， $ p>1 $ 时， $ \int_{1}^{+\infty}\frac{1}{x^p}dx $ 收敛，故 $ \int_{1}^{+\infty}f(x)dx $ 收敛。

解 应选(B).

当  $ 0 < \alpha \leq 1 $ 且 x 充分大时， $ \frac{\ln x}{x^{\alpha}} > \frac{1}{x^{\alpha}} $，由于  $ \int_{1}^{+\infty} \frac{1}{x^{\alpha}} dx $ 发散，因此  $ \int_{1}^{+\infty} \frac{\ln x}{x^{\alpha}} dx $ 发散；

当  $ \alpha > 1 $ 时，取充分小的正数  $ \varepsilon $，使  $ \alpha - \varepsilon > 1 $，由  $ \lim_{x \to +\infty} \frac{\frac{\ln x}{x^\alpha}}{\frac{1}{x^{\alpha - \varepsilon}}} = \lim_{x \to +\infty} \frac{\ln x}{x^\varepsilon} = 0 $，且  $ \int_1^{+\infty} \frac{1}{x^{\alpha - \varepsilon}} \, dx $ 收敛，