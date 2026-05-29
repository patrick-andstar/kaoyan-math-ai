注 (1) 此命题反过来不对，如取  $ a_n = (-1)^n $，则  $ \lim_{n \to \infty} |(-1)^n| = 1 $。但  $ \lim_{n \to \infty} (-1)^n $ 不存在。

(2) 在本题中若  $ A = 0 $，则  $ \left|a_n\right| - \left|A\right| = \left|a_n\right| - 0 = \left|a_n - 0\right| $，即有  $ \lim_{n \to \infty} a_n = 0 \Leftrightarrow \lim_{n \to \infty} |a_n| = 0 $，这个结论常用。

由  $ 0 \leqslant \left| \frac{\sin n}{n^2} \right| \leqslant \frac{1}{n^2} $，得  $ \lim_{n \to \infty} \left| \frac{\sin n}{n^2} \right| = 0 $，故  $ \lim_{n \to \infty} \frac{\sin n}{n^2} = 0 $

一般地，若要证  $ \lim_{n \to \infty} a_n = 0 $，可转化为证  $ \lim_{n \to \infty} |a_n| = 0 $，由于  $ |a_n| \geq 0 $，若使用夹逼准则，便省了一半的力气，只需找到一个数列  $ \{b_n\} $ 满足  $ |a_n| \leq b_n $，且  $ \lim_{n \to \infty} b_n = 0 $ 即可。

(3) 此结论对函数亦成立，即若  $ \lim_{x \to x_0} f(x) = A $，则  $ \lim_{x \to x_0} |f(x)| = |A| $，而反之不成立。但  $ \lim_{x \to x_0} f(x) = 0 \Leftrightarrow \lim_{x \to x_0} |f(x)| = 0 $。

### 例 2.3 证明数列  $ \left\{n^{(-1)^{n}}\right\} $ 极限不存在

证 从数列

 $$ \left\{n^{(-1)^{n}}\right\}:\frac{1}{1},2,\frac{1}{3},4,\frac{1}{5},6,\cdots,\frac{1}{2n-1},2n,\cdots $$ 

中选取一个子列  $ \{2n\} $: 2, 4, …, 2n, …，该数列不是有界数列，由下文收敛数列的性质定理 3 的逆否命题知该子列发散，因此，由 “收敛数列的任何子列也收敛” 的逆否命题知，原数列极限不存在。

该数列存在收敛的子列  $ \left\{\frac{1}{2n-1}\right\} $：1， $ \frac{1}{3} $， $ \frac{1}{5} $， $ \cdots $， $ \frac{1}{2n-1} $， $ \cdots $，但原数列发散。这说明一个数列的某个子列收敛并不能保证原数列收敛。

例 2.4 设  $ x_{n}=\begin{cases}\dfrac{n^{2}+\sqrt{n}}{n}, & n \text{为正奇数}, \\ \dfrac{1}{n}, & n \text{为正偶数},\end{cases} $ 则当  $ n \rightarrow \infty $ 时，变量  $ x_{n} $ 为（）.

(A)无穷大量 (B)无穷小量 (C)有界变量但不是无穷小量 (D)无界变量但不是无穷大量

解 应选(D).

 $$ \lim_{n\to\infty}x_{2n}=\lim_{n\to\infty}\frac{1}{2n}=0, $$ 

 $$ \lim_{n\to\infty}x_{2n-1}=\lim_{n\to\infty}\frac{(2n-1)^{2}+\sqrt{2n-1}}{2n-1}=+\infty, $$ 