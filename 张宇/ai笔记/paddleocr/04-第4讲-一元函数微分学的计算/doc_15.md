由于 $ f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}x^{n} $，根据函数展开式的唯一性，比较系数，有 $ n=m+3 $，所以

 $$ \frac{f^{(n)}(0)}{n!}=-\frac{1}{m+1}, $$ 

即 $ f^{(n)}(0)=-\frac{n!}{n-2} $

方法总结 对于  $ g(x)=x^{k}f(x) $ 型，可以考虑用泰勒公式求  $ g^{(n)}(0) $.

公式  $ \ln(1+x)=\sum_{n=1}^{\infty}(-1)^{n-1}\frac{x^{n}}{n}=x-\frac{x^{2}}{2}+\frac{x^{3}}{3}-\frac{x^{4}}{4}+\cdots+(-1)^{n-1}\frac{x^{n}}{n}+\cdots,-1<x\leqslant1 $

注

 $$ f(x)=x^{2}\ln(1-x)=x^{2}\left(-x-\frac{x^{2}}{2}-\cdots-\frac{x^{n-2}}{n-2}-\cdots\right) $$ 

又 $ f(x)=f(0)+f'(0)x+\frac{f''(0)}{2!}x^{2}+\cdots+\frac{f^{(n)}(0)}{n!}x^{n}+\cdots $，根据展开式的唯一性，对比 $ x^{n} $的系数，得 $ -\frac{1}{n-2}=\frac{f^{(n)}(0)}{n!} $，故 $ f^{(n)}(0)=-\frac{n!}{n-2} $。

例4.19 设 $ f(x)=x^22^x $，则当 $ n\geq1 $时， $ f^{(n)}(0)= $___。

☐ 分析 本题可以用莱布尼茨求导公式，也可以用泰勒公式。

莱布尼茨法： $ x^{2} $幂次较低， $ f^{(n)}(x) $只有3项。

泰勒公式： $ 2^{x} $ 没有泰勒展开式，需要对其变形后再展开。

解 应填  $ n(n-1)(\ln 2)^{n-2} $

方法一 利用泰勒公式展开，有

 $$ f(x)=x^{2}2^{x}=x^{2}\mathrm{e}^{x\ln2}=x^{2}\sum_{n=0}^{\infty}\frac{\left(x\ln2\right)^{n}}{n!}=\sum_{n=0}^{\infty}\frac{\left(\ln2\right)^{n}}{n!}x^{n+2}=\sum_{n=2}^{\infty}\frac{\left(\ln2\right)^{n-2}}{(n-2)!}x^{n}, $$ 

又 $ f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}x^{n} $，由泰勒展开式的唯一性，得 $ \frac{(\ln2)^{n-2}}{(n-2)!}=\frac{f^{(n)}(0)}{n!} $。又 $ f'(0)=0 $，故

 $$ f^{(n)}(0)=\frac{(\ln2)^{n-2}}{(n-2)!}n!=n(n-1)(\ln2)^{n-2}(n=1,2,3,\cdots) $$ 

方法二 利用莱布尼茨高阶求导公式，有

 $$ \begin{aligned}f^{(n)}(x)&=\mathrm{C}_{n}^{0}x^{2}\left(2^{x}\right)^{(n)}+\mathrm{C}_{n}^{1}\bullet2x\bullet\left(2^{x}\right)^{(n-1)}+\mathrm{C}_{n}^{2}\bullet2\bullet\left(2^{x}\right)^{(n-2)}\\&=x^{2}\bullet2^{x}\bullet(\ln2)^{n}+n\bullet2x\bullet2^{x}\bullet(\ln2)^{n-1}+\frac{n(n-1)}{2}\bullet2\bullet2^{x}\bullet(\ln2)^{n-2},\end{aligned} $$ 

当x=0时， $ f^{(n)}(0)=n(n-1)(\ln2)^{n-2}(n=1,2,3,\cdots) $

方法总结 对于  $ g(x)=x^{k}f(x) $ 型，k 取值较小，本题可以用莱布尼茨求导公式，也可以用泰勒公式。