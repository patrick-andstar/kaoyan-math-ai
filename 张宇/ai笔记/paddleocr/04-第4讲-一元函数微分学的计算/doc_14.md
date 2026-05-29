 $$ \begin{aligned}&\mathrm{e}^{x}=\sum_{n=0}^{\infty}\frac{x^{n}}{n!}=1+x+\frac{x^{2}}{2!}+\cdots+\frac{x^{n}}{n!}+\cdots,-\infty<x<+\infty.\\ &\frac{1}{1+x}=\sum_{n=0}^{\infty}(-1)^{n}x^{n}=1-x+x^{2}-x^{3}+\cdots+(-1)^{n}x^{n}+\cdots,-1<x<1.\\ &\frac{1}{1-x}=\sum_{n=0}^{\infty}x^{n}=1+x+x^{2}+\cdots+x^{n}+\cdots,-1<x<1.\\ &\ln(1+x)=\sum_{n=1}^{\infty}(-1)^{n-1}\frac{x^{n}}{n}=x-\frac{x^{2}}{2}+\frac{x^{3}}{3}-\frac{x^{4}}{4}+\cdots+(-1)^{n-1}\frac{x^{n}}{n}+\cdots,-1<x\leq1.\\ &\sin x=\sum_{n=0}^{\infty}(-1)^{n}\frac{x^{2n+1}}{(2n+1)!}=x-\frac{x^{3}}{3!}+\frac{x^{5}}{5!}-\frac{x^{7}}{7!}+\cdots+(-1)^{n}\frac{x^{2n+1}}{(2n+1)!}+\cdots,-\infty<x<+\infty.\\ &\cos x=\sum_{n=0}^{\infty}(-1)^{n}\frac{x^{2n}}{(2n)!}=1-\frac{x^{2}}{2!}+\frac{x^{4}}{4!}-\frac{x^{6}}{6!}+\cdots+(-1)^{n}\frac{x^{2n}}{(2n)!}+\cdots,-\infty<x<+\infty.\\ &(1+x)^{\alpha}=1+\alpha x+\frac{\alpha(\alpha-1)}{2!}x^{2}+\cdots+\frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}x^{n}+\cdots,\begin{cases}x\in(-1,1),&\alpha\leq-1,\\x\in(-1,1],&-1<\alpha<0,\\x\in[-1,1],&\alpha>0,\alpha\notin\mathbf{N}_{+},\\x\in\mathbf{R},&\alpha\in\mathbf{N}_{+}.\end{cases}\\ &\tan x=x+\frac{1}{3}x^{3}+\cdots.\\ &\arcsin x=x+\frac{1}{6}x^{3}+\cdots.\\ &\arctan x=x-\frac{1}{3}x^{3}+\cdots.\\ &\end{aligned} $$ 

③函数泰勒展开式的唯一性：无论 $ f(x) $由何种方法展开，其泰勒展开式具有唯一性.于是我们可以通过比较①，②中公式的系数，获得 $ f^{(n)}(x_{0}) $或者 $ f^{(n)}(0) $.

例 4.18 设  $ f(x)=x^{2}\ln(1-x) $，则当  $ n \geq 3 $ 时， $ f^{(n)}(0)= $（）.

(A) $ -\frac{n!}{n-2} $ (B) $ \frac{n!}{n-2} $ (C) $ -\frac{(n-2)!}{n} $ (D) $ \frac{(n-2)!}{n} $

☐分析 本题可以用莱布尼茨求导公式，也可以用泰勒公式.

若用泰勒公式，先抽象展开， $ f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}x^{n} $，然后用具体展开， $ f(x)=-\sum_{m=0}^{\infty}\frac{x^{m+3}}{m+1} $，最后令 $ x^{n} $的系数相等。

解 应选(A).

利用泰勒公式展开，有

 $$ f(x)=x^{2}\ln(1-x)=x^{2}\cdot\sum_{m=1}^{\infty}(-1)^{m-1}\cdot\frac{(-1)^{m}x^{m}}{m}=-\sum_{m=1}^{\infty}\frac{x^{m+2}}{m}=-\sum_{m=0}^{\infty}\frac{x^{m+3}}{m+1} $$ 