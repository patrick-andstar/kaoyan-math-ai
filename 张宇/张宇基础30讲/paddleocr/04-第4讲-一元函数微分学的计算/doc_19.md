 $$ f^{(n)}(0)=(-1)^{n-3}n(n-1)(n-3)!=\frac{(-1)^{n-1}n!}{n-2}(n\geqslant3)\ . $$ 

方法二 利用泰勒展开，

 $$ f(x)=x^{2}\ln(1+x)=x^{2}\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}x^{n}=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}x^{n+2}=\sum_{n=3}^{\infty}\frac{(-1)^{n-3}}{n-2}x^{n}, $$ 

由泰勒展开系数的唯一性，得 $ \frac{(-1)^{n-3}}{n-2}=\frac{f^{(n)}(0)}{n!} $，故 $ f^{(n)}(0)=\frac{(-1)^{n-3}}{n-2}n!=\frac{(-1)^{n-1}}{n-2}n!(n\geqslant3) $.