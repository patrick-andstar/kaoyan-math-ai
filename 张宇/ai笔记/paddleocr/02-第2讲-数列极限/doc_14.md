非零解．证明： $ \{x_{n}\} $ 收敛．

♡ 分析 ①验： $ x_{1}>a>0 $

②设： $ x_{k}>a>0 $

③证： $ x_{k+1}>a>0 $

 $$ x_{k+1}=2\ln(1+x_{k}),\ 2\ln(1+a)=a\ . $$ 

由于 $ f(x)=2\ln(1+x) $在x>0时单调递增，因此 $ 2\ln(1+x_k)>2\ln(1+a) $，故 $ x_{k+1}>a $，于是 $ \{x_n\} $有下界。再由 $ \{x_n\} $单调递减，知 $ \{x_n\} $收敛。

★ c. 利用重要不等式（见夹逼准则的注(2)）.

→用得不多

d.  $ x_{n}-x_{n-1} $ 与  $ x_{n-1}-x_{n-2} $ 同号，则  $ \{x_{n}\} $ 单调.

★ e. 利用结论： $ x_{n+1}=f(x_n)(n=1,2,\cdots), x_n\in $ 区间 I.

无法确定是单调递增还是单调递减

若 $ f'(x)>0, x\in $区间 $ I $，则数列 $ \{x_n\} $单调，且 $ \begin{cases} 当x_2>x_1\text{时，数列}\{x_n\}\text{单调增加，} \\ 当x_2<x_1\text{时，数列}\{x_n\}\text{单调减少。} \end{cases} $

 $ f(x) $单调增加 证明见例2.13

可以通过例题帮助理解结论

若 $ f'(x)<0, x\in $区间 $ I $，则数列 $ \{x_n\} $不单调。

 $ f(x) $ 单调减少

例2.12 设  $ 0 < x_{1} < 3 $,  $ x_{n+1} = \sqrt{x_{n}(3 - x_{n})} $ ( $ n = 1, 2, \cdots $), 证明数列  $ \{x_{n}\} $ 的极限存在, 并求此极限.

分析 证明这种由递推形式给出的数列的收敛性, 一般都是根据“单调有界数列必收敛”这一准则进行证明; 在证明了极限存在的前提下再求极限.

证 由例 2.1 知数列  $ \{x_n\} $ 是有界的，对任意正整数  $ n > 1 $，都有  $ 0 < x_n \leq \frac{3}{2} \rightarrow \frac{\sqrt{ab} \leq \frac{a+b}{2}(a, b > 0)}{} $ 重要不等式

再证明  $ \{x_n\} $ 单调：当  $ n > 1 $ 时，

 $$ \begin{aligned}x_{n+1}-x_{n}&=\sqrt{x_{n}(3-x_{n})}-x_{n}=\sqrt{x_{n}}(\sqrt{3-x_{n}}-\sqrt{x_{n}})\\&=\frac{2\sqrt{x_{n}}\left(\frac{3}{2}-x_{n}\right)}{\sqrt{3-x_{n}}+\sqrt{x_{n}}}=\sqrt{x_{n}}\cdot\frac{ 分子有理化 }{\sqrt{3-x_{n}}+\sqrt{x_{n}}}\geqslant0,\quad\begin{aligned}& 由 x_{n}\leqslant\frac{3}{2}, 得 3-2x_{n}\geqslant0.\\& 再由 \sqrt{x_{n}}\geqslant0,\sqrt{3-x_{n}}\geqslant0.\end{aligned}\end{aligned} $$ 

即  $ x_{n+1} \geqslant x_{n}(n > 1) $，所以数列  $ \left\{x_{n}\right\}(n > 1) $ 是单调增加的。

 $$ \lim_{n\to\infty}x_{n}\xlongequal{ 存在 }a\leftarrow $$ 

根据单调有界数列必有极限的准则知 $ \lim_{n\to\infty}x_{n} $存在，设其为a，则

 $$ \underbrace{a=\lim_{n\to\infty}x_{n}}_{}=\lim_{n\to\infty}\sqrt{x_{n-1}(3-x_{n-1})}=\sqrt{a(3-a)}, $$ 

解得  $ a=\frac{3}{2} $ 或 a=0 （舍去）. 故

对题干等式两边取极限



由于  $ \{x_{n}\} $ 单调增加，且  $ x_{n}>0 $ ，故 a>0