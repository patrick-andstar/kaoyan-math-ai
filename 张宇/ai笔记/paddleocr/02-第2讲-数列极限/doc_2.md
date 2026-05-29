这两个子列的项在原数列中交错出现。

(2) 等差数列.

首项为  $ a_{1} $，公差为  $ d(d \neq 0) $ 的数列  $ a_{1}, a_{1} + d, a_{1} + 2d, \cdots, a_{1} + (n - 1)d, \cdots $.

①通项公式 $ a_{n}=a_{1}+(n-1)d $

②前 n 项的和  $ S_{n}=\frac{n}{2}\left[2a_{1}+(n-1)d\right]=\frac{n}{2}(a_{1}+a_{n}) $

(3) 等比数列.

首项为  $ a_{1} $，公比为  $ r(r \neq 0) $ 的数列  $ a_{1}, a_{1}r, a_{1}r^{2}, \cdots, a_{1}r^{n-1}, \cdots $.

①通项公式 $ a_{n}=a_{1}r^{n-1} $

②前 n 项的和  $ S_{n}=\begin{cases}na_{1},&r=1,\\\dfrac{a_{1}(1-r^{n})}{1-r},&r\neq1.\end{cases} $

③常用  $ 1+r+r^{2}+\cdots+r^{n-1}=\frac{1-r^{n}}{1-r}(r\neq1) $ →有限项和不会发散，收敛和发散的概念，只在无穷项时会涉及

这两个求和公式针对的前n项和，即有限项和，当讨论无限项和时，需要使用无穷级数理论

(4) 单调数列.

若对所有正整数  $ n $，有  $ a_{n+1} \geqslant a_n (a_{n+1} \leqslant a_n) $，则称数列  $ \{a_n\} $ 为单调不减（不增）数列。将  $ \geqslant (\leqslant) $ 换成  $ > (<) $，则称为单调递增（递减）数列。单调递增数列与单调递减数列统称为单调数列。

(5) 有界数列.

若对所有正整数  $ n $，存在正实数  $ M $，有  $ |a_n| \leq M $，则称数列  $ \{a_n\} $ 为有界数列。

①找 M，使得  $ |a_n| \leqslant M $；

证明数列有界的几种方法：

②放缩法；



③找最值；

④基本不等式法.

(6) 一些常见数列前 n 项的和.

 $$ \sum_{k=1}^{n}k=1+2+3+\cdots+n=\frac{n(n+1)}{2} $$ 

 $$ \begin{aligned}& \textcircled{2} \sum_{k=1}^{n}k^{2}=1^{2}+2^{2}+3^{2}+\cdots+n^{2}=\frac{n(n+1)(2n+1)}{6}．\\ &\begin{aligned}\\ &\star\textcircled{3} \sum_{k=1}^{n}\frac{1}{k(k+1)}=\frac{1}{1\times2}+\frac{1}{2\times3}+\frac{1}{3\times4}+\cdots+\frac{1}{n(n+1)}=\frac{n}{n+1}．\\ &\end{aligned}\\ &\\ &\lim_{n\rightarrow\infty}\sum_{k=1}^{n}\frac{1}{k(k+1)}=\lim_{n\rightarrow\infty}\frac{n}{n+1}=1\\ \end{aligned}\begin{aligned}\\ & 怎么算出来吗？\quad 复项相消 \\ &\rightarrow\begin{aligned}\\ &=1-\frac{1}{2}+\frac{1}{2}-\frac{1}{3}+\frac{1}{3}-\frac{1}{4}+\cdots+\frac{1}{n-\frac{1}{n+1}}\\ &\end{aligned}\\ &\begin{aligned}\\ &=1-\frac{1}{n+1}\\ &\end{aligned}\\ \end{aligned} $$ 