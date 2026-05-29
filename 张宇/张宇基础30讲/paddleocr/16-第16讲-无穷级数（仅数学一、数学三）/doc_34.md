 $$ S^{\prime}(x)=\left(\sum_{n=0}^{\infty}a_{n}x^{n}\right)^{\prime}=\sum_{n=0}^{\infty}\left(a_{n}x^{n}\right)^{\prime}=\sum_{n=1}^{\infty}na_{n}x^{n-1}(|x|<R), $$ 

逐项求导后所得到的幂级数与原级数有相同的收敛半径，但收敛域可能缩小.

5 重要展开式 左  $ \xrightarrow{展开} $ 右 通过重要展开式间接求无穷级数的和函数 求和

(1)  $ e^{x} = \sum_{n=0}^{\infty} \frac{x^{n}}{n!} = 1 + x + \frac{x^{2}}{2!} + \cdots + \frac{x^{n}}{n!} + \cdots, -\infty < x < +\infty. $

 $$ \frac{1}{1+x}=\sum_{n=0}^{\infty}(-1)^{n}x^{n}=1-x+x^{2}-x^{3}+\cdots+(-1)^{n}x^{n}+\cdots,-1<x<1 $$ 

 $$ \frac{1}{1-x}=\sum_{n=0}^{\infty}x^{n}=1+x+x^{2}+\cdots+x^{n}+\cdots,-1<x<1 $$ 

 $$ \ln(1+x)=\sum_{n=1}^{\infty}(-1)^{n-1}\frac{x^{n}}{n}=x-\frac{x^{2}}{2}+\frac{x^{3}}{3}-\frac{x^{4}}{4}+\cdots+(-1)^{n-1}\frac{x^{n}}{n}+\cdots,-1<x\leqslant1 $$ 

 $$ \sum_{n=1}^{\infty}(-1)^{n-1}\frac{(-x)^{n}}{n}=\ln(1-x). $$ 

 $$ \begin{aligned}(5)\ \sin x=&\sum_{n=0}^{\infty}(-1)^{n}\frac{x^{2n+1}}{(2n+1)!}\\ 逐项 & 求导 \\=&x-\frac{x^{3}}{3!}+\frac{x^{5}}{5!}-\frac{x^{7}}{7!}+\cdots+(-1)^{n}\frac{x^{2n+1}}{(2n+1)!}+\cdots,-\infty<x<+\infty.\end{aligned} $$ 

 $$ \sum_{n=1}^{\bar{z}}\frac{x^{n}}{n}=-\ln(1-x) $$ 

 $$ \begin{aligned}\cos x=&\sum_{n=0}^{\infty}(-1)^{n}\frac{x^{2n}}{(2n)!}\\=&1-\frac{x^{2}}{2!}+\frac{x^{4}}{4!}-\frac{x^{6}}{6!}+\cdots+(-1)^{n}\frac{x^{2n}}{(2n)!}+\cdots,-\infty<x<+\infty.\end{aligned} $$ 

 $$ \begin{aligned}(7)\ \underline{\quad(1+x)^{\alpha}=1+\alpha x+\frac{\alpha(\alpha-1)}{2!}x^{2}}+\cdots+\frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}x^{n}+\cdots,\begin{cases}x\in(-1,1), 当 \alpha\leqslant-1 时 ,\\x\in(-1,1], 当 -1<\alpha<0 时 ,\\x\in[-1,1], 当 \alpha>0 且 \alpha\notin\mathbf{N}_{+} 时 ,\\x\in(-\infty,+\infty), 当 \alpha\in\mathbf{N}_{+} 时 .\end{cases}\\ 记住前 3 项就行 \end{aligned} $$ 

注 (1)～(6)右端x的取值范围是指收敛域，而对于(7)，问题比较复杂，其收敛区间的端点是否收敛与 $ \alpha $的取值有关，可以证明(这里不证)：

当  $ \alpha \leqslant -1 $ 时，收敛域为  $ (-1, 1) $;

当 $ -1<\alpha<0 $时，收敛域为 $ (-1,1] $;

当  $ \alpha > 0 $ 且  $ \alpha \notin \mathbf{N}_{+} $ 时，收敛域为  $ [-1, 1] $;

当  $ \alpha \in \mathbb{N}_+ $ 时，收敛域为  $ (-\infty, +\infty) $.

比如，当 $ \alpha=-1 $时，得到

 $$ \frac{1}{1+x}=1-x+x^{2}-x^{3}+\cdots+(-1)^{n}x^{n}+\cdots,-1<x<1\;; $$ 