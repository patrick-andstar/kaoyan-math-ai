 $$ \lim_{n\to\infty}\frac{u_{n+1}}{u_{n}}=\lim_{n\to\infty}\frac{a^{n+1}\cdot(n+1)!}{(n+1)^{n+1}}\cdot\frac{n^{n}}{a^{n}\cdot n!}=\lim_{n\to\infty}a\left(\frac{n}{n+1}\right)^{n}=\lim_{n\to\infty}\frac{a}{\left(1+\frac{1}{n}\right)^{n}}=\frac{a}{e}, $$ 

这里  $ \rho = \frac{a}{e} $，显然当  $ 0 < \frac{a}{e} < 1 $，即 0 < a < e 时，原级数收敛；当  $ \frac{a}{e} > 1 $，即 a > e 时，原级数发散；当 a = e 时，由于当  $ n \to \infty $ 时， $ \left(1 + \frac{1}{n}\right)^n $ 单调增加且趋向于 e，故存在 N > 0，当 n > N 时， $ \frac{u_{n+1}}{u_n} = \frac{e}{\left(1 + \frac{1}{n}\right)^n} > 1 \Rightarrow u_{n+1} > u_n $， $ \{u_n\} $ 单调增加，从而知  $ \lim_{n \to \infty} u_n \neq 0 $，由级数收敛的必要条件，知原级数发散。

综上所述，当 0 < a < e 时，原级数收敛；当  $ a \geq e $ 时，原级数发散。选 (A).

(5) 根值判别法（也叫柯西判别法）.

给出一正项级数  $ \sum_{n=1}^{\infty}u_{n} $，如果  $ \lim_{n\to\infty}\sqrt[n]{u_{n}}=\rho $，那么

①若  $ \rho<1 $，则  $ \sum_{n=1}^{\infty}u_{n} $ 收敛； $ \rightarrow $ 证明：存在  $ N>0 $，当  $ n>N $ 时， $ \sqrt[n]{u_{n}}<\frac{\rho+1}{2}=k $

 $ 0<k<1\Rightarrow0<u_{n}<k^{n}\rightarrow0\left(n\rightarrow\infty\right) $ 故  $ \rho<1 $ 时

<div style="text-align: center;"><img src="imgs/img_in_image_box_811_502_902_679.jpg" alt="Image" width="8%" /></div>


②若  $ \rho > 1 $，则  $ \sum_{n=1}^{\infty} u_{n} $ 发散．  $ \sum_{n=1}^{\infty} u_{n} $ 收敛

柯西

(1789—1857)

注 (1) 同样要指出，若  $ \rho = 1 $，根值判别法也会失效。如  $ \sum_{n=1}^{\infty} \frac{1}{n} $ 发散，有  $ \lim_{n \to \infty} \sqrt[n]{\frac{1}{n}} = \rho = 1 $； $ \sum_{n=1}^{\infty} \frac{1}{n^2} $ 收敛，也有  $ \lim_{n \to \infty} \sqrt[n]{\frac{1}{n^2}} = \rho = 1 $。

(2)  $ \sqrt[n]{u_n} \geq 1 (n = 1, 2, \cdots) $，则  $ \lim_{n \to \infty} $ 不等于 0，不必取极限，就可推知  $ \sum_{n=1}^{\infty} u_n $ 发散。

例 16.12 级数  $ \sum_{n=1}^{\infty}\left[e^{\frac{\sin^{2}\alpha n}{n^{2}}}+\left(\cos\frac{1}{\sqrt{n}}\right)^{n^{2}}-1\right] $ （ ）.

(A) 收敛 (B) 发散 (C) 敛散性与  $ \alpha $ 有关 (D) 无法判断

解 应选(A).

对级数  $ I_{1}=\sum_{n=1}^{\infty}\left(e^{\frac{\sin^{2}\alpha n}{n^{2}}}-1\right) $，当  $ n\to\infty $ 时， $ \frac{\sin^{2}\alpha n}{n^{2}}\to0^{+} $，可判断其为正项级数。当  $ n\to\infty $ 时， $ e^{\frac{\sin^{2}\alpha n}{n^{2}}}-1 $ 等价于  $ \frac{\sin^{2}\alpha n}{n^{2}} $，而  $ \frac{\sin^{2}\alpha n}{n^{2}} $ 满足  $ 0<\frac{\sin^{2}\alpha n}{n^{2}}\leq\frac{1}{n^{2}} $，且  $ \sum_{n=1}^{\infty}\frac{1}{n^{2}} $ 收敛，从而  $ I_{1} $ 收敛。