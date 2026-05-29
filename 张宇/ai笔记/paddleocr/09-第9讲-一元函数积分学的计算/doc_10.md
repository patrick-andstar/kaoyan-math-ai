比如

 $$ \int\frac{1}{x+1}\mathrm{d}x=\ln\left|x+1\right|+C, $$ 

 $$ \int\frac{2}{(2x-1)^{2}}\mathrm{d}x=\int\frac{1}{(2x-1)^{2}}\mathrm{d}(2x-1)=-\frac{1}{2x-1}+C, $$ 

 $$ \int\frac{x-1}{x^{2}+1}\mathrm{d}x=\int\frac{1}{2}\frac{2x}{x^{2}+1}\mathrm{d}x-\int\frac{1}{x^{2}+1}\mathrm{d}x=\frac{1}{2}\ln(x^{2}+1)-\arctan x+C $$ 

利用分部积分逆推 $ I=\int\frac{\mathrm{d}x}{\left(1+x^{2}\right)^{2}} $，由于

 $$ \begin{aligned}\int\frac{1}{1+x^{2}}\mathrm{d}x&=\frac{x}{1+x^{2}}+\int x\cdot\frac{2x}{\left(1+x^{2}\right)^{2}}\mathrm{d}x\\&=\frac{x}{1+x^{2}}+2\int\frac{x^{2}+1-1}{\left(1+x^{2}\right)^{2}}\mathrm{d}x\\&=\frac{x}{1+x^{2}}+2\arctan x-2I,\end{aligned} $$ 

因此 $ I=\frac{x}{2(1+x^{2})}+\frac{1}{2}\arctan x+C $

(3) 方法（如何拆）.

① $ Q_{m}(x) $的一次单因式 $ ax+b $产生一项 $ \frac{A}{ax+b} $

② $ Q_{m}(x) $的k重一次因式 $ (ax+b)^{k} $产生k项，分别为 $ \frac{A_{1}}{ax+b},\frac{A_{2}}{(ax+b)^{2}},\cdots,\frac{A_{k}}{(ax+b)^{k}}(k=2,3,\cdots) $

③ $ Q_{m}(x) $的二次单因式 $ px^{2}+qx+r $产生一项 $ \frac{Ax+B}{px^{2}+qx+r} $

④ $ Q_{m}(x) $的k重二次因式 $ (px^{2}+qx+r)^{k} $产生k项，分别为

 $$ \frac{A_{1}x+B_{1}}{px^{2}+qx+r},\frac{A_{2}x+B_{2}}{\left(px^{2}+qx+r\right)^{2}},\cdots,\frac{A_{k}x+B_{k}}{\left(px^{2}+qx+r\right)^{k}} $$ 

比如， $ Q_{m}(x)=(ax+b)^{2}(px^{2}+qx+r)^{2} $，则有

 $$ \frac{P}{Q}=\frac{A_{1}}{ax+b}+\frac{A_{2}}{(ax+b)^{2}}+\frac{A_{3}x+B}{px^{2}+qx+r}+\frac{A_{4}x+C}{(px^{2}+qx+r)^{2}} $$ 

例 9.8 求  $ \int \frac{4x^{2}-6x-1}{(x+1)(2x-1)^{2}} dx $.

## 解 本题主要考查有理函数的积分

先将被积函数分解为最简有理分式之和。这时应有分解式

 $$ \frac{4x^{2}-6x-1}{(x+1)(2x-1)^{2}}=\frac{A}{x+1}+\frac{B}{2x-1}+\frac{C}{(2x-1)^{2}} $$ 