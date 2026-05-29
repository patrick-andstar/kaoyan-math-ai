(3)常用的语言：①  $ \lim_{n\to\infty}x_n=a\Leftrightarrow $ 任意  $ \varepsilon>0 $，存在  $ N\in\mathbb{N}_+ $，当  $ n>N $ 时，恒有  $ |x_n-a|<\varepsilon $，且当  $ a=0 $ 时，称  $ x_n $ 为  $ n\to\infty $ 时的无穷小量。 $ x_n $ 与  $ a $ 的距离任意小不等关系

a. 与函数极限的定义作对比.

 $ \lim_{x\to+\infty}f(x)=a\Leftrightarrow $ 任意  $ \varepsilon>0 $ ，存在  $ X>0 $ ，当  $ x>X $ 时，恒有  $ |f(x)-a|<\varepsilon $

b. 定义中的 n > N，N 未必只能取整数，因为 n > 10 000 和 n > 10 000.1 表达的意思是一样的.

②  $ \lim_{n\to\infty}x_n=\infty\Leftrightarrow $ 任意  $ x>0 $，存在  $ N\in\mathbb{N}_+ $，当  $ n>N $ 时，恒有  $ |x_n|>x $。此时称  $ x_n $ 为  $ n\to\infty $ 时的无穷大量。

(4) 数列收敛与其子列收敛的关系.

定理 1 若数列  $ \{a_n\} $ 收敛，则其任何子列  $ \{a_{n_k}\} $ 也收敛，且  $ \lim_{k \to \infty} a_{n_k} = \lim_{n \to \infty} a_n $。

推论： $ \lim_{n\to\infty}a_n=a\Leftrightarrow\lim_{k\to\infty}a_{2k}=a $ 且  $ \lim_{k\to\infty}a_{2k-1}=a $

 $ \lim_{k\to+\infty}a_{3k}=\lim_{k\to+\infty}a_{3k+1}=a $，推不出 $ \lim_{n\to\infty}a_n=a $。

 $$ A\Rightarrow B\cap C $$ 

 $$ \overline{B}\cup\overline{C}\Rightarrow\overline{A} $$ 

因为 $ a_{3k+2} $缺失

此定理为我们提供了一个判断数列发散的方法：对于一个数列  $ \{a_{n}\} $，如果能找到一个发散的子列，则原数列一定发散；如果能找到至少两个收敛的子列  $ \{a_{n_{i}}\} $ 和  $ \{a_{n_{i}}\} $，但它们收敛到不同极限，则原数列也一定发散。

如  $ \left\{n^{(-1)^{n}}\right\} $，详见例 2.3.

再例如，对于数列  $ \left\{(-1)^{n}\right\} $： $ -1, 1, -1, 1, \cdots, (-1)^{n}, \cdots $，我们找到其收敛的子列

 $$ \left\{\left(-1\right)^{2k}\right\}:1,1,\cdots,1,\cdots;\left\{\left(-1\right)^{2k-1}\right\}:-1,-1,\cdots,-1,\cdots, $$ 

它们的极限分别为 1 和 -1，所以原数列发散。

例 2.2 证明：若  $ \lim_{n\to\infty}a_n=A $，则  $ \lim_{n\to\infty}|a_n|=|A| $。

♣分析 证明  $ \lim_{n\to\infty}|a_n|=|A| $，关键是要找到  $ \|a_n|-|A\| $ 与  $ |a_n-A| $ 的关系，这时就要联想到三角不等式。

证 因为  $ \lim_{n\to\infty}a_n=A $，所以对任意正数  $ \varepsilon $，存在正整数 N，当  $ n>N $ 时，有

 $$ \left|a_{n}-A\right|<\varepsilon. $$ 

又由不等式 $ \left|a\right|-\left|b\right|\leqslant\left|a-b\right| $，有

 $$ \left|\begin{array}{c}\left|a_{n}\right|-\left|A\right|\end{array}\right|\leqslant\left|a_{n}-A\right|<\varepsilon. $$ 

故  $ \lim_{n\to\infty}|a_n|=|A| $