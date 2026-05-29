 $$ \sum_{i=1}^{n}\sum_{j=1}^{n}\frac{1}{(1+x_{i})(1+y_{j}^{2})}\frac{1}{n^{2}}=\sum_{i=1}^{n}\sum_{j=1}^{n}\frac{1}{\left(1+\frac{i}{n}\right)\left(1+\frac{j^{2}}{n^{2}}\right)}\frac{1}{n^{2}}=\sum_{i=1}^{n}\sum_{j=1}^{n}\frac{n}{(n+i)(n^{2}+j^{2})} $$ 

是函数 $ f(x,y) $在D上的一个二重积分，所以

 $$ \lim_{n\to\infty}\sum_{i=1}^{n}\sum_{j=1}^{n}\frac{n}{(n+i)(n^{2}+j^{2})}=\iint_{D}\frac{1}{(1+x)(1+y^{2})}\mathrm{d}x\mathrm{d}y=\int_{0}^{1}\mathrm{d}x\int_{0}^{1}\frac{1}{(1+x)(1+y^{2})}\mathrm{d}y. $$ 

注 $ ^{1} $(1) 实际还可以用 “配凑法”，直接从题干出发.

 $$ \begin{aligned}\lim_{n\rightarrow\infty}\sum_{i=1}^{n}\sum_{j=1}^{n}\frac{n}{(n+i)(n^{2}+j^{2})}=&\lim_{n\rightarrow\infty}\sum_{i=1}^{n}\sum_{j=1}^{n}\frac{1}{\left(1+\frac{i}{n}\right)\left(1+\frac{j^{2}}{n^{2}}\right)}\cdot\frac{1}{n^{2}}\\=&\lim_{n\rightarrow\infty}\sum_{i=1}^{n}\sum_{j=1}^{n}\frac{1}{1+\frac{i}{n}}\cdot\frac{1}{1+\frac{j^{2}}{n^{2}}}\cdot\frac{1}{n}\cdot\frac{1}{n}\\=&\int_{0}^{1}\mathrm{d}x\int_{0}^{1}\frac{1}{(1+x)(1+y^{2})}\mathrm{d}y.\end{aligned} $$ 

(2) 此题结果为  $ \frac{\pi}{4} \ln 2 $

14.2 (D) 解 所给问题为直角坐标系下的二重积分，积分区域  $ D=\left\{(x,y)\mid x^{2}+y^{2}\leq2y\right\} $ 在直角坐标系下可以表示为  $ x^{2}+(y-1)^{2}\leq1 $，即圆心在  $ (0,1) $，半径为 1 的圆域。因此区域 D 可表示为

 $$ -1\leqslant x\leqslant1,\;1-\sqrt{1-x^{2}}\leqslant y\leqslant1+\sqrt{1-x^{2}}, $$ 

也可以表示为

 $$ 0\leqslant y\leqslant2,-\sqrt{2y-y^{2}}\leqslant x\leqslant\sqrt{2y-y^{2}}. $$ 

因此

 $$ \iint\limits_{D}f(xy)\mathrm{d}x\mathrm{d}y=\int_{-1}^{1}\mathrm{d}x\int_{1-\sqrt{1-x^{2}}}^{1+\sqrt{1-x^{2}}}f(xy)\mathrm{d}y, $$ 

可知(A)不正确.又

 $$ \iint\limits_{D}f(xy)\mathrm{d}x\mathrm{d}y=\int_{0}^{2}\mathrm{d}y\int_{-\sqrt{2y-y^{2}}}^{\sqrt{2y-y^{2}}}f(xy)\mathrm{d}x, $$ 

且题设中没有给出f为偶函数的条件，可知(B)也不正确.

在极坐标系下， $ x^{2}+y^{2}=2y $ 转化为  $ r=2\sin\theta $ 。因此 D 可以表示为

 $$ 0\leqslant\theta\leqslant\pi,0\leqslant r\leqslant2\sin\theta, $$ 

因此