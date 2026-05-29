16.6  $ (-2, 4) $ 解 用比值判别法，因为

 $$ \lim_{n\to\infty}\left|\frac{\frac{(n+1)(x-1)^{n+1}}{3^{n+1}}}{\frac{n(x-1)^{n}}{3^{n}}}\right|=\lim_{n\to\infty}\frac{n+1}{3n}\left|x-1\right|=\frac{1}{3}\left|x-1\right|, $$ 

所以当  $ \frac{1}{3}|x-1|<1 $，即  $ |x-1|<3 $ 时，幂级数  $ \sum_{n=1}^{\infty}\frac{n}{3^n}(x-1)^n $ 绝对收敛；当  $ \frac{1}{3}|x-1|>1 $，即  $ |x-1|>3 $ 时，幂级数  $ \sum_{n=1}^{\infty}\frac{n}{3^n}(x-1)^n $ 发散。

根据收敛半径的定义可知收敛半径 R=3 ，收敛区间为  $ (-2,4) $

又因为当x=4时，幂级数为 $ \sum_{n=1}^{\infty}n $，发散；当x=-2时，幂级数为 $ \sum_{n=1}^{\infty}(-1)^{n}n $，发散，所以收敛域为 $ (-2,4) $.

16.7  $ \frac{\pi^{2}-5}{2} $ 解 由狄利克雷收敛定理可知， $ f(x) $ 在  $ x=\pm\pi $ 处的傅里叶级数收敛于

 $$ \frac{f(-\pi^{+})+f(\pi^{-})}{2}\;. $$ 

因为 $ f(\pi^{-})=-5,\ f(-\pi^{+})=x^{2}\bigg|_{x=-\pi}=\pi^{2} $，故 $ S(\pm\pi)=\frac{f(-\pi^{+})+f(\pi^{-})}{2}=\frac{\pi^{2}-5}{2} $.

16.8  $ \frac{2}{3}\pi $ 解  $ b_{3}=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin3xdx=\frac{1}{\pi}\int_{-\pi}^{\pi}(\pi x+x^{2})\sin3xdx=2\int_{0}^{\pi}x\sin3xdx=\frac{2}{3}\pi $

16.9 解 由正项数列 $\{a_n\}$ 单调减少知 $\lim_{n \to \infty} a_n$ 存在，记为 $a, a \geq 0$，且对任意 $n \in \mathbb{N}_+$ 都有 $a_n \geq a$。从而 $\frac{1}{a_n + 1} \leq \frac{1}{a + 1}$ ($n = 1, 2, \cdots$)。另一方面，已知 $\sum_{n=1}^{\infty} (-1)^n a_n$ 发散，故 $a > 0$。因若 $a = 0$，则由莱布尼茨判别法知 $\sum_{n=1}^{\infty} (-1)^n a_n$ 应收敛。既然常数 $a > 0$，故等比级数 $\sum_{n=1}^{\infty} \left( \frac{1}{a + 1} \right)^n$ 的公比 $\frac{1}{a + 1} < 1$，$\sum_{n=1}^{\infty} \left( \frac{1}{a + 1} \right)^n$ 收敛。由比较判别法知 $\sum_{n=1}^{\infty} \left( \frac{1}{a_n + 1} \right)^n$ 亦收敛。

16.10 解  $ \prod_{n=2}^{\infty}2^{\frac{\ln n}{n^{\alpha}}}=2^{\sum_{n=2}^{\infty}\frac{\ln n}{n^{\alpha}}} $，根据指数函数的连续性可知  $ \prod_{n=2}^{\infty}2^{\frac{\ln n}{n^{\alpha}}} $ 与  $ \sum_{n=2}^{\infty}\frac{\ln n}{n^{\alpha}} $ 同敛散.

以下同例 16.8. 故当  $ 0 < \alpha \leq 1 $ 时， $ \prod_{n=2}^{\infty} 2^{\frac{\ln n}{n^{\alpha}}} $ 发散；当  $ \alpha > 1 $ 时， $ \prod_{n=2}^{\infty} 2^{\frac{\ln n}{n^{\alpha}}} $ 收敛.

16.11 分析 这是交错级数，但不易判别  $ \{|u_n|\} $ 的单调性，因此不能使用莱布尼茨判别法．为了能