若 $ \int_{1}^{+\infty}\frac{1}{x^{2-p-\varepsilon}}dx $收敛，即2-p>1，p<1，则 $ \int_{1}^{+\infty}\frac{\ln x}{(1+x)x^{1-p}}dx $也收敛.

综上，当 0 < p < 1 时，反常积分  $ \int_{0}^{+\infty}\frac{\ln x}{(1+x)x^{1-p}}dx $ 收敛.

8.4  $ 2\sqrt{2}-2 $ 解 原式  $ \lim_{n\to\infty}\sum_{i=1}^{n}\frac{1}{\sqrt{n^{2}+ni}}=\lim_{n\to\infty}\sum_{i=1}^{n}\frac{1}{\sqrt{1+\frac{i}{n}}}\cdot\frac{1}{n}=\int_{0}^{1}\frac{1}{\sqrt{1+x}}\,\mathrm{d}x=2\sqrt{1+x}\Big|_{0}^{1}=2\sqrt{2}-2 $

注 能凑成  $ \frac{i}{n} $，则用定积分定义；凑不成的，先用放缩法，放缩后再用定积分定义。常见的几种凑定积分定义的式子有

(1)

 $$ \begin{aligned}\lim_{n\rightarrow\infty}\left(\frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{n+n}\right)&=\lim_{n\rightarrow\infty}\sum_{i=1}^{n}\frac{1}{n+i}=\lim_{n\rightarrow\infty}\sum_{i=1}^{n}\frac{1}{1+\frac{i}{n}}\bullet\frac{1}{n}\\&=\int_{0}^{1}\frac{1}{1+x}\mathrm{d}x=\ln\left(1+x\right)\Big|_{0}^{1}=\ln2.\end{aligned} $$ 

这里分母上有  $ n+i $，提出 n 后，会化成  $ 1+\frac{i}{n} $

(2)

 $$ \begin{aligned}&\begin{aligned}\\ &\lim_{n\rightarrow\infty}\left(\frac{n}{n^{2}+1^{2}}+\frac{n}{n^{2}+2^{2}}+\cdots+\frac{n}{n^{2}+n^{2}}\right)=\lim_{n\rightarrow\infty}\sum_{i=1}^{n}\frac{n}{n^{2}+i^{2}}\\ &\end{aligned}\\ &=\lim_{n\rightarrow\infty}\sum_{i=1}^{n}\frac{n^{2}}{n^{2}+i^{2}}\bullet\frac{1}{n}=\lim_{n\rightarrow\infty}\sum_{i=1}^{n}\frac{1}{1+\left(\frac{i}{n}\right)^{2}}\bullet\frac{1}{n}\\ &=\int_{0}^{1}\frac{1}{1+x^{2}}\mathrm{d}x=\arctan x|_{0}^{1}=\frac{\pi}{4}.\\ \end{aligned} $$ 

这里分母上有  $ n^{2} + i^{2} $，提出  $ n^{2} $ 后，会化成  $ 1 + \left(\frac{i}{n}\right)^{2} $

(3)对于本题，分母上有 $ n^{2}+ni $，提出 $ n^{2} $后，会化成 $ 1+\frac{i}{n} $

8.5  $ \frac{2}{\pi} $ 解 当各项分母相同且均为 n 时，

 $$ \lim_{n\to\infty}\sum_{i=1}^{n}\frac{\sin\frac{i\pi}{n}}{n}=\lim_{n\to\infty}\frac{1}{n}\sum_{i=1}^{n}\sin\frac{i}{n}\pi=\int_{0}^{1}\sin\pi x\mathrm{d}x, $$ 