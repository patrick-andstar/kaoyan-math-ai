 $$ \begin{aligned}\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}&=\frac{\sqrt{n+1}-\sqrt{n}}{\sqrt{n}\cdot\sqrt{n+1}}& 像 p 级数 , 故通分处理 \\ &=\frac{1}{\sqrt{n}\cdot\sqrt{n+1}(\sqrt{n+1}+\sqrt{n})}\sim\frac{1}{\sqrt{n}\cdot\sqrt{n}\cdot(\sqrt{n}+\sqrt{n})}\\ &=\frac{1}{2n^{\frac{3}{2}}}.\\ \end{aligned} $$ 

## 解 应选(A)

方法一  $ \left|\left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right)\sin(n+k)\right|\leq\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}=\frac{\sqrt{n+1}-\sqrt{n}}{\sqrt{n(n+1)}}=\frac{1}{\sqrt{n(n+1)}(\sqrt{n+1}+\sqrt{n})}\leq\frac{1}{n^{\frac{3}{2}}} $

因而原级数绝对收敛，选(A).

方法二  $ \left|\left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right)\sin(n+k)\right|\leq\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}} $

设  $ u_{n}=\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}} $，因为  $ \lim_{n\to\infty}u_{n}=0 $，且

 $$ \begin{aligned}S_{n}=&\frac{1}{\sqrt{1}}-\frac{1}{\sqrt{2}}+\frac{1}{\sqrt{2}}-\frac{1}{\sqrt{3}}+\cdots+\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\\=&1-\frac{1}{\sqrt{n+1}}\rightarrow1(n\rightarrow\infty),\end{aligned} $$ 

故  $ \sum_{n=1}^{\infty}u_{n}=\lim_{n\to\infty}S_{n}=1 $ ，即级数  $ \sum_{n=1}^{\infty}\left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right) $ 收敛，故原级数绝对收敛．选(A).

例 16.19 若  $ \sum_{n=1}^{\infty}nu_{n} $ 绝对收敛， $ \sum_{n=1}^{\infty}\frac{v_{n}}{n} $ 条件收敛，则（）.

(A)  $ \sum_{n=1}^{\infty}u_{n}v_{n} $ 条件收敛

(B)  $ \sum_{n=1}^{\infty}u_{n}v_{n} $ 绝对收敛

(C)  $ \sum_{n=1}^{\infty}(u_{n}+v_{n}) $ 收敛

(D)  $ \sum_{n=1}^{\infty}(u_{n}+v_{n}) $ 发散

 $ \sum_{n=1}^{\infty}nu_{n} $ 绝对收敛  $ \sum_{n=1}^{\infty}\frac{v_{n}}{n} $ 条件收敛

(2) 分析  $ u_n \cdot v_n = \underline{nu_n} \cdot \frac{v_n}{n} $，又  $ 0 \leq |u_n \cdot v_n| = |nu_n| \cdot \left| \frac{v_n}{n} \right| $，由  $ \lim_{n \to \infty} \frac{v_n}{n} = 0 $，故  $ n $ 充分大时， $ \left| \frac{v_n}{n} \right| \leq \frac{1}{2} $，得  $ 0 \leq |u_n \cdot v_n| \leq \frac{1}{2} |nu_n| $，根据比较判别法得  $ \sum_{n=1}^{\infty} |u_n \cdot v_n| $ 收敛，故原级数绝对收敛。 $ \rightarrow $ 实际上，若  $ \sum_{n=1}^{\infty} a_n $ 收敛， $ \sum_{n=1}^{\infty} b_n $ 绝对收敛，则  $ \sum_{n=1}^{\infty} a_n b_n $ 绝对收敛，可以当结论记住（证明可以采用反证法）

解 应选(B).

因为 $ \sum_{n=1}^{\infty}\frac{v_{n}}{n} $条件收敛，故由级数收敛的必要条件知 $ \lim_{n\to\infty}\frac{v_{n}}{n}=0 $，从而数列 $ \left\{\frac{v_{n}}{n}\right\} $有界，即存在M>0，