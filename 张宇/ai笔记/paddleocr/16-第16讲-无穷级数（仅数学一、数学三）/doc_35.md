当  $ \alpha = -\frac{1}{2} $ 时，得到

 $$ \frac{1}{\sqrt{1+x}}=1-\frac{1}{2}x+\frac{1\times3}{2\times4}x^{2}-\frac{1\times3\times5}{2\times4\times6}x^{3}+\cdots,-1<x\leqslant1. $$ 

例 16.28 求  $ \sum_{n=1}^{\infty}\left(1+\frac{1}{2}+\cdots+\frac{1}{n}\right)x^{n} $ 的和函数.

分析 利用  $ \sum_{n=0}^{\infty}a_{n}x^{n}\cdot\sum_{n=0}^{\infty}b_{n}x^{n}=\sum_{n=0}^{\infty}\left(\sum_{i=0}^{n}a_{i}b_{n-i}\right)x^{n} $

解

 $$ \begin{aligned}&\sum_{n=1}^{\infty}\left(1+\frac{1}{2}+\cdots+\frac{1}{n}\right)x^{n}.\\=&\sum_{n=0}^{\infty}\left(1+\frac{1}{2}+\cdots+\frac{1}{n+1}\right)x^{n+1}\\=&x\bullet\sum_{n=0}^{\infty}\left(1+\frac{1}{2}+\cdots+\frac{1}{n+1}\right)x^{n}\\=&x\bullet\sum_{n=0}^{\infty}\left(1\bullet1+\frac{1}{2}\bullet1+\cdots+\frac{1}{n+1}\bullet1\right)x^{n}\\a_{i}&\xleftarrow{}\\=&x\bullet\sum_{n=0}^{\infty}\left(\sum_{i=0}^{n}\frac{1}{i+1}\bullet\textcircled{1}\right)x^{n}\xrightarrow{b_{n-i}}\\=&x\bullet\sum_{n=0}^{\infty}\frac{1}{n+1}x^{n}\bullet\sum_{n=0}^{\infty}x^{n}\\=&\sum_{n=0}^{\infty}\frac{x^{n+1}}{n+1}\bullet\sum_{n=0}^{\infty}x^{n}\\=&\sum_{n=1}^{\infty}\frac{x^{n}}{n}\bullet\sum_{n=0}^{\infty}x^{n}\\=&[-\ln(1-x)]\bullet\frac{1}{1-x}(-1<x<1).\end{aligned} $$ 

例 16.29 设函数  $ y = f(x) $ 满足  $ y'' + 2y' + 5y = 0 $，且  $ f(0) = 1 $， $ f'(0) = -1 $。

(1) 求  $ f(x) $ 的表达式；

(2) 设  $ a_{n}=\int_{n\pi}^{+\infty}f(x)dx $，求  $ \sum_{n=1}^{\infty}a_{n} $

解 (1) 由例 15.16 可知， $ f(x)=\mathrm{e}^{-x}\cos 2x $

(2) 由于  $ \int f(x)dx = \int e^{-x} \cos 2x dx = \frac{\left| \begin{array}{cc} (e^{-x})' & (\cos 2x)' \\ e^{-x} & \cos 2x \end{array} \right|}{(-1)^2 + 2^2} + C = \frac{-e^{-x} \cos 2x + 2e^{-x} \sin 2x}{5} + C $，因此  $ a_n = \frac{e^{-n\pi}}{5} $。