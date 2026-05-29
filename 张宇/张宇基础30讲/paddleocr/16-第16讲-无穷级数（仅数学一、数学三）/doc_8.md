 $$ \frac{1}{c}=\frac{1}{2}\left(\frac{1}{a}+\frac{1}{b}\right). $$ 

于是， $ \sum_{n=1}^{\infty}\frac{1}{n} $ 叫作调和级数.

注2  $ \sum_{n=1}^{\infty}\frac{1}{n^{p}} $ 叫作 p 级数，调和级数  $ \sum_{n=1}^{\infty}\frac{1}{n} $ 是 p 级数中 p=1 时的特殊情况。这里不加证明地给出重要结论：

$p$ 级数 $\sum_{n=1}^{\infty}\frac{1}{n^{p}}\left\{\begin{aligned}& 发散, &p\leqslant1,\\& 收敛, &p>1.\end{aligned}\right.$

对比记忆 $p$ 积分 $\int_{1}^{+\infty}\frac{1}{x^{p}}dx$ 发散，$p\leqslant1$ 收敛，$p>1$

这个结论十分重要，在比较判别法中，常选取比较对象为  $ \sum_{n=1}^{\infty}\frac{1}{n^{p}} $ 或者  $ \sum_{n=0}^{\infty}aq^{n} $，在以后的多种场合都会派上用场，考生需牢记。

例 16.5 设正项级数  $ \sum_{n=1}^{\infty}a_{n} $ 收敛，证明：级数  $ \sum_{n=1}^{\infty}a_{n}^{2} $ 收敛.

回顾：若  $ \lim_{n\to\infty}a_n=a>0 $ ，则有  $ a_n>0 $

证 由  $ \sum_{n=1}^{\infty}a_{n} $ 收敛可得  $ \lim_{n\to\infty}a_{n}=0 $，即当  $ n\to\infty $ 时（存在  $ N>0 $，当  $ n>N $ 时）， $ a_{n}<M $（极限的有界性），于是  $ a_{n}^{2}=a_{n}\cdot a_{n}<Ma_{n} $，故由比较判别法知  $ \sum_{n=1}^{\infty}a_{n}^{2} $ 收敛。

 $$ \sum_{n=1}^{\infty}a_{n}^{3}=\sum_{n=1}^{\infty}a_{n}\cdot a_{n}^{2}<M\sum_{n=1}^{\infty}a_{n}^{2} $$ 

利用  $ \sum a_{2n+1} < \sum a_{n} $

注 本题的结论应当记住，如下例就用到了它。同样的方法可以证明  $ \sum a_{n}^{3}, \sum a_{2n}, \sum a_{2n+1} $ 都收敛。

例 16.6 (1) 设  $ \sum_{n=1}^{\infty} u_n $ 是正项级数，若  $ \sum_{n=1}^{\infty} \sqrt{u_n u_{n+1}} $ 收敛，且  $ \{u_n\} $ 单调减少，证明： $ \sum_{n=1}^{\infty} u_n $ 收敛；

(2) 设  $ \sum_{n=1}^{\infty} u_n $ 和  $ \sum_{n=1}^{\infty} v_n $ 都是正项级数，且  $ \sum_{n=1}^{\infty} u_n $ 和  $ \sum_{n=1}^{\infty} v_n $ 都收敛，证明： $ \sum_{n=1}^{\infty} u_n v_n $ 收敛。

证 (1) 由  $ \{u_n\} $ 单调减少可得  $ u_{n+1} \leq u_n $，两边同时乘以  $ u_{n+1} $，进而可得  $ u_{n+1}^2 \leq u_n u_{n+1} $，于是  $ u_{n+1} \leq \sqrt{u_n u_{n+1}} $。因为  $ \sum_{n=1}^{\infty} \sqrt{u_n u_{n+1}} $ 收敛，所以  $ \sum_{n=1}^{\infty} u_n $ 收敛。

(2)由 $ \sum_{n=1}^{\infty}u_{n} $和 $ \sum_{n=1}^{\infty}v_{n} $收敛可得 $ \sum_{n=1}^{\infty}u_{n}^{2} $和 $ \sum_{n=1}^{\infty}v_{n}^{2} $收敛，且 $ u_{n}v_{n}\leq\frac{1}{2}(u_{n}^{2}+v_{n}^{2}) $，故由比较判别法知 $ \sum_{n=1}^{\infty}u_{n}v_{n} $收敛.