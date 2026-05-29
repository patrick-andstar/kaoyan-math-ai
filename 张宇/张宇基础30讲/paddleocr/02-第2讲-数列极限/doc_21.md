2.8 设  $ x_{1}=2 $,  $ x_{n}+(x_{n}-4)x_{n-1}=3(n=2,3,\cdots) $，证明  $ \lim_{n\to\infty}x_n $ 存在，并求其值.

## 解答

2.1 (B) 解 数列极限的概念是描述变量在给定过程中的变化趋势，数列极限存在与否与前有限项的值无关，因此可以排除 (A).

由于  $ \lim_{n\to\infty}a_n=0,\lim_{n\to\infty}b_n=1 $ ，由极限四则运算规则可知  $ \lim_{n\to\infty}a_n b_n $ 必定存在，  $ \lim_{n\to\infty}\frac{b_n}{a_n} $ 不符合极限四则运算规则，由无穷小量的性质可知其肯定不存在．因此可以排除 (C)，(D)．故由排除法，应选 (B)．

2.2 (A) 解  $ \lim_{n\to\infty}\frac{x_{n+1}}{x_n}=\frac{1}{2}<1 $，由数列极限的保号性可知，存在正整数 N，当 n>N 时， $ \frac{x_{n+1}}{x_n}<1 $。又  $ x_n>0 $，于是  $ x_{n+1}<x_n $。所以  $ \{x_n\} $ 单调递减且有下界，于是  $ \lim_{n\to\infty}x_n $ 存在。

设  $ \lim_{n\to\infty}x_n=A\geq0 $ 。若 A>0 ，此时  $ \lim_{n\to\infty}\frac{x_{n+1}}{x_n}=\frac{\lim\limits_{n\to\infty}x_{n+1}}{\lim\limits_{n\to\infty}}=\frac{A}{A}=1 $ ，矛盾。于是 A=0 ，即  $ \lim_{n\to\infty}x_n=0 $ 。

2.3 1 解 所给极限为“ $ \infty-\infty $”型未定式，表达式中含有根式，可先将其变形，即

 $$ \begin{aligned}&\begin{aligned}\\ &\lim_{n\rightarrow\infty}(\sqrt{n+\sqrt{n}}-\sqrt{n-\sqrt{n}})\\=&\lim_{n\rightarrow\infty}\frac{(\sqrt{n+\sqrt{n}}-\sqrt{n-\sqrt{n}})\bullet(\sqrt{n+\sqrt{n}}+\sqrt{n-\sqrt{n}})}{\sqrt{n+\sqrt{n}}+\sqrt{n-\sqrt{n}}}\\ &\end{aligned}\\=&\lim_{n\rightarrow\infty}\frac{2\sqrt{n}}{\sqrt{n+\sqrt{n}}+\sqrt{n-\sqrt{n}}}=\lim_{n\rightarrow\infty}\frac{2}{\sqrt{1+\frac{1}{\sqrt{n}}}+\sqrt{1-\frac{1}{\sqrt{n}}}}=1.\\ \end{aligned} $$ 

2.4 100 解

 $$ \begin{aligned}\lim_{n\rightarrow\infty}\frac{n^{99}}{n^{k}-(n-1)^{k}}&=\lim_{n\rightarrow\infty}\frac{n^{99}}{n^{k}\left[1-\left(1-\frac{1}{n}\right)^{k}\right]}\\&=-\lim_{n\rightarrow\infty}\frac{n^{99-k}}{\left(1-\frac{1}{n}\right)^{k}}-1=-\lim_{n\rightarrow\infty}\frac{n^{99-k}}{k\left(-\frac{1}{n}\right)}=\frac{1}{k}\lim_{n\rightarrow\infty}n^{99-k+1}.\end{aligned} $$ 

由此可知，极限存在且不为零的充要条件是 $ 99-k+1=0 $，即k=100。

2.51 解 因为

 $$ \frac{n}{\sqrt{n^{2}+n}}\leqslant\sum_{i=1}^{n}\frac{1}{\sqrt{n^{2}+i}}\leqslant\frac{n}{\sqrt{n^{2}+1}}, $$ 

又  $ \lim_{n\to\infty}\frac{n}{\sqrt{n^{2}+n}}=\lim_{n\to\infty}\frac{n}{\sqrt{n^{2}+1}}=1 $ ，根据夹逼准则，所以原式 = 1.