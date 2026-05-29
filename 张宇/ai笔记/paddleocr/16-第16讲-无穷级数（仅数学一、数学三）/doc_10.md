考虑到  $ \lim_{n\to\infty}\frac{\sin(n^{-\alpha}\ln n)}{n^{-\alpha}\ln n}=1 $ ，故原级数与  $ \sum_{n=2}^{\infty}n^{-\alpha}\ln n $ 敛散性相同.

①当 $ 0<\alpha\leq1 $，且n充分大时，有 $ \frac{\ln n}{n^{\alpha}}>\frac{1}{n^{\alpha}}>0 $，而 $ \sum_{n=2}^{\infty}\frac{1}{n^{\alpha}} $发散，故 $ \sum_{n=2}^{\infty}\frac{\ln n}{n^{\alpha}} $发散.

②当  $ \alpha > 1 $ 时，总存在充分小的  $ \varepsilon > 0 $，使  $ \alpha - \varepsilon > 1 $，此时  $ \lim_{n \to \infty} \frac{\frac{\ln n}{n^{\alpha}}}{\frac{1}{n^{\alpha - \varepsilon}}} = \lim_{n \to \infty} \frac{\ln n}{n^{\varepsilon}} = 0 $。由于  $ \sum_{n=2}^{\infty} \frac{1}{n^{\alpha - \varepsilon}} $ 收敛，故  $ \sum_{n=2}^{\infty} \frac{\ln n}{n^{\alpha}} $ 收敛。

对比例8.19



综上所述，当 $ 0<\alpha\leq1 $时，原级数发散，当 $ \alpha>1 $时，原级数收敛。选(D)。

注 懂得了以上道理，形如  $ e^{n^{-\alpha}\ln n}-1\sim\frac{\ln n}{n^{\alpha}} $， $ \ln(1+n^{-\alpha}\ln n)\sim\frac{\ln n}{n^{\alpha}}(n\rightarrow\infty) $ 等均可作为上例的变体形式出现在试卷中.

例 16.9 设  $ a_n > 0 $,  $ p > 1 $, 且  $ \lim_{n \to \infty} [n^p (\mathrm{e}^{\frac{1}{n}} - 1) a_n] = 1 $, 若级数  $ \sum_{n=1}^{\infty} a_n $ 收敛, 则  $ p $ 的取值范围是 ___.

解 应填 $ (2, +\infty) $

因为当  $ n \to \infty $ 时，  $ \mathrm{e}^{\frac{1}{n}} - 1 $ 与  $ \frac{1}{n} $ 是等价无穷小，所以由  $ \lim_{n \to \infty} [n^p (\mathrm{e}^{\frac{1}{n}} - 1) a_n] = 1 $，可知  $ \lim_{n \to \infty} \frac{a_n}{n} = 1 $。又级数  $ \sum_{n=1}^{\infty} a_n $ 收敛，故  $ \sum_{n=1}^{\infty} \frac{1}{n^{p-1}} $ 收敛，因此  $ p > 2 $。

例 16.10 设数列 $\{a_n\}$, $\{b_n\}$ 满足 $0 < a_n < \frac{\pi}{2}$, $0 < b_n < \frac{\pi}{2}$, $\cos a_n - a_n = \cos b_n$, 且级数 $\sum_{n=1}^{\infty} b_n$ 收敛.

证明：

$\lim_{n \to \infty} b_n = 0$

(1)  $ \lim_{n\to\infty}a_n=0 $；常见题型： $ \frac{u_n}{v_n}=w_n $， $ u_n\cdot v_n=\frac{u_n}{n}\cdot n\cdot v_n $，题型归纳不是关键，要学会分析题目，回归定义与性质

 $$ \begin{aligned}&\frac{u_{n}}{v_{n}}=w_{n},\quad u_{n}*v_{n}\begin{cases}\leqslant\frac{u_{n}^{2}+v_{n}^{2}}{2},\\=\frac{u_{n}}{n}*n*v_{n}\\=\frac{u_{n}}{v_{n}}*v_{n}^{2},\end{cases}\\ \end{aligned} $$ 

(2) 级数  $ \sum_{n=1}^{\infty}\frac{a_{n}}{b_{n}} $ 收敛.

证 (1) 由例 2.11 可知  $ \lim_{n\to\infty}a_n=0 $