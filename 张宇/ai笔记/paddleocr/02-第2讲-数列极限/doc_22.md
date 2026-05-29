### 2.61 解 因为

 $$ 1\leqslant\sqrt[n]{1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n}}\leqslant\sqrt[n]{n}, $$ 

而 $ \lim_{n\to\infty}\sqrt[n]{n}=1 $，所以

 $$ \lim_{n\to\infty}\sqrt[n]{1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n}}=1\quad. $$ 

2.7 解 本题考虑夹逼准则. 由  $ f(x) $ 在  $ [a, b] $ 上连续，知  $ e^{f(x)} $ 在  $ [a, b] $ 上非负连续，且  $ 0 < m \leq e^{f(x)} \leq M $，其中 M，m 分别为  $ e^{f(x)} $ 在  $ [a, b] $ 上的最大值和最小值，于是  $ 0 < m \leq \frac{1}{n} \sum_{k=1}^{n} e^{f(x_k)} \leq M $，故

 $$ \sqrt[n]{m}\leqslant\sqrt[n]{\frac{1}{n}\sum_{k=1}^{n}\mathrm{e}^{f(x_{k})}}\leqslant\sqrt[n]{M}\quad. $$ 

又  $ \lim_{n\to\infty}\sqrt[n]{m}=\lim_{n\to\infty}\sqrt[n]{M}=1 $ ，根据夹逼准则，得  $ \lim_{n\to\infty}\sqrt[n]{\frac{1}{n}\sum_{k=1}^{n}e^{f(x_k)}}=1 $

2.8 证明 先证单调性. 由  $ x_{n}+(x_{n}-4)x_{n-1}=3 $ ，得  $ x_{n}=\frac{3+4x_{n-1}}{1+x_{n-1}} $ ，又  $ x_{1}=2 $ ，所以  $ x_{2}=\frac{3+4\times2}{1+2}=\frac{11}{3}> $  $ x_{1}>0 $ ，假设  $ x_{k}>x_{k-1}>0 $ 成立，则

 $$ x_{k+1}-x_{k}=\frac{3+4x_{k}}{1+x_{k}}-\frac{3+4x_{k-1}}{1+x_{k-1}}=\frac{x_{k}-x_{k-1}}{(1+x_{k})(1+x_{k-1})}>0, $$ 

故  $ x_{k+1} > x_{k} $，即数列  $ \{x_{n}\} $ 单调增加.

再证明其有界．因 $ x_{n}=\frac{3+4x_{n-1}}{1+x_{n-1}}=3+\frac{x_{n-1}}{1+x_{n-1}}<3+1=4 $，所以数列 $ \left\{x_{n}\right\} $有上界．

由单调有界准则知  $ \lim_{n\to\infty}x_n $ 存在. 设  $ \lim_{n\to\infty}x_n=A $，当  $ n\to\infty $ 时，由  $ x_n=\frac{3+4x_{n-1}}{1+x_{n-1}} $，得  $ A=\frac{3+4A}{1+A} $，解得  $ A=\frac{3\pm\sqrt{21}}{2} $，由题设， $ x_n>x_1>0 $，根据极限保号性可知 A>0，故  $ \lim_{n\to\infty}x_n=\frac{3+\sqrt{21}}{2} $.