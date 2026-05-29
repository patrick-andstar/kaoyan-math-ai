分子不变，将分母放缩成相同的，则

 $$ \frac{n(n+1)}{2(n^{2}+n+n)}\leqslant\frac{1}{n^{2}+n+1}+\frac{2}{n^{2}+n+2}+\cdots+\frac{n}{n^{2}+n+n}\leqslant\frac{n(n+1)}{2(n^{2}+n+1)}, $$ 

又  $ \lim_{n\to\infty}\frac{n(n+1)}{2(n^2+n+1)}=\lim_{n\to\infty}\frac{n(n+1)}{2(n^2+n+n)}=\frac{1}{2} $，所以根据夹逼准则，原式  $ =\frac{1}{2} $

找带头大哥

例 2.10 求极限  $ \lim_{n\to\infty}\sqrt[n]{a_1^n+a_2^n+\cdots+a_m^n} $，其中  $ a_i(i=1,2,\cdots,m) $ 都是非负数.

解 设  $ a = \max\{a_1, a_2, \cdots, a_m\} $，则

 $$ a^{n}\leqslant a_{1}^{n}+a_{2}^{n}+\cdots+a_{m}^{n}\leqslant m\bullet a^{n}, $$ 

即  $ a \leqslant \sqrt[n]{a_{1}^{n} + a_{2}^{n} + \cdots + a_{m}^{n}} \leqslant a \cdot m^{\frac{1}{n}} $，且  $ \lim_{n \to \infty} m^{\frac{1}{n}} = 1 $．故

 $$ \lim_{n\to\infty}\sqrt[n]{a_{1}^{n}+a_{2}^{n}+\cdots+a_{m}^{n}}=\max\{a_{1},a_{2},\cdots,a_{m}\} $$ 

## 注 这是一个结论，应当记住。

如当  $ 0 < a < b $ 时， $ \lim_{n \to \infty} (a^{-n} + b^{-n})^{\frac{1}{n}} = \lim_{n \to \infty} \sqrt[n]{\left(\frac{1}{a}\right)^n + \left(\frac{1}{b}\right)^n} = \frac{1}{a} $。又如当  $ 0 \leqslant x \leqslant \frac{\pi}{2} $ 时，

 $$ \frac{1}{a}>\frac{1}{b}>0 $$ 

 $$ \begin{aligned}&\lim_{n\rightarrow\infty}\sqrt[n]{\sin^{n}x+\cos^{n}x}=\left\{\begin{aligned}\\ &\cos x,&0\leq x\leq\frac{\pi}{4},\\&\sin x,&\frac{\pi}{4}<x\leq\frac{\pi}{2}.\\ &\end{aligned}\right.\\ &( 定义函数的方法之一 )\\ \end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_771_807_892_955.jpg" alt="Image" width="11%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_105_951_269_1074.jpg" alt="Image" width="15%" /></div>


再如  $ \lim_{n\to\infty}\sqrt[n]{1+|x|^{3n}}=\begin{cases}1,&|x|\leq1,\\|x|^{3},&|x|>1.\end{cases} $

约束式

例 2.11 设  $ 0 < a_n < \frac{\pi}{2} $， $ 0 < b_n < \frac{\pi}{2} $， $ \cos a_n - a_n = \cos b_n $，且  $ \lim_{n \to \infty} b_n = 0 $，求  $ \lim_{n \to \infty} a_n $， $ \lim_{n \to \infty} \frac{a_n}{b_n^2} $

(1) 分清约束式、关系式和定义式；(2) 做一至两步的逆运算；(3) 联想一些经典形式。

解 由  $ \cos a_n - \cos b_n = a_n > 0 $，知  $ 0 < a_n < b_n $，则由夹逼准则，得  $ \rightarrow $ 根据  $ \cos x $ 的单调性， $ \cos x $ 在

 $$ \lim_{n\to\infty}a_{n}=0, $$ 

 $$ \left(0,\frac{\pi}{2}\right) $$ 