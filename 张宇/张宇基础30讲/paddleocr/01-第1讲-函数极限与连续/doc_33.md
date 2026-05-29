③  $ \lim_{x\to x_0}\frac{f(x)}{g(x)}=\frac{A}{B}(B\neq0) $.

事实上，由于 $ f(x) $， $ g(x) $的趋核运算值均为其实数核值，故如

 $$ \lim_{x\to x_{0}}\left[f(x)+g(x)\right]=\lim_{x\to x_{0}}f(x)+\lim_{x\to x_{0}}g(x)=A+B $$ 

显然成立，比如

 $$ \lim_{x\to0}(x+\sin x)=\lim_{x\to0}x+\lim_{x\to0}\sin x=0+0=0, $$ 

 $$ \lim_{x\to1}\frac{\sin x}{x}=\frac{\lim\limits_{x\to1}\sin x}{\lim\limits_{x\to1}x}=\frac{\sin1}{1}=\sin1 $$ 

下面说明两种情况.

① $ f(x) $， $ g(x) $中恰有一个不存在核值.

设  $ \lim_{x\to x_0}f(x)=A $， $ \lim_{x\to x_0}g(x) $ 不存在或为无穷大量，则

a.  $ \lim_{x\to x_0}\left[f(x)\pm g(x)\right]=A\pm $ (不存在或 $ \infty $) = 不存在或 $ \infty $ 实数运算为平 不存在或 $ \infty $ 作有限平移，依然为移运算 不存在或 $ \infty $.

如  $ \lim_{x\to0}\left(\frac{\sin x}{x}+\sin\frac{1}{x}\right) $，其中  $ \lim_{x\to0}\frac{\sin x}{x}=1 $， $ \lim_{x\to0}\sin\frac{1}{x} $ 不存在（在 -1 到 1 之间振荡），则  $ \lim_{x\to0}\left(\frac{\sin x}{x}+\sin\frac{1}{x}\right)= $

 $ \frac{1+ 不存在 }{ }= $ 不存在．

仅供理解，不要写出来.

b.  $ \lim_{x\to x_0}\frac{f(x)g(x)}{} $ = A·(不存在或 $ \infty $).

①实数运算

②为放缩运算

这里的趋核运算有多种情况。

(i) 如  $ \lim_{x\to0}x\sin\frac{1}{x} $，其中  $ \lim_{x\to0}x=0 $， $ \lim_{x\to0}\sin\frac{1}{x} $ 不存在.

此时 A=0 ，可以将 “-1 到 1 之间振荡” 的情形压缩成 0 ，故  $ \lim_{x\to0}x\sin\frac{1}{x}=0 $ 。有界振荡 =0 。此时极限存在，即趋核运算值为 0 。

(ii) 如  $ \lim_{x\to\infty}\sin\frac{1}{x^{2}}\cdot x $，其中  $ \lim_{x\to\infty}\sin\frac{1}{x^{2}}=0 $， $ \lim_{x\to\infty}x=\infty $，理由同 (i)， $ \lim_{x\to\infty}\sin\frac{1}{x^{2}}\cdot x=0 $

(iii) 如  $ \lim_{x\to0}\cos x\cdot\sin\frac{1}{x} $，其中  $ \lim_{x\to0}\cos x=1 $， $ \lim_{x\to0}\sin\frac{1}{x} $ 不存在。此时 A=1，放缩结果不变，故  $ \lim_{x\to0}\cos x\sin\frac{1}{x} $ 不存在。

c.  $ \lim_{x\to x_0}\frac{f(x)}{g(x)}=\lim_{x\to x_0}f(x)\cdot\frac{1}{g(x)} $，讨论与b.类似.