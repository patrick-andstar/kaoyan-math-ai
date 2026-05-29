 $$ \frac{\left[3+(-1)^{n}\right]^{n}}{n}\bullet\frac{(-1)^{n}}{4^{n}}=\begin{cases}-\frac{1}{(2k-1)\bullet2^{2k-1}},&n=2k-1,\\\frac{1}{2k},&n=2k.\end{cases} $$ 

由于 $ -\sum_{k=1}^{\infty}\frac{1}{(2k-1)\cdot2^{2k-1}} $收敛， $ \sum_{k=1}^{\infty}\frac{1}{2k} $发散，故 $ \sum_{n=1}^{\infty}\frac{\left[3+(-1)^{n}\right]^{n}}{n}\cdot\frac{(-1)^{n}}{4^{n}} $发散.

综上，幂级数的收敛域为 $ \left(-\frac{1}{4},\frac{1}{4}\right) $.

16.13 解 设

 $$ S(x)=\sum_{n=1}^{\infty}\left(\frac{1}{2n+1}-1\right)x^{2n},\;S_{1}(x)=\sum_{n=1}^{\infty}\frac{x^{2n}}{2n+1},\;S_{2}(x)=\sum_{n=1}^{\infty}x^{2n}, $$ 

则

 $$ S(x)=S_{1}(x)-S_{2}(x),x\in(-1,1). $$ 

由于

 $$ S_{2}(x)=\sum_{n=1}^{\infty}x^{2n}=\frac{x^{2}}{1-x^{2}}, $$ 

 $$ \left[xS_{1}(x)\right]^{\prime}=\sum_{n=1}^{\infty}x^{2n}=\frac{x^{2}}{1-x^{2}},x\in(-1,1), $$ 

因此

 $$ xS_{1}(x)=\int_{0}^{x}\frac{t^{2}}{1-t^{2}}\mathrm{d}t=-x+\frac{1}{2}\ln\frac{1+x}{1-x} $$ 

又由于

 $$ S_{1}(0)=0, $$ 

故

 $$ S_{1}(x)=\left\{\begin{aligned}&-1+\frac{1}{2x}\ln\frac{1+x}{1-x},&\left|x\right|\in(0,1),\\ &0,&x=0,\end{aligned}\right. $$ 

因此

 $$ S(x)=S_{1}(x)-S_{2}(x)=\begin{cases}\displaystyle\frac{1}{2x}\ln\frac{1+x}{1-x}-\frac{1}{1-x^{2}},&\left|x\right|\in(0,1),\\0,&x=0.\end{cases} $$ 

16.14 解

 $$ \sum_{n=0}^{\infty}\frac{(-1)^{n}(n^{2}-n+1)}{2^{n}}=\sum_{n=2}^{\infty}n(n-1)\left(-\frac{1}{2}\right)^{n}+\sum_{n=0}^{\infty}\left(-\frac{1}{2}\right)^{n}, $$ 

 $$ \sum_{n=0}^{\infty}\left(-\frac{1}{2}\right)^{n}=\frac{1}{1+\frac{1}{2}}=\frac{2}{3}. $$ 