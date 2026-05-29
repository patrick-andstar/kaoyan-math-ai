可知  $ \lim_{n\to\infty}x_{2n}\neq\lim_{n\to\infty}x_{2n-1} $，因此  $ \lim_{n\to\infty}x_n $ 不存在，且当  $ n\to\infty $ 时， $ \{x_n\} $ 既不是无穷大量，也不是无穷小量，它是无界变量，故选 (D).

## 3 收敛数列的性质

定理 2(唯一性) 给出数列  $ \left\{x_{n}\right\} $，若  $ \lim_{n\to\infty}x_{n}=a $（存在），则 a 是唯一的.

定理 3(有界性) 若数列  $ \left\{x_{n}\right\} $ 极限存在，则数列  $ \left\{x_{n}\right\} $ 有界.

定理 4(保号性) 设  $ \lim_{n\to\infty}x_n=a>b $，则存在 N>0，当 n>N 时，有  $ x_n>b $ 。若数列  $ \{x_n\} $ 从某项起有  $ x_n\geq b $，且  $ \lim_{n\to\infty}x_n=a $，则  $ a\geq b $，其中 b 为任意实数。常考 b=0 的情形。

脱帽解法： $ \lim_{n\to\infty}x_{n}>a\Rightarrow x_{n}>a $（严格不等）.

戴帽解法： $ x_{n} \geqslant a \Rightarrow \lim_{n \to \infty} x_{n} \geqslant a $（非严格不等）.

例 2.5 已知  $ a_{n}=1-\frac{(-1)^{n}}{n}(n=1,2,\cdots) $，则  $ \{a_{n}\} $ （）

(A)有最大值，有最小值

(B)有最大值，没有最小值

(C) 没有最大值，有最小值

(D) 没有最大值，没有最小值

分析 写出开头几项： $ 1+\frac{1}{1} $， $ 1-\frac{1}{2} $， $ 1+\frac{1}{3} $，…，观察规律，发现在“1”的附近摆动.

解 应选(A).

 $ \lim_{n\to\infty}a_n=1,a_1=2>1,a_2=1-\frac{1}{2}<1 $ . 由于  $ \lim_{n\to\infty}(a_n-a_1)<0 $ ，则存在  $ N_1>0 $ ，当  $ n>N_1 $ 时， $ a_n<a_1 $ . 又由于  $ \lim_{n\to\infty}(a_n-a_2)>0 $ ，则存在  $ N_2>0 $ ，当  $ n>N_2 $ 时， $ a_n>a_2 $ . 取  $ N=\max\{N_1,N_2\} $ ，当  $ n>N $ 时， $ a_n $ 不可能是最大、最小值，故前有限项必存在最大、最小值 .  $ \begin{aligned}\frac{1}{n}&\text{是保证}N\geq N_1\text{且}N\geq N_2\\&\text{有}n>N\text{时，有}n>N_1\text{且}n>N_2\end{aligned} $

注 $ ^{(1)} $最值是比较出来的.

(2) 此题用保号性说明了 n > N 后的项没有资格参与比较，故前有限项必有最大、最小值.

## 4 极限四则运算规则

①对于数列极限，有

设  $ \lim_{n\to\infty}x_n=a,\lim_{n\to\infty}y_n=b $ ，则

(1)  $ \lim_{n\to\infty}(x_n\pm y_n)=a\pm b $;

 $$ \lim_{n\to\infty}(x_{n}+y_{n})=\lim_{n\to\infty}x_{n}+\lim_{n\to\infty}y_{n}:\quad\lim_{n\to\infty}(x_{n}-y_{n})=\lim_{n\to\infty}x_{n}-\lim_{n\to\infty}y_{n} $$ 

(2)  $ \lim_{n\to\infty}x_ny_n = ab $;

 $$ \lim_{n\to\infty}x_{n}y_{n}=\lim_{n\to\infty}x_{n}\bullet\lim_{n\to\infty}y_{n}:\quad\lim_{n\to\infty}\frac{x_{n}}{y_{n}}=\frac{\lim\limits_{n\to\infty}x_{n}}{\lim\limits_{n\to\infty}y_{n}}\Big(\lim_{n\to\infty}y_{n}\neq0\Big). $$ 

②对于函数极限，有

 $$ \lim_{x\to x_{0}}\left[f(x)+g(x)\right]=\lim_{x\to x_{0}}f(x)+\lim_{x\to x_{0}}g(x);\quad\lim_{x\to x_{0}}\left[f(x)-g(x)\right]=\lim_{x\to x_{0}}f(x)-\lim_{x\to x_{0}}g(x) $$ 

 $$ \lim_{x\to x_{0}}f(x)g(x)=\lim_{x\to x_{0}}f(x)\bullet\lim_{x\to x_{0}}g(x):\quad\lim_{x\to x_{0}}\frac{f(x)}{g(x)}=\frac{\lim\limits_{x\to x_{0}}f(x)}{\lim\limits_{x\to x_{0}}g(x)}\Big(\lim\limits_{x\to x_{0}}g(x)\neq0\Big). $$ 

(3) 若  $ b \neq 0 $，则  $ \lim_{n \to \infty} \frac{x_n}{y_n} = \frac{a}{b} $