例 8.6  $ \lim_{n\to\infty}\left(\frac{n+1}{n^2+1}+\frac{n+2}{n^2+4}+\frac{n+3}{n^2+9}+\cdots+\frac{n+n}{n^2+n^2}\right)= $（ ）.

(A)  $ \int_{0}^{1}\frac{1+x}{1+x^{2}}dx $ (B)  $ \int_{0}^{1}\frac{1}{1+x}dx $ (C)  $ \int_{0}^{1}\frac{x}{1+x^{2}}dx $ (D)  $ \int_{0}^{1}\frac{2x}{1+x^{2}}dx $

分析  $ \lim_{n\to\infty}\sum_{i=1}^{n}f\left(\frac{i}{n}\right)\cdot\frac{1}{n}=\int_{0}^{1}f(x)dx,\quad\lim_{n\to\infty}\sum_{i=1}^{n}f\left(\frac{2i-1}{2n}\right)\frac{1}{n}=\int_{0}^{1}f(x)dx $

如  $ \lim_{n\to\infty}\left(\frac{1}{n^{2}+n+1}+\frac{2}{n^{2}+n+2}+\cdots+\frac{n}{n^{2}+n+n}\right) $，利用夹逼准则，有

 $$ \begin{aligned}\frac{\frac{n(n+1)}{2}}{n^{2}+n+n}&\leqslant\sum_{i=1}^{n}\frac{i}{n^{2}+n+i}\leqslant\frac{\frac{n(n+1)}{2}}{n^{2}+n+1},\\\frac{1}{2}&\quad\frac{1}{2}\end{aligned} $$ 

故  $ \lim_{n\to\infty}\sum_{i=1}^{n}\frac{i}{n^{2}+n+i}=\frac{1}{2} $

此题若用夹逼准则，有

\[\begin{aligned}&\frac{n^{2}+\frac{n(n+1)}{2}}{n^{2}+n^{2}}<\sum_{i=1}^{n}\frac{n+i}{n^{2}+i^{2}}<\frac{n^{2}+\frac{n(n+1)}{2}}{n^{2}+1},\\ &\quad\begin{aligned}\\ &\downarrow\quad\quad\quad\quad\

所以此题采用“凑定积分定义”法，即对于 $ \lim_{n\to\infty}\sum_{i=1}^{n}g(n,i) $，判别 $ g(n,i) $能否写成 $ f\left(\frac{i}{n}\right)\cdot\frac{1}{n} $或 $ \frac{1}{n}f\left(\frac{2i-1}{2n}\right) $.

解 应选(A).

对于 n 项和的极限，先提  $ \frac{1}{n} $

 $$ \lim_{n\to\infty}\left(\frac{n+1}{n^{2}+1}+\frac{n+2}{n^{2}+4}+\frac{n+3}{n^{2}+9}+\cdots+\frac{n+n}{n^{2}+n^{2}}\right)=\lim_{n\to\infty}\sum_{i=1}^{n}\frac{n+i}{n^{2}+i^{2}} $$ 

若能凑成 $ f\left(\frac{i}{n}\right) $，则用定积分定义；

若不能，则考虑夹逼准则。

 $$ \begin{aligned}\underline{\underline{\textcircled{1}}}\lim_{n\rightarrow\infty}\sum_{i=1}^{n}\frac{n^{2}+ni}{n^{2}+i^{2}}\bullet\frac{1}{n}\underline{\underline{\textcircled{2}}}\lim_{n\rightarrow\infty}\sum_{i=1}^{n}\frac{1+\frac{i}{n}}{1+\left(\frac{i}{n}\right)^{2}}\bullet\frac{1}{n}\underline{\underline{\textcircled{3}}}\int_{0}^{1}\frac{1+x}{1+x^{2}}\mathrm{d}x.\end{aligned} $$ 

## 注 “凑定积分定义” 的步骤如下：

①先提出 $ \frac{1}{n} $；②再凑出 $ \frac{i}{n} $；③由于 $ \frac{i}{n}=0+\frac{1-0}{n}i $，故 $ \frac{i}{n} $可以读作“0到1上的x”，且 $ \frac{1}{n}=\frac{1-0}{n} $，读作“0到1上的dx”，于是，“凑定义”完毕。

例 8.7 设  $ f(x) $ 是  $ [a, b] $ 上非负的连续函数，且  $ f(x) $ 不恒等于零，证明必有  $ \int_{a}^{b} f(x) \, dx > 0 $ .

证 因函数 $ f(x) $在 $ [a,b] $上不恒等于零，且非负，故至少存在一点 $ x_{0}\in(a,b) $，使得 $ f(x_{0})\neq0 $，即 $ f(x_{0})>0 $。