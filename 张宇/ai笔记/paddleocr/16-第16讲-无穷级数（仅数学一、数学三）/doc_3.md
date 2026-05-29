现将级数中的各项逐一相加，得到下面这些和：

 $$ S_{1}=u_{1},S_{2}=u_{1}+u_{2},S_{3}=u_{1}+u_{2}+u_{3},\cdots,S_{n}=u_{1}+u_{2}+\cdots+u_{n},\cdots, $$ 

方法：

①写 $ S_{n}=u_{1}+u_{2}+\cdots+u_{n} $

> 叫数项级数的前n项和

②求 $ \lim_{n\to\infty}S_n $

这称为级数的部分和， $ \{S_n\} $ 就是级数的部分和数列。显然，我们愿意去研究当  $ n \to \infty $ 时所发生的事情，因为  $ \lim_{n \to \infty} S_n = \sum_{n=1}^{\infty} u_n $，这便道出了无穷多项相加的方法：用极限工具来处理。若  $ \lim_{n \to \infty} S_n = S $（一个存在的有限数），则称  $ \sum_{n=1}^{\infty} u_n $ 收敛，并称  $ S $ 为该收敛级数  $ \sum_{n=1}^{\infty} u_n $ 的和；若  $ \lim_{n \to \infty} S_n $ 不存在，则称  $ \sum_{n=1}^{\infty} u_n $ 发散。雅各布·伯努利曾在自己的文章中这样写道：“末项消逝的无穷级数之和有时有限而有时无限或不定。”这里的“有限”与“无限或不定”就分别对应着“收敛”与“发散”。

研究一个级数  $ \sum_{n=1}^{\infty}u_{n} $ 是收敛还是发散，也可以简单说成研究级数  $ \sum_{n=1}^{\infty}u_{n} $ 的敛散性.

如判别几何级数（也叫等比级数）

 $$ \sum_{n=1}^{\infty}a q^{n-1}=a+a q+a q^{2}+\cdots+a q^{n-1}+\cdots $$ 

的敛散性，其中 $ a\neq0 $

在公比 q 满足  $ |q| < 1 $ 的情形下，初等数学知识告诉我们，部分和

 $$ S_{n}=\frac{a(1-q^{n})}{1-q}, $$ 

判别级数发散性的步骤：

①写 $ S_{n}=\frac{a(1-q^{n})}{1-q} $

且  $ \lim_{n\to\infty}q^n=0 $ ，因此  $ \lim_{n\to\infty}S_n=\frac{a}{1-q} $ ，这个极限是存在的，故当  $ |q|<1 $ 时， $ \sum_{n=1}^{\infty}aq^{n-1} $ 收敛。

②算 $ \lim_{n\to\infty}S_{n} $是否存在



反之，当 $ |q|\geq1 $时， $ \sum_{n=1}^{\infty}a q^{n-1} $是发散的，这是因为

若 q > 1，则  $ \lim_{n \to \infty} q^n = +\infty, \lim_{n \to \infty} S_n $ 不存在；

若 q=1，则  $ \sum_{n=1}^{\infty}a q^{n-1}=a+a+\cdots+a+\cdots $（无穷多个 a 相加）， $ \lim_{n\to\infty}S_{n}=\lim_{n\to\infty}na=\begin{cases}+\infty,&a>0,\\-\infty,&a<0,\quad n\to\infty\end{cases} $  $ \lim_{n\to\infty}S_{n} $ 亦不存在；

(考生可轻易看出，当 $ q\geq1 $时， $ \lim_{n\to\infty}S_n $为 $ \pm\infty $，到底是 $ + \infty $还是 $ - \infty $，由a的正负决定)

若 $q=-1$，则 $\sum_{n=1}^{\infty} a q^{n-1} = a + (-a) + a + (-a) + \cdots$，这是一个十分著名且有趣的级数，欧拉、莱布尼茨都在这个级数的敛散性判别上犯了错误，今天的我们当然可以清晰地给出正确答案，部分和 $S_1 = a$，$S_2 = 0$，$S_3 = a$，$S_4 = 0$，$\cdots$，它们交错着等于 $a$ 和 $0$，显然 $\lim_{n \to \infty} S_n$ 不存在（不唯一，自然不存在）；