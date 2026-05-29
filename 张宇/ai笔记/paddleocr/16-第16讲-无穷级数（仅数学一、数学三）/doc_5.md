★性质 4 若  $ \sum_{n=1}^{\infty}u_{n} $ 收敛，则  $ \lim_{n\to\infty}u_{n}=0 $

注1 证  $ \sum_{n=1}^{\infty}u_{n} $ 收敛  $ \Leftrightarrow \lim_{n\to\infty}S_{n}=A $ 。又因为当 n>1 时， $ u_{n}=S_{n}-S_{n-1} $，所以  $ \lim_{n\to\infty}u_{n}=\lim_{n\to\infty}S_{n}-\lim_{n\to\infty}S_{n-1}=A-A=0 $ 。

注2  $ u_{n} $ 的妙用：当 n > 1 时， $ u_{n} = S_{n} - S_{n-1} $

例：对于正项级数  $ \sum_{n=1}^{\infty}u_{n} $， $ S_{n} $ 是级数前 n 项和，当 n > 1 时，则

 $$ \frac{u_{n}}{S_{n}^{2}}=\frac{S_{n}-S_{n-1}}{S_{n}^{2}}\leqslant\frac{S_{n}-S_{n-1}}{S_{n}\cdot S_{n-1}}=\frac{1}{S_{n-1}}-\frac{1}{S_{n}} $$ 

分析： $ u_{n} $ 与  $ S_{n}^{2} $ 不同类，所以要化为同类

注3 此性质是级数收敛的必要条件. 其逆否命题: 若  $ \lim_{n\to\infty}u_n\neq0 $，则  $ \sum_{n=1}^{\infty}u_n $ 必发散，且即使  $ \lim_{n\to\infty}u_n=0 $，也不能保证  $ \sum_{n=1}^{\infty}u_n $ 收敛，见例 16.13.

<div style="text-align: center;"><img src="imgs/img_in_image_box_398_792_527_894.jpg" alt="Image" width="12%" /></div>


 $$ \int_{1}^{+\infty}\frac{1}{x^{p}}\mathrm{d}x\Rightarrow\begin{cases}p>1, 收敛 ,\\ p\leq1, 发散 \end{cases}\Leftrightarrow\sum_{n=1}^{\infty}\frac{1}{n^{p}}\Rightarrow\begin{cases}p>1, 收敛 .\\ p\leq1, 发散 .\end{cases} $$ 

应用：判别 $ \sum_{n=1}^{\infty}\ln\left(1+\frac{1}{n}\right) $的敛散性.

 $$ \mathrm{n}\left(1+\frac{1}{n}\right)=\ln\frac{n+1}{n}=\ln(n+1)-\ln n $$ 

例 16.1 证明： $ \sum_{n=1}^{\infty}(u_{n+1}-u_{n}) $ 收敛  $ \Leftrightarrow \lim_{n\to\infty}u_n $ 存在．  $ \lim_{n\to\infty}n $ 不存在，所以  $ \sum_{n=1}^{\infty}\ln\left(1+\frac{1}{n}\right)=\sum_{n=1}^{\infty}\left[\ln(n+1)-\ln n\right] $ 发散

证  $ S_{n}=\sum_{k=1}^{n}(u_{k+1}-u_{k})=(u_{2}-u_{1})+(u_{3}-u_{2})+\cdots+(u_{n+1}-u_{n})=u_{n+1}-u_{1} $，故  $ \sum_{n=1}^{\infty}(u_{n+1}-u_{n}) $ 收敛  $ \Leftrightarrow \lim_{n\to\infty}S_{n} $ 存有限项相加，去括号无影响。

在，即  $ \lim_{n\to\infty}u_{n+1}-u_1 $ 存在，也即  $ \lim_{n\to\infty}u_{n+1} $ 存在  $ \Leftrightarrow\lim_{n\to\infty}u_n $ 存在。

例 16.2 记  $ \sum_{n=1}^{\infty}u_{n} $ 的部分和  $ S_{n}=u_{1}+u_{2}+\cdots+u_{n} $，若  $ \lim_{n\to\infty}u_{n}=0 $， $ \lim_{n\to\infty}S_{2n}=S $（或  $ \lim_{n\to\infty}S_{2n+1}=S $），证明： $ \sum_{n=1}^{\infty}u_{n}=S $。